
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'LEARNING CI/CD PIPELINES WITH AWS SERVICE  '

if __name__ == '__main__':
    app.run()
