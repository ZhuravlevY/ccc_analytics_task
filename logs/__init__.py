import yaml
import logging.config
from os import path

DAG_FOLDER_PATH = path.dirname(__file__)
CONFIG_PATH = path.join(DAG_FOLDER_PATH, "..", "config")
CONFIG_FILE_NAME = "log_config.yml"

with open(path.join(CONFIG_PATH, CONFIG_FILE_NAME), 'r') as fl:
    cfg = yaml.safe_load(fl)
    logging.config.dictConfig(cfg)

