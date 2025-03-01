# Todo API with Flask

## About the Project 📂
A simple Todo API built with Flask for my portfolio. This project showcases my ability to design and implement a backend API with Flask, 
featuring basic CRUD functionality to manage tasks. This is a foundational project to demonstrate my backend development skills, which I aim to expand upon with more complex applications in the future.

# A Fun Fact And What Differentiates This Project From Others 🤣
## Secure With Authentication and Symmetric Encryption in Future🛡️

## Current Status 🔄
- **Work Status:** Ongoing
- **Current Features:**
  - **Initial API Setup (No DB Interactions):** The API is up and running without database interaction at the moment, focused primarily on setting up basic routes.
  - **Authentication (Auth) Priority:** Implemented secure authentication before diving into database interaction, ensuring that only authorized users can access routes and data.
  - **Error Handling:** Basic error handling has been added, but there are plans to improve error formatting and make it more specific in future versions.
  - **ORM Setup:** Set up Object Relational Mapping (ORM) models for easy building of tables. This is part of the future implementation to interact with the database.
  - **Flask Migrate:** Implemented Flask Migrate to help with migrations and changes to database tables.
  - **Tech Features (rather than functional):**
    - Setup of essential technical infrastructure, like authentication and ORM models, ahead of route and repository interactions.

## Future Goals 🔮
- **Working Routes Interacting with DB:** The next major step is to get the routes working and interacting with the database using the repository pattern for easier and cleaner code management.
- **Improved Error Handling:** Current error handling is basic and needs to be improved by formatting errors more consistently and making them more specific to each case, rather than using general error responses.
- **Code Documentation:** Aiming to provide comprehensive code documentation, explaining the logic and structure of the application, which will make the project more maintainable and understandable for future developers.
- **Enhanced Security for Edge Cases:** Adding additional layers of security, including symmetric encryption of todo text data before saving to the database and encrypting it when retrieved and sent in JSON responses. This would ensure extra data protection for sensitive information.


## Folder Structure 📁

The project is structured as follows:

```
app
    |__ .env Well Of course u will add your .env file and make configurations on configuration which stated in here after this section
    |__ app.py
    |__ extensions.py
    |__ models.py
    |__ repos.py
    |__ requirements.txt
    |__ routes.py
    |__ schemas.py
    |__ services.py
    |__ README.md
```    

To ensure the application works correctly, you'll need to configure the environment variables in your `.env` file. 

Below is an example of the necessary variables to include in your `.env` file:

```ini
# Flask app configuration

# Set the port number the app will run on (default is 5000)
PORT = "5000"

# Secret key for securely signing session cookies (replace with your own secret key)
SECRET_KEY = "your-secret-key-here"

# Database URL (replace with your actual database connection URL)
DATABASE_URL = "your-database-url-here"

# Google OAuth credentials (replace with your actual Google OAuth Client ID and Secret)
GOOGLE_ID = "your-google-client-id-here"
GOOGLE_SECRET = "your-google-client-secret-here"

```

## 🚀 About Me
 * I’m a self-taught backend developer with a strong passion for programming and building efficient, scalable systems. At 20 years old, I’m constantly learning and improving my skills in backend technologies, and I currently study Software Engineering  at Canterbury Christ Church University.

* When I’m not coding, I enjoy chess, watching anime, and occasionally gaming in my free time. These hobbies help me relax and fuel my creative thinking for my software projects.



## 🛠 Core Backend Skills
* Python (Flask)
* PostgreSQL
* MongoDB
## 🛠 Additional Skills

* Passionate about mobile development using Flutter for various applications.

* Experience with web technologies for small to moderate projects.

* Comfortable with full-stack development for self-initiated or side projects, creating well-rounded, functional solutions.


## Current Projects And 
👩‍💻 I’m currently focused on building my backend portfolio, while also developing my step_sync library for Flutter. This library helps count steps using raw sensor data and mathematical calculations. Alongside this, I’m expanding my portfolio with additional projects and handling small, local freelance jobs.

🧠 I believe learning is a continuous journey. While I’ve gained proficiency in my core backend skills, I’m always pushing to expand my knowledge. In the future, I’m particularly excited to dive deeper into FastAPI and further strengthen my expertise in backend development.  

👯‍♀️ I'm looking to collaborate on anything that interests me and suitable for my level to collaborate. 

## 📫 How to reach me
* Email: devalierentabak@outlook.com
* Social Media: aliern046 (Instagram)
