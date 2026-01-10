#Record Management Software
#The User will give his/her name and can make a file(.txt) where his/her record will be saved and he/she can retrive the file to see what has been done so far
#we will use datetime function to keep track of time the user has written the record
#we will also use os to keep track of exisiting files and also remove the file if the user want

import os
def getdate():
    """ This Function helps in Getting the date and time"""
    import datetime
    a=datetime.datetime.now()
    date=a.strftime("%d/%m/%Y|%H:%M:%S%p")#convers the datetime function to desired choice
    return date
user=str(input("Enter Your Name:-"))
user.capitalize()
user1=str(input("Enter The Name of File(.txt) where You Want to Store Your Progress:-"))
user1.capitalize()
user2=user.capitalize()+user1.capitalize()+".txt"
exist=os.path.exists(user2)#This checks the file path whether the file exists or not
var3="n"
can_delete=False
with open(user2,"a+") as file:#a+ mode helps both in append and read
    if not exist:
            file.write(f'                 Welcome To The "{user2.capitalize()}" File You Have Successfully Created,{user.capitalize()}\n')
            print("The File has Been Successfully Created,", user.capitalize(),",Run The Program Again To Store and Update your Record")
    else:
        can_delete=True
        var1=str(input("Press {y} To Add Record or {n} To Discontinue:-"))
        while(var1=="y"):
            var=str(input("Enter Your Progress/Record:-"))
            file.write(f"[{getdate()}]:-{var.capitalize()}\n")#f strings are used to write the record in desired format
            print([getdate()], "The Record Has Been Successfully Updated")
            var1 = str(input("Press {y} To Add Record or {n} to Discontinue:-"))
        var3=str(input(f'{user.capitalize()},Do You Want To Retrieve Your Record For The current file "{user2}"(y/n):-'))
        def retrieve():
            """ This Function helps in retrieving the record/progres of the user"""
            length =len(f'                 Welcome To The "{user2}" File You Have Successfully Created,{user}\n')
            v=length + 1#This line helps in getting the length of the first line and +1 is written to move the pointer to the second line
            file.seek(v)#since open() returns a file pointer therefore seek() helps in telling where the file pointer is
            c = file.read()#With this function we can read the contents of the file
            print(c)
        if(var3=="y"):
            print(f'Here Is your Record For "{user2}" File')
            retrieve()
if can_delete and var3 in('y','n'):
            var4 = str(input(f'{user.capitalize()},Do You Want To Remove/Delete Your "{user2}" File(y/n):-'))
            if(var4=='y'):
                os.remove(user2)#It helps in removing the file the user has made
                print([getdate()],f'{user.capitalize()},Your File "{user2}" Has Been Sucessfully Deleted')
            else:
                print("Keep Updating!!!")
#To use the Doc function write print(functionname.__doc__)
