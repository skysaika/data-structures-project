"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src import queue


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        test_queue = queue.Queue()
        test_queue.enqueue('data_1')
        test_queue.enqueue('data_2')
        self.assertEqual(test_queue.head.data, 'data_1')
        self.assertEqual(test_queue.head.next_node.data, 'data_2')

    def test_str_queue(self):
        test_queue = queue.Queue()
        test_queue.enqueue('data_1')
        self.assertEqual(str(test_queue), "data_1")

