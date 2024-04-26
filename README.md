# JinifyNote 📝

JinifyNote, personalized sticky note solution! JinifyNote is a Django-based application designed to help organize your thoughts and tasks effortlessly.

![JinifyNote Screenshot](https://github.com/jeenakarmi/Notes_Project/blob/main/Home.png)

## Features

- **User Authentication:** 🔒 Secure user authentication system allowing users to sign up and log in.
  
- **Create Note:** 📝 Easily create new sticky notes to capture your thoughts and tasks.
  
- **View Note:** 👀 Access your existing sticky notes to review and reference them.
  
- **Edit Note:** ✏️ Modify the content of your sticky notes to keep them up-to-date.
  
- **Delete Note:** 🗑️ Remove sticky notes that are no longer needed or relevant.


## Setup Instructions

### Python Environment Setup:

1. Create a new Python virtual environment for the project:

    ```
    python3 -m venv myenv
    ```

3. Activate the virtual environment:

    - On Windows:
      ```
      myenv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source myenv/bin/activate
      ```

### Install Dependencies:

1. Install the project dependencies within the virtual environment:

    ```
    pip install -r requirements.txt
    ```

### Database Configuration:

1. Replace the default database configuration in your Django settings (`settings.py`) with your own database settings. Find the `DATABASES` dictionary and replace it with your database configuration. For example:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'YourDatabaseName',
            'USER' : 'YourDatabaseUser',
            'PASSWORD' :'YourDatabasePassword',
            'HOST':'YourDatabaseHost'
        }
    }
    ```

    Replace `'YourDatabaseName'`, `'YourDatabaseUser'`, `'YourDatabasePassword'`, and `'YourDatabaseHost'` with your actual database details.

### Run the Application:

1. Once the dependencies are installed and the database configuration is updated, run the Django development server:

    ```
    python manage.py runserver
    ```

3. Access the Application:

    - Open a web browser and go to the URL provided by the Django development server, `http://127.0.0.1:8000/`.

4. Explore JinifyNote:

    - Once the server is running, you can explore the JinifyNote application.
    - Sign up for a new account or log in if you already have one.
    - Start creating, viewing, editing, and deleting your sticky notes as needed.
---
If you encounter any issues during the setup process or have any questions or feedback, feel free to reach out. Happy note-taking! 😊
