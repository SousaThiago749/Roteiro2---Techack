import whois

def whois_lookup(dominio):
    try:
        info = whois.whois(dominio)
        return str(info)
    except Exception as e:
        return f"Erro ao buscar WHOIS: {e}"


if __name__ == "__main__":
    dominio = input("Digite o domínio para consulta WHOIS: ")
    resultado = whois_lookup(dominio)
    print("\n===== RESULTADO WHOIS =====")
    print(resultado)
    print("===========================")
