from flask import Flask
from flask import render_template, url_for, request


app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    q = request.args.get('q')
    print q
    return render_template('index.html', q=q)


if __name__ == '__main__':
    app.run(debug=True)

