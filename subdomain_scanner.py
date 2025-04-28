import requests
from concurrent.futures import ThreadPoolExecutor

def carregar_wordlist(caminho):
    try:
        with open(caminho, 'r') as f:
            return [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"Arquivo de wordlist '{caminho}' não encontrado.")
        return []

def verificar_subdominio(subdominio):
    url = f"http://{subdominio}"
    try:
        resposta = requests.get(url, timeout=3)
        return (subdominio, resposta.status_code)
    except requests.RequestException:
        return (subdominio, None)

def escanear_subdominios(dominio, wordlist):
    subdominios = [f"{prefixo}.{dominio}" for prefixo in wordlist]
    encontrados = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        for subdominio, status in executor.map(verificar_subdominio, subdominios):
            if status:
                encontrados.append((subdominio, status))

    return encontrados


if __name__ == "__main__":
    dominio = input("Digite o domínio base (ex: google.com): ")
    caminho_wordlist = input("Caminho da wordlist (ex: wordlist.txt): ")

    wordlist = carregar_wordlist(caminho_wordlist)
    resultados = escanear_subdominios(dominio, wordlist)

    print("\n===== SUBDOMÍNIOS ENCONTRADOS =====")
    for sub, status in resultados:
        print(f" - {sub} [HTTP {status}]")
    print("==================================")
