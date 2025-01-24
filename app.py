from flask import Flask, render_template, url_for
from flask_assets import Environment, Bundle
app = Flask(__name__)
assets = Environment(app)
scss = Bundle('scss/styles.scss', filters='pyscss', output='css/styles.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/membership')
def membership():
    return render_template('membership.html')


if __name__ == "__main__":
    app.run(debug=False)
