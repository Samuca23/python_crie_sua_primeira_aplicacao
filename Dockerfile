# Use a imagem oficial do Python como base
FROM python:3.8

# Copie o arquivo Python para dentro do contêiner
COPY app.py /app.py

# Defina o diretório de trabalho
WORKDIR /

# Execute o arquivo Python quando o contêiner for iniciado
CMD ["python", "app.py"]