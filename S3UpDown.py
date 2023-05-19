# INSTALAR A BIBLIOTECA
# pip install boto3

# IMPORTAR A BIBLIOTECA
import boto3

# INICIAR UM CLIENT S3
s3 = boto3.client('s3')

#INSERIR OS DADOS DE CONEXÃO E CAMINHO
bucket_name = 'seu_bucket'
local_file_path = 'caminho_do_arquivo_local/arquivo.txt'
s3_file_path = 'caminho_no_s3/arquivo.txt'

# FAZENDO UPLOAD DO ARQUIVO
s3.upload_file(local_file_path, bucket_name, s3_file_path)

# FAZENDO DOWNLOAD DO ARQUIVO
response = s3.get_object(Bucket=bucket_name, Key=s3_file_path)
content = response['Body'].read()

# Caminho onde você deseja salvar o arquivo no disco local
local_file_path = 'caminho_no_seu_disco_local/arquivo.txt'

# GRAVANDO ARQUIVO NO DISCO
with open(local_file_path, 'wb') as file:
    file.write(content)

# REMOVENDO O ARQUIVO
s3.delete_object(Bucket=bucket_name, Key=s3_file_path)
