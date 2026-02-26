from flask import Flask, redirect, render_template, request, url_for
from werkzeug.wrappers import Response

app = Flask(__name__)

def load_todos() -> list[str]:
    try:
        with open("todos.txt", "r") as file:
            todos = list[str](line.strip() for line in file)
    except FileNotFoundError:
        todos = list[str]()
    return todos

def save_todos(todos: list[str]) -> None:
    with open("todos.txt", "w") as file:
        file.write("\n".join(todos))

@app.route("/", methods=["GET", "POST"])
def index() -> Response | str:
    todos = load_todos()
    if request.method == "POST":
        new_todo = request.form.get("todo")
        if new_todo:
            todos.append(new_todo)
            save_todos(todos)
            return redirect(url_for("index"))
    return render_template("index.html", todos=todos)

@app.route("/delete/<int:todo_id>")
def delete(todo_id: int) -> Response | str:
    if request.method == "GET":
        todos = load_todos()
        todos_length = len(todos)
        try:
            if todo_id < 0 or todos_length <= todo_id:
                raise ValueError("Error: invalid ToDo ID")
            del todos[todo_id]
            save_todos(todos)
        except Exception as error:
            return f"{error}"
        return redirect(url_for("index"))
    return ""

if __name__ == "__main__":
    app.run(debug=True)
