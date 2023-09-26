class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# 1. 왼쪽 자식과 오른쪽 자식에 대한 노드 개수를 파악한다.   
# 2. 트리 구조를 세팅(데이터 크기로 정렬)
   
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

root_node = Node(6)
root_node.insert(3)
root_node.insert(1)           
root_node.insert(7)           
root_node.insert(4)           
root_node.insert(5)           
            
root_node.print_tree()
