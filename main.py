class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def stack_push(self, item):
        self.data.append(item)

    def stack_pop(self):
        if len(self.data) == 0:
            last_item = None
        else:
            last_item = self.data.pop()
        return last_item

    def stack_peek(self):
        if len(self.data) == 0:
            last_item = None
        else:
            last_item = self.data[-1]
        return last_item

    def stack_size(self):
        return len(self.data)


def check_balance(list_check):
    check_stack = Stack()
    for item in list_check:
        check_stack.stack_push(item)

    count_1 = 0
    count_2 = 0
    count_3 = 0
    while True:
        res = check_stack.stack_pop()
        if res is None:
            break
        if res == ")":
            count_1 += 1
        elif res == "]":
            count_2 += 1
        elif res == "}":
            count_3 += 1
        elif res == "(":
            count_1 -= 1
        elif res == "[":
            count_2 -= 1
        elif res == "{":
            count_3 -= 1

    if count_1 == 0 and count_2 == 0 and count_3 == 0:
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == "__main__":
    list_check = "[([])(([[]]))]{()}{}[]"
    print(check_balance(list_check))




