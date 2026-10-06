from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        todo = {
            "text": request.form["todo"]["text"],
            "done": request.form["todo"]["done"],
        }
        todos.append(todo)
        return redirect(url_for("index"))
    return render_template("index.html", todos=todos)


@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(todos):
        del todos[index]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/toggle/<int:index>")
def toggleDone(index):
    todos[index].done = not todos[index].done
    return redirect(url_for("index"))
