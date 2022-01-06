import logging
import inspect


class BaseClass:
    def getLogger(self):
        loggerName  = inspect.stack()[1][3]
        logger      = logging.getLogger(loggerName)

        # File object
        file   = logging.FileHandler('logfile.log',mode='w+')

        # Log format
        format = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file.setFormatter(format)


        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        logger.debug("a debug statement is executed")
        logger.info("information message")
        logger.warning("warning messge")
        logger.error("error message")
        logger.critical("critical message")
        return logger


