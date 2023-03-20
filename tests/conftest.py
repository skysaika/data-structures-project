import pytest

from src.stack import Stack, Node


@pytest.fixture
def stack() -> Stack:
    stack = Stack()
    stack.push('test_data')
    return stack

@pytest.fixture
def node(stack) -> Node:
    return stack.top