list1 = [7,8,1,2,3,4,5]
list2 = [3,4,1,29,1,5,1]
list3 = [4,1,69,2,7,3,6]

list4 = list(map(lambda x,y: x+y, list1, list2))
res = list(map(lambda x,y: x*y, list3,list4))

print(res)
