import logging


logging.basicConfig(
    filename='log.txt',
    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
    level=logging.INFO
)