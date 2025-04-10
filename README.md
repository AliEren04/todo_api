# Todo API with Flask

## About the Project 📂
A simple Todo API built with Flask for my portfolio. This project showcases my ability to design and implement a backend API with Flask, 
featuring basic CRUD functionality to manage tasks. This is a foundational project to demonstrate my backend development skills, which I aim to expand upon with more complex applications in the future.

# A Fun Fact And What Differentiates This Project From Others 🤣
## Secure With Authentication 🛡️


# Important Note: 
-Please configure your env file with the correct values for the API to work and use it securely as default values may not be secure which all are in the .env file and shown in this readme to configure it if you scroll down.

## Current Status 🔄
- **Work Status:** API WORKS FOUNDATIONAL EXTRAS MISSING FOR NOW
- **Current Features:**
- **General Security:** Implemented general security measures for the API including session management and secure cookies as well as http-only and secure flags to prevent session hijacking, cross-site scripting (XSS), and cross-site request forgery (CSRF) attacks, additionally, due to use of orm (SQLAlchemy) the API is protected against SQL injection attacks, ORMS are slow but secure which is why I use them however, if needed I will use raw SQL queries to boost performance which was not needed in this project. Last thing to add is rate limiting to prevent abuse like dos, ddos etc and ensure fair usage of the API.



  - **Initial API Setup** The API is Functional And Ready To Use, 

  - **Authentication (Auth) Priority:** Implemented secure authentication with providers like Google, Facebook Although Facebook not tested manually yet and needs to be tested  and classic auth will be added as soon as possible.

  - **Maintainability:** Implemented maintainable code structure with clear separation of concerns, proper documentation soon, and consistent coding style with different layers such as repositories, services, routes, and models with oop principles.

  - **Error Handling:** Basic error handling has been added, but there are plans to improve error formatting and make it more specific in future versions as well as a logging system.


## Future Goals 🔮
- **Improved Error Handling:** Current error handling is basic and needs to be improved by formatting errors more consistently and making them more specific to each case, rather than using general error responses.
- **Code Documentation:** Aiming to provide comprehensive code documentation, explaining the logic and structure of the application, which will make the project more maintainable and understandable for future developers.

- **More Authentication Providers** Facebook Auth has been added but others like classic auth like a form login will be added in the future and not promise but maybe github will be added with time.

- **Logging System:** Aiming to add a logging system to the API to track and monitor the application's behavior and performance.

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
    |__ utils.py
    |__ README.md
```    

To ensure the application works correctly, you'll need to configure the environment variables in your `.env` file well of course you will not have .env file so create it basically a file with .env extension and add the variables shown below. 

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

# Facebook OAuth credentials (replace with your actual Facebook OAuth Client ID and Secret)
FACEBOOK_ID = "your-facebook-client-id-here"
FACEBOOK_SECRET = "your-facebook-client-secret-here"

# Development Status ("Development" or "Production")
DEVELOPMENT = "Development"

#If Development is set to "Development" then the app will run in development mode
#Security Minimizations Therefore Please adjust accordingly otherwise you are very vulnerable:
#Flask Session Cookies:
#Flask Session Cookies:
#... etc
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
