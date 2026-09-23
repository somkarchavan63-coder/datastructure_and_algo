from create_linked_list import linkedlist

ll=linkedlist()
ll.insert(1)
ll.insert(2)
ll.insert(3)

def has_cycle(node):
    slow=node
    fast=node
    while fast.next==None or fast.next.next==None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return " cycle present"

    return "no cycle is present"

res=has_cycle(ll.head)
print(res)


    