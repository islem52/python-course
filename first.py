# number = 5
# iteration =0
# cond = False

# while cond==False:
#     iteration = iteration+1
#     new = int(input("enter a number: "))
#     if new>number:
#         print("the number is greater than it should be")
#     else: 
#         if new<number:
#             print("the number is lesser than it should be")
#         else:
#             print("you are correct")
#             print("you sucsseded after"+iteration+"tries")
#             cond==True
            
# op1 = input("entrer la première opérande")
# op2 = input("entrer la deuxième opérande")

# operations =["add","mutiply","substract"]

# cond = False

# while cond ==False :
#     operation = str(input("entrer l'operation arithmétique:"))
#     if operations.__contains__(operation):
#         cond = True

# if operation == operations[0]:
#     print('')



# git init : initialiser historique des repo
#git add . : pour considerer les changes
#git commit -m "message"
# git checkout -b "branch-name" : créer une branche




#############################################""""
# word =(input("enter a word :")) ;
# num=0
# for i in word:
#     num = num + 1

# if num > 1 : 
#     print(f"you typed {num} chars") 

# #************************************************************************************
# number = int(input("please enter a number :"))

# if number%2==0: 
#     print("the number you entered is even ")
# else:
#     print('the number you entered is odd')

# age = int(input("please enter your age :"))
# if age >= 18 :
#     print("you are a mature person")
# else :
#     print(f"you can return after {18 - age} years")

#-**********************************************

houmaScore = int(input("enter the result of houma"))
branyaScore = int(input("enter the score of Beranya")) 

result = houmaScore - branyaScore

if result > 0 : 
    print("el Houma wins!!!")
elif result<0:
    print("branya wins")
else:
    print('draw') 
    