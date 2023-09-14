class Queue:
  def __init__(self):
    self.queue= []
    
  def __len__(self):
    return len(self.queue)
  
  def is_empty(self):
    return len(self.queue) == 0
  
  def enqueue(self,item):
    self.queue.append(item)

  def dequeue(self):  #자바로는 어떻게 구현하는거죠??? array범위정해서 복사?
    if self.is_empty():
      return 'Empty'
    else:
      return self.queue.pop(0)
  def peek(self):
    if self.is_empty():
      return 'Empty'
    else:
      return self.queue[0]
    
queue = Queue()
queue.enqueue(10)    
queue.enqueue(20)    
queue.enqueue(30)

print(queue.dequeue() )
print(queue.dequeue() )
print(queue.dequeue() )
print(queue.peek())
print(queue.is_empty())

print()





#숫자뒤집기
ex = 123456
ex2 = 987654321


def reverse(ex):
  queue =  Queue()
  
  while ex >0 :   
    queue.enqueue(ex%10)        
    ex //= 10
  
  answer = 0
  while queue:
    answer = (answer*10) + queue.dequeue()
  return answer  
    
print(reverse(ex))
print(reverse(ex2))