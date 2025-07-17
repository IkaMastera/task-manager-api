#!/bin/bash

#Exit Immediately if a command fails
set -e

echo "Checking for virtual environment..."
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

echo "Activating virtual envrionment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Running tests..."
pytest --html=reports/report.html --self-contained-html

echo "Test report saved at: reports/report.html"