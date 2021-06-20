#import functools
import logging
import os

import boto3

boto3_session = boto3.session.Session(
)

logger = logging.getLogger(
    __name__,
)


def bind(
        handler,
    ):
    #handler = functools.partial(
    #    twecs.drivers.aws.lambda.entry_point,
    #    handler=twecs.drivers.aws.lambda.handlers.wise.handler,
    #)
    def bound_entry_point(
            event,
            context,
        ):
        response = entry_point(
            context=context,
            event=event,
            handler=handler,
        )
        return response

    return bound_entry_point


def entry_point(
        context,
        event,
        handler,
    ):
    set_up_logging(
    )

    response = handler(
        configuration=os.environ,
        context=context,
        event=event,
    )

    return response


def set_up_logging(
    ):
    root_logger = logging.getLogger(
        name=None,
    )

    root_logger.setLevel(
        logging.DEBUG,
    )

    formatter = logging.Formatter(
        fmt='%(name)s: %(levelname)s: %(message)s',
        style='%',
    )

    for handler in root_logger.handlers:
        handler.setFormatter(
            formatter,
        )
