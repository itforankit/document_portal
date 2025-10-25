# Project Setup Guide

## Create Project Folder and Environment Setup

```bash
# Create a new project folder
mkdir <project_folder_name>

# Move into the project folder
cd <project_folder_name>

# Open the folder in VS Code
code .

# Create a new Conda environment with Python 3.10
conda create -p <env_name> python=3.10 -y

# Activate the environment (use full path to the environment)
conda activate <path_of_the_env>
source /Users/ankitsinghal/AI_workspace/document_portal/.venv/bin/activate
# Install dependencies from requirements.txt
pip install -r requirements.txt

# Initialize Git
git init

# Stage all files
git add .

# Commit changes
git commit -m "<write your commit message>"

# Push to remote (after adding remote origin)
git push

# Cloning the repository
git clone https://github.com/sunnysavita10/document_portal.git
```
## Minimum Requirements for the Project

### LLM Models
- **Groq** (Free)
- **OpenAI** (Paid)
- **Gemini** (15 Days Free Access)
- **Claude** (Paid)
- **Hugging Face** (Free)
- **Ollama** (Local Setup)

### Embedding Models
- **OpenAI**
- **Hugging Face**
- **Gemini**

### Vector Databases
- **In-Memory**
- **On-Disk**
- **Cloud-Based**

## API Keys

### GROQ API Key
- [Get your API Key](https://console.groq.com/keys)  
- [Groq Documentation](https://console.groq.com/docs/overview)

### Gemini API Key
- [Get your API Key](https://aistudio.google.com/apikey)  
- [Gemini Documentation](https://ai.google.dev/gemini-api/docs/models)


## testing steps of docker image in local
1. Download the docker and dowcker desoktop in your system
2. run the docker engine in your system
3. first create the codker file
4. build the image form current project
5. run the image inside the container
6. if everytinf is fine running then push the image in to dockerhub

### Deployment
github action [will have to write the yaml configuration]
ECR for containing the docker image similiar to docker but in AWS native place
ECS+Fargate [this is for the image orchestration, it's serverless service]



## test docker with below command
Open terminal
docker help
docker --version
docker ps
docker ps -a ## for the containers

## Build a docker image
# build dcoker image
docker build -t document-portal-app
## 

# run docker container
docker run -d -p 8080:8080 --name doc-portal document-portal-app

## pushing to docker hub
docker tag document-portal-system itforankit/document-portal-system:latest
docker push itforankit/document-portal-system:latest

#running test3