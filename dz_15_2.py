import pytest
from tree import Tree

def test_insert():
    tree = Tree()
    tree.insert(5)
    assert tree.root.data == 5

    tree.insert(3)
    assert tree.root.left.data == 3

    tree.insert(7)
    assert tree.root.right.data == 7

    tree.insert(1)
    assert tree.root.left.left.data == 1

def test_get_min():
    tree = Tree()
    tree.insert(5)
    assert tree.get_min() == 5

    tree.insert(3)
    assert tree.get_min() == 3

    tree.insert(7)
    assert tree.get_min() == 3

    tree.insert(1)
    assert tree.get_min() == 1

def test_get_max():
    tree = Tree()
    tree.insert(5)
    assert tree.get_max() == 5

    tree.insert(3)
    assert tree.get_max() == 5

    tree.insert(7)
    assert tree.get_max() == 7

    tree.insert(9)
    assert tree.get_max() == 9

def test_remove():
    tree = Tree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    tree.remove(1)
    assert tree.get_min() == 3
    assert tree.root.left.left is None

    tree.remove(7)
    assert tree.get_max() == 8
    assert tree.root.right.data == 8
    assert tree.root.right.right is None

    tree.remove(5)
    assert tree.root.data == 6
    assert tree.get_min() == 3
    assert tree.get_max() == 8