import logging

class Registros:
    """Classe que gerencia os logs do sistema. 

    Atributos:
        str (arquivo): 
    """
    def __init__(self, arquivo_log='app.log') -> None:
        self.logger = logging.getLogger("Logging")
        self.logger.setLevel(logging.DEBUG)

        # Criar um manipulador de arquivo
        manipulador_arquivo = logging.FileHandler(arquivo_log)
        manipulador_arquivo.setLevel(logging.DEBUG)

        # Definir o formato dos logs
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        manipulador_arquivo.setFormatter(formatter)

        # Adicionar os manipuladores ao logger
        self.logger.addHandler(manipulador_arquivo)

    def debug(self, msg: str) -> None:
        """Cria mensagem de Debug.

        Retorna:
            None.
        """
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        """Cria mensagem de informação.

        Retorna:
            None.
        """
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        """Cria mensagem de atenção.

        Retorna:
            None.
        """
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """Cria mensagem de erro.

        Retorna:
            None.
        """
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        """Cria mensagem crítica.

        Retorna:
            None.
        """
        self.logger.critical(msg)