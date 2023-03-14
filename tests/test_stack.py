"""Здесь надо написать тесты с использованием unittest для модуля stack."""

from src.stack import Stack, Node

def test_push():
    stack = Stack()
    stack.push('testdata')
    node = stack.top
    assert isinstance(stack.top, Node)
    assert stack.top.data == 'testdata'
    assert stack.top.next_node is None
    stack.push('testdata1')
    assert isinstance(stack.top.next_node, Node)
    assert stack.top.data == 'testdata1'
    assert stack.top.next_node is node
