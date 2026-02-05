class Logger:
    def log(self, message: str):
        raise NotImplementedError


class ConsoleLogger(Logger):
    def log(self, message: str):
        print("🖥 LOG:", message)


class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message: str):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")


logger = ConsoleLogger()
logger.log("Tizim ishga tushdi")
