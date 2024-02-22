## Description
University Applicants Management system built using principles of Domain Driven Design with Hexagonal Architecture (also known as Clean Architecture).

Here we have Entities - Applicants, Users, Programmes, Statistics, Notification  whose relationships have been exploited to create CRUD endpoint in REST & GRPC under OpenAPI standard.

## Tools Used
  - Python3.12
  - Postgres
  - SMTP
  - FastAPI
  - Poetry
  - Sqlalchemy
  - Uvicorn
  - Pydantic

## Installation

**- db(alembic)
alembic upgrade head: apply every migrations
alembic downgrade base: rollback every migrations
alembic revision --autogenerate -m "revision_name": create new migration
alembic history: get alembic revision history
How to migration
Create or modify models from app/model/*.py
alembic -x ENV=[dev|stage|prod] revision --autogenerate -m "revision_name"
Check auto generated migration file from app/migrations/versions/*.py
alembic -x ENV=[dev|stage|prod] upgrade head
If ENV does not exist, it will be applied to the test.
server
uvicorn app.main:app --reload: base
options
host: --host 0.0.0.0
port: --port 8000
test
pytest: base
pytest --cov=app --cov-report=term-missing: coverage with stdout
pytest --cov=app --cov-report=html: coverage with html**


- Open `localhost:8000/docs` for API Documentation

- Open `localhost:8000/graphql` for GraphQL Documentation

_*Note:* In case you are not able to access `pipenv` from you `PATH` locations, replace all instances of `pipenv` with `python3 -m pipenv`._

## Testing

For Testing, `unittest` module is used for Test Suite and Assertion, whereas `pytest` is being used for Test Runner and Coverage Reporter.

- Run the following command to initiate test:
  ```sh
  $ pipenv run pytest
  ```
- To include Coverage Reporting as well:
  ```sh
  $ pipenv run pytest --cov-report xml --cov .
  ```

## License

&copy; MIT License