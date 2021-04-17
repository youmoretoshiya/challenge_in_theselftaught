def is_same(a, b):
    return a is b

class Person:
    def __init__(self):
        self.name = "Bill"

bill = Person()
same_bill = bill
print(is_same(bill, same_bill))

another_bill = Person()
print(is_same(bill, another_bill))
