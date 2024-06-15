# Mapping the basics cli commands of Alembic

## Create a new migration

```bash
# alembic revision -m "revision description"
$ alembic revision -m "create users table"
```

## Run the migrations

```bash
$ alembic upgrade head

# or run a specific migraion
# alembic upgrade <migration id>
$ alembic upgrade 133962d1058b
```

## Rollback migration

```bash
# alembic downgrade -<number of migrations>
$ alembic downgrade -1

# or alembic downgrade <migration id>
$ alembic downgrade 133962d1058b
```
