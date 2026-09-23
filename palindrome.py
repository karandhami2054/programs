palindrome = input("Enter your sentence: ")
if palindrome == palindrome[-1::-1]:
    print("palindrome")
else:
    print("Not palindrome")

name = [1, 2, 3, 2, 1]
eman = name.copy()
eman.reverse()
print(eman)
if name == eman:
    print("Palindrome")
else:
    print("not Palindrome")


# WAP count the no. of students with grade "A" in following list
student_list = ["C", "D", "A", "A", "B", "B", "A"]

print("no. of student with grade A is : ", student_list.count("A") )
student_list.sort()
print("In Ascending Order :", student_list)
