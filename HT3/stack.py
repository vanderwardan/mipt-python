from sys import stdin


class Stack:
    def __init__(self, container):
        self.stack = []
        for elem in container:
            self.stack.append(elem)

    def top(self):
        return self.stack[-1]

    def pop(self):
        elem = self.stack[-1]
        self.stack.pop()
        return elem

    def push(self, elem):
        self.stack.append(elem)

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return " ".join(map(str, self.stack))


exec(stdin.read())
