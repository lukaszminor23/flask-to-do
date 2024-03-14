from config import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


class Todo(db.Model):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    todo: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[str] = mapped_column(String, nullable=False)
    due_date: Mapped[str] = mapped_column(String, nullable=False)
