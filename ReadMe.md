# Django Blog & Content Management System (CMS)

This is a full-featured **Django Blog & Content Management System (CMS)** built for multi-user collaboration. It supports **Admin, Editor, and Author roles**, has **rich text editing**, **categories**, a **subscriber system**, and **dynamic dashboards**. The project is designed to be production-ready, secure, and responsive.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [User Roles & Permissions](#user-roles--permissions)  
- [Features](#features)  
- [How It Works](#how-it-works)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Email Configuration](#email-configuration)  
- [Technologies Used](#technologies-used)  
- [License](#license)  

---

## Project Overview

This CMS allows multiple users to collaborate on creating and publishing blog content:

- **Admin** users manage all users, approve author applications, and moderate content.  
- **Editors** can create, edit, and publish posts, and moderate comments.  
- **Authors** can create and edit their own posts but cannot publish without approval.  
- **Visitors** can apply to become Authors via a subscription form.

Posts can be categorized, commented on, and displayed on the homepage in a card-based UI.  

---

## User Roles & Permissions

| Role        | Permissions                                                                 |
|------------|-----------------------------------------------------------------------------|
| **Admin**   | Full access: manage users, assign roles, see all posts, approve/reject author applications, moderate comments |
| **Editor**  | Can view & edit all posts, publish posts, moderate comments                 |
| **Author**  | Can create/edit only their own posts; cannot publish without Editor/Admin approval |
| **Visitor** | Can view published posts, apply to become an Author via a form             |

---

## Features

- **Rich text editing** with CKEditor for posts.  
- **Post status workflow:** Draft or Published.  
- **Post categories** for organizing content.  
- **Comment system** with moderation by Editors/Admins.  
- **Dashboard** tailored to user role (Admin, Editor, Author).  
- **Subscriber form** for visitors to apply as Authors.  
- **Role-based access control** to restrict actions.  
- **Responsive UI** using Bootstrap cards for posts and categories.  
- **Email notifications** for password setup and author applications.  

---

## How It Works

### 1. Post Workflow

1. **Authors** create a post in draft status.  
2. **Editors** and **Admins** can review and publish it.  
3. Published posts appear on the homepage and category pages.  

### 2. Categories

- Posts are assigned to a category.  
- Users can browse posts by clicking a category.  
- Category pages display posts in a responsive card grid.  

### 3. Dashboard

- **Authors** see only their posts.  
- **Editors** see all posts and can publish or edit any post.  
- **Admins** see all posts, manage users, approve author applications, and moderate comments.  
- Dashboard links are dynamic based on role, e.g., "📝 All Posts" for Editors/Admins, "📝 My Posts" for Authors.  

### 4. Author Applications

- Visitors can submit an application via the `/subscribe/` page.  
- Admin receives the application and can approve/reject.  
- Approved users are assigned the **Author** group.  

### 5. Authentication & Email

- Admin registers new users via `/admin-register/`.  
- Upon registration, users receive a **password setup email**.  
- Users log in at `/login/` and are redirected to the site dashboard (not Django admin).  
- Password resets are handled via email.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/geecosmic/blog_cms.git
cd blog_cms


Usage

Visit / to see the blog homepage.

Visit /dashboard/ after login to manage posts.

Admins can register new users via /admin-register/.

Visitors can apply to become Authors via /subscribe/.

Categories are browsable via the navigation bar.





Technologies Used

Python 3.14

Django 6.0

CKEditor 4 (rich text editor)

Bootstrap 5 (responsive UI)

SQLite (default, can switch to PostgreSQL,Mysql)


