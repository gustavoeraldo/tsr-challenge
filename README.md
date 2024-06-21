# tsr-challenge

## Requirements

You must have installed on your machine:

* Python > 3.10 installed
* Docker

## Basic Setup

1. Create .env file in the project directory:
```bash
# Command to create a .env file
touch .env
```

2. Add the env variables to the .env file
```bash
API_VERSION=1.0.0
DATABASE_URL=""
```

If you are running the application **locally**, add to .env file:
`DATABASE_URL="postgresql://postgres:postgres@localhost:5433/tsf_api"`

if you are using **Docker to run the application**, instead of the previous database url, use:
`DATABASE_URL="postgresql://postgres:postgres@pg_master/tsf_api"`


## Setup to run locally

1. Follow the previous setup, you should create the .env file.

2. Install pipenv globaly:

```bash 
pip install pipenv`
```

3. Create .venv folder in the project directory:

```bash
mkdir .venv
```

4. Activate the virtual environment:

```bash
pipenv shell
```

5. Install the project dependencies:

```bash
pipenv install
```

6. Start the database:

```bash
docker compose up -d pg_master
```

7. Run the migrations to create and insert data in the database:

```bash
alembic upgrade head
```

And then you can run the project.

## Run with Docker

1. Open the project directory and give the entrypoint chmod permissions.

```bash
chmod +x bin/entrypoint.sh
```

2. Build and start the database and application:
```bash
docker compose up -d
```

3. Acess the API in the [browser](http://localhost:8000/docs#/).

## Run the project manually

Once the setup is done, you can run the project with:
```bash
uvicon main:app --reload
```

Or you can also run by vscode debugger. If everything
has gone ok so far, you will be able to access the api in the [browser](http://localhost:8000/docs#/).
