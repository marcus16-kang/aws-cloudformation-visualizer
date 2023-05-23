import boto3
from botocore.config import Config

from cfn_visualizer import visualizer

client = boto3.client('cloudformation', config=Config(region_name='us-east-1'))

visualizer(client, stack_name='test-bastion-stack')
