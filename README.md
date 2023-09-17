# NASA Exoplanet Archive Data Retrieval

Este script em Python, `nexsci_data_retriever.py`, fornece uma classe chamada `ExoplanetDownloader` para baixar e salvar dados de exoplanetas do NExSci (NASA Exoplanet Science Institute) de forma rápida e eficiente. O script permite que você obtenha dois tipos de dados e os salve em arquivos CSV:

1. **Dados de Exoplanetas Confirmados**: Baixa dados de todos os exoplanetas confirmados com `default_flag=1` e os salva em um arquivo CSV.

2. **Tabela PSCompPars das Referências**: Baixa dados da tabela PSCompPars com apenas os dados de referência para os parãmetros estelares e planetários e também salva em um arquivo CSV.

> 🔭 Projeto futuro: Tabela com dados de Espectrocopia de Transmissão e Emissão de atmosferas de exoplanetas 

## Uso

1. Importe o módulo `nexsci_data_retriever`:

   ```python
   import nexsci_data_retriever as ndr
   ```

2. Inicialize uma instância da classe `ExoplanetDownloader` fornecendo o diretório onde os arquivos CSV serão salvos:

   ```python
   # import os
   # diretorio_do_notebook = os.getcwd()
   diretorio_do_notebook = '/seu/caminho/de/diretorio'
   downloader = ndr.ExoplanetDownloader(diretorio_do_notebook)
   ```

3. Baixe os dados desejados:

   - Para baixar dados de exoplanetas confirmados:

     ```python
     downloader.download_confirmed_planets()
     ```

   - Para baixar dados das referências:

     ```python
     downloader.download_pscomppars()
     ```
> ⚠️ **Observação**: Consulte [este link](https://exoplanetarchive.ipac.caltech.edu/docs/ps-conf-ext-mapping.pdf) para obter a lista completa da descrição das colunas.

## Requisitos

- Python 3.x
- pandas
- pytz

Certifique-se de ter esses pacotes instalados em seu ambiente Python antes de usar o script.

> Status do projeto: Em desenvolvimento
