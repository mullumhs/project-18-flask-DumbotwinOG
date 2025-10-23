from flask import Flask

app = Flask(__name__)




@app.route('/hello')		# Route	

def say_hello():		# Function

    return "Hello, visitor!"




@app.route('/hello/<name>')

def hello(name):

    return f'Hello, {name}!'



@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')

def calculator(num1, operation, num2):

    add = num1 + num2
    
    
    if operation == "add":
        return add
    
    
    
    # Program the logic of a calculator here

    # E.g. if operation = "add" then result = num1 + num2



    



if __name__ == '__main__':

    app.run(debug=True)