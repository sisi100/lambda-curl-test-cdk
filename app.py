import pathlib

import aws_cdk as cdk
from aws_cdk import BundlingOptions, DockerImage
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as lambda_

app = cdk.App()
stack = cdk.Stack(app, "lambda-curl-test-stack")

# cURL用のレイヤーを作成する
layer = lambda_.LayerVersion(
    stack,
    "layer",
    description="Layer to execute cURL commands",
    code=lambda_.Code.from_asset(
        str(pathlib.Path(__file__).resolve().parent.joinpath(".layer")),
        bundling=BundlingOptions(
            # image=DockerImage(image="public.ecr.aws/sam/build-python3.9:latest-arm64"),
            image=DockerImage(image="public.ecr.aws/sam/build-python3.9:1.84.0-20230517004013-arm64"),
            user="root",
            command=[
                "bash",
                "-c",
                "&&".join(
                    [
                        "yum install curl",
                        "mkdir -p /asset-output/bin/",
                        "mkdir -p /asset-output/lib/",
                        "cp /bin/curl /asset-output/bin/",
                        "cp -r /usr/lib64/libcurl.* /asset-output/lib",
                        "cp -r /usr/lib64/libnghttp2.* /asset-output/lib",
                        "cp -r /usr/lib64/libidn2.* /asset-output/lib",
                        "cp -r /usr/lib64/libssh2.* /asset-output/lib",
                        "cp -r /usr/lib64/libldap-2.4.* /asset-output/lib",
                        "cp -r /usr/lib64/liblber-2.4.* /asset-output/lib",
                        "cp -r /usr/lib64/libunistring.* /asset-output/lib",
                        "cp -r /usr/lib64/libsasl2.* /asset-output/lib",
                        "cp -r /usr/lib64/libssl3.* /asset-output/lib",
                        "cp -r /usr/lib64/libsmime3.* /asset-output/lib",
                        "cp -r /usr/lib64/libnss3.* /asset-output/lib",
                    ]
                ),
            ],
        ),
    ),
    compatible_architectures=[lambda_.Architecture.ARM_64],
)

# Function
func = lambda_.Function(
    stack,
    "function",
    description="Test with cURL command",
    code=lambda_.Code.from_asset(
        str(pathlib.Path(__file__).resolve().parent.joinpath("runtime")),
    ),
    runtime=lambda_.Runtime.PYTHON_3_9,
    architecture=lambda_.Architecture.ARM_64,
    handler="index.handler",
    layers=[layer],
)


# 基本用途がVPCの中に入れて動作確認を想定してるので、VPCに入れられるようにしておく
func.role.add_managed_policy(
    iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaVPCAccessExecutionRole")
)

app.synth()
