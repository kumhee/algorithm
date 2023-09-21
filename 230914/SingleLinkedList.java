// 단일 연결 리스트 (Single Linked List) 예시 (JAVA)
class Node {
    int data;
    Node next;
}

class SinglyLinkedList {
    private Node head;

    public void insert(int data){ 
        Node newNode = new Node()
        newNode.data = data;
        newNode.next = null;

        if(head == null){
            head = newNode;
        } else {
            Node temp = head;
            while(temp.next != null)
                temp = temp.next;
            temp.next = newNode;
        }
    }

    public void delete(int data) {
        if (head == null)
            return;

        if (head.data == data) {
            head = head.next;
            return;
        }

        Node prevNode = null, currentNode = head;

        while (currentNode != null && currentNode.data != data) {
            prevNode = currentNode;
            currentNode = currentNode.next;
        }

        if (currentNode == null)
            return;

        prevNode.next = currentNode.next;
    }

} 