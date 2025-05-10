from collections import Counter
import re
import os
import time
import logging
import platform

# Configuração do logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class LogFileHandler:
    def __init__(self, file_paths):
        self.file_paths = [os.path.normpath(path) for path in file_paths]  # Normaliza os caminhos
        self.last_positions = {path: 0 for path in self.file_paths}  # Posições dos arquivos que já foram lidos
        self.previous_ips = set()  # IPs processados na última verificação
        logging.info(f"Inicializando monitoramento para os arquivos: {', '.join(self.file_paths)}")

    def clear_screen(self):
        """Limpa a tela dependendo do sistema operacional."""
        if platform.system() == "Windows":
            os.system("cls")  # Comando para limpar a tela no Windows
        else:
            os.system("clear")  # Comando para limpar a tela em sistemas UNIX

    def process_logs(self):
        # Regex para capturar IPs e tipo de requisição (GET, POST, etc.)
        ip_pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+)")
        request_type_pattern = re.compile(r'"(\S+) ')  # Captura o tipo da requisição (GET, POST, etc.)

        # Dicionário para armazenar informações
        ip_info = {}
        new_ips = set()  # Conjunto para armazenar os novos IPs encontrados

        # Processa cada arquivo de log
        for file_path in self.file_paths:
            if not os.path.exists(file_path):
                logging.error(f"Arquivo {file_path} não encontrado durante o processamento.")
                continue

            try:
                with open(file_path, "r") as file:
                    # Move o cursor para a posição onde parou para cada arquivo
                    file.seek(self.last_positions[file_path])
                    new_lines = file.readlines()
                    self.last_positions[file_path] = file.tell()  # Atualiza a posição final do arquivo
            except Exception as e:
                logging.error(f"Erro ao ler o arquivo {file_path}: {e}")
                continue

            for line in new_lines:
                ip_match = ip_pattern.search(line)
                request_type_match = request_type_pattern.search(line)

                if ip_match:
                    ip = ip_match.group(1)
                    request_type = request_type_match.group(1) if request_type_match else "Desconhecido"

                    if ip not in ip_info:
                        ip_info[ip] = {"count": 0, "requests": Counter(), "files": set()}

                    ip_info[ip]["count"] += 1
                    ip_info[ip]["requests"][request_type] += 1
                    ip_info[ip]["files"].add(file_path)  # Adiciona o arquivo de onde o IP foi encontrado
                    new_ips.add(ip)  # Adiciona o IP encontrado ao conjunto de novos IPs

        # Filtra os IPs para exibir apenas os que fizeram novas requisições desde a última verificação
        new_ip_info = {ip: info for ip, info in ip_info.items() if ip in new_ips}

        if not new_ip_info:
            print(".", end="", flush=True)
            return

        # Limpa a tela antes de exibir as novas informações
        self.clear_screen()

        # Exibe o resultado no terminal
        print("IP Address\tRequests\tTop Request Type\tFiles")
        print("--------------------------------------------------------------")
        for ip, info in new_ip_info.items():
            top_request_type = info["requests"].most_common(1)[0][0] if info["requests"] else "Desconhecido"
            files_list = ", ".join(info["files"])
            print(f"{ip}\t{info['count']}\t{top_request_type}\t{files_list}")

        # Exibe informações detalhadas por IP (opcional)
        print("\nDetalhes por IP:")
        for ip, info in new_ip_info.items():
            print(f"\nIP: {ip}")
            print(f"Total de Requisições: {info['count']}")
            print("Arquivos:")
            for file in info["files"]:
                print(f"  {file}")
            print("Tipos de Requisições:")
            for req_type, count in info["requests"].items():
                print(f"  {req_type}: {count}")

        # Atualiza o conjunto de IPs processados
        self.previous_ips = new_ips

if __name__ == "__main__":
    log_file_paths = [
        "Z:/PROJ VUE/Logs/olivetta.com.br/access.log", 
        "Z:/PROJ VUE/Logs/api.certificados.olivetta.com.br/access.log", 
        "Z:/PROJ VUE/Logs/certificados.olivetta.com.br/access.log", 
        "Z:/PROJ VUE/Logs/default/access.log"
    ]

    # Verifica se os arquivos existem antes de começar
    for log_file_path in log_file_paths:
        if not os.path.exists(log_file_path):
            logging.error(f"Arquivo {log_file_path} não encontrado.")
            exit()

    # Inicializa o manipulador de log com múltiplos arquivos
    log_handler = LogFileHandler(log_file_paths)

    logging.info("Iniciando varredura a cada 15 segundos. Pressione Ctrl+C para sair.")
    
    # Loop principal para fazer a varredura a cada 15 segundos
    try:
        while True:
            log_handler.process_logs()  # Processa os logs
            time.sleep(20)  # Aguarda 15 segundos antes de realizar a próxima varredura
    except KeyboardInterrupt:
        logging.info("Encerrando o processo de varredura.")
