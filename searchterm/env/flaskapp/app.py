from flask import Flask, render_template, request, redirect
from data import Articles

app = Flask(__name__)
app.debug = True

Articles = Articles()

@app.route('/' )
def index():
    return render_template('index.html')

@app.route('/<string:searchTerm>/' , methods = ['GET', 'POST'])
def index1():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    #return render_template('articles.html', articles = Articles)
    return render_template('articles.html', entries = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

if __name__ == '__main__':
    app.run()
