# Reconhecimento de Alvo - Roteiro 2

## Respostas às Questões de Pesquisa

1. Além do PortScan, quais são as 5 ferramentas mais úteis para reconhecimento em um pentest?

- WHOIS, DNS Enumeration, Subdomain Scanner, Nmap, Wireshark

2. Qual a diferença entre um scanner de portas SYN e um TCP Connect Scan?

- O TCP Connect, realiza uma conexão completa com a porta alvo. Como depende da pilha TCP do sistema operacional, é mais fácil de detectar por firewalls e logs.

- O SYN, envia apenas o pacote SYN e aguarda a resposta. Se receber um SYN-ACK, a porta está aberta, então envia um RST para evitar completar a conexão. É mais rapido e discreto, pois não finaliza a conexão, ideal para pentests discretos.


3. Como um pentester pode evitar ser detectado por sistemas de prevenção de intrusão (IPS) durante o reconhecimento?

- Como falado anteriormente, um dos metodos para evitar ser detectado é utilizando o SYN, como ele não finaliza a conexão, fica muito mais dificil detectar um pentester. Outro meio bastante utilizado é a fragmentação de pacotes, ou seja, pegar o pacote completo e dividir em pacotes menores, isso faz com que fique mais dificil de reconhecer por um sistema. 

---

## Descrição da Arquitetura e Decisões de Design

O projeto foi estruturado de forma modular para facilitar a manutenção e adição de novas ferramentas no futuro. Cada funcionalidade principal está em um arquivo separado que pode ser reutilizado pelo menu principal, `main.py`.

Arquivos principais:

- `main.py`: Interface principal do usuário com menus de navegação.
- `portscanner.py`: Código do PortScan desenvolvido no Roteiro 1.
- `whois_lookup.py`: Consulta WHOIS.
- `dns_enum.py`: Enumeração de registros DNS.
- `subdomain_scanner.py`: Scanner de subdomínios com wordlist.
- `vuln_scan_nmap.py`: Scan de vulnerabilidades usando Nmap.
- `subdomain_list.txt`: Lista de subdominios para testes do `subdomain_scanner.py`.

---

## Análise das Ferramentas Integradas

1. **Port Scanner (TCP/UDP)**

   - Técnica básica e essencial de coleta de informações sobre serviços em execução.
2. **WHOIS Lookup**

   - Permite obter informações do registrante de um domínio.
   - Compatível com Windows (via biblioteca `python-whois`).
3. **DNS Enumeration**

   - Identifica registros DNS importantes como MX, NS, A, entre outros.
   - Compatível com Windows (`dnspython`).
4. **Subdomain Scanner**

   - Descobre subdomínios existentes usando tentativa e erro com um arquivo txt, com todos subdomínios que o usuário quiser testar.
   - Compatível com Windows (`requests`).
5. **Vulnerability Scan (Nmap)**

   - Utiliza `nmap` com scripts NSE para identificar vulnerabilidades conhecidas.
   - Requer Linux/Kali com Nmap instalado.

---

## Documentação Técnica e Manual do Usuário

### Requisitos

- Instalar dependências com:

```bash
pip install requests dnspython python-whoi
```

- Para usar `vuln_scan_nmap.py`, o `nmap` deve estar instalado no sistema (Linux/Kali).

### Execução

Execute o sistema principal com:

```bash
python main.py
```

Siga o menu interativo e selecione a ferramenta desejada. As entradas são feitas diretamente via terminal/console.

---

## Resultados dos Testes

### Whois

![1745859024052](image/README/1745859024052.png)

### DNS Enumeration

![1745859150592](image/README/1745859150592.png)

### Subdomain Scanner

![1745859257051](image/README/1745859257051.png)

### Scan de Vulnerabilidade (Nmap)

```
Digite o IP ou domínio para scan de vulnerabilidades: 127.0.0.1

===== RESULTADO SCAN DE VULNERABILIDADES =====
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-04-28 13:28 EDT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000010s latency).
All 1000 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 1000 closed tcp ports (reset)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.45 seconds

==============================================
```