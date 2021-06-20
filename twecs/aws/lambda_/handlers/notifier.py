import importlib
import json
import logging

import twecs.aws.lambda_
import twecs.aws.lambda_.parameters

logger = logging.getLogger(
    __name__,
)


def handler(
        configuration,
        context,
        event,
    ):
    notifier_name = configuration['NOTIFIER']
    logger.debug(
        'notifier name: %s',
        notifier_name,
    )

    notifier_module = importlib.import_module(
        name=f'twecs.notifiers.{notifier_name}',
    )

    parameters = twecs.aws.lambda_.parameters.retrieve(
        path=configuration['PARAMETER_PATH'],
    )

    for transfer in event['Records']:
        notifier_module.execute(
            parameters=parameters,
            transfer=transfer,
        )


entry_point = twecs.aws.lambda_.bind(
    handler=handler,
)
