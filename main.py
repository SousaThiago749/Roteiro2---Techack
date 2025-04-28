from portscanner import escanear_host, escanear_rede
from whois_lookup import whois_lookup
from dns_enum import dns_enum
from subdomain_scanner import escanear_subdominios, carregar_wordlist
from vuln_scan_nmap import scan_vulnerabilidades_nmap


def menu():
    print("""
====================================
   FERRAMENTAS DE RECONHECIMENTO
====================================
1 - Port Scan (Host)
2 - Port Scan (Rede)
3 - WHOIS Lookup
4 - DNS Enumeration
5 - Subdomain Scanner
6 - Scan de Vulnerabilidades (Nmap)
0 - Sair
====================================
""")
    return input("Escolha uma opção: ")


def main():
    while True:
        opcao = menu()

        if opcao == '1':
            host = input("\nAlvo (IP ou hostname): ")
            porta_i = int(input("Porta inicial: "))
            porta_f = int(input("Porta final: "))
            protocolo = input("Protocolo (TCP/UDP): ").upper()
            resultado = escanear_host(host, porta_i, porta_f, protocolo)
            print("\n--- Resultados ---")
            for porta, servico, status in resultado:
                print(f"Porta {porta} ({servico}): {status}")

        elif opcao == '2':
            rede = input("\nDigite a rede no formato CIDR (ex: 192.168.0.0/24): ")
            porta_i = int(input("Porta inicial: "))
            porta_f = int(input("Porta final: "))
            protocolo = input("Protocolo (TCP/UDP): ").upper()
            resultados = escanear_rede(rede, porta_i, porta_f, protocolo)
            print("\n--- Resultados ---")
            for host, portas in resultados.items():
                print(f"\nHost: {host}")
                for porta, servico, status in portas:
                    print(f"  Porta {porta} ({servico}): {status}")

        elif opcao == '3':
            dominio = input("\nDigite o domínio para consulta WHOIS: ")
            print("\n--- Resultado WHOIS ---")
            print(whois_lookup(dominio))

        elif opcao == '4':
            dominio = input("\nDigite o domínio para enumeração DNS: ")
            dados = dns_enum(dominio)
            for tipo, valores in dados.items():
                print(f"\n[{tipo}]")
                for val in valores:
                    print(f" - {val}")

        elif opcao == '5':
            dominio = input("\nDigite o domínio base (ex: google.com): ")
            wordlist_path = input("Caminho da wordlist (ex: subdomain_list.txt): ")
            wordlist = carregar_wordlist(wordlist_path)
            encontrados = escanear_subdominios(dominio, wordlist)
            print("\n--- Subdomínios encontrados ---")
            for sub, status in encontrados:
                print(f" - {sub} [HTTP {status}]")

        elif opcao == '6':
            alvo = input("\nDigite o IP ou domínio para scan de vulnerabilidades: ")
            print("\n--- Resultado Vulnerabilidades ---")
            print(scan_vulnerabilidades_nmap(alvo))

        elif opcao == '0':
            print("Saindo... Até mais!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()