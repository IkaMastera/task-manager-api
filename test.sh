#!/bin/bash
set -e

# Check if Docker daemon is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker does not appear to be running."
    echo "💡 Please start Docker Desktop (or your Docker daemon) and try again."
    exit 1
fi

echo "🐳 Docker is running. Continuing..."

echo "Building Docker image..."
docker build -t test-runner .

echo "Running container and executing tests..."
docker run --rm -v $(pwd)/reports:/app/reports test-runner

echo "Test report generated in: ./reports/report.html"