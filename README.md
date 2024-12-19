# Gymnasium Flask

A web application built with Flask to manage gymnasium operations efficiently. This project provides features for gym management, including user registration, schedules, and membership handling.

## Features

- User registration and authentication
- Membership management
- Workout schedule tracking
- Admin panel for managing users and gym details

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (or any other database)
- **Other Tools**: Flask extensions (e.g., Flask-SQLAlchemy, Flask-WTF)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CodewithTanzeel/gymnasium-flask.git
   cd gymnasium-flask
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

6. Open the application in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

- Register as a user or log in as an admin.
- Manage memberships, workout schedules, and user details through the dashboard.

## Contribution

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message"
   ```
4. Push to your fork:
   ```bash
   git push origin feature/your-feature
   ```
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Flask extensions: Flask-SQLAlchemy, Flask-WTF

---

Would you like me to refine or customize this further based on your project details?
