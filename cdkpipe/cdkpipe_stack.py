from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lmb,
    aws_apigateway as apigw,
    CfnOutput
    #    core
    # aws_sqs as sqs,
)
from os import path
from constructs import Construct


class CdkpipeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        this_dir = path.dirname(__file__)
        handler = lmb.Function(self, 'Handler',
                               runtime=lmb.Runtime.PYTHON_3_7,
                               handler='handler.handler',
                               code=lmb.Code.from_asset(path.join(this_dir, 'lambda')))

        gw = apigw.LambdaRestApi(self, 'Gateway',
                                 description='Endpoint for web service powered by aws lambda',
                                 handler=handler.current_version)

        self.url_output = CfnOutput(self, 'Url',
                                    value=gw.url)
        # example resource
        # queue = sqs.Queue(
        #     self, "CdkpipeQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
