# NASA Exoplanet Archive Data Retrieval

Este script fornece a classe `ExoplanetDownloader` projetada para baixar dados de exoplanetas do NExSci e salvá-los como arquivos CSV. Esta classe simplifica o processo de obtenção de dados exoplanetários/estelares e oferece flexibilidade na escolha dos dados a serem incluídos. Em geral, ele permite que você obtenha dois tipos de dados e os salve em arquivos CSV:

1. **Dados de Exoplanetas Confirmados com default_flag = 1**;

2. **Tabela PSCompPars com as Referências associadas aos parâmetros estelares/planetários**.

## Clonando o Repositório

Para obter o código-fonte deste script, você pode clonar o repositório diretamente em seu sistema usando o seguinte comando:

```bash
git clone https://github.com/SarahBarbosa/NExSci-Data-Retriever.git
```

## Uso

1. Importe o módulo `nexsci_data_retriever`:

   ```python
   from nexsci_data_retriever import ExoplanetDownloader
   ```

2. Inicialize uma instância da classe `ExoplanetDownloader` fornecendo o diretório onde os arquivos CSV serão salvos:

   ```python
   import os
   diretorio_do_notebook = os.getcwd()
   downloader = ExoplanetDownloader(diretorio_do_notebook)
   ```

3. Baixe os dados desejados:

   - Para baixar dados de exoplanetas confirmados:

     ```python
     downloader.download_confirmed_planets()
     ```

   - Para baixar dados da tabela PSCompPars e referências associadas:

     ```python
     downloader.download_pscomppars()
     ```

> ⚠️ **Observação**: Consulte [este link](https://exoplanetarchive.ipac.caltech.edu/docs/ps-conf-ext-mapping.pdf) para obter a lista completa da descrição das colunas.

## Métodos 

```python
download_confirmed_planets(include_catalog_name=False,
                           include_errors=False,
                           include_system=False,
                           include_photometry=False,
                           file_name='exoplanetas.csv')
```
Aqui, você baixa os dados de todos os exoplanetas confirmados com `default_flag=1` (indicando parâmetros padrão) e os salva em um arquivo CSV.

- `include_catalog_name` (bool, opcional): Se True, inclui colunas de outros catálogos (HD, HIP, TIC, GAIA).
- `include_errors` (bool, opcional): Se True, inclui colunas de incertezas nos parâmetros.
- `include_system` (bool, opcional): Se True, inclui colunas relacionadas ao sistema planetário (movimento e posição).
- `include_photometry` (bool, opcional): Se True, inclui colunas de fotometria.
- `file_name` (str, opcional): Nome do arquivo CSV de saída.

## Requisitos

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Acknowledging the NASA Exoplanet Archive

This research has made use of the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program.

---

> 🔭 Projeto em desenvolvimento: Tabela com dados de Espectrocopia de Transmissão e Emissão de atmosferas de exoplanetas
