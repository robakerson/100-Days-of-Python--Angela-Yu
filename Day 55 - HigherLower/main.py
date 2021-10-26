from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style ="text-align: center">Hello, World!</h1>' \
           '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width=200>'


@app.route('/bye')
@make_bold
def bye():
    return 'bye!'


# variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)