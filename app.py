import pathlib

import aws_cdk as cdk
from aws_cdk import aws_lambda as lambda_

app = cdk.App()
stack = cdk.Stack(app, "request-test-lambda-stack")

# LambdaLayer
layer = lambda_.LayerVersion(
    stack,
    "layer",
    layer_version_name="x86_64_curl_test_layer",
    description="Layer to execute cURL commands",
    code=lambda_.Code.from_asset(
        str(pathlib.Path(__file__).resolve().parent.joinpath("runtime/layer")),
    ),
    compatible_architectures=[lambda_.Architecture.X86_64],
)

# Function
lambda_.Function(
    stack,
    "function",
    description="Test with cURL command",
    code=lambda_.Code.from_asset(
        str(pathlib.Path(__file__).resolve().parent.joinpath("runtime/function")),
    ),
    runtime=lambda_.Runtime.PYTHON_3_9,
    architecture=lambda_.Architecture.X86_64,  # ARM_64では動かない
    handler="index.handler",
    layers=[layer],
)

app.synth()
