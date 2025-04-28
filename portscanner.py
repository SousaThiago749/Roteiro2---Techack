import socket
import ipaddress
import errno


def carregar_portas_conhecidas():
    return {
        20: "FTP (Data)", 21: "FTP (Control)", 22: "SSH",
        23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
        110: "POP3", 111: "RPCbind", 135: "Microsoft RPC",
        139: "NetBIOS", 143: "IMAP", 443: "HTTPS",
        445: "Microsoft DS", 993: "IMAPS", 995: "POP3S",
    }

def escanear_portas_tcp(host, porta_inicial, porta_final, well_known_ports):
    resultado = []
    for porta in range(porta_inicial, porta_final + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            retorno = s.connect_ex((host, porta))
            if retorno == 0:
                status = "open"
            elif retorno in (errno.ECONNREFUSED, 111, 10061):
                status = "closed"
            else:
                status = "filtered"
        except socket.timeout:
            status = "filtered"
        except Exception:
            status = "filtered"
        finally:
            s.close()

        servico = well_known_ports.get(porta, "Desconhecido")
        resultado.append((porta, servico, status))
    return resultado

def escanear_portas_udp(host, porta_inicial, porta_final, well_known_ports):
    resultado = []
    for porta in range(porta_inicial, porta_final + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1.0)
        try:
            if porta == 53:
                dns_query = (
                    b'\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00'
                    b'\x03www\x06google\x03com\x00\x00\x01\x00\x01'
                )
                s.sendto(dns_query, (host, porta))
            else:
                s.sendto(b"", (host, porta))

            s.recvfrom(1024)
            status = "open"
        except socket.timeout:
            status = "filtered"
        except ConnectionRefusedError:
            status = "closed"
        except Exception:
            status = "filtered"
        finally:
            s.close()

        servico = well_known_ports.get(porta, "Desconhecido")
        resultado.append((porta, servico, status))
    return resultado

def escanear_rede(cidr, porta_inicial, porta_final, protocolo='TCP'):
    resultados = {}
    well_known_ports = carregar_portas_conhecidas()

    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError:
        return {}

    for host in network.hosts():
        host_str = str(host)
        if protocolo.upper() == 'UDP':
            portas = escanear_portas_udp(host_str, porta_inicial, porta_final, well_known_ports)
        else:
            portas = escanear_portas_tcp(host_str, porta_inicial, porta_final, well_known_ports)
        resultados[host_str] = portas

    return resultados

def escanear_host(host, porta_inicial, porta_final, protocolo='TCP'):
    well_known_ports = carregar_portas_conhecidas()
    if protocolo.upper() == 'UDP':
        return escanear_portas_udp(host, porta_inicial, porta_final, well_known_ports)
    else:
        return escanear_portas_tcp(host, porta_inicial, porta_final, well_known_ports)
