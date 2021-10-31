from flask import Flask, render_template, request
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', msg_sent=False)
    elif request.method == 'POST':
        print(request.form['personal_name'])
        print(request.form['email'])
        print(request.form['phone_num'])
        print(request.form['message'])
        return render_template('contact.html', msg_sent=True)

@app.route('/post/<int:post_num>')
def post(post_num):
    for post in API_BLOG_POSTS:
        if post['id']==post_num:
            requested_post = post
    return render_template('post.html', post=requested_post)


# @app.route('/form-entry', methods=['post'])
# def receive_data():
#     print(request.form['personal_name'])
#     print(request.form['email'])
#     print(request.form['phone_num'])
#     print(request.form['message'])
#     return "<h1>successfully sent your message</h1>"

if __name__ == '__main__':
    app.run(debug=True)