from typing import Any


class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data: Any = data
        self.next_node: Node | None = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top: Node | None = None

    def __str__(self) -> str:
        """
        Метод строкового представления класса Stack
        """
        self.stack: Node

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        prev_top = self.top
        self.top = self.top.next_node
        return prev_top.data

    # def __str__(self) -> str:
    #     result = ''
    #     current_node = self.__top
    #     while current_node is not None:
    #         result += str(current_node.data) + ' -> '
    #         current_node = current_node.next_node
    #     else:
    #         result += 'None'
    #     return result

