from flask import render_template

from config import app, db
from models import Todo
from form import Form


@app.route('/')
def home():
    form = Form()
    # content = db.session.execute(db.select(Todo).scalars().all())
    return render_template('index.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
