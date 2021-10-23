class StackEmpty(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise StackEmpty("Stack is empty, nothing to pop")
        return self.stack.pop()

    def __str__(self):
        return "Stack: " + str(self.stack)


if __name__ == '__main__':
    s = Stack()
    s.push(34)
    s.push(23)
    s.push(18)

    try:
        v = s.pop()
        print(v)            # 18
        print(s)            # ???
        print(s.stack)      # [34, 23]

        print(s.pop())      # 23
        print(s.pop())      # 34

        print(s.pop())
    except StackEmpty:
        print("Stack is empty, nothing to pop")



