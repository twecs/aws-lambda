import logging
import os

import twecs.aws.lambda_
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

    parameters['api_key'] = os.environ['WISE_API_KEY']

    parameters['base_url'] = configuration['WISE_API_BASE_URL']

    twecs.wise.set_up_transfer(
        **parameters,
    )

    return None


entry_point = twecs.aws.lambda_.bind(
    handler=handler,
)
