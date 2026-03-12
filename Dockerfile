# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files into /app
COPY src/add.py .
COPY src/result.py .

# Run the Python script
CMD ["python", "result.py"]