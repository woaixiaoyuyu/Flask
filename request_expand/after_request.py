from flask import Flask

app = Flask(__name__)


# The function will be called without any arguments.
# If it returns a non-None value
@app.before_request
def process_request1():
    print("request1 comming")


@app.before_request
def process_request2():
    print("request2 comming")


# Your function must take one parameter
@app.after_request
def process_response1(response):
    print("response1 leaving")
    return response


@app.after_request
def process_response2(response):
    print("response2 leaving")
    return response


@app.route('/index', methods=['GET'])
def index():
    return 'Hello World!'

# request1 comming
# request2 comming
# response2 leaving
# response1 leaving


if __name__ == '__main__':
    app.run()
