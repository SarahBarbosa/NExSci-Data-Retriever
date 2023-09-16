import os
import pandas as pd
from datetime import datetime
import pytz

class ExoplanetDownloader:
    """
    Classe para baixar dados de exoplanetas da NExSci e salvar em arquivos CSV.

    Parâmetros:
    -----------
    data_directory : str
        O diretório onde os arquivos CSV serão salvos.

    Métodos:
    --------
    download_confirmed_planets():
        Baixa os dados de todos os exoplanetas confirmados com default_flag=1 e salva em um arquivo CSV.

    download_pscomppars():
        Baixa os dados da tabela PSCompPars e as referências associadas e salva em arquivos CSV.

    Exemplo de Uso:
    ---------------
    import nexsci_data_retriever as ndr
    notebook_directory = '/caminho/do/seu/diretorio'
    downloader = ndr.ExoplanetDownloader(notebook_directory)

    downloader.download_confirmed_planets()
    downloader.download_pscomppars()
    """

    def __init__(self, data_directory):
        """
        Inicializa uma instância do ExoplanetDownloader.

        Parâmetros:
        -----------
        data_directory : str
            O diretório onde os arquivos CSV serão salvos.
        """
        self.url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query='
        self.data_directory = data_directory

    def download_confirmed_planets(self):
        """
        Baixa os dados de todos os exoplanetas confirmados com default_flag=1 e salva em um arquivo CSV.
        """
        tt = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%m/%d/%Y, %H:%M:%S")
        print(f'>> {tt} Baixando todos os exoplanetas confirmados da NExSci...')
        
        print('>> Baixando default_flag = 1')
        where = 'where+default_flag=1'
        full = self.url + 'select+*+from+ps+' + where + '&format=csv'
        df = pd.read_csv(full, low_memory=False)
        
        print('>> Salvando o dataframe de exoplanetas...')
        file_name = 'exoplanetas.csv'
        df.to_csv(os.path.join(self.data_directory, file_name), index=False)
        
        print('>> Concluído!')

    def download_pscomppars(self):
        """
        Baixa os dados da tabela PSCompPars e as referências associadas e salva em arquivos CSV.
        """
        print('>> Baixando PSCompPars')
        pscomppars = 'select+*+from+pscomppars+&format=csv'
        full_pscomppars = self.url + pscomppars
        pscomppars_table = pd.read_csv(full_pscomppars, low_memory=False)
        
        print('>> Acessando referências...')
        columns = ['pl_nome'] + [col for col in pscomppars_table.columns if col.endswith("reflink")]
        pscomppars_table = pscomppars_table[columns]
        
        print('>> Salvando a tabela de referências...')
        file_name = 'referencias.csv'
        pscomppars_table.to_csv(os.path.join(self.data_directory, file_name), index=False)
        
        print('>> Concluído!')
