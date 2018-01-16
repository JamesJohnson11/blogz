from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/blog', methods=['POST', 'GET'])
def blog():
    return render_template('blog.html')

@app.route('/newpost', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        return redirect('/blog')

    return render_template('new_post.html')


if __name__ == '__main__':
    app.run()


