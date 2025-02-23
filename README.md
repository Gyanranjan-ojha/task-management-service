# Task Management Service

## Overview
A Secure and Dynamic Task Management System built with Django.

## Features

## Prerequisites

Before installing, ensure you have the following installed:

- Python (version 3.10 or higher)
- PostgreSQL Server (version 17 or higher)
- Git (latest version)

## Installation

**1. Clone the project**

```bash
  git clone https://github.com/Gyanranjan-ojha/task-management-service.git
```

**2. Navigate to the project directory**

```bash
  cd task-management-service
```

## Setup

- Create a virtual environment

```bash
  python -m venv .venv
```

- Activate the virtual environment

- For Ubuntu

```bash
  source venv/bin/activate
```

- For Windows

```bash
  venv/Scripts/activate
```

- Install python dependencies

```bash
  pip install -r requirements.txt
```

- .env Configuration

Create a `.env` file in the root directory and provide the necessary environment variables:

```bash
  CURRENT_ENV='<(development/test/production)>'
  DJANGO_SECRET_KEY='<provide any complex string>'
  DJANGO_ALLOWED_HOSTS='*'
  DB_HOST='<DB_HOST>'
  DB_USER='<DB_USER>'
  DB_PASSWORD='<DB_PASSWORD>'
  DB_NAME='<DB_NAME>'
  DB_PORT=<DB_PORT>
  EMAIL_HOST_USER='<email host user>'
  EMAIL_HOST_PASSWORD='<email host password>'
```

- Create database from .env file, if not exists.

```bash
  python create_db.py
```

- Create a "logs" folder inside the root folder

```bash
  mkdir logs
```

- Migrate the Database for creating tables by django commands

```bash
  python manage.py makemigrations accounts
  python manage.py makemigrations tasks
  python manage.py makemigrations
  python manage.py migrate accounts
  python manage.py migrate tasks
  python manage.py migrate
```

- Starting the Backend Server

```bash
  python manage.py runserver
```

## Tech Stack

**Framework:** Django

**Database:** PostgreSQL Database
