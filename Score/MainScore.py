from flask import Flask, render_template
from Score import read_score

app = Flask(__name__)


@app.route('/')
def index():
    score = read_score()
    return render_template('index.html', SCORE=score)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=30000)
