# Django Blog Project

## Project Overview
This is a full-featured Django blog application with user authentication, profile management, and blog post functionalities.

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Oyshik-ICT/PostForge.git
cd PostForge
```

### 2. Create a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Apply database migrations
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

## Project Features
- User Registration, Login and Authentication
- Create, Update, and Delete Blog Posts
- User Profiles with Profile Pictures
- Pagination for Blog Posts
- Latest Posts View

## Project Structure
- `blog/`: Blog application views, models, and templates
- `user/`: User authentication and profile management
- `blog_project/`: Main project configuration
- `templates/`: HTML templates
- `media/`: User-uploaded profile pictures


## Troubleshooting
- Ensure all dependencies are installed
- Check your Python and Django versions
- Verify database migrations are applied
- Make sure you're in the virtual environment
