class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new


    def insert(self, data, i):
        if i < 0:
            return
        new_node = Node(data)
        if i == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < i - 1:
            current = current.next
            count += 1
        if current:
            new_node.next = current.next
            current.next = new_node

    def print(self):
        val = self.head
        while val is not None:
            if val.next is None:
                print(val.data)
            else:
                print(val.data, end=" -> ")
            val = val.next

    def delete(self, i):
        if i < 0 or not self.head:
            return None
        if i == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data
        current = self.head
        count = 0
        while current.next and count < i - 1:
            current = current.next
            count += 1
        if current.next:
            deleted_data = current.next.data
            current.next = current.next.next
            return deleted_data

    def index(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def swap(self, i, j):
        if i == j:
            return

        current_i = self.head
        prev_i = None
        count_i = 0
        while current_i and count_i < i:
            prev_i = current_i
            current_i = current_i.next
            count_i += 1

        current_j = self.head
        prev_j = None
        count_j = 0
        while current_j and count_j < j:
            prev_j = current_j
            current_j = current_j.next
            count_j += 1

        if not (current_i and current_j):
            return

        if prev_i:
            prev_i.next = current_j
        else:
            self.head = current_j

        if prev_j:
            prev_j.next = current_i
        else:
            self.head = current_i

        current_i.next, current_j.next = current_j.next, current_i.next

    def isort(self):
        if not self.head or not self.head.next:
            return  

        sorted_head = None  

        current = self.head
        while current:
            next_node = current.next  

            # Insert the current node into the sorted list
            if not sorted_head or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                prev_sorted = None
                sorted_current = sorted_head
                while sorted_current and current.data >= sorted_current.data:
                    prev_sorted = sorted_current
                    sorted_current = sorted_current.next
                prev_sorted.next = current
                current.next = sorted_current

            current = next_node 

        self.head = sorted_head 
if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()           # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    print(L.index(7))   # 3
    print(L.index(9))   # -1
    L.swap(1, 4)
    L.print()           # 3 -> 8 -> 2 -> 7 -> 5 -> 10 -> 6
    L.swap(2, 0)
    L.print()           # 2 -> 8 -> 3 -> 7 -> 5 -> 10 -> 6