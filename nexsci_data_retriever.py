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
    overwrite : bool, opcional
        Se True, os arquivos serão sobregravados se já existirem. Se False, um aviso será emitido.

    Métodos:
    --------
    download_confirmed_planets():
        Baixa os dados de todos os exoplanetas confirmados com default_flag=1 (indica que são 
        parâmetros padrões) e salva em um arquivo CSV.

    download_pscomppars():
        Baixa os dados da tabela PSCompPars e as referências associadas e salva 
        em arquivos CSV.

    Exemplo de Uso:
    ---------------
    import nexsci_data_retriever as ndr

    notebook_directory = '/caminho/do/seu/diretorio'
        
    downloader = ndr.ExoplanetDownloader(notebook_directory, overwrite=False)

    downloader.download_confirmed_planets()
    downloader.download_pscomppars()
    """

    BASE_URL = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query='
    CONFIRMED_PLANETS_QUERY = 'select+*+from+ps+where+default_flag=1&format=csv'
    PSCOMPPARS_QUERY = 'select+*+from+pscomppars&format=csv'
    CONFIRMED_PLANETS_FILENAME = 'exoplanetas.csv'
    PSCOMPPARS_FILENAME = 'referencias.csv'

    def __init__(self, data_directory, overwrite=False):
        """
        Inicializa uma instância do ExoplanetDownloader.

        Parâmetros:
        -----------
        data_directory : str
            O diretório onde os arquivos CSV serão salvos.
        overwrite : bool, opcional
            Se True, os arquivos serão sobregravados se já existirem. Se False, um aviso será emitido.
        """
        self.data_directory = data_directory
        self.overwrite = overwrite

    def download_confirmed_planets(self, include_catalog_name=False,
                                   include_errors=False,
                                   include_system=False,
                                   include_photometry=False,
                                   file_name='exoplanetas.csv'):
        """
        Baixa os dados de todos os exoplanetas confirmados com default_flag=1 e 
        salva em um arquivo CSV.

        Parâmetros:
        -----------
        include_catalog_name : bool, opcional
            Se True, inclui colunas de outros catálogos (HD, HIP, TIC, GAIA).
        include_errors : bool, opcional
            Se True, inclui colunas de incertezas para os parâmetros.
        include_system: bool, opcional
            Se True, inclui colunas referentes ao sistema planetário (movimento e posição).
        include_photometry : bool, opcional
            Se True, inclui colunas de fotometria.
        file_name : str, opcional
            Nome do arquivo CSV de saída.
        """
        try:
            tt = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%m/%d/%Y, %H:%M:%S")
            print(f'>> {tt} Baixando todos os exoplanetas confirmados da NExSci...')
            
            print('>> Baixando default_flag = 1')
            full_url = self.BASE_URL + self.CONFIRMED_PLANETS_QUERY
            df = pd.read_csv(full_url, low_memory=False)

            columns_to_remove = ['default_flag', 'soltype', 'pl_controv_flag',
                                 'rv_flag', 'pul_flag', 'ptv_flag', 'tran_flag', 
                                 'ast_flag', 'obm_flag', 'micro_flag', 'etv_flag', 
                                 'ima_flag', 'dkin_flag', 'pl_nnotes', 'pl_refname',
                                 'st_refname', 'rowupdate', 'pl_pubdate', 'releasedate',
                                 'st_nphot', 'st_nrvc', 'pl_ntranspec', 'pl_nespec',
                                 'st_nspec', 'sy_refname', 'rastr', 'decstr']
            df.drop(columns_to_remove, axis=1, inplace=True)

            if not include_catalog_name:
                df.drop(['hd_name', 'hip_name', 'tic_id', 'gaia_id'], axis=1, inplace=True)
            
            if not include_errors:
                columns_to_remove = [col for col in df.columns if col.endswith(("err1", "err2", "lim", "str"))]
                df.drop(columns_to_remove, axis=1, inplace=True)
            
            if not include_system:
                if not include_errors:
                    system_columns = ['sy_pm', 'sy_pmra', 'sy_pmdec', 'sy_dist', 'sy_plx', 
                                      'ra', 'dec', 'glat', 'glon', 
                                      'elat', 'elon']
                else:
                    system_columns = [
                    'sy_pm', 'sy_pmerr1', 'sy_pmerr2', 'sy_pmra', 'sy_pmraerr1', 'sy_pmraerr2', 
                    'sy_pmdec', 'sy_pmdecerr1', 'sy_pmdecerr2', 'sy_dist', 'sy_disterr1', 
                    'sy_disterr2', 'sy_plx', 'sy_plxerr1', 'sy_plxerr2', 'ra', 'raerr1', 'raerr2',
                    'dec', 'decerr1', 'decerr2', 'glat', 'glaterr1', 'glaterr2', 'glon', 'glonerr1', 
                    'glonerr2', 'elat', 'elaterr1', 'elaterr2', 'elon', 'elonerr1', 'elonerr2'
                    ]

                df.drop(system_columns, axis=1, inplace=True)
            
            if not include_photometry:
                if not include_errors:
                    photometry_columns = ['sy_bmag', 'sy_vmag', 'sy_jmag', 'sy_hmag',
                    'sy_kmag','sy_umag', 'sy_gmag', 'sy_rmag', 'sy_imag', 'sy_zmag', 'sy_w1mag', 
                    'sy_w2mag', 'sy_w3mag', 'sy_w4mag', 'sy_gaiamag', 'sy_icmag', 'sy_tmag', 
                    'sy_kepmag']
                else:
                    photometry_columns = ['sy_bmag', 'sy_bmagerr1', 'sy_bmagerr2', 'sy_vmag', 'sy_vmagerr1', 'sy_vmagerr2', 
                    'sy_jmag', 'sy_jmagerr1', 'sy_jmagerr2', 'sy_hmag', 'sy_hmagerr1', 'sy_hmagerr2', 
                    'sy_kmag', 'sy_kmagerr1', 'sy_kmagerr2', 'sy_umag', 'sy_umagerr1', 'sy_umagerr2', 
                    'sy_gmag', 'sy_gmagerr1', 'sy_gmagerr2', 'sy_rmag', 'sy_rmagerr1', 'sy_rmagerr2', 
                    'sy_imag', 'sy_imagerr1', 'sy_imagerr2', 'sy_zmag', 'sy_zmagerr1', 'sy_zmagerr2', 
                    'sy_w1mag', 'sy_w1magerr1', 'sy_w1magerr2', 'sy_w2mag', 'sy_w2magerr1', 'sy_w2magerr2', 
                    'sy_w3mag', 'sy_w3magerr1', 'sy_w3magerr2', 'sy_w4mag', 'sy_w4magerr1', 'sy_w4magerr2', 
                    'sy_gaiamag', 'sy_gaiamagerr1', 'sy_gaiamagerr2', 'sy_icmag', 'sy_icmagerr1', 'sy_icmagerr2', 
                    'sy_tmag', 'sy_tmagerr1', 'sy_tmagerr2', 'sy_kepmag', 'sy_kepmagerr1', 'sy_kepmagerr2'
                    ]
                
                df.drop(photometry_columns, axis=1, inplace=True)

            file_path = os.path.join(self.data_directory, file_name)
            if os.path.isfile(file_path) and not self.overwrite:
                print('>> Arquivo já existe. Use overwrite=True para sobregravar.')
            else:
                print('>> Salvando o dataframe de exoplanetas...')
                df.to_csv(file_path, index=False)
                print(f'>> Arquivo salvo como {file_path}')
                print('>> Concluído!')
        except Exception as e:
            print(f'Erro durante o download de exoplanetas: {str(e)}')


    def download_pscomppars(self):
        """
        Baixa os dados da tabela PSCompPars e as referências associadas e salva em arquivos CSV.
        """
        try:
            print('>> Baixando PSCompPars')
            full_url = self.BASE_URL + self.PSCOMPPARS_QUERY
            pscomppars_table = pd.read_csv(full_url, low_memory=False)
            
            file_path = os.path.join(self.data_directory, self.PSCOMPPARS_FILENAME)
            if os.path.isfile(file_path) and not self.overwrite:
                print('>> Arquivo já existe. Use overwrite=True para sobregravar.')
            else:
                print('>> Acessando referências...')
                columns = ['pl_nome'] + [col for col in pscomppars_table.columns if col.endswith("reflink")]
                pscomppars_table = pscomppars_table[columns]
                
                print('>> Salvando a tabela de referências...')
                pscomppars_table.to_csv(file_path, index=False)
                print('>> Concluído!')
        except Exception as e:
            print(f'Erro durante o download de PSCompPars: {str(e)}')