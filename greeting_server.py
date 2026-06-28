
# Imports the Flask class from the Flask library. 
from flask import Flask 

# This creates an instance of the Flask application. 
# The __name__ variable is a special Python variable that allows Flask to location files and
# know where the app is running from. Basically it says start my app here. 
# __name__ being placed here means Flask knows where our app lives. 

# Classes are just blueprints for object instances. They follow the same type of formula. 


greeting_server = Flask(__name__) 


# This is a decorator and says whenever someone visits the root URL (/), run the function below.
#  
# This isn't a directory. Think of this like the main page of a website. An about page would be /about
# or a login page would be /login. So if your site is http://localhost:5000 then 
# you see where the root URL comes from. http://localhost:5000/


# .route() is a method of the class Flask

# The decorator, @, wraps the function below to the route module. 


# The actual function Python will run when you visit the root URL. 

@greeting_server.route('/') 
def hello(): 
    return "Hey guys! We just dockerized a Flash app. You're a cloud engineer!" 


# Tells the Python container to listen on all network interfaces or Layer 3 interfaces on port 5000 
# to run this code.
# .run() is a method of the class Flask

if __name__ == '__main__': 
    # This method below basically says start a loop that never stops and listen for incoming traffic
    # So basically this piece of code doesn't just start and close. It stays open. 
    greeting_server.run(host='0.0.0.0', port=5000)   



    # The __name__ variable belongs to all Python files. It says how was this file used?
    # If you run the code directly using python greeting_server.py. That means __name__ == '__main__'
    # If you imported the greeting_server app as a module into another piece of code, then you would
    # get __name__ == 'greeting_server' instead. 
    # The if is exactly that. If this file is being run directly, then start up these interfaces on 
    # port 5000.
    # These are dunder (double underscore) methods/variables. They're system level like __init__
    # The apostrophes just make __main__ a string value because __name__ is a string. 