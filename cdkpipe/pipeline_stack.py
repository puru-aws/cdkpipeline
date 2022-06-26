from aws_cdk import (
    # Duration,
    Stack,
    aws_codepipeline as codepipeline,
    aws_apigateway as apigw,
    aws_codepipeline_actions as cpactions,
    pipelines,
    aws_secretsmanager as sm
    #    core
    # aws_sqs as sqs,
)
from os import path
from constructs import Construct


class PipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipelines.Cdkpipelines(self, 'Pipeline',
                               cloud_assembly_artifact=cloud_assembly_artifact,
                               pipeline_name='cdkPipeline',
                               source_action=cpactions.GitHubSourceAction(
                                   action_name='GitHub',
                                   output=source_artifact,
                                   oauth_token=sm.Secret.from_secret_attributes(self, "ImportedSecret",
                                                                                secret_complete_arn="arn:aws:secretsmanager:eu-west-1:039738803183:secret:github-token-efCyDf",
                                                                                )))
