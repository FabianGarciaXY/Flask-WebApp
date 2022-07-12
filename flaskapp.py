from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
	{
		'author':'Corey Schafer',
		'title':'Blog Post 1',
		'content':'First post content',
		'date_posted':'April 20, 2018'
	},
 	{
		'author': 'John',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
  	},
   	{
		'author': 'Johna',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'April 21, 2018'
  	},
    {
		'author': 'Johna',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'April 21, 2018'
  	},
    {
		'author': 'Johna',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'April 21, 2018'
  	}
]


@app.route('/')
@app.route('/home')
def home() -> str:
	return render_template('home.html', data = posts)

@app.route('/about')
def about() -> str:
	return render_template('about.html', title='Flask - About')


if __name__ == '__main__':
	app.run(debug=True)