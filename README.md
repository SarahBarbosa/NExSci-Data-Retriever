# NASA Exoplanet Archive Data Retrieval

> Status do projeto: Em desenvolvimento

Este script em Python, `nexsci_data_retriever.py`, fornece uma classe chamada `ExoplanetDownloader` para baixar e salvar dados de exoplanetas do NExSci (NASA Exoplanet Science Institute). O script permite que você obtenha dois tipos de dados e os salve em arquivos CSV:

1. **Dados de Exoplanetas Confirmados**: Baixa dados de todos os exoplanetas confirmados com `default_flag=1` e os salva em um arquivo CSV.

2. **Tabela PSCompPars e Referências**: Baixa dados da tabela PSCompPars junto com as referências associadas e as salva em arquivos CSV separados.

## Uso

1. Importe o módulo `nexsci_data_retriever`:

   ```python
   import nexsci_data_retriever as ndr
   ```

2. Inicialize uma instância da classe `ExoplanetDownloader` fornecendo o diretório onde os arquivos CSV serão salvos:

   ```python
   diretorio_do_notebook = '/seu/caminho/de/diretorio'
   downloader = ndr.ExoplanetDownloader(diretorio_do_notebook)
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

## Requisitos

- Python 3.x
- pandas
- pytz

Certifique-se de ter esses pacotes instalados em seu ambiente Python antes de usar o script.

## Observação

Este script busca dados no arquivo NExSci, portanto, é necessária uma conexão à internet ativa durante a execução. O script salva os dados baixados em arquivos CSV no diretório especificado.

---

Sinta-se à vontade para personalizar o script e adaptá-lo às suas necessidades específicas. Se você encontrar algum problema ou tiver dúvidas, consulte a documentação do arquivo NExSci para obter mais informações sobre os dados disponíveis e as opções de consulta.
