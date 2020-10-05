# aws-dask-sm-fargate
Perform data science and ML with Dask on AWS SageMaker and Fargate.

# Architecture

![aws-dask-fargate-arch](./solution-arch.png)

## Prerequisites
1. Install docker - https://docs.docker.com/get-docker/
2. Install AWS CLI - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

## Implementing Distributed Dask on AWS Fargate


1. Log into your AWS account and choose your region
2. Clone this project: https://github.com/rvvittal/aws-dask-sm-fargate and from project root: cd ECS-Dask/base-image
3. Build docker dask image: docker build -t dask .
4. Create ECR repo "dask" using the following instruction: - https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html
5. Login to your ECR repo from AWS CLI. Get login command from "View Push Commands" from your ECR repo AWS console.
6. Tag the dask image you built earlier for registering it into ECR.  Get this command from "View Push Commands" from your ECR repo AWS console. 
7. Push the above tagged dask image to ECR. Get this command from "View Push Commands" from your ECR repo AWS console. 
8. Use CloudFormation Console to provision resources using dask-fargate-main.template located in project root.


## Setup Network Load Balancer for monitoring Fargate Dask Cluster

1. Navigate to Amazon ECS > Fargate Dask Cluster > Dask Scheduler Service > Tasks and select running task and copy the private IP for the running task
2. Navigate to EC2 > Target Groups and select the dask-scheduler-tg 
3. Select Targets and click Register targets
4. Select dask-vpc-main and paste the private IP from step 2 and click button - Include as pending below
5. Navigate to EC2 > Load Balancers and copy the DNS Name to browser tab to view the Dask Dashboard
   


## EDA on SageMaker notebook with Fargate Dask Cluster

1.  Navigate to Amazon ECS > Clusters and ensure Fargate-Dask-Cluster is running with 1 task each for Dask-Scheduler and Dask-Workersv
2.  Navigate to Amazon SageMaker > Notebook Instances > Open Jupyter and upload dask-sm-fargate-example.ipynb and dask-dashboard-ui.png files from project root
2.  Execute each cell of the notebook and observe the results. 
3.  Use the network load balancer public DNS to monitor the performance of the cluster as you execute the notebook cells.

