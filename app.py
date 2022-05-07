from flask import Flask
from flask import jsonify
app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/person/')
def hello():
    return jsonify({'name':'Tokyo',
                    'address':'Bahamas'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

app.logger.debug('This is a DEBUG message')
app.logger.info('This is an INFO message')
app.logger.warning('This is a WARNING message')
app.logger.error('This is an ERROR message')