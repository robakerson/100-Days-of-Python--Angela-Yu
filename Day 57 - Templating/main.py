from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, cur_year=year)


@app.route('/guess/<string:name>')
def name(name):
    my_params = {
        'name': name,
    }
    res = requests.get(url="https://api.agify.io", params=my_params)
    age = res.json()['age']
    res = requests.get(url="https://api.genderize.io", params=my_params)
    gender = res.json()['gender']
    return f'<h1>Hey {name.title()},<h1>' \
           f'<h2>I think you are {gender},<h2>' \
           f'<h3>And maybe {age} years old<h3>'


# my_params = {
#         'name': 'tim',
#     }
#
# res = requests.get(url="https://api.genderize.io", params=my_params)
#
# print(res.json())
# print(res.text)
#
# text = res.text
# print(res.json)
# print(text)
# print(text[0])
# print(text[1])
#
# hey = {"name":"tim","gender":"male","probability":0.99,"count":47038}
# print(hey['name'])

if __name__ == '__main__':
    app.run(debug=True)