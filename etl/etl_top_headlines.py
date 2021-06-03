import yaml
import boto3
import logging
from datetime import datetime
from newsapi import NewsApiClient
from os import path

from utils.api_utils import get_top_headlines, get_sources_id
from utils.s3_utils import upload_string_to_s3

DAG_FOLDER_PATH = path.dirname(__file__)
CONFIG_PATH = path.join(DAG_FOLDER_PATH, "..", "config")
CONFIG_FILE_NAME = "config.yml"

with open(path.join(CONFIG_PATH, CONFIG_FILE_NAME), 'r') as fl:
    cfg = yaml.safe_load(fl)
    AWS_ACCESS_KEY_ID = cfg["s3_file_sink"]["aws_access_key_id"]
    AWS_SECRET_ACCESS_KEY = cfg["s3_file_sink"]["aws_secret_access_key"]
    BUCKET_NAME = cfg["s3_file_sink"]["bucket_name"]
    API_KEY = cfg["etl_sources"]["news_api"]["api_key"]

news_api = NewsApiClient(api_key=API_KEY)

client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

logger = logging.getLogger(__name__)


def store_top_headlines_ito_s3():

    """Get live top and breaking headlines for English sources and store them in S3 bucket"""

    logger.info("[store_top_headlines_ito_s3] - Start processing")
    for source_attr in get_sources_id(news_api=news_api, language="en"):
        top_headlines = str(get_top_headlines(news_api=news_api, sources=source_attr.id))
        current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = f"test/{source_attr.name}/{current_timestamp}_headlines.csv"
        upload_string_to_s3(s3_client=client,
                            data=top_headlines,
                            bucket_name=BUCKET_NAME,
                            path=file_path)
    logger.info("[store_top_headlines_ito_s3] - End processing")