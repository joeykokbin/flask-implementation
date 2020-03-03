# Project-Implementation
Implementation for CS50's final project

Folders:

1) __pycache__
This stores Python3 ByteCode compiled and ready to be executed.
The cached files allows Python to use these files on the 2nd time, without compiling.
This folder and its content will be listed in ".gitignore".

2) templates
This houses the app's routes, sorted by folders (authentication, content, transact)
The .html files outside of folders are either main routes (i.e. index) or helper functions like apology.

3) static
The static folder houses CSS files, JS files as well as any pictures that is used in the website.

Within the main folder, these are a few files that are important.
****)__init__.py
This file can be empty, or with barebone initialisation code.
If empty, then its single purpose is to act as a namespace package, allowing other .py files to reference other files and import functions.
For example, to import functions from any files in the same level, you would do:
from auth import auth_bp (for this, we can use auth_bp to invoke the function).
or import auth (imports everything in auth. To access the individual attributes we use auth.auth_bp).

1) run.py
Main file that will be used to run the flask web application.
For those new to Flask as I am, I will list out the important lines of code in the file.

1a) *login_manager = LoginManager()*
This creates a LoginManager object, that would help Flask in facilitating authentication related procedures.
This isn't essential, one could write own Python code to "log people in or register people".

1b) *db_path = os.path.join(os.path.dirname(__file__), 'bakery.db')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(db_path)*

For some reason, setting the path to be "sqlite:///bakery.db" (as a relative path) does not create bakery.db at runtime.
Therefore, this code (from online) provides the full path name so Flask SQLAlchemy can reach the correct path.
# If possible, internalise env configs to be in a .env file and load it before running the Flask program

1c) *with app.app_context():*

Any code inside this block will be executed under the "app_context".
With env variables and other attributes, sometimes users would like to access them within views.
However, importing "app" instance within the modules makes your project prone to circular import issues.
This is solved by Flask with the *application context*.  

1d) *from database import db, Order, Product, User*
**From database.py**
*db = SQLAlchemy()*

As with 1a), we create an object (in this case a database object based on SQLlite3 provided by SQLAlchemy).
Within run.py, we import the object, as well as the 3 classes that we shall create as tables with *db_create_all()*

1e) *db.init_app(app)
    login_manager.init_app(app)*

We instantiate the 2 objects with the "app" instance.
This allows login_manager and db objects to be "tied" to the current "app" instance.

1f) *from routes import main_bp*
**From routes.py**
*main_bp = Blueprint('main_bp', __name__, template_folder = "templates", static_folder = "static")*

We create a Blueprint object named 'main_bp', telling it to look for files in the relevant directory.
NOTE: a circular import issue will surface if you try to import the app instance "app" from run.py.
This usually happens because you require the "app" instance for any app-defined routes like @app.route("/home")

The workaround I chose is to create the Blueprint object (main_bp) in "routes.py".
Then, inside "run.py", I register the blueprint with *app.register_blueprint*.
It is important to only import the routes AFTER you register the blueprint.

Why import the routes? To register it within the application context.

2) *helpers.py*
Defined a list of functions designed to facilitate the application.

3) *bakery.db*
A back-end database run on SQLlite3 to mimic a real-life implementation.

4) *database.py*
A python file to initialise the original database.

5) *routes.py*
This defines all routes that is not related to transactions, not authentication.
# index, about.

6) *auth.py*
This defines all routes that need authentication.
# login, logout, register.

7) *transact.py*
This defines all routes associated with transactions.
# buy, orderhistory


-- To run this program, we can use the terminal (powershell) and run:

$env:FLASK_APP = "run.py"
python -m flask run

or

under command prompt:

set FLASK_APP=run.py
set FLASK_ENV=development
set YOURAPPLICATION_SETTINGS=C:\Users\Asys\Desktop\Life\Programming\Languages and Courses - External\Introduction to Computer Science\cS50\Week 10 - Final\Project Implementation\main\.env
flask run
--


Javascript and CSS files reside in the static folders, whereas HTML files reside in the templates.
