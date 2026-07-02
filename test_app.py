# from app import add

# def test_add():
#     assert add(2, 3) == 5

from app import add, library_name

def test_add():
    assert add(2, 3) == 5

def test_library_name():
    assert library_name() == "Library Management System"