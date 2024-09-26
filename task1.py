class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head

    @staticmethod
    def merge_sorted(list1, list2):
        merged_list = LinkedList()
        p1, p2 = list1.head, list2.head

        while p1 and p2:
            if p1.data <= p2.data:
                merged_list.append(p1.data)
                p1 = p1.next
            else:
                merged_list.append(p2.data)
                p2 = p2.next

        while p1:
            merged_list.append(p1.data)
            p1 = p1.next

        while p2:
            merged_list.append(p2.data)
            p2 = p2.next

        return merged_list

# Демонстрація роботи

# Створення двох списків
list1 = LinkedList()
list2 = LinkedList()

list1.append(1)
list1.append(3)
list1.append(5)

list2.append(2)
list2.append(4)
list2.append(6)

print("Перший список:")
list1.print_list()

print("Другий список:")
list2.print_list()

# Об'єднання двох відсортованих списків
merged_list = LinkedList.merge_sorted(list1, list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()

# Реверсування списку
print("Реверсований список:")
merged_list.reverse()
merged_list.print_list()

# Сортування списку методом вставок
merged_list.insertion_sort()
print("Відсортований список:")
merged_list.print_list()