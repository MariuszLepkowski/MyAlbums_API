## Requirements

- Python 3.10+
- Docker


## Setup 
```bash
# Clone the repo
git clone https://github.com/MariuszLepkowski/MyAlbums_API
```

## Run with Docker

```bash
# Start the app
docker-compose up

# Stop the app
docker-compose down
```
Visit: http://localhost:5000

# Database Configuration

This project uses PostgreSQL with SQLAlchemy as ORM.

Database settings are configured via .env file:
```
DB_USER=your_db_name
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
DB_HOST=db
DB_PORT=5432
```

You can customize these as needed. The db service in docker-compose.yml will create the database automatically.

## First-time Setup with SQLAlchemy

To begin using the database:

## 1. Initialize database (tables)

```commandline
docker-compose exec web flask shell
```

Inside the shell:
```commandline
from app.extensions import db
db.create_all()
```

That will create all tables in the connected Postgres DB.

## Optional: Database Migrations with Flask-Migrate

This project includes Flask-Migrate for database version control.
It allows you to update database schema safely as models evolve.

## 1. Initialize migrations (only once):

```commandline
docker-compose exec web flask db init
```

##  2. After changing or adding models:

```commandline
docker-compose exec web flask db migrate -m "Describe your changes"
docker-compose exec web flask db upgrade
```

This will generate and apply Alembic migrations inside the migrations/ directory.

You can use this instead of db.create_all() once migrations are initialized.