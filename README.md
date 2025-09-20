# 🐄 Wisecow DevOps Assessment

[![CI/CD Pipeline](https://github.com/meghanavalluri02/wisecow-devops-assessment/actions/workflows/cicd.yml/badge.svg)](https://github.com/meghanavalluri02/wisecow-devops-assessment/actions)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-wisecow--devops-blue)](https://hub.docker.com/r/meghanavalluri/wisecow-devops)

**Complete implementation of Accuknox DevOps Trainee Assessment - Problem Statement 1**

## 🎯 Requirements Mapping

| Requirement | Status | Implementation | Evidence |
|-------------|--------|----------------|----------|
| **Dockerization** | ✅ | Ubuntu 22.04 + fortune, cowsay, netcat | `Dockerfile`, `docker run -p 4499:4499` |
| **Kubernetes** | ✅ | 2-replica Deployment, NodePort Service | `deployment.yaml`, `service.yaml`, `kubectl get pods` |
| **Service Exposure** | ✅ | Port-forward (8080), NodePort (30080) | `kubectl port-forward`, `minikube service` |
| **CI/CD Pipeline** | ✅ | GitHub Actions → Docker Hub | [Pipeline](https://github.com/meghanavalluri02/wisecow-devops-assessment/actions) |
| **TLS Implementation** | ✅ | Self-signed cert + K8s secret | `generate-tls.bat`, `kubectl get secret wisecow-tls` |
| **Public Repo** | ✅ | All artifacts hosted | [Repo](https://github.com/meghanavalluri02/wisecow-devops-assessment) |
| **Documentation** | ✅ | This README | - |

## 🚀 Quick Start

### Prerequisites
- Docker Desktop
- Minikube
- kubectl
- Git

### Setup
```bash
git clone https://github.com/meghanavalluri02/wisecow-devops-assessment.git
cd wisecow-devops-assessment
minikube start --driver=docker
docker build -t wisecow:latest .
minikube image load wisecow:latest
kubectl apply -f deployment.yaml -f service.yaml
kubectl port-forward svc/wisecow-service 8080:80

Visit: http://localhost:8080

HTTPS Access:
generate-tls.bat
kubectl port-forward svc/wisecow-service 8443:80

Visit: https://localhost:8443 (click "Proceed" on warning)


📂 Project Structure
.
├── Dockerfile          # Builds Wisecow container
├── deployment.yaml     # 2-replica Kubernetes deployment
├── service.yaml        # NodePort service (port 30080)
├── generate-tls.bat    # TLS certificate generator
├── wisecow.sh          # Wisecow application script
├── certs/             # TLS certificates (tls.crt, tls.key)
├── .github/workflows/ # CI/CD pipeline
│   └── cicd.yml       # GitHub Actions workflow
└── README.md          # This file

🔧 CI/CD Pipeline
File: .github/workflows/cicd.yml
Triggers: Push/pull to main
Actions: Builds Docker image, pushes to Docker Hub
Status: Check Runs

🔐 TLS Setup
Certificate: Self-signed (RSA 2048-bit, 365 days)
Secret: kubectl create secret tls wisecow-tls --cert=certs/tls.crt --key=certs/tls.key

🧪 Testing
Docker: docker run -p 4499:4499 wisecow:latest → http://localhost:4499
Kubernetes: kubectl get pods (2/2 Running)
Load Balancing: Refresh http://localhost:8080 10x
HTTPS: https://localhost:8443 with warning bypass

