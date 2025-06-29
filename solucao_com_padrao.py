class LoggerSingleton:
    """
    Uma classe de logger que implementa o padrão Singleton.
    Garante que só uma instância exista.
    """
    _instance = None

    def __new__(cls):
        """
        Sobrescreve o método __new__ para controlar a criação de instâncias.
        """
        if cls._instance is None:
            print("Criando a ÚNICA instância do Logger Singleton.")
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
            cls._instance.log_file = "app_log_singleton.txt"
        else:
            print("A instância já existe. Retornando a instância existente.")
        return cls._instance

    def log(self, message):
        """Escreve uma mensagem no arquivo de log."""
        with open(self.log_file, "a") as f:
            f.write(f"LOG: {message}\n")

print("--- Solução com o padrão ---")

logger1 = LoggerSingleton()
logger1.log("Mensagem 1. Esta é a primeira instância.")

logger2 = LoggerSingleton()
logger2.log("Mensagem 2. Usando a mesma instância.")


print(f"logger1 é o mesmo objeto que logger2? {logger1 is logger2}")

