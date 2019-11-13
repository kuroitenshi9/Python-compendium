class Fifo:
    pass

    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        return "-".join(self.elements)

    def show(self):
        print(self.elements)

    def get(self):
        if len(self.elements) == 0:
            return 'brak elementów'
        else:
            return self.elements.pop(0)

    def put(self, value):
        list_element.append(new_element)
        return "added"

list_element = ["a", "b", "c", "d"]
fifo1 = Fifo(list_element)

print(fifo1)
print(fifo1.get())
print(fifo1)
new_element = input("Choose new element for class FIFO: ")
fifo1.put(new_element)
print(fifo1)
