# Portico Backend Mono Repo

This monorepo contains multiple projects related to platform runtime, crew management, and more.

## Table of Contents

- [Getting Started](#getting-started)
- [Directory Structure](#directory-structure)
- [Setting Up the Environment](#setting-up-the-environment)
- [Running the Projects](#running-the-projects)
- [Testing](#testing)
- [Linting and Formatting](#linting-and-formatting)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to set up and run the projects in this monorepo.

### Prerequisites

- Python 3.11 or higher
- Poetry for dependency management
- Docker (if using Docker for services like databases)
- VS Code (recommended for development)

## Directory Structure

```plaintext

|____.flake8                        # Formatting Settings
|____crews                          # Crew AI Crew Definition Module
| |____crews
| |____pyproject.toml
| |____tests
| |____README.md
| |____.env.example                 # Local Crew Module Testing Environment (Template)
| |____poetry.toml
| |____poetry.lock
|____core                           # Portico Core Platform Runtime
| |____core
| |____|____db                      # DB Models
| |____|____routes                  # API Blueprints
| |____|____services                # API Services
| |____|____static                  # API Services
| |____|___|______api
                |____swagger.json   # API Swagger Definitions
| |____alembic.ini                  # DB Config Alembic
| |____pyproject.toml
| |____tests                        # Core Platform Tests
| |____README.md
| |____.env
| |____crew_config.json             # Dynamic Crew Configuration Used To Load Crews and Runtime
| |____poetry.toml
| |____alembic                      # DB Alembic Scripts
| |____.env.example                 # Platform Runtime Environment Config (Template)
| |____poetry.lock
| |____database.db                  # SQLLite DB for Local Testing
|____pyproject.toml
|____libs
| |____tests
| |____libs
| |____|____azure                   # Azure Storage Services
| |____|____crewai                  # CrewAI Tools and Utils
| |____|____file                    # File Based Utils
| |____README.md
| |____poetry.toml
| |____poetry.lock
|____README.md
|____.gitignore
|____manage.py                      # Mono Repo Manager Utility to setup and run app, tests, lint etc.
|____poetry.lock
|____.vscode
| |____settings.json                # VS Code Settings for MonoRepo Intellisense, Flake8 etc.
```

### Setting Up the Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/gen-aitech/portico_be_mono.git
   cd portico_be_mono
   ```

2. Install Poetry if not already installed:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:

   ```bash
   poetry install --no-root
   ```

4. Set up environment variables:

   - In the core folder
   - Copy the `.env.example` file to `.env` and update the variables accordingly.
   - For example:

      ```plaintext
      SERVER_HOSTNAME=0.0.0.0
      SERVER_HOSTNAME_STR=localhost
      SERVER_PORT=8000
      APPLICATION_ROOT=/
      PREFERRED_URL_SCHEME=http
      OPENAI_MODEL_NAME=gpt-3.5-turbo-0125

      ADMIN_USERNAME=admin
      ADMIN_PASSWORD=adminpassword

      AZURE-STORAGE-CONNECTION-STRING=<ADD CONNECTION STRING>
      BlobEndpoint=<ADD_BLOB_ENDPOINT>
      AZURE_STORAGE_ENDPOINT=<ADD_AZURE_STORAGE_END_POINT>

      # For development, uncomment the below 2 lines and comment the lines below that
      DB_ENV=development
      DATABASE_URL=sqlite:///./database.db
      # For production, comment the above 2 lines and uncomment the following lines
      # DB_ENV=production
      # POSTGRES-USER=<Key Vault>
      # POSTGRES-PASSWORD=<Key Vault>
      # POSTGRES_HOST=<Server Name>
      # POSTGRES_PORT=28575
      # POSTGRES_DB=defaultdb
      # POSTGRES_PARAMS=?sslmode=require

     ```

     ```bash
     cp .env.example .env
     ```

     - Note: CrewAI seems to be requiring AGENTOPS_API_KEY to be defined to work properly. Create that with `AGENTOPS_API_KEY=xxx` if you don't have a key

5. Initialize pre-commit hooks:

   ```bash
   poetry run pre-commit install
   ```

### Install Dependencies

To install the dependencies for all projects in the monorepo, run:

```bash
python manage.py install
```


# Run Core App

```bash
python manage.py run_app
```

# Lint Code

```bash
python manage.py lint
```

# Format Code

```bash
python manage.py format
```

# Run Tests

```bash
python manage.py test
```

# Run with PM2

```
pm2 start manage.py --interpreter /usr/bin/python3 --name portico_be -- run_app
```

# Run the app

```bat
set ENV=local && poetry run python manage.py run_app
```

```bash
ENV=local poetry run python manage.py run_app
```
