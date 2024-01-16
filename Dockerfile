# Use uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do seu projeto Flask
COPY . .

# Defina a variável de ambiente para indicar que o Python não está em modo interativo
ENV PYTHONUNBUFFERED 1

# Expõe a porta que o Gunicorn vai rodar
EXPOSE 8000

# Comando para rodar a aplicação usando Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]
