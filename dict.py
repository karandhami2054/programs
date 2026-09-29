# result = {}
# for i in range(1,4):
#     subject = input("Enter subjects name: ")
#     mark = int(input("Enter your marks: "))
#     result[subject] = mark
# print(result)


# store subject and mark in dictionary form
result1 = {}
subject1 = input("Enter subjects name: ")
mark1 = int(input("Enter your marks: "))
result1.update({subject1: mark1})
print(result1)