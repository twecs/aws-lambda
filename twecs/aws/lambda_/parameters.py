import logging

import twecs.aws.lambda_

boto3_client_ssm = twecs.aws.lambda_.boto3_session.client(
    'ssm',
)

logger = logging.getLogger(
    __name__,
)


def retrieve(
        path,
    ):
    parameters = {
    }

    paginator = boto3_client_ssm.get_paginator(
        'get_parameters_by_path',
    )

    iterator = paginator.paginate(
        PaginationConfig={
            'MaxItems': 20,
        },
        Path=parameters_path,
        WithDecryption=True,
    )

    for response in iterator:
        for parameter in response['Parameters']:
            name = parameter['Name']
            value = parameter['Value']
            parameters[name] = value

    return parameters
