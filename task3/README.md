# GitLab CI/CD Pipeline for Docker Image Build and Test

This project contains a GitLab CI/CD pipeline for building and testing a Docker image with an Apache server.

## Pipeline Stages

### 1. Build Stage

- Uses `docker:dind` service and `docker:latest` image.
- Builds the Docker image tagged `apache-image` from `../task2/`.
- Runs the container on port 12345.
- Waits 5 seconds for the container to start.

### 2. Test Stage

- Uses `python:3.9` image.
- Installs `requests` and `beautifulsoup4`.
- Executes `health_check.py` from `../task4/` to check the container's health.

## Setup

1. Configure GitLab CI/CD in your repository.
2. Add the above code to your `.gitlab-ci.yml` file.
3. Ensure `Dockerfile` and `docker-compose.yml` are in `../task2/`, and `health_check.py`
