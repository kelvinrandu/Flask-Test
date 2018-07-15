from flask import Flask, render_template
from data import Articles #

app = Flask(__name__)

# assign variable Articles to function Article located in data.py file
Articles = Articles()

# route to home page
@app.route('/')
def index():
	return render_template('home.html')

# route to about page
@app.route('/about')
def about():
	return render_template('about.html')

# route to  articles page
@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

# route to each article page
@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html',  id= id)

if __name__== '__main__':
	app.run(debug=True)
