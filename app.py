# Import the Flask class
from flask import Flask

# Create an instance of the class
app = Flask(__name__)

# use the route() decorator to tell Flask what URL should trigger the function
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
# if __name__ == '__main__':
#     app.run()

# We use the route() decorator to tell Flask what URL should trigger the function.
# methods specify which HTTP methods are allowed. The default is ['GET']
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"
# below is a special variable in Python which takes the value of the script name.
# This line ensures that our Flask app runs only when it is executed in 
# the main file and not when it is imported in some other file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)