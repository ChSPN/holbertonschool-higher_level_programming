# Docker Project #
This repository contains files and configurations for the Docker project developed as part of the Holberton School curriculum.

## Project Overview ##
This project focuses on creating and managing Docker containers to encapsulate and run applications. The main objectives include:
- Learning Docker fundamentals
- Building Docker images
- Running Docker containers
- Managing Docker volumes and networks

## Repository Structure ##
- Dockerfile: Contains the instructions to build the Docker image.
- config.txt: Configuration file with necessary parameters.
- .github/workflows: Contains GitHub Actions workflows for CI/CD.

## Getting Started ##
To build and run the Docker container:
- Clone the repository:
git clone https://github.com/ChSPN/holbertonschool-docker_project.git
cd holbertonschool-docker_project
- Build the Docker image:
 docker build -t my-docker-project .
- Run the Docker container:
 docker run -d -p 80:80 my-docker-project

## License ##
