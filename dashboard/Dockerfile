FROM python:3.11-slim

WORKDIR /app

# Copie todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . /app

# Instale as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Defina o comando que será executado quando o contêiner iniciar
CMD ["streamlit", "run", "app.py", "--server.port=80", "--server.enableCORS=false"]
