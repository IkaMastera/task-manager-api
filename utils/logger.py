import logging

def get_logger(name="pytest"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

        
        file_handler = logging.FileHandler("reports/test.log",)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger