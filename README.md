Sample app deployment from docker to Amazon EC2

# Sample Docker App CI/CD

This project demonstrates deploying a sample application from GitHub Actions to Docker Hub and AWS EC2 using a fully automated CI/CD pipeline.

---

## 🚀 Features
- Build Docker images from source code
- Push images to Docker Hub with multiple tags (`latest`, commit SHA, release tag)
- Deploy container to AWS EC2 via SSH
- Automatic versioning using GitHub release tags (e.g., `v1.0.1`, `v1.0.2`)

---

## 📋 Prerequisites
- Docker installed locally
- AWS EC2 instance with Docker installed
- GitHub repository with Actions enabled
- Configured GitHub Secrets:
  - `DOCKER_USERNAME` → Docker Hub username
  - `DOCKER_PASSWORD` → Docker Hub access token
  - `EC2_HOST` → EC2 public IP/DNS
  - `EC2_SSH_KEY` → contents of your `.pem` private key

---

## ⚙️ Setup
Clone the repository and build locally:
```bash
git clone <repo-url>
cd sample-docker
docker build -t easygodevops/sample-app .
docker run -p 80:3000 easygodevops/sample-app


🔄 CI/CD Workflow
The pipeline is defined in .github/workflows/ci-cd.yml:

**Build Job**

Triggered on push to main or when a GitHub release tag (v*) is created

Builds Docker image

Pushes to Docker Hub with tags:

latest

commit SHA

GitHub release tag (e.g., v1.0.1)

**Deploy Job**

Runs after build completes

SSHs into EC2

Pulls the latest image (or release tag)

Stops/removes old container

Runs new container on port 80
=============================================================================

After deployment we can also verify 
<img width="763" height="333" alt="Sample docker deployment" src="https://github.com/user-attachments/assets/fc09b1cb-57c6-4306-9b94-72744697a4a8" />





