import json
import logging

import twecs.aws.lambda_
import twecs.aws.lambda_.secrets
import twecs.wise

boto3_client_sns = twecs.aws.lambda_.boto3_session.client(
    'sns',
)

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

    transfer = twecs.wise.set_up_transfer(
        **parameters,
    )

    notification_topic_arn = configuration['NOTIFICATION_TOPIC_ARN']
    logger.debug(
        'ARN of the SNS topic for notification: %s',
        notification_topic_arn,
    )

    transfer_str = json.dumps(
        obj=transfer,
        indent=None,
    )

    boto3_client_sns.publish(
        Message=transfer_str,
        TopicArn=notification_topic_arn,
    )

    return None


entry_point = twecs.aws.lambda_.bind(
    handler=handler,
)
