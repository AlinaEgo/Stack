from task_1 import Stack


def balance(some_stack = Stack):
    if some_stack.size() % 2 != 0:
        return print("Несбалансированно")
    else:
        new_stack = Stack([])
        while some_stack.size() > 0:
            if some_stack.peek() == "]" or some_stack.peek() == ")" or some_stack.peek() == "}":
                new_stack.push(some_stack.pop())
            else:
                congruence = some_stack.pop() + new_stack.pop()
                if congruence == '()' or congruence == '[]' or congruence == '{}':
                    continue
                else:
                    return print("Несбалансированно")
        if some_stack.size() == 0:
            return print("Сбалансированно")

if __name__ == '__main__':
    stack1 = balance(Stack('(((([{}]))))'))
    stack2 = balance(Stack('[([])((([[[]]])))]{()}'))
    stack3 = balance(Stack('{{[()]}}'))
    stack4 = balance(Stack('}{}'))
    stack5 = balance(Stack('{{[(])]}}'))
    stack6 = balance(Stack('[[{())}]'))