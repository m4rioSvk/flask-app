# Flask App — Learning Project

A simple Python Flask web API built for learning Azure DevOps and CI/CD pipelines.

## What this app does

Two API endpoints that return JSON data:

| Endpoint | Description |
|----------|-------------|
| `/` | Returns a hello message and status |
| `/about` | Returns app info and author |

## How the pipeline works

```
Your PC → push to GitHub → Azure pipeline runs on Microsoft's VM
                                      ↓
                           installs Flask + runs tests
                                      ↓
                           ✅ pass (code is good)
                                      ↓
                    [later] deploy to Azure App Service
                                      ↓
                           🌍 public URL anyone can access
```

## Project structure

```
flask-app/
├── app.py                  # Flask web API (2 endpoints)
├── test_app.py             # 5 automated tests
├── requirements.txt        # Python dependencies
├── azure-pipelines.yml     # CI pipeline definition
└── README.md               # This file
```

## How to run locally

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

App will be available at `http://localhost:5000`

## How to run tests

```bash
pytest test_app.py -v
```

Expected output:
```
test_app.py::test_home_status_code        PASSED
test_app.py::test_home_returns_message    PASSED
test_app.py::test_about_status_code       PASSED
test_app.py::test_about_returns_author    PASSED
test_app.py::test_unknown_route_returns_404 PASSED

5 passed in 0.18s
```

## What the pipeline does on every push

1. Spins up a fresh Ubuntu VM on Azure
2. Installs Python 3.12
3. Installs Flask + pytest from `requirements.txt`
4. Runs all 5 tests
5. Reports pass ✅ or fail ❌
6. VM is destroyed

## Key concepts learned

- **Flask** — Python web framework for building APIs
- **REST API** — server that returns JSON data instead of HTML pages
- **Virtual environment** — isolated Python installation per project
- **pytest** — automated testing framework
- **CI Pipeline** — automatically verifies code on every push
- **requirements.txt** — list of dependencies the pipeline installs
