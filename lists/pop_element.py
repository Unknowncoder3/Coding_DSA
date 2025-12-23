#pop() in list example
mylist=[10,20,30,40,50]
print("Original list:", mylist)
popped_element=mylist.pop(2)
print("Popped element at index 2:", popped_element)
print("List after popping element at index 4:", mylist)
popped_element=mylist.pop()
print("Popped last element:", popped_element)
print("List after popping last element:", mylist)
#if we try to pop from an empty list, it raises an IndexError
empty_list=[]
try:
    empty_list.pop()
except IndexError as e:
    print("Error:", e)
