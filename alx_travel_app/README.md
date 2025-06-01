# alx_travel_app_0x00

A Django-based travel listing application that supports Listings, Bookings, and Reviews.  
This project uses MySQL as the database backend and includes a management command to seed sample data.

---

## Features

- Define and manage travel Listings, Bookings, and Reviews
- API-ready serializers for Listings and Bookings
- Database seeding command to populate sample data
- MySQL backend support

---

## Project Structure

alx_travel_app_0x00/
├── manage.py
├── alx_travel_app/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── listings/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── management/
│ └── commands/
│ ├── seed.py
│ └── init.py
└── README.md

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL server running
- Virtualenv (recommended)

### Installation Steps

1. Clone the repo

```bash
git clone <your-repo-url>
cd alx_travel_app_0x00

```

2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure MySQL connection in `alx_travel_app/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Seed the database with sample data

```bash
python manage.py seed
```

7. Run the development server

```bash
python manage.py runserver
```
## Usage
- Access the app API endpoints (to be defined in `listings/urls.py` and views)
- Use the seeded data to test the app functionality

## Contributing
Feel free to open issues or submit pull requests for improvements!
