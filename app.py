from flask import Flask , render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def index():
    return render_template('about.html')
@app.route('/membership')
def index():
    return render_template('membership.html')

if __name__ == "__main__":
   app.run(debug=True)
