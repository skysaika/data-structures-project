"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Stack, Node


def test_push(stack, node):
    assert isinstance(stack.top, Node)
    assert stack.top.data == 'test_data'
    assert stack.top.next_node is None
    stack.push('testdata1')
    assert isinstance(stack.top.next_node, Node)
    assert stack.top.data == 'testdata1'
    assert stack.top.next_node is node

def test_pop(stack, node):
    """Проверка удаления элемента из стек."""
    stack.push('testdata_1')
    node_2 = stack.top
    assert stack.pop() is node_2
    assert stack.pop() is node
    with pytest.raises(AttributeError):
        stack.pop()

Node('testdata', None)