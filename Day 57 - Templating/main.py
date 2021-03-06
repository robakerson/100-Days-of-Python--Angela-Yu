from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
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
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    res = requests.get(blog_url)
    all_posts = res.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)