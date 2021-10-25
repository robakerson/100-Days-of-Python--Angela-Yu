from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def say_bye():
    return 'bye'


if __name__ == '__main__':
    app.run()

# Decorator functions:

# def speed_calc_decorator(function):
#     def wrapper_function():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed: {end_time - start_time}s")
#
#     return wrapper_function
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
#
# fast_function()
# slow_function()