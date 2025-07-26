# 🧪 Task Manager API - QA Automation & DevOps Portfolio Project

Welcome to my QA Automation + DevOps showcase project. This repo demonstrates how to build a reliable, testable, and containerized API testing pipeline using modern tools and best practices.

--

## Project Goal

The goal of this project is to simulate a real-world QA Automation + DevOps workflow by:

- Writing API tests using `pytest`
- Running tests inside Docker containers
- Automating test pipelines with GitHub Actions
- Adding logging, error handling, and load testing
- Demonstrating CI/CD skills and Linux fundamentals

---

## 🔧 Tech Stack

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| Python + Pytest | Writing and running API tests       |
| Docker       | Containerization of tests              |
| Docker Compose | Running app + test environments      |
| GitHub Actions | CI/CD pipeline for automation        |
| Locust       | Load testing under stress              |
| Logging      | Debugging and observability            |
| Linux        | Shell scripting, permissions, basics   |

---

## Test Coverage

✅ **10 API tests** written in `pytest`, including:

- Availability & response codes
- POST/GET/DELETE functionality
- Parametrized endpoint tests
- Response time checks
- Invalid data tests
- Logging and error handling

📁 Output:
- HTML report (`reports/report.html`)
- Log file (`reports/test.log`)

--

## Load Testing
Used locust to simulate user load and monitor performance thresholds.

--

<details>
<summary><strong>📁 Project Structure</strong></summary>

```bash
task-manager-api/
├── .github/
│   └── workflows/
│       └── pytest.yml               # CI/CD pipeline with GitHub Actions
├── reports/
│   ├── report.html                  # Pytest HTML report (auto-generated)
│   └── test.log                     # Log output from tests
├── tests/
│   ├── __init__.py
│   ├── confest.py
│   └── test_api.py                  # Main API test suite using pytest
├── utils/
│   └── logger.py                    # Reusable logger config
├── .gitignore                       # Ignores logs, reports, venv, etc.
├── docker-compose.yml              # Runs app and test containers
├── requirements.txt                # Python dependencies
├── run.sh                          # Bash script to run tests locally
├── test.sh                         # Bash script to run tests inside Docker
└── README.md                       # Project documentation
```

</details>