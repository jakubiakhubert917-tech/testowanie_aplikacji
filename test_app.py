import pytest
from app import TodoList

def test_add_task():
    todo = TodoList()
    assert todo.add_task("Kupić mleko") == True
    assert len(todo.get_tasks()) == 1
    assert todo.get_tasks()[0] == "Kupić mleko"

def test_add_empty_task():
    todo = TodoList()
    assert todo.add_task("") == False
    assert len(todo.get_tasks()) == 0

def test_remove_task():
    todo = TodoList()
    todo.add_task("Zadanie 1")
    removed = todo.remove_task(0)
    assert removed == "Zadanie 1"
    assert len(todo.get_tasks()) == 0