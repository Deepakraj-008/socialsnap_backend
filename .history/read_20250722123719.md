## How to Run the Django Backend

This guide assumes you have Python 3.10+ and `pip` installed on your system.

1.  **Unzip the project:**
    Unzip the `socialsnap_backend.zip` file to your desired location.

2.  **Navigate to the project directory:**
    Open your terminal or command prompt and navigate to the `socialsnap_backend` directory:
    ```bash
    cd path/to/socialsnap_backend
    ```

3.  **Create a virtual environment (recommended):**
    It's good practice to use a virtual environment to manage project dependencies:
    ```bash
    python3 -m venv venv
    ```

4.  **Activate the virtual environment:**
    *   **On Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

5.  **Install dependencies:**
    Install all required Python packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

6.  **Apply database migrations:**
    Since the project is configured to use SQLite, the database file (`db.sqlite3`) is included. However, you might need to run migrations again if there are any pending changes or if you delete the `db.sqlite3` file.
    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser (if you haven't already):**
    You will be prompted to enter an email, username, and password. This superuser account will allow you to access the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The server will typically start at `http://127.0.0.1:8000/`.

9.  **Access the Django Admin:**
    Open your web browser and go to `http://127.0.0.1:8000/admin/`. Log in with the superuser credentials you created in step 7.

**Note:** This setup uses SQLite for the database, which is a file-based database and does not require a separate database server like PostgreSQL or MySQL. If you wish to switch to a different database, you will need to modify `socialsnap/settings.py` and install the appropriate database connector.

