import logging
import os


def get_logger(name=__name__, log_file=None, log_level=logging.INFO):
    """default log level INFO"""
    logger = logging.getLogger(name)
    fmt = "%(asctime)s %(filename)s %(lineno)d: %(message)s"
    datefmt = "%y-%m-%d %H:%M:%S"
    logging.basicConfig(format=fmt, datefmt=datefmt)
    if log_file is not None:
        log_file_folder = os.path.split(log_file)[0]
        if log_file_folder:
            os.makedirs(log_file_folder, exist_ok=True)
        fh = logging.FileHandler(log_file, "w", encoding="utf-8")
        fh.setFormatter(logging.Formatter(fmt, datefmt))
        logger.addHandler(fh)
    logger.setLevel(log_level)
    return logger


logger = get_logger()
