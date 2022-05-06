# Import the Flask class:
from flask import Flask

# Create an instance of the class:
app = Flask(__name__)

# use the route() decorator to tell Flask what URL should trigger the function:
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
# if __name__ == '__main__':
#     app.run()

# We use the route() decorator to tell Flask what URL should trigger the function.
# methods specify which HTTP methods are allowed. The default is ['GET']:
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"
# below is a special variable in Python which takes the value of the script name.
# This line ensures that our Flask app runs only when it is executed in 
# the main file and not when it is imported in some other file:
if __name__ == '__main__':
# Run the Flask application:
    app.run(host='0.0.0.0', port=105)

# Above, host specifies the server on which we want our flask application to run.
# The default value for host is localhost or 127.0.0.1.
# 0.0.0.0 means “all IPv4 addresses on the local machine”. 
# This ensures that the server will be reachable from all addresses.
# The default port value is 5000 and you can set the parameterportto use the 
# port number of your choice.