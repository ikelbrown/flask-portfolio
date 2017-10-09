from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Welcome'

@app.route('/projects')
def projects():
    return render_template('projects.html')

@pp.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)

