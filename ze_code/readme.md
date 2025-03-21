# Yuri Vargas da Fonseca - PDBD004

## Descrição

Este repositório contém um sistema para gerenciamento de parceiros, onde é possível carregar dados de parceiros a partir de um arquivo GeoJSON chamado `pdvs.json`, consultar parceiros por ID e localizar o parceiro mais próximo de uma coordenada geográfica. O sistema utiliza MySQL para armazenar os dados geoespaciais e Python para manipulação dos dados.

### Funcionalidades:
- Processar um arquivo GeoJSON (`pdvs.json`) para inserir dados de parceiros no banco de dados.
- Carregar dados de um parceiro pelo seu ID.
- Buscar o parceiro mais próximo com base nas coordenadas geográficas fornecidas.

## Requisitos

- Python 3.x
- MySQL 8.0 ou superior
- Bibliotecas Python:
  - `mysql-connector-python`
  - `geojson`

## Como Usar

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter o MySQL instalado e configurado corretamente. Crie o banco de dados `ze_code` e a tabela de `partners`.
3. Adapte as credenciais de banco de dados no arquivo `process_geojson_file.py`:
   ```python
   password = "sua_senha"  # coloque sua senha do MySQL aqui
