#!/bin/bash

#Exit Immediately if a command fails
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running tests..."
pytest --html=reports/report.html --self-contained-html

echo "Test report saved at: reports/report.html"