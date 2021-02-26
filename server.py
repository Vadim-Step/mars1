from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
def news(title):
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
