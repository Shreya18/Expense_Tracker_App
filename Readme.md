# Expense Tracker

A Django-based expense tracker application that allows users to track their expenses, including the item purchased, cost, currency, and purchase date. The application also provides a dashboard for monthly expense analysis.

## Features

- Add, view, and delete expenses.
- Supports multiple currencies (USD, GBP, INR).
- Monthly expense analysis dashboard.

## Prerequisites

- Docker
- Docker Compose (optional but recommended for easier management)

## Installation

1. **Clone the repository:**

    ```sh
    git clone <project_url>
    cd expense_tracker
    ```

2. **Create and activate a virtual environment (optional but recommended if not using Docker):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional, for accessing Django admin):**

    ```sh
    python manage.py createsuperuser
    ```

## Running the Application

### Using Docker

1. **Build the Docker image:**

    ```sh
    docker build -t expense_tracker .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8000:8000 expense_tracker
    ```

### Without Docker

1. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

2. Open your browser and go to `http://localhost:8000`.

## Usage

- **Home Page:** View all expenses and options to add or delete an expense.
- **Add Expense:** Form to add a new expense.
- **Dashboard:** View a monthly analysis of expenses.

## Project Structure

```plaintext
expense_tracker_app/
├── expense_tracker/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── expenses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── index.html
│   ├── add_expense.html
│   └── dashboard.html
├── Dockerfile
├── requirements.txt
├── manage.py
