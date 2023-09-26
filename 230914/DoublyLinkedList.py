# 이중 연결 리스트 (Doubly Linked List) 예시 (Python)
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
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
            newNode.prev = temp
    
    def prepend(self, data):
        newNode = Node(data)
        if not self.is_empty():
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode

    def delete(self, data):
        prev_node, current_node = None, self.head
        
        if not self.is_empty():
            if self.head.data == data:
                temp = self.head
                if temp.next: # head 다음 노드가 존재하는 경우에만 prev를 None으로 설정
                    temp.next.prev = None
                self.head = temp.next
                temp.next = None
            else:
                current_node = self.head
                
                while current_node and current_node.data != data:
                    current_node = current_node.next

                if current_node:
                    prev_node = current_node.prev
                    nextNode = current_node
                    
                    if current_node:
                        prev_node.next = nextNode
                    if nextNode:
                        nextNode.prev = prev_node
                        
    def reverse(self):
        current_node = self.head
        
        while current_node:
            temp = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp
            
            if not temp:
                self.head = current_node
            
            current_node = temp
            
def print_linked_list(linked_list):
    current_node = linked_list.head
    while current_node is not None:
        print(current_node.data, end=" ")
        current_node = current_node.next
 
    print()

linked_list = DoublyLinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Original Linked List:")
print_linked_list(linked_list)

linked_list.delete(2)

print("Linked List after deleting 2:")
print_linked_list(linked_list)

linked_list.reverse()

print("Reversed Linked List:")
print_linked_list(linked_list)

