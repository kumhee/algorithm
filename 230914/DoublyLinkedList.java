// 이중 연결 리스트 (Doubly Linked List) 예시 (JAVA)
class Node {
    int data;
    Node prev;
    Node next;
}

class DoublyLinkedList {
    private Node head;

    public DoublyLinkedList() {
        this.head = null;
    }

    public boolean isEmpty() {
        return this.head == null;
    }

    public void append(int data) {
        Node newNode = new Node();

        if (isEmpty()) {
            this.head = newNode;
        } else {
            Node temp = this.head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
            newNode.prev = temp;
        }
    }

    public void prepend(int data) {
        Node newNode = new Node();
        if (!isEmpty()) {
            newNode.next = this.head;
            this.head.prev = newNode;
        }
        this.head = newNode;
    }

    public void delete(int data) {
        Node currentNode = this.head;

        if (!isEmpty()) {
            if (this.head.data == data) {
                Node temp = this.head;
                if (temp.next != null) {
                    temp.next.prev = null;
                }
                this.head = temp.next;
                temp.next = null;
            } else {
                while (currentNode != null && currentNode.data != data) {
                    currentNode = currentNode.next;
                }

                if (currentNode != null) {
                    Node prevNode = currentNode.prev;
                    Node nextNode = currentNode.next;
                    if (prevNode != null) {
                        prevNode.next = nextNode;
                    }
                    if (nextNode != null) {
                        nextNode.prev = prevNode;
                    }
                }
            }
        }
    }
}
