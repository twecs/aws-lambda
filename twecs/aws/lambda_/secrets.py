import logging

import twecs.aws.lambda_

boto3_client_secretsmanager = twecs.aws.lambda_.boto3_session.client(
    'secretsmanager',
)

logger = logging.getLogger(
    __name__,
)


def retrieve(
        arn,
    ):
    response = boto3_client_secretsmanager.get_secret_value(
        SecretId=arn,
    )

    logger.debug(
        'ID of secret version retrieved: %s',
        response['VersionId'],
    )

    secret_value = response['SecretString']

    return secret_value
