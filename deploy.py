import argparse
from pathlib import Path
import boto3

def get_command_line_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', '-e', type=Path, default="non-prod")
    return parser.parse_args()

def deploy(env: str='non-prod', region_name: str='us-west-2') -> None:
    """Deploy to the specified environment. To be completed in DE-3365
    
    Args:
        env: The environment to deploy to. Valid values are 'non-prod' and 'prod'.
    """
    print(f'Deploying to {env} in {region_name}')
    client = boto3.client('glue', region_name=region_name)
    identity = boto3.client('sts').get_caller_identity()
    print(f'AWS Account ID: {identity.get("Account")}, Arn: {identity.get("Arn")}')

if __name__ == '__main__':
    arguments = get_command_line_arguments()
    deploy(arguments.env)