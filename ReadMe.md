# Django Blog & Content Management System (CMS)

A full-featured **Django Blog & CMS** built for multi-user
collaboration.\
Supports **Admin, Editor, and Author roles**, with **rich text
editing**, **categories**, a **subscriber system**, and **dynamic
dashboards**.\
Designed to be production-ready, secure, and responsive.

------------------------------------------------------------------------

## Table of Contents

-   Project Overview\
-   User Roles & Permissions\
-   Features\
-   How It Works\
-   Installation\
-   Usage\
-   Email Configuration\
-   Technologies Used\
-   License

------------------------------------------------------------------------

## Project Overview

This CMS allows multiple users to collaborate on blog content:

-   **Admin**: manage users, approve authors, moderate content.\
-   **Editor**: create, edit, publish posts, moderate comments.\
-   **Author**: create and edit own posts; needs approval to publish.\
-   **Visitor**: view posts and apply to become an Author.

Posts support categories, comments, and appear on the homepage in a
card-based layout.

------------------------------------------------------------------------

## User Roles & Permissions

  -----------------------------------------------------------------------
  Role                           Permissions
  ------------------------------ ----------------------------------------
  **Admin**                      Full access: manage users, assign roles,
                                 approve/reject authors, moderate
                                 comments

  **Editor**                     View & edit all posts, publish posts,
                                 moderate comments

  **Author**                     Create/edit own posts only; cannot
                                 publish without approval

  **Visitor**                    View posts, apply to become an Author
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Features

-   Rich text editing with **CKEditor**\
-   Post status: Draft / Published\
-   Post categories\
-   Comment system with moderation\
-   Role-based dashboards\
-   Author application system\
-   Role-based access control\
-   Responsive UI with Bootstrap\
-   Email notifications for setup and approvals

------------------------------------------------------------------------

## How It Works

### Post Workflow

1.  Authors create posts as drafts.\
2.  Editors/Admins review and publish.\
3.  Published posts appear on homepage and categories.

### Categories

-   Each post belongs to a category.\
-   Users browse posts by category.\
-   Displayed in responsive card layout.

### Dashboard

-   Authors: see only their posts.\
-   Editors: see and manage all posts.\
-   Admins: manage posts, users, comments, and applications.\
-   Menu adapts based on role.

### Author Applications

-   Visitors apply via `/subscribe/`.\
-   Admin reviews and approves/rejects.\
-   Approved users become Authors.

### Authentication & Email

-   Admin creates users via `/admin-register/`.\
-   Users receive password setup email.\
-   Login at `/login/` (custom dashboard, not Django admin).\
-   Password reset via email.

------------------------------------------------------------------------

## Installation

### 1. Clone Repository

``` bash
git clone https://github.com/geecosmic/Blog-CMS.git
cd blog_cms
```

### 2. Create Virtual Environment

``` bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4. Run Migrations

``` bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User

``` bash
python manage.py createsuperuser
```

### 6. Start Server

``` bash
python manage.py runserver
```

------------------------------------------------------------------------

## Usage

-   Visit `/` for homepage.\
-   Visit `/dashboard/` after login.\
-   Admins register users at `/admin-register/`.\
-   Visitors apply at `/subscribe/`.\
-   Categories available in navigation bar.

------------------------------------------------------------------------

## Email Configuration

Add to `settings.py`:

``` python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'Blog CMS <your-email@gmail.com>'
```

For production: use Gmail, SendGrid, or PythonAnywhere email.\
(Note: free PythonAnywhere only emails PythonAnywhere addresses).

------------------------------------------------------------------------

## Technologies Used

-   Python 3.14\
-   Django 6.0\
-   CKEditor 4\
-   Bootstrap 5\
-   SQLite (default; PostgreSQL supported)

------------------------------------------------------------------------

## License

MIT License

**Author:** George Eyo 
