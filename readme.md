# Bolsa capixaba ETL

Este projeto realiza a extração, transformação e carregamento (ETL) dos dados da Bolsa Capixaba, utilizando 
Apache Spark e Python. O objetivo é processar os dados brutos (bronze) e gerar dados tratados e organizados (silver) 
para análise.

### O que aprendi com o projeto

Este projeto foi uma excelente oportunidade para aplicar e reforçar conceitos essenciais da engenharia de dados, além de integrar diversas tecnologias amplamente utilizadas no mercado. Abaixo estão os meus principais aprendizados:

- **PySpark / Apache Spark**: Realizei todo o processamento de dados em larga escala utilizando PySpark, aplicando transformações, limpezas e particionamento de forma eficiente e escalável.
- **Web Scraping com Selenium**: Automatizei a extração de dados de um portal público usando Selenium, simulando o comportamento de um usuário real para obter os arquivos necessários.
- **Apache Airflow**: Modelei todo o processo de ETL em DAGs, separando as etapas de extração, transformação e carga de forma clara, com agendamento e monitoramento integrados.
- **Docker / Docker Compose**: Containerizei a aplicação com Docker e orquestrei os serviços com Docker Compose, facilitando a execução e portabilidade do projeto entre diferentes ambientes.
- **Arquitetura de Dados**: Implementei uma estrutura de camadas inspirada em Data Lakes (Bronze, Silver, Gold), com foco em modularidade, rastreabilidade e controle de qualidade dos dados.
- **Boas práticas de Engenharia de Dados**: Trabalhei com logs estruturados, organização de diretórios, versionamento de dados, modularização de código e tratamento de exceções.
- **Integração futura com Cloud (Azure Data Lake)**: Estruturei o projeto pensando na escalabilidade para ambientes em nuvem, prevendo a persistência dos dados processados diretamente em um Data Lake.

Este projeto reforçou tanto a parte técnica quanto a visão arquitetural de um pipeline de dados robusto e profissional.

### ✅ Próximos Passos

| Etapa              | Descrição                                    | Prioridade | Status       | Observações                      |
|--------------------|----------------------------------------------|------------|--------------|----------------------------------|
| Definir schema     | Definir o schema dos dados bronze/silver     | Alta       | Feito        | Verificar colunas variáveis      |
| Upload para Azure  | Enviar dados bronze/silver para Data Lake    | Média      | Em andamento | Usar SDK do Azure                |
| Melhorar DAGs      | Modularizar e aplicar retries nos operadores | Média      | Pendente     | Testar com DAG simples primeiro  |


## Visão Geral
O processo ETL envolve a leitura de arquivos CSV, Parquet e JSON, que contêm informações sobre os benefícios sociais da 
Bolsa Capixaba. O pipeline realiza as seguintes etapas:

1. **Extração (Extract)**: Leitura dos arquivos de dados em formatos CSV, Parquet ou JSON.

2. **Transformação (Transform)**: Limpeza, renomeação e formatação dos dados:

   - Renomeação de colunas para nomes mais legíveis.

   - Conversão de tipos de dados.

   - Formatação de valores, como valores de benefícios.

3. **Carregamento (Load)**: Armazenamento dos dados tratados no formato Parquet, particionado por ano e 
mês de benefício.


## Estrutura do Projeto
~~~
bolsa_capixaba/
│
├── dags/                         # DAGs do Airflow (orquestração de pipelines)
│
├── src/                          # Código fonte (transformações, validações etc)
│   ├── ingestion/                # Scripts de ingestão
│   ├── processing/               # Transformações (ETL, limpeza, etc)
│   ├── utils/                    # Funções auxiliares (log, conexões etc)
│
├── notebooks/                    # Notebooks para análise e prototipagem
│
├── data/                         # Dados locais temporários
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── logs/                         # Logs das execuções dos pipelines
│
├── requirements.txt              # Dependências do projeto
├── Dockerfile                    # Containerização do projeto
├── docker-compose.yaml           # Configurações do airflow
├── README.md                     # Documentação inicial
└── .env                          # Variáveis de ambiente (não versionar)
~~~


## Dependências
As dependências do projeto estão listadas no arquivo requirements.txt:
   - dotenv
   - python-dotenv
   - selenium
   - webdriver-manager
   - pyspark
   - apache-airflow
   - apache-airflow-providers-apache-spark
   - apache-airflow-providers-postgres
   - apache-airflow-providers-microsoft-azure

Você pode instalar as dependências com o seguinte comando:
~~~~bash
pip install -r requirements.txt
~~~~

## Como Executar
Executando o projeto pelo docker:

~~~~bash
docker-compose up --build
~~~~
O processo ETL será iniciado automaticamente e os dados transformados estarão disponíveis na pasta silver.

   ✅ Dica: Se você já executou anteriormente e não precisa reconstruir a imagem, use apenas docker-compose up.
   
## Estrutura do Código

│ **load_data_from_web.py**
   ### Este script executa a extração pela web dos dados. Ele realiza as seguintes operações:
   Baixa os dados: Abre os dados abertos em https://dados.es.gov.br e procura pelos arquivos da bolsa capixaba.
   Salva csv: Por fim, deixa os dados na camada bronze pra realizar o tratamento mais tarde.

│ **process_data.py**

   ### Este script contém o pipeline ETL. Ele realiza as seguintes operações:
   
   Leitura dos dados: O script lê arquivos dos diretórios de entrada (bronze), verificando o tipo de 
   cada arquivo (CSV, Parquet, JSON).
   
   Aplicação das transformações: Aplica as transformações nas colunas do DataFrame, como renomeação e formatação.
   
   Gravação dos dados: Os dados tratados são gravados no formato Parquet no diretório de saída (silver).
   
   ### Funções de Transformação
   rename_cols(df): Renomeia as colunas do DataFrame para nomes mais legíveis.
   
   cast_col_types(df): Converte tipos de dados para garantir consistência (ex.: de string para numérico).
   
   format_benefit_value(df): Formata os valores de benefícios, garantindo que os dados estejam no formato correto.
   
# Contribuindo
Contribuições são **bem-vindas!** Sinta-se à vontade para abrir um pull request ou reportar issues.

1. Fork o projeto

2. Crie uma branch para a sua feature (git checkout -b feature/feature-name)

3. Faça as mudanças necessárias

4. Commit suas alterações (git commit -am 'Add new feature')

5. Push para a branch (git push origin feature/feature-name)

6. Abra um pull request para a branch main


