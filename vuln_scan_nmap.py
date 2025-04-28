import subprocess

def scan_vulnerabilidades_nmap(alvo):
    try:
        comando = ["nmap", "-sV", "--script", "vuln", alvo]
        resultado = subprocess.check_output(comando, text=True, stderr=subprocess.STDOUT)
        return resultado
    except subprocess.CalledProcessError as e:
        return f"Erro na execução do Nmap: {e.output}"
    except FileNotFoundError:
        return "Comando 'nmap' não encontrado. Certifique-se de que está instalado (Linux/Kali)."


if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio para scan de vulnerabilidades: ")
    resultado = scan_vulnerabilidades_nmap(alvo)
    print("\n===== RESULTADO SCAN DE VULNERABILIDADES =====")
    print(resultado)
    print("==============================================")