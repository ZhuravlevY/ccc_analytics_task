import boto3
import io
import logging

from utils._helpers import to_bytes


logger = logging.getLogger(__name__)


def upload_string_to_s3(s3_client: boto3.client,
                        data: str,
                        bucket_name: str,
                        path: str) -> bool:

    """Upload string data to S3 bucket"""

    try:
        logger.info(f"[upload_string_to_s3] - Start - "
                    f"bucket_name={bucket_name} "
                    f"path={path}")

        data = to_bytes(data, encoding="utf-16")
        s3_client.upload_fileobj(io.BytesIO(data),
                                 bucket_name,
                                 path)
        logger.info("[upload_string_to_s3] - End processing")
        return True
    except Exception as ex:
        logger.error(repr(ex))
