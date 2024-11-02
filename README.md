# TalentNavigator_Backend
# The Backend Setup Azure Dev 

 

cd into the project root folder 

python –m venv venv 

Source venv/bin/activate or venv\Scripts\activate 

pip install poetry 

poetry install  

az login 

Make sure core/.env.local is setup for the deployment you are testing (dev, qa, prod) 

DB Setup (One time only) 

cd core 

poetry run alembic upgrade head 

Run init_db.py 

Run init_roles.py 

Run init_users.py 

python manage.py run_app (here the default env is already 'local') 

 

 

 

# The Backend Setup (Local Standalone) 

 

Clone azurite repo 

Cd azurite folder or (npm install -g azurite)->)(azurite) 

Npm install  

npm config set strict-ssl false 

Npm run start(npm run azurite 

 

cd into the project root folder 

python –m venv venv 

Source venv/bin/activate or venv\Scripts\activate 

pip install poetry 

poetry install  

Make sure core/.env.local-standalone is setup 

Set ENV=local-standalone or export ENV=local-standalone 

DB Setup (One time only) 

cd core 

Delete database.db (if exists) 

poetry run python core\db\init_db.py 

poetry run python core\db\init_roles.py 

poetry run python core\db\init_user_roles.py 

python manage.py run_app 

 

 

# .env.local-standalone 

SERVER_HOSTNAME=0.0.0.0 

SERVER_HOSTNAME_STR=localhost 

SERVER_HOSTNAME_EXTERNAL_PORT=8000 

SERVER_PORT=8000 

APPLICATION_ROOT=/ 

PREFERRED_URL_SCHEME=http 

CORS_ORIGINS=http://localhost:3000 

OPENAI-API-KEY=xxx 

GOOGLE-API-KEY=xxx 

OPENAI_MODEL_NAME=gpt-4o 

OPENAI_DEPLOYMENT_NAME=gpt-4o 

LLM_PROVIDER=openai 

SERPER-API-KEY=xxx 

AGENTOPS-API-KEY=xxx 

SECRET-KEY=abc123 

ADMIN-USERNAME=admin 

ADMIN-PASSWORD=adminpassword 

ADMIN-EMAIL=admin@example.com 

ENABLE_AGENT_OPS=false 

AZURE-STORAGE-CONNECTION-STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;" 
 

DB_ENV=development 

DATABASE_URL=sqlite:///./database.db 

 

 

# .env.local 

AUTH_PROVIDER=azure_ad 

SERVER_HOSTNAME=0.0.0.0 

SERVER_HOSTNAME_STR=localhost 

SERVER_HOSTNAME_EXTERNAL_PORT=8000 

SERVER_PORT=8000 

APPLICATION_ROOT=/ 

PREFERRED_URL_SCHEME=http 

CORS_ORIGINS=http://localhost:3000 

OPENAI_MODEL_NAME=gpt-4o 

OPENAI_DEPLOYMENT_NAME=gpt-4o 

AZURE_OPENAI_VERSION="2024-02-15-preview" 

AZURE_OPENAI_VERSION_GPT_4O="2024-02-15-preview" 

AZURE_OPENAI_VERSION_GPT_4="2024-05-01-preview" 

AZURE_OPENAI_DEPLOYMENT="gpt-4o" 

AZURE_OPENAI_MODEL="gpt-4o" 

AZURE_OPENAI_ENDPOINT="https://staffingcopilot-openai-dev.openai.azure.com/" 

LLM_PROVIDER=Azure 

ENABLE_AGENT_OPS=false 

DB_ENV=production 

POSTGRES_HOST=staffingcopilot-postgresql-dev.postgres.database.azure.com 

POSTGRES_PORT=5432 

POSTGRES_DB=portico_db 

POSTGRES_PARAMS=?sslmode=require 

KEY_VAULT_URL="https://staffingcopilot-kv-dev.vault.azure.net" 

AZURE_AD_FE_TENANT_ID=189de737-c93a-4f5a-8b68-6f4ca9941912 

AZURE_AD_FE_CLIENT_ID=7926d248-5ca8-41f9-a4cc-3be58fcbf4aa 
