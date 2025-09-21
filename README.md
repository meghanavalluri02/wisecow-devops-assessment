Wisecow DevOps Assessment



**Complete Accuknox DevOps Trainee Assessment - Problem Statement 1**

## Requirements Mapping

| Requirement | Status | Implementation | Evidence |
|-------------|--------|----------------|----------|
| Dockerization | ✅ | Ubuntu 22.04 + fortune, cowsay, netcat | `Dockerfile`, `docker run -p 4499:4499` |
| Kubernetes | ✅ | 2-replica Deployment, NodePort Service | `deployment.yaml`, `service.yaml`, `kubectl get pods` |
| Service Exposure | ✅ | Port-forward (8080), NodePort (30080) | `kubectl port-forward`, `http://localhost:8080` |
| CI/CD Pipeline | ✅ | GitHub Actions → Docker Hub | [Actions](https://github.com/meghanavalluri02/wisecow-devops-assessment/actions) |
| TLS Implementation | ✅ | Self-signed cert + K8s secret | `generate-tls.bat`, `kubectl get secret wisecow-tls` |
| Public Repo | ✅ | All artifacts hosted | [Repo](https://github.com/meghanavalluri02/wisecow-devops-assessment) |
| Documentation | ✅ | This README | - |

## Quick Start

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
# Visit: http://localhost:8080
```

### HTTPS Access
```bash
generate-tls.bat
kubectl port-forward svc/wisecow-service 8443:80
# Visit: https://localhost:8443 (click "Proceed")
```

## Project Structure
```
.
├── Dockerfile          # Container build
├── deployment.yaml     # K8s deployment (2 replicas)
├── service.yaml        # NodePort service (30080)
├── generate-tls.bat    # TLS cert generator
├── wisecow.sh          # Wise cow app
├── certs/              # TLS certs
├── .github/workflows/  # CI/CD
│   └── cicd.yml
└── README.md
```

## CI/CD Pipeline
- **File:** `.github/workflows/cicd.yml`
- **Trigger:** Push to main
- **Action:** Build → Docker Hub push
- **Status:** [Check Actions](https://github.com/meghanavalluri02/wisecow-devops-assessment/actions)

## TLS Setup
```bash
generate-tls.bat
kubectl create secret tls wisecow-tls --cert=certs/tls.crt --key=certs/tls.key
```

## Testing
- **Docker:** `docker run -p 4499:4499 wisecow:latest` → `http://localhost:4499`
- **K8s:** `kubectl get pods` (2/2 Running) → `kubectl port-forward ... 8080:80`
- **Load Balance:** Refresh `localhost:8080` multiple times
- **HTTPS:** `https://localhost:8443` (ignore warning)

## Problem Statement 2: Python Scripts


### System Health Monitor
- **File:** `scripts/system_health.py`
- **Monitors:** CPU, memory, disk, processes
- **Alerts:** >80% usage to console/log
- **Run:** `python scripts/system_health.py`
- **Log:** `system_health.log`

### App Health Checker
- **File:** `scripts/app_health_checker.py`
- **Checks:** Wise Cow HTTP status (UP/DOWN)
- **Run:** `docker run -p 4499:4499 wisecow:latest` then `python scripts/app_health_checker.py`
- **Log:** `app_health.log`
=======
Evidence
Pods: 3/3 Running (kubectl get pods -n kube-system | findstr kubearmor) 
Policy: Applied (kubectl get ksp wisecow-network-audit) 
Violation: 100% packet loss on ICMP ping
Legitimate: HTTP port 4499 works normally 


## Problem Statement 3: KubeArmor (Bonus)

- **Install:** Helm chart in kube-system
- **Policy:** `kubearmor-policy.yaml` - Audit ICMP traffic
- **Violation:** Ping blocked (100% packet loss)
- **Evidence:** Screenshots in repo

