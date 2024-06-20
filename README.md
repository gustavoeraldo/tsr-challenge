# tsr-challenge


## Requirements

* Have python > 3.10 installed
* Docker

## Setup

1. Install pipenv:
```bash 
pip install pipenv`
```

2. Create .venv folder in the project directory:
```bash
mkdir .venv
```

3. Activate the virtual environment:
```bash
pipenv shell
```

4. Install the project dependencies:

```bash
pipenv install
```

## Run the project

Once the setup is done, you can run the project with:
```bash
uvicon main:app --reload
```

Or you can also run by vscode debugger. If everything
has gone ok so far, you will be able to access the api in the [browser](http://localhost:8000/docs#/).


## Alembic

```bash
# To run migrations
$ alembic upgrade head

# Run a new migration
$ alembic revision -m "revision description"

# To rollback a migration
# alembic downgrade -<number of migration>
$ alembic downgrade -1
```