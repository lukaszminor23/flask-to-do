from datetime import date

from flask import render_template, redirect, url_for

from config import app, db
from models import Todo
from form import Form


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()
    all_todos = db.session.execute(db.select(Todo)).scalars().all()
    if form.validate_on_submit():
        new_todo = Todo(
            todo=form.text.data,
            created_at=date.today().strftime("%Y-%m-%d"),
            due_date=form.due_date.data
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('index.html', form=form, todos=all_todos)


@app.route('/delete_todo/<int:todo_id>')
def delete_todo(todo_id):
    todo = db.session.get(Todo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
