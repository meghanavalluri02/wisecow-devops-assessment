# 🐄 Wisecow DevOps Assessment

[![CI/CD Pipeline](https://github.com/meghanavalluri02/wisecow-devops-assessment/actions/workflows/cicd.yml/badge.svg)](https://github.com/meghanavalluri02/wisecow-devops-assessment/actions)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-wisecow--devops-blue)](https://hub.docker.com/r/meghanavalluri/wisecow-devops/tags)

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


## Problem Statement 2: Python Monitoring Scripts

Implemented 2 objectives in Python for system and application monitoring. Scripts located in `scripts/` folder. Both use `psutil` and `requests` libraries for cross-platform compatibility.

### 1. System Health Monitoring Script (Objective 1)
- **File:** `scripts/system_health.py`
- **Description:** Monitors CPU, memory, disk usage, and running processes. Alerts to console and log file if thresholds exceeded (CPU > 80%, Memory > 80%, Disk > 85%, Processes > 500).
- **Features:** Continuous monitoring (every 60 seconds), logging to `system_health.log`, formatted reports.
- **Run:** `python scripts/system_health.py`
- **Test:** Run script; open multiple apps to spike CPU/memory for alerts. Stop with Ctrl+C.
- **Example Output:**


🖥️ System Health Monitor Started...
System Health Report - 2025-09-20 11:30:25
CPU: 20.9% (OK)
🚨 MEMORY ALERT: 83.1% usage (threshold: 80%)
Disk: 55.4% (211GB free)
Processes: 368

- **Log:** `system_health.log` records alerts with timestamps.

### 2. Application Health Checker Script (Objective 4)
- **File:** `scripts/app_health_checker.py`
- **Description:** Checks HTTP status of Wise Cow app (localhost:4499). Reports UP (status 200) or DOWN (error/timeout/non-200). Includes response time.
- **Features:** Continuous monitoring (every 30 seconds), logging to `app_health.log`, handles timeouts/connections.
- **Run:** `python scripts/app_health_checker.py` (start Wise Cow Docker first: `docker run -p 4499:4499 wisecow:latest`)
- **Test:** Run script with app running (UP); stop Docker for DOWN test. Stop with Ctrl+C.
- **Example Output (UP):**

🌐 Application Health Monitor Started...
Application Health Report - 2025-09-20 11:50:15
✅ Wise Cow Application: UP | Status: 200 | Response: 0.08s
📊 Health Summary:
UP: 1/1 applications
✅ Wise Cow Application: UP

- **Example Output (DOWN):**

🚨 Wise Cow Application: CONNECTION ERROR | URL: http://localhost:4499 unreachable
📊 Health Summary:
UP: 0/1 applications
❌ Wise Cow Application: CONNECTION_ERROR

- **Log:** `app_health.log` records UP/DOWN with timestamps/response times.

### Problem Statement 2 Requirements Mapping
| Objective | Status | Implementation | Evidence |
|-----------|--------|----------------|----------|
| **System Health Monitoring** | ✅ COMPLETE | CPU/memory/disk/processes with alerts | `system_health.py`, console/log output |
| **Application Health Checker** | ✅ COMPLETE | HTTP status/uptime with error handling | `app_health_checker.py`, UP/DOWN tests |



