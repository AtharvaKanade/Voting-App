# 🐱 vs 🐶 Voting App

A simple two-tier web application where users can vote for either Cats or Dogs and see live results update in real time. Built as part of a DevOps assignment to demonstrate Git, Docker, and Kubernetes workflows.

---

## What the App Does

- Presents users with a voting page with two options: **Cats** or **Dogs**
- Records each vote into a **PostgreSQL** database
- Displays live vote counts and a visual progress bar for each option
- Results update every time the page is loaded after a vote

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend / API | Python, Flask |
| Database | PostgreSQL 15 |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes (Minikube) |
| Version Control | Git, GitHub |

---

## Project Structure
```
voting-app/
├── app/
│   ├── app.py              # Flask application (routes, DB logic)
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Multi-stage Docker build
│   └── templates/
│       └── index.html      # Frontend UI
├── k8s/
│   ├── postgres-secret.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── app-deployment.yaml
│   └── app-service.yaml
├── docker-compose.yml
└── README.md
```

---

## How to Run

### Option 1 — Using Docker Compose (Recommended for local dev)

Make sure Docker is installed and running, then:
```bash
docker compose up --build
```

Visit: `http://localhost:5000`

To stop:
```bash
docker compose down
```

---

### Option 2 — Using Kubernetes (Minikube)

Make sure Minikube and kubectl are installed.

**1. Start Minikube**
```bash
minikube start
```

**2. Point Docker to Minikube's environment**
```bash
eval $(minikube docker-env)
```

**3. Build the image inside Minikube**
```bash
docker build -t voting-app:latest ./app
```

**4. Apply all manifests**
```bash
kubectl apply -f k8s/postgres-secret.yaml
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml
kubectl apply -f k8s/app-deployment.yaml
kubectl apply -f k8s/app-service.yaml
```

**5. Get the app URL**
```bash
minikube service voting-app-service --url
```

Open the URL in your browser and start voting!

---

## Environment Variables

The Flask app reads these environment variables for database configuration:

| Variable | Description | Default |
|---|---|---|
| `DB_HOST` | PostgreSQL host | `localhost` |
| `DB_NAME` | Database name | `votingdb` |
| `DB_USER` | Database user | `postgres` |
| `DB_PASSWORD` | Database password | `password` |

These are automatically set by Docker Compose and Kubernetes manifests.

---