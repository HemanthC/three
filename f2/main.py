from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

from datetime import datetime


@app.route('/')
def time():
    date = datetime.now()
    return str(date)
if __name__ == '__main__':
    app.run(debug=True,port=3000)
