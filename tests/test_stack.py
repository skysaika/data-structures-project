"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack, Node


class TestStack(unittest.TestCase):
    """Тесты для модуля stack."""

    def __init__(self, methodName: str):
        super().__init__(methodName)
        self.stack = None

    def test_push(self):
        """Тестируем push."""
        stack = Stack()
        stack.push('testdata')
        self.assertEqual(stack.top.data, 'testdata')
        self.assertIsInstance(stack.top, Node)
        self.assertEqual(stack.top.data, 'testdata')
        self.assertIs(stack.top.next_node, None)
        stack.push('testdata1')
        self.assertIsInstance(stack.top.next_node, Node)
        self.assertEqual(stack.top.data, 'testdata1')

    def test_pop(self):
        """Тестируем pop."""
        stack = Stack()
        stack.push('testdata_1')
        node_2 = stack.top
        self.assertIs(stack.pop(), node_2.data)
        with self.assertRaises(AttributeError):
            stack.pop()

    def test_str(self) -> str:
        """Тестируем str."""
        stack = Stack()
        stack.push('testdata')
        self.assertIs('testdata', str(stack.top.data))




