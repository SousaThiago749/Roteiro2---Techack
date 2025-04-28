import dns.resolver

def dns_enum(dominio):
    registros = ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT']
    resultados = {}

    for tipo in registros:
        try:
            resposta = dns.resolver.resolve(dominio, tipo)
            resultados[tipo] = [rdata.to_text() for rdata in resposta]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            resultados[tipo] = ['N/A']
        except Exception as e:
            resultados[tipo] = [f"Erro: {str(e)}"]

    return resultados


if __name__ == "__main__":
    dominio = input("Digite o domínio para enumeração DNS: ")
    dados = dns_enum(dominio)
    print("\n===== RESULTADOS DNS =====")
    for tipo, valores in dados.items():
        print(f"\n[{tipo}]")
        for val in valores:
            print(f" - {val}")
    print("==========================")