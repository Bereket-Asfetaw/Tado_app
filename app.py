from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    def __repr__(self) -> str:
        return f'{self.sno}, {self.title}'
@app.route('/', methods=['GET', 'POST'])
def todoApp():
    if request.method == 'POST':
        todoTitle = request.form['title']
        todoDesc = request.form['desc']
        todo = Todo(title=todoTitle, desc=todoDesc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
if __name__ == '__main__':
    app.run(debug=True)