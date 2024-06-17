# tsr-challenge


```bash

# To run migrations
$ alembic upgrade head

# Run a new migration
$ alembic revision -m "revision description"

# To rollback a migration
# alembic downgrade -<number of migration>
$ alembic downgrade -1
```