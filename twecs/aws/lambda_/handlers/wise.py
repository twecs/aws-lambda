import logging

import twecs.aws.lambda_
import twecs.aws.lambda_.secrets
import twecs.wise

logger = logging.getLogger(
    __name__,
)


def handler(
        configuration,
        context,
        event,
    ):
    parameters = {
        **event,
    }

    api_key = twecs.aws.lambda_.secrets.retrieve(
        arn=configuration['WISE_API_KEY_SECRET_ARN'],
    )
    parameters['api_key'] = api_key

    parameters['base_url'] = configuration['WISE_API_BASE_URL']

    twecs.wise.set_up_transfer(
        **parameters,
    )

    return None


entry_point = twecs.aws.lambda_.bind(
    handler=handler,
)
