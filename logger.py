import logging

class initLogger:
    def __init__(self, config):
        logging.basicConfig(level=logging.DEBUG,
                    format=config.getLogDataFormat(),
                    datefmt=config.getLogDateFormat(),
                    filename=config.getLogPath()+'\\'+config.getLogFile(),
                    filemode=config.getLogWriteMode())

    def writeInfo(self, message):
        logging.info(message)

    def writeDebug(self, message):
        logging.debug(message)

    def writeWarning(self, message):
        logging.warning(message)
    
    def writeError(self, message):
        logging.error(message)

    def writeCritical(self, message):
        logging.critical(message)