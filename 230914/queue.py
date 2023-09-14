class Queue:
    def __init__(self) :
        self.queue = []
        
    def __len__(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return "Empty"
        else :
            return self.queue.pop(0)
        
    def peek(self):
        if self.is_empty():
            return "Empty"
        else :
            return self.queue[0]
        
        
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.peek())

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

print(queue.is_empty())
        