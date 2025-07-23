import logging

def get_logger(name="pytest"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

        # Log to file
        file_handler = logging.FileHandler("reports/test.log", mode="w")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Log to console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger