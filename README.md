# Todo API with Flask

## About the Project 📂
A simple Todo API built with Flask for my portfolio. This project showcases my ability to design and implement a backend API with Flask, 
featuring basic CRUD functionality to manage tasks. This is a foundational project to demonstrate my backend development skills, which I aim to expand upon with more complex applications in the future.

# An Interesting Fact And What Differentiates This Project From Others
Secure With Authentication And Your Todo So Only Authenticated You Can View It 🛡️


# Important Note: 
-Please configure your env file with the correct values for the API to work and use it securely as default values may not be secure which all are in the .env file and shown in this readme to configure it if you scroll down.

## Current Status 🔄
- **Work Status:** API WORKS FOUNDATIONAL EXTRAS MISSING FOR NOW
- **Current Features:**
- **General Security:** Implemented general security measures for the API including JWT authentication for secure token-based user sessions and multi-auth support for flexible authentication methods. Enhanced session management with HTTP-only and secure flags to prevent session hijacking, cross-site scripting (XSS), and cross-site request forgery (CSRF) attacks. The API is protected against SQL injection attacks using SQLAlchemy ORM, which ensures secure data handling.

In this project, the ORM is an ideal choice as it simplifies managing user-specific data (e.g., each user can only access their own TODO lists) and differentiates between users while maintaining security and data isolation. Although ORMs may introduce some performance overhead, they offer better maintainability and security for managing relationships, especially in a multi-auth, user-specific data context. Raw SQL queries will be considered if performance becomes a bottleneck, but are not necessary at this stage. Finally, rate limiting was added to protect the API from abuse such as DDoS attacks and ensure fair usage



  - **Initial API Setup** The API is Functional And Ready To Use, 

  - **Authentication (Auth) Priority:** Implemented secure authentication with providers like Google and Facebook additionally, classic auth like a form one email password etc will be added as soon as possible.

  - **Maintainability:** Implemented maintainable code structure with clear separation of concerns, and consistent coding style with different layers such as repositories, services, routes, and models with oop principles.

 - **Improved Error Handling:** Current error handling is improved more specific to cases however, logging and more advanced error handling missing.


## Future Goals 🔮
- **Improved Error Handling:** Current error handling is basic and needs to be Much More Specific and Logging Needs To Be Added. 

- **Code Documentation:** Aiming to provide comprehensive code documentation, explaining the logic and structure of the application, which will make the project more maintainable and understandable for future developers.

- **More Authentication Providers** Facebook Auth has been added but others like classic auth like a form login will be added soon in the future and not promise but maybe github will be added with time.

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

# Secret key for securely signing session cookies even though i am not using and using JWT required by some dependencies (replace with your own secret key)
FLASK_SECRET_KEY = "your-secret-key-here"

# Database URL (replace with your actual database connection URL)
DATABASE_URL = "your-database-url-here"

# Google OAuth credentials (replace with your actual Google OAuth Client ID and Secret)
GOOGLE_ID = "your-google-client-id-here"
GOOGLE_SECRET = "your-google-client-secret-here"

#JWT Secret Key To Create Json Web Tokens 
JWT_SECRET_KEY= "your-jwt-secret-key-here"
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

* Passionate about mobile development.

* Experience with web technologies for small to moderate projects.

* Comfortable with full-stack development for self-initiated or side projects, creating well-rounded, functional solutions.


## Current Projects And 
👩‍💻 I’m currently focused on building my backend portfolio, while also developing my step_sync library for Flutter. This library helps count steps using raw sensor data and mathematical calculations. Alongside this, I’m expanding my portfolio with additional projects and handling small, local freelance jobs.

🧠 I believe learning is a continuous journey. While I’ve gained proficiency in my core backend skills, I’m always pushing to expand my knowledge. In the future, I’m particularly excited to dive deeper into Django mainly and FastAPI for where cocurrency required and further strengthen my expertise in backend development.  