class Stack():

    def __init__(self, stack:str=''):
        self.stack = list(stack)

# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        return False if len(self.stack) > 0 else True

# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, item:str):
        self.stack += item

# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.stack.pop()

# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется
    def peek(self):
        return self.stack[-1]

#size - возвращает количество элементов в стеке
    def size(self):
        return len(self.stack)

