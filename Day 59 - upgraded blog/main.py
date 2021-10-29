from flask import Flask, render_template
import requests

app = Flask(__name__)
BLOG_API = 'https://api.npoint.io/5deaf41b4f8078c817e6'
res = requests.get(url=BLOG_API)
API_BLOG_POSTS = res.json()

@app.route('/')
def home():
    return render_template('index.html', posts=API_BLOG_POSTS)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)