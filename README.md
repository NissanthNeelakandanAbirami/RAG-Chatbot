This project allows you to build a PDF Reader application that integrates with AWS Bedrock to use Amazon Titan Embeddings. The application processes PDF files and creates a vector store using FAISS and stores it in Amazon S3.

Setup Instructions

Step 1: Clone the Repository

git clone <your-repository-url>
cd <repository-folder>

Step 2: Set Up Virtual Environment

Create a virtual environment:

python3 -m venv .venv

Activate the virtual environment:

source .venv/bin/activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Configure AWS Credentials

Ensure your AWS credentials are correctly set up using the following command:

aws configure

Access Key ID: Your IAM user's access key

Secret Access Key: Your IAM user's secret access key

Region: us-east-1

Step 5: Verify Bedrock Access

Make sure you have access to the Titan Embeddings v2 model in AWS Bedrock. You can check this by running:

aws bedrock list-foundation-models --region us-east-1

Step 6: Build Docker Image

Ensure you're in the correct directory containing the Dockerfile.

Build the Docker image:

docker build -t pdf-reader-admin .

Step 7: Run the Docker Container

Run the Docker container with the necessary environment variables and port mapping:

docker run -e BUCKET_NAME=<your-s3-bucket-name> -v ~/.aws:/root/.aws -p 8083:8083 -it pdf-reader-admin

Replace <your-s3-bucket-name> with the name of your S3 bucket.

Step 8: Access the Application

Once the container is running, open your browser and navigate to:

http://localhost:8083

Step 9: Test the Application

You can upload a PDF file through the interface to start processing and creating the vector store.

Docker Commands Summary

Command

Description

docker build -t pdf-reader-admin .

Build the Docker image

docker run -e BUCKET_NAME=<bucket> -v ~/.aws:/root/.aws -p 8083:8083 -it pdf-reader-admin

Run the Docker container

Common Issues

AccessDeniedException

If you see an AccessDeniedException when calling the InvokeModel operation, ensure that:

Your IAM user has the AmazonBedrockFullAccess policy attached.

You have requested access to the Titan Embeddings v2 model in AWS Bedrock.

Unable to Locate Credentials

Ensure your AWS credentials are set up correctly in ~/.aws/credentials or use the following command:

aws configure

Model Not Found Error

Verify that you're using the correct model ID:

amazon.titan-embed-g1-text-02

Restart Your Environment (Optional)

If issues persist, restart your terminal, Docker, or VS Code to ensure all credentials are loaded properly.

Developed by Nissanth Neelakandan Abirami
