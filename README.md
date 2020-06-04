# aws-dask-sm-fargate
Perform data science and ML with Dask on AWS SageMaker and Fargate.

# Installation Instructions

## PreReqs
1.  Install AWS CLI - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
2.  Install Docker - https://docs.docker.com/get-docker/

## Dask Fargate Installation
1.  Clone this repo to your workstation
1.  From repo root: cd ECS-Dask; tar -xzf base-image.tar.gz; cd base-image
1.  Create ECR repo "dask" using this doc - https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html
1.  Login to your ECR repo from aws cli. Get login command from "View Push Commands" from your ECR repo AWS console  
1.  Build docker dask image: docker build -t dask .
1.  Tag image: docker tag dask:latest <AWS Account ID>.dkr.ecr.us-west-2.amazonaws.com/dask:latest
1.  Push image to ECR repo: docker push <AWS Account ID>.dkr.ecr.us-west-2.amazonaws.com/dask:latest
1.  Use CloudFormation Console to provision Fargate cluster using dask-cluster.template 
    1.  Outbound Internet connectivity is required for package downloads. If deploying to private subnet, ensure NAT gateway route to internet exists
1.  Provision SageMaker Notebook instance from AWS SageMaker console, choose VPC/Subnet/Security Group used in previous step
1.  Open SageMaker Notebook and upload the example dask-sm-fargate-example1.ipynb file for testing.
 

