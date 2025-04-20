<!-- Project Banner -->
<p align="center">
  <img src="static/img/todo_icon_clean_cropped.png" alt="Todo API Logo" width="200" height="200">
</p>

<h1 align="center">✅ Todo — Task Management API</h1>

<p align="center">
  A simple, powerful backend for managing daily tasks, built with Django and Django REST Framework.
  <br><br>
  <a href="#-features"><strong>✨ Explore Features »</strong></a>
  <br><br>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/python-3.12-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/status-in%20development-yellow" alt="Project Status">
</p>

---

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Environment Variables](#-environment-variables)
- [Resources](#-resources)
- [License](#-license)
- [Contact & Contribution](#-contact--contribution)
- [Host](#-hosting)
---

## 📌 About
**Todo** is a powerful, scalable server-side application that provides a seamless <span style="color: #4CAF50;"><strong>API</strong></span> for managing tasks with high security and performance.  
It features **JWT-based authentication**, **email verification**, **password reset functionality**, and a complete **CRUD system** for managing tasks, subtasks, and tags — all tailored for each individual user.
**Key Features:**
- Authentication with **JWT tokens** for secure, token-based access
- Full <span style="color: #2196F3;">**task and subtask management**</span> capabilities
- <span style="color: #FFC107;">**Email verification**</span> and easy password reset
- Task categorization with **user-defined tags**
- Task filtering by **status**, **priority**, **overdue**, and **recurring tasks**
- Built following the <span style="color: #3F51B5;">**SOLID**</span> and <span style="color: #F44336;">**ACID**</span> principles for clean, maintainable code
This project is perfect for developers looking to integrate a <span style="color: #4CAF50;">**robust**, scalable task management system with modern development practices and high standards of security</span>. 🚀
Whether you're building **a personal productivity tool** or **a professional task management system**, **Todo** sets a solid foundation for all your needs! 💡
---

## ✨ Features
- <span style="color: #4CAF50;"><strong>JWT Authentication</strong></span>: Secure login and token-based authentication system for users.
- <span style="color: #2196F3;"><strong>Task Management</strong></span>: Full **CRUD** operations (Create, Read, Update, Delete) for tasks and subtasks.
- <span style="color: #FFC107;"><strong>Email Verification</strong></span>: Upon signup, users receive a verification email to activate their account.
- <span style="color: #FF5722;"><strong>Password Reset</strong></span>: Users can reset their password with a verification code sent via email.
- <span style="color: #673AB7;"><strong>Task Categorization</strong></span>: Organize tasks with **user-defined tags** for better management.
- <span style="color: #9C27B0;"><strong>Task Filtering</strong></span>: Filter tasks by **status** (in progress, done, todo), **priority** (low, medium, high), **overdue** tasks, and **recurring tasks**.
- <span style="color: #009688;"><strong>User Tags</strong></span>: Each user can create and manage their own custom tags for better task organization.
- <span style="color: #3F51B5;"><strong>ACID & SOLID Principles</strong></span>: Built using the <span style="color: #F44336;">**ACID**</span> and <span style="color: #FFC107;">**SOLID**</span> principles for clean, scalable, and maintainable code.
- <span style="color: #FF9800;"><strong>Secure Database</strong></span>: Using <span style="color: #607D8B;">**SQLite**</span> for development and <span style="color: #9E9E9E;">**MySQL**</span> for production to ensure data integrity and security.

---
## 🛠️ Tech Stack

The **Todo** app is built using modern technologies to ensure a robust, scalable, and maintainable solution.

- <span style="color: #008080;"><strong>Django</strong></span>: The backbone of the application, providing a powerful web framework.
- <span style="color: #0077B5;"><strong>Django REST Framework</strong></span>: For building a RESTful API with ease and efficiency.
- <span style="color: #FF5722;"><strong>JWT</strong></span>: Secure authentication with JSON Web Tokens for API access.
- <span style="color: #795548;"><strong>SQLite</strong></span>: Lightweight, embedded database used for development.
- <span style="color: #00BCD4;"><strong>MySQL</strong></span>: Reliable, production-grade database for scalable deployments.
- <span style="color: #FF9800;"><strong>HTML5 & CSS3</strong></span>: For styling the front-end (forms, templates, etc.).
- <span style="color: #4CAF50;"><strong>Git</strong></span>: Version control to track and manage changes.
- <span style="color: #2196F3;"><strong>Postman</strong></span>: For testing the API endpoints and ensuring smooth interaction.
- <span style="color: #3F51B5;"><strong>Solidity & ACID</strong></span>: Following **SOLID** principles for maintainable code and **ACID** for robust database transactions.

---


## 🏗️ Installation

Follow these steps to get the project up and running locally.

### 🛠️ Requirements:
- <span style="color: #4CAF50;"><strong>Python 3.10+</strong></span> (For compatibility and features)
- <span style="color: #0077B5;"><strong>pip</strong></span> (Python package installer)
- <span style="color: #FF5722;"><strong>MySQL</strong></span> (for production setup)
- <span style="color: #795548;"><strong>SQLite</strong></span> (for development setup)

### 📥 Installation Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/omarZACK/Todo
   cd Todo
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your database:
   - For **development**: The app uses **SQLite** by default.
   - For **production**: Set up **MySQL** (edit `DATABASES` in `settings.py` to configure MySQL).

5. Run migrations to set up the database schema:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel (optional but recommended):
   ```bash
   python manage.py createsuperuser
   ```

7. Start the server:
   ```bash
   python manage.py runserver
   ```

### 🚀 Verify:
- Open your browser and go to `http://127.0.0.1:8000/` to see the app in action.
- For the admin panel, go to `http://127.0.0.1:8000/admin/` (login with the superuser credentials you created).

---

## 🌍 Environment Variables

To run the project locally or in production, you'll need to configure several environment variables. These are used for sensitive data like API keys, database credentials, and other configuration settings that should not be hardcoded.

### Required Environment Variables:
Create a `.env` file in the root of your project and add the following variables:

- **`GOOGLE_CLIENT_ID`**: Your Google API client ID for authentication.
  ```bash
  GOOGLE_CLIENT_ID=your_google_client_id
  ```

- **`GOOGLE_CLIENT_SECRET`**: Your Google API client secret for authentication.
  ```bash
  GOOGLE_CLIENT_SECRET=your_google_client_secret
  ```

- **`EMAIL_HOST_USER`**: Your email address (for Gmail, use your Gmail account).
  ```bash
  EMAIL_HOST_USER=your_email@gmail.com
  ```

- **`EMAIL_HOST_PASSWORD`**: The password or application-specific password for your email account.
  ```bash
  EMAIL_HOST_PASSWORD=your_email_password_or_app_password
  ```

- **`DJANGO_SECRET_KEY`**: A secret key used by Django for cryptographic signing. Generate a strong key, e.g. using `django.core.management.utils.get_random_secret_key()`.
  ```bash
  DJANGO_SECRET_KEY=your_django_secret_key
  ```

- **`DEFAULT_FROM_EMAIL`**: The default email address to use for sending emails.
  ```bash
  DEFAULT_FROM_EMAIL=your_default_email_address
  ```

- **`DB_NAME`**: The name of your database.
  ```bash
  DB_NAME=your_database_name
  ```

- **`DB_USER`**: The username for your database connection.
  ```bash
  DB_USER=your_database_username
  ```

- **`DB_PASSWORD`**: The password for your database connection.
  ```bash
  DB_PASSWORD=your_database_password
  ```

- **`DB_HOST`**: The host of your database server.
  ```bash
  DB_HOST=your_database_host
  ```

- **`ALLOWED_HOSTS`**: A list of allowed hosts for your app (e.g., for production).
  ```bash
  ALLOWED_HOSTS=yourdomain.com
  ```

- **`FRONTEND_URL`**: The URL of your frontend application (if applicable).
  ```bash
  FRONTEND_URL=http://localhost:3000
  ```

### Setting Up the .env File:
1. Create a `.env` file in the root directory of your project.
2. Add the environment variables as shown above, replacing the placeholders with actual values.
3. Use a library like `django-environ` to easily manage these variables in your Django project.

### Example .env File:
```bash
  GOOGLE_CLIENT_ID=your_google_client_id
  GOOGLE_CLIENT_SECRET=your_google_client_secret
  EMAIL_HOST_USER=your_email@gmail.com
  EMAIL_HOST_PASSWORD=your_email_password_or_app_password
  DJANGO_SECRET_KEY=your_django_secret_key
  DEFAULT_FROM_EMAIL=your_default_email_address
  DB_NAME=your_database_name
  DB_USER=your_database_username
  DB_PASSWORD=your_database_password
  DB_HOST=your_database_host
  ALLOWED_HOSTS=yourdomain.com
  FRONTEND_URL=http://localhost:3000
```
## 📚 Resources

<div style="text-align: center;">
  <table align="center">
    <tr>
      <td align="center" style="padding: 15px;">
        <img src="https://img.icons8.com/color/48/000000/django.png" alt="Django"/><br>
        <a href="https://www.djangoproject.com/" style="color:#007BFF; text-decoration:none;"><strong>Django Docs</strong></a>
      </td>
      <td align="center" style="padding: 15px;">
        <img src="https://img.icons8.com/?size=100&id=21887&format=png&color=FA5252" alt="DRF"/><br>
        <a href="https://www.django-rest-framework.org/" style="color:#007BFF; text-decoration:none;"><strong>DRF Docs</strong></a>
      </td>
      <td align="center" style="padding: 15px;">
        <img src="https://img.icons8.com/?size=100&id=43482&format=png&color=ff0000" alt="JWT"/><br>
        <a href="https://django-rest-framework-simplejwt.readthedocs.io/en/latest/" style="color:#007BFF; text-decoration:none;"><strong>Simple JWT Docs</strong></a>
      </td>
      <td align="center" style="padding: 15px;">
        <img src="https://img.icons8.com/color/48/000000/css3.png" alt="CSS3"/><br>
        <a href="https://css-tricks.com/" style="color:#007BFF; text-decoration:none;"><strong>CSS-Tricks</strong></a>
      </td>
      <td align="center" style="padding: 15px;">
        <img src="https://img.icons8.com/color/48/000000/gmail.png" alt="Gmail API"/><br>
        <a href="https://developers.google.com/gmail/api" style="color:#007BFF; text-decoration:none;"><strong>Gmail API</strong></a>
      </td>
      <td align="center" style="padding: 15px;">
        <img src="https://img.icons8.com/color/48/000000/python.png" alt="Python"/><br>
        <a href="https://www.python.org/" style="color:#007BFF; text-decoration:none;"><strong>Python Docs</strong></a>
      </td>
    </tr>
  </table>
</div>

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



<p style="font-size:14px; color:#444;">✨ Explore these resources to improve your workflow and sharpen your development skills!</p>
---

## 📞 Contact & Contribution

For any questions, suggestions, or feedback, feel free to reach out!

- **Email**: [o.e.wawy@gmail.com](o.e.wawy@gmail.com)
- **GitHub**: [https://github.com/omarZACK](https://github.com/omarZACK)

<p><img src="https://img.shields.io/badge/Contact-Open%20for%20inquiries-blue" alt="Contact" /></p>

### How to Contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a **Pull Request** with a clear description of your changes.

<p><img src="https://img.shields.io/badge/Contact%20and%20Contribute-Open%20for%20PRs-green" alt="Contact & Contribution" /></p>

---

## 🌐 Hosting

This project is hosted on [PythonAnywhere](https://www.pythonanywhere.com/).

You can view the live application at:

[Your live site URL on PythonAnywhere](https://omarwawy.pythonanywhere.com)

### How to Deploy on PythonAnywhere:
1. Create an account on [PythonAnywhere](https://www.pythonanywhere.com/).
2. Upload your project files (including the requirements.txt).
3. Set up a virtual environment and install dependencies.
4. Configure your WSGI settings to point to your Django project.
5. Run your app and enjoy hosting it with PythonAnywhere!
<p><img src="https://img.shields.io/badge/Hosting-on%20PythonAnywhere-blue" alt="PythonAnywhere" /></p>
