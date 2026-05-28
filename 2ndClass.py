#string
'''
s="python programming"


list1=list(map(int, input().split()))
print(list1)
print(*list1)
print(*list1, sep=",")
print(type(*list1))
'''
'''
replace
upper
lower
count
replace
find
title
strip
'''

# set-is a composite data type
# features of set-
# 1) it is a collection of different data types
# 2) but here duplicates are not allowed
# 3) unordered
# 4) mutable
# 5) ---{}
'''
a = {1, 2, 3, "naresh-it", 5.4}
# i want to add some data to existing set-
a.remove(3)
print(a)'''

# tuple-is a composite data type
# features of tuple-
# 1) it is a collection of different data types
# 2) but here duplicates are allowed
# 3) ordered
# 4) immutable
# 5) ----()

a = {1:"one", 2:"two", 3:"three", "naresh-it":"python", 5.4:"float"}
b={"naresh-it":"python", 5.4:"float", 1:"one", 2:"two", 3:"three"}
print(a.update(b))