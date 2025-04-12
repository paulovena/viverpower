FROM python:3.11-slim

WORKDIR /app

# Copie todos os arquivos para o contêiner
COPY . /app

# Instale as dependências a partir do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=80", "--server.enableCORS=false"]
