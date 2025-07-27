dic = {'Alice':85,'Bob':75,'Charlie':95,}
name = input("Enter the stdent's name:")
if name in dic:
    print(name, "'s marks = ", dic[name])
else:
    print('the student doesn\'t exist')