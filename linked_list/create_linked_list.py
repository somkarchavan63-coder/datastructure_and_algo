class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
         new_node=node(data)

         if self.head is None:
             self.head=new_node
             return 

         curr=self.head
         while curr.next!=None:
             curr=curr.next

         curr.next=new_node
         


    def delete_index(self,index):
        if index==0:
            self.head=self.head.next
            return
        curr=self.head
        
        for i in range(index-1):
            curr=curr.next

        curr.next=curr.next.next


    def display(self):
            curr=self.head
            result=[]
            while curr!=None:
                result.append(curr.data)
                curr=curr.next
            return result

    def insert_index(self,data,index):
        new_node=node(data)
        count=0
        curr=self.head
        
        for i in range(index-1):
            curr=curr.next
            

        new_node.next=curr.next
        curr.next=new_node
        
        
        


connect=linkedlist()
connect.insert(5)
connect.insert(10)
connect.insert(15)
connect.insert_index(4,1)

print(connect.display())
