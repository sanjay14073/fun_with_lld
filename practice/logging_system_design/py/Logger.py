import logging


class ApplicationLogger():
    '''
    ApplicationLogger is a singleton class that provides a global logging instance.
    '''
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            logger = logging.getLogger("ApplicationLogger")
            logger.setLevel(logging.INFO)

            if not logger.handlers:
                handler = logging.StreamHandler()
                formatter = logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )
                handler.setFormatter(formatter)
                logger.addHandler(handler)
            cls.__instance.logger = logger
        return cls.__instance
    
    def log(self, msg):
        '''
        Log a message with the given level.
        :param level: Logging level
        :param msg: Message to log
        '''
        self.logger.info(msg)

# Usage example
logger1 = ApplicationLogger()
logger2 = ApplicationLogger()
print(f"Are both logger instances the same? {logger1 is logger2}")  # Should print True

logger1.log("This is a log message from logger1.")
logger2.log("This is a log message from logger2.")