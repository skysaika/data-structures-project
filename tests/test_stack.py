"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src import stack
from src.stack import Node



class TestStack(unittest.TestCase):
    """Тесты для модуля stack."""
    def test_push(self):
        """Проверка добавления элемента в начало списка."""
        # self.assertIsInstance('stack.top', Node)
        self.assertEqual('stack.top.data', 'test_data')
        self.assertIs('stack.top.next_node', None)
        stack.push('testdata1')
        self.assertIsInstance('stack.top.next_node', Node)
        self.assertEqual('stack.top.data', 'testdata1')
        self.assertIs('stack.top.next_node', None)


if __name__ == '__main__':
    unittest.main()


# import pytest
#
# from src.stack import Stack, Node
#
#
# def test_push(stack, node):
#     assert isinstance(stack.top, Node)
#     assert stack.top.data == 'test_data'
#     assert stack.top.next_node is None
#     stack.push('testdata1')
#     assert isinstance(stack.top.next_node, Node)
#     assert stack.top.data == 'testdata1'
#     assert stack.top.next_node is node
#
#
# def test_pop(stack, node):
#     """Проверка удаления элемента из стека."""
#     stack.push('testdata_1')
#     node_2 = stack.top
#     assert stack.pop() is node_2.data
#     assert stack.pop() is node.data
#     with pytest.raises(AttributeError):
#         stack.pop()
#
#
# Node('testdata', None)