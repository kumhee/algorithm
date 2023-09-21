# 단일 연결 리스트 (Single Linked List) 예시 (Python)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None

    def append(self, data):
        newNode = Node(data)
        
        if self.is_empty():
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    def prepend(self, data):
        newNode = Node(data)
        if not self.is_empty():
            newNode.next = self.head
        self.head = newNode

    def delete(self, data):
        prev_node, current_node = None, self.head
        
        if not self.is_empty():
            if self.head.data == data:
                self.head = self.head.next
            else:
                while current_node is not None and current_node.data != data:
                    prev_node = current_node
                    current_node = current_node.next

                if current_node is not None:
                    prev_node.next = current_node.next

def print_linked_list(linked_list):
    current_node = linked_list.head
    while current_node is not None:
        print(current_node.data, end=" ")
        current_node = current_node.next
 
    print()

# 단일 연결 리스트를 역순으로 뒤집는 함수 만들어보기
def reverse(linked_list):
    prev_node = None
    curr_node = linked_list.head
    
    while curr_node is not None:
        temp = curr_node.next
        curr_node.next = prev_node
        
        prev_node = curr_node
        curr_node = temp
        
    linked_list.head = prev_node

linked_list = SinglyLinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print_linked_list(linked_list)

linked_list.delete(2)

print_linked_list(linked_list)

reverse(linked_list)
print_linked_list(linked_list)

 
