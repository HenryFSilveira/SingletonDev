
class Logger:
    """Uma classe simples de logger, sem o padrão Singleton."""
    def __init__(self):
        print("Criando uma nova instância de Logger.")
        self.log_file = "app_log.txt"

    def log(self, message):
        """Escreve uma mensagem no arquivo de log."""
        with open(self.log_file, "a") as f:
            f.write(f"LOG: {message}\n")

print("--- Solução sem o padrão ---")

logger1 = Logger()
logger1.log("Primeira mensagem do Logger 1")

logger2 = Logger()
logger2.log("Segunda mensagem do Logger 2")

print(f"logger1 é o mesmo objeto que logger2? {logger1 is logger2}")

