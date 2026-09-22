from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#   이 방법을 쓰려면 flask run 이 아닌, python app.py 방식으로 실행해야함.
# if __name__ == "__main__":
#     app.run(debug=True)
