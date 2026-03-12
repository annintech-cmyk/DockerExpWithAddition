
```markdown
# Python Docker App - PostElevenLabs

## Overview

This is a simple Python Docker application that demonstrates how to containerize Python scripts. The project contains two Python files:

- `add.py` – Contains the addition function or logic.  
- `result.py` – Imports `add.py` and runs the main script to show the result.

Docker is used to package the app so it can run in an isolated environment without worrying about local Python dependencies.

---

## Project Structure

```

PostElevenLabs
│
├── src/
│   ├── add.py
│   └── result.py
├── Dockerfile
├── README.md
├── requirements.txt   # Optional if dependencies exist
└── .venv/ ❌ ignored

````

---

## Dockerfile Explained

Here’s what the Dockerfile does:

```dockerfile
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy Python scripts into the container
COPY src/add.py .
COPY src/result.py .

# Set the default command to run the main script
CMD ["python", "result.py"]
````

* `FROM python:3.11-slim` – Uses a lightweight Python 3.11 base image.
* `WORKDIR /app` – Sets the working directory inside the container.
* `COPY` – Copies your Python files into the container.
* `CMD` – Defines the command that runs when the container starts.

---

## Build and Run with Docker

1. **Build the Docker image**:

```bash
docker build -t python-docker-app .
```

2. **Run the Docker container**:

```bash
docker run --rm python-docker-app
```

* `--rm` automatically removes the container after it finishes.
* The output from `result.py` will appear in your terminal.

---

## Notes

* This app is **self-contained**; Python dependencies are handled in the Docker container.
* You can expand the Dockerfile to include a `requirements.txt` if your scripts need external libraries:

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```

---

## References

* [Docker Official Documentation](https://docs.docker.com/get-started/)
* [Python Docker Images](https://hub.docker.com/_/python)

```



### **Command**

```bash
docker push annintech/maddition-app:tagname
```

* `annintech` → Your Docker Hub username
* `maddition-app` → Name of the Docker image (repository)
* `tagname` → The tag/version of the image (like `latest` or `v1.0`)

---

### **Steps to push your Docker image**

1. **Log in to Docker Hub** (if not already):

```bash
docker login
```

It will prompt for your Docker Hub username and password.

2. **Tag your local image** (if you didn’t already):

```bash
docker tag python-docker-app annintech/maddition-app:latest
```

* `python-docker-app` → the image you built locally
* `annintech/maddition-app:latest` → the repository and tag on Docker Hub

3. **Push to Docker Hub**:

```bash
docker push annintech/maddition-app:latest
```

4. **Verify on Docker Hub**:
   Go to `https://hub.docker.com/r/annintech/maddition-app` and you should see your image.

---

✅ After this, anyone can pull and run your image:

```bash
docker pull annintech/maddition-app:latest
docker run --rm annintech/maddition-app:latest
```

