from tkinter import *
from tkinter import ttk


root=Tk()
root.title("Original")
frm=ttk.Frame(root,padding=30)
frm.grid()
ttk.Label(frm,text="Do you know A fortune that you don’t use?  ").grid(column=0,row=0)
ttk.Button(frm,text="YES",command=root.destroy).grid(column=1,row=0)
ttk.Button(frm,text="NO",command=root.destroy).grid(column=2,row=0)
btn = ttk.Button(frm)
# print(btn.configure().keys())
# print(set(btn.configure().keys()) - set(frm.configure().keys()))
# print(dir(btn))
# print(set(dir(btn)) - set(dir(frm)))
# fred = Button(self, fg="red", bg="blue")
root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,25,30]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, marker='*',color='lightblue', linewidth=3 )
ax.scatter([2,4,6],
 [5,15,25],
 color='darkgreen',
 marker='^')
ax.set_xlim(1, 6.5)
plt.sav
efig('foo.png')
plt.show()
from os import name

import learn

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import seaborn and matplotlib

import matplotlib.pyplot as plt
import seaborn as sns



# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkmacosx import Button

window=tk.Tk()
but=Button(
             text="click mi",
             bg="blue",
             fg="yellow",
             width=300,height=25,
             font="Nazanin"

)

lab= tk.Label(
             text="Hellow ? world!",
             bg="yellow",
             fg="green",
             width=20,height=20,
             font="Nazanin"
# )
entry=tk.Entry(
             bg="blue",
             fg="yellow",
             width=50,
             font="Nazanin"

)

# lab.pack()
# but.pack()
entry.pack()
window.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk


window=tk.Tk()
label=tk.Label(text="Name")
entry=tk.Entry()
label.pack()
entry.pack()
name=entry.get()
entry.delete(0)
window.mainloop()

from  tkinter import *

window=Tk()
window.geometry("340x340")
window.title("python learning ")
icon=PhotoImage(file="logok.gif")
window.iconphoto(True,icon)
window.mainloop()

#---------------------------------------------------------------------------------------------------------------------------
learning python preliminary and advanced
The subject of casting
print("----------------")
x=int("3")
print(x)
print(type(x))
y=float(4)
print("----------------")
print(y)
print(type(y))
print("----------------")
t=str(4.2)
print(t)
print(type(t))
print("----------------")
#---------------------------------------------------------------------------------------------------------------------------
#The subject of string
# Myname="Mahnaz"
# Myfamily="Ataee"
# print(Myname+Myfamily)
# Myname1='Myname is :"Mahnaz" '
# print(Myname1)
# # Myname2='Myname is :\n "Mahnaz" '
# # Myname3='Myname is :\t "Mahnaz" '
# Myname3='Myname is :\b "Mahnaz" '
# Myname4="""
# Myname is :
#  "Mahnaz"""
#
# print(Myname4)
#---------------------------------------------------------------------------------------------------------------------------
#slicing string
# x="problem!"
#index (x) :01234
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[0:4])
# print(x[:4])
# print(x[2:])
# print(x[-4:-1])
# تا ایندس قبل از مثلا 4 نشون میده
# اگه شما هیچی نزارید از 0 شروع میکنه
# اگه شما هیچی نزارید تا اخر نشون میده
# اگر شما بخاید از ایندکس اخر بیاید به اول ایندکس آن منفی میشود
#---------------------------------------------------------------------------------------------------------------------------

#جلسه سوم پایتون
#
# maps=["Iran","germany","china"]
# print(len(maps))
# maps.append("usa")
# maps.pop(1)
# for x in maps:
#         print(x)

#خواندن پشته و stack
#مطالب در پایتون
#ساخت رزومه با بیلدر
#کار با os


#تمام دیکشنری های سیستم را نشان میدهد نرم افزارها و فایل های اجرایی
# import os
# path="/"
# dir_list=os.listdir(path)
# print("files and directionris in",path,":")
# print(dir_list)

# import os
# print(os.uname())
# os.system("IS")
# print(list(os.environ))

#کتابخانه داک
#pypl

#---------------------------------------------------------------------------------------------------------------------------
#concatenat string
#
# name="Mahnaz"
# lastname=" Ataee"
# city=" mashhad"
# x=name +" " +lastname+" "+city
# # print(x)
#
#
# # # باید از format string استفاده کنیم
# Age = 30
# # text = "My age is : " + str(Age)
# # print(text)
#
# c= f"my name is :{name}"+  f"   my lastname is :{lastname}"+ f"  my city is :{city}" + f" my age is :{Age}"
# print(c)

#---------------------------------------------------------------------------------------------------------------------------
# String Methods
# txt="mahnaz"
# print(txt.capitalized())
# capitalize  اولین حرف را بزرگ می کند
# print(txt.casefold())
# casefold  حروف را کوچک می کند
# print(txt.count(" "))
# count این حرف که داخل آن قرار می گیرد چند بار استفاده شده
# print(txt.find("i"))
#find موقعیت آن وسطش را به من برگردان
# print(txt.index("i"))
# index اولین شماره اندیس ارایه حرف را به من بده
# print(txt.format())
# format میتونیم هرتعداد که خواستیم اکولاد بزاریم و در داخل ان مقادیر را اظافه کنیم
# print(txt.strip())
# strip با استفاده از این میتوانیم فاصله ها را حذف کنیم
# print(txt.title())#**
# title   هر عنوانی که قرار بگیرد حرف اول آن را با حروف بزرگ چاپ میکنه
# print(txt.upper())#**
# upper  همه ی حروف را بزرگ می کند
# print(txt.lower())#**
# lower  همه ی حروف را کوچک می کند
# print(len(txt))#*** بسیار مهم برای پیدا کردن تعداد کاراکترهای یک رشته
#---------------------------------------------------------------------------------------------------------------------------

# booleans

# oldepass="1234"
#
# newpass1="123456"
# newpass2="1234569"


# print(bool("engineer"))
# print(bool(12))
# print(bool(" "))
# print(1==3)
#
# print(newpass1==newpass2)

#---------------------------------------------------------------------------------------------------------------------------
#game moaama
#هر عددی را وارد کنی 8 را برمیگرداند.
# first_number=int(input("Enter your number 1-9 : "))
# number=first_number
# number*=2
# number+=8
# number+=first_number
# number-=2
# number//=3
# number-=first_number
# number*=4
# print(number)
#---------------------------------------------------------------------------------------------------------------------------
# lists data type for astoreg
# thislist=[12,2,6,8]
#لیست ها میتوانند مقادیر تکراری را در خود قرار بدهند

# mylist=["mina","monire","sahar","sara"]
# print(mylist[1:6])
# print(mylist[-1:-6])
#فضاهای خالی ایندکس گذاری میشوند.

# liste1=["mahnaz",5,True]
# print(liste1)
#
# numberr=[1,2,3,8,4,6]
# print(numberr[1:])


#---------------------------------------------------------------------------------------------------------------------------
#change lists item
#تغییر یک لیست در ایتم
#
# mylists=["monire","sara","fateme","zahra","nima","setare"]
# print(len(mylists))
# # mylists[5]="mahnaz"
# mylists[1:2]=["mahnaz","jafar"]
#
# print(mylists)
# print(len(mylists))
# # ایندکسی که وجود ندارد بهش اظافه میشه
#
# mylists1=["monire","sara","fateme"]
# # mylists1[2:4]=["nader","negah"]
#
# mylists1.insert(1,"negin")
# print(mylists1)
#---------------------------------------------------------------------------------------------------------------------------
#افزایش آیتم ها لیست

# frends=["monire","sara","fateme","zahra","nima","setare"]
# new_frends=["sepehr","nadya","negar"]

# print(mylists)

# mylists.append(56)
#اون چیزی که میخای به انتهای لیستت اظافه کنی به من بده به معنی پیوست کردن
# print(mylists)

# قراردادن یک مقدار در یک لیست

# insertt
# mylists.insert(1,"mahii")

# print(mylists)

#extend  بسط دادن این لیست اظافه میشه به لیست دیگ
# frends.extend(new_frends)
# print(frends)
# new_frends.extend(frends)
# print(new_frends)



# ما در لیست ها میتوانیم مقادیر را تغییر دهیم ولی در تاپل ها نمیتوانیم تغییر دهیم
#یعنی نمیتوانیم به تاپل ها چیزی را اظافه کنیم

#
# cars=("ferary","bogati","porshe")
# # cars.ex


#---------------------------------------------------------------------------------------------------------------------------

#rimove items lists حذف کردن ایتم عنصر از لیست


# lists1=["taha","gadir","helma"]
# lists1.remove("taha")
# lists1.remove("samira")
# lists1.pop(2)
#اگه بهش هیچ مقداری را ندیم میاد مقدار اخر را حذف میکند
# lists1.pop()

# print(lists1)
# pope اون اندیس مورد نظر رو بهش میدیم و برای ما ان را حذف میکنه
# del lists1
# print(lists1)

#
# lists1.clear()
# print(lists1)
#پاک سازی لیست


#---------------------------------------------------------------------------------------------------------------------------

#sorted item lists   براساس حروف الفبا مرتب میکنیم


# lists1=[9,6,2]
# list2=["Asal","nima","dara","Sanok"]
#
# lists1.sort()
# list2.sort()
# print(lists1)
# print(list2)
# newlist=list2.copy()
# print(newlist)

#---------------------------------------------------------------------------------------------------------------------------
#lists



#باید به عنوان یک برنامه نویس بلد باشید نیازهای خودتون رو برطرف کنید

#سایت rogramiz





#stack ower flow

#تیک سبز عشقه !!
#---------------------------------------------------------------------------------------------------------------------------
#Tupples


#نه میشه به اونا چیزی اظافه کنی نه میشه ازشوت چیزی حذف کنی


#immutable and
frends=("farhad","vahid","yasna","bahar")

# print(frends)
# print(type(frends))
#
# newlist=list(frends)
# print(type(newlist))
# newlist[1]="farrid"
# print(newlist)
# newtupple=tuple(newlist)
# print(type(newtupple))
# tuple1=(1,2,3)
# tuple2=("r","u","k")
# tuple3=tuple1+tuple2
# print(tuple3)
#
# #زمانی هست که شما یک تاپل با یک ایتم دارید برای اینکه محیط بفهمد ایتم شما از نوع تاپل هست باید یک کاما بزارید
# tuple4=("farshid",)
# print(type(tuple4))

#---------------------------------------------------------------------------------------------------------------------------

#sets نامرتب و بدون ایندکس گذاری
#غیر قابل تغییر و نباید یک مقدار تکراری وجود داشته باشد unik


# sets1={"kir","gyo","no asab","khab"}
# sets2={"kir","gyo","no asab","khab"}

# print(sets1)

# mysets1={"reza","ali","helma","sina"}
# mysets2={"mahnaz","nilofar"}

# print("farid" in mysets)
# mysets.add("genium")
# print(mysets)

# mysets1.update(mysets2)
# print(mysets1)
# mysets1.remove("reza")
# print(mysets1)
# mysets1.discard("ali")
# print(mysets1)

# mysets1.pop()
# print(mysets1)
# #pop از انتهای ست حذف می کند
# mysets1.clear()
# print(mysets1)
# myset3=mysets1.union(mysets2)
# print(myset3)

#instraction update  بین دو تا لیست مشترک هاش زو چاپ میکنه
# x={"nima","moji","mohamad"}
# y={"niki","mahnaz","asma","moji"}
# x.symmetric_difference_update(y)
# print(x)

# symmetric_difference_update  مقادیر مشترک از ست ها حذف میشوند

#---------------------------------------------------------------------------------------------------------------------------
#python dictionary

# me={
#
#   "name" : "mahnaz" ,
#   "lastname" : "ataee" ,
#   "age" : 21
#
# }

# print(type(me))
# #در دیکشنری ها نمیتوانید مقادیر تکراری بزارید
#
# x=me.values()
# print(x)
#
# x=me.get('name')
# print(x)
#
# x=me.keys()
# print(x)
#
# x=me.items()
# print(x)
#
#
# x= "frend" in me
# print(x)
#را های بررسی یک کلید در یک دیکشنری

#---------------------------------------------------------------------------------------------------------------------------
# Python Dictionaries(change and add items)
#
# me={
#
#   "name" : "mahnaz" ,
#   "lastname" : "ataee" ,
#   "age" : 21
#
# }
# #ما میتوانیم از دو طریق مقادیر آن را تغییر بدهیم
# me["age"]=40
# print(me)
# me.update({"name":"mina"})
# print(me)
# me["frind"]="vahid"
# print(me)
# me['friend']='ali'
# me.update({'languge':'pertion'})
# print(me)
#اظافه کردن کلیدهای مختلف به دیکشنری ها

#---------------------------------------------------------------------------------------------------------------------------
# Python Dictionaries(Remove Items)

#
# me={
#
#   "name" : "mahnaz" ,
#   "lastname" : "ataee" ,
#   "age" : 21
#
# }
#اخرین ایتم درر دیکشنری را از آن حذف می کن popitem

# me.popitem()
# print(me)

# print(me)
# me.pop("lastname")
# print(me)
#
# friends=["mozgan","neda","soraya"]
# print(friends)
# friends.pop()
# print(friends)
#
# del me['name']
# print(me)
# me.clear()
# print(me)

#---------------------------------------------------------------------------------------------------------------------------
# dictionr1={
#
#   "name" : "mahnaz" ,
#   "lastname" : "ataee" ,
#   "age" : 21
#
# }

# dict2=dict.copy()
# print(dict2)
# dict2['friend']="dorsa"
# print(dict2)
# print(dict)
# dictionry1=dict(dictionr1)
# print(dictionry1)
# dictionr1['color']="black"
# print(dictionry1)

# nested dictionry

# name_family={
#   'child1':{'name':'negar','lastname':'ataee'},
#   'child2':{'name':'nazanin','lastname':'rahmati'}
#
# }
#
# print(name_family['child1'])
# print(name_family['child1'])

#---------------------------------------------------------------------------------------------------------------------------
# python conditions


# a=50
# b=32
#
# if a>b:
#   print("a greater than b")
#
# else:
#   print("a less than b")

#short hand if

#
# a=2
# b=330
#
# print("A") if a>b else print("B")

# if a>b:
#pass یک کلمه کلیدی که که هیچ اتفاقی نمیوفتد و فقط به دستورات بعدی ما را پاس میدهد
#---------------------------------------------------------------------------------------------------------------------------

#whiles loops
#
# while True:
#   print('hello')

#تا زمانی که  کوچک از 6 هست بیا نام را نمایش بده و نام به 1 اظافه کنnum
# num=1

# while num<10:
#   num+=1
#   if num==6:
#     continue
# # وقتی به کانتنیو رسید دستورات بعدی را اجرا نمیکند
#   print(num)
# i = 1
# while i > 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

#---------------------------------------------------------------------------------------------------------------------------
# Tasks python

# stored_password='12345'
# intered_password=input("enter your password: ")
# while intered_password!=stored_password:
#        intered_password=input("ooo yuo are wrong, enter again: ")
#
# print("you are successfully")

#
# friendes=["ali","reza","neda"]
#
# m= "bahram" in friendes
# print(m)

#
# users={
#      "amir": "1234",
#      "reza" : "4567",
#      "farid" : "6789"
#
#     }
#
# entred_username = input("enter your username: ")
# entred_password = input("enter your password: ")
#
# while entred_username not in users or users[entred_username]!=entred_password:
#     print("you are username or password  wrong ")
#     entred_username = input("enter your username again: ")
#     entred_password = input("enter your password again: ")
#
# print("your are loged in!")

#---------------------------------------------------------------------------------------------------------------------------
# for loop in python
#به ازای هر مقدار همون x به من نماییش بده سلام را
# اخری 3 تا 3 تا اضافه میکنه
#
# number=0
# for x in range(1,8):
#     number+=1
# print(number)

# a1=['mahnazi','jafar','neda','anita','ali','maryam','anoshe']
# b2=['mahnazi','sogand','neda','anahita','sardar','mozgan','setare']
#
# b=[]
# for i in a1:
#     for y in b2:
#         if i==y:
#             b.append(y)
#
# print(b)

# name=input("enter your fullname: ")
# name=name.lower()
# name=name.replace(" "," ")
# b=[]
# for nam in name:
#     if nam not in b:
#       b.append(nam)
#       print(f"your name has :{name.count(nam)}{nam}")
#
#---------------------------------------------------------------------------------------------------------------------------
# function
# call
# def me():
#     print("my name is mahnaz")
#
# me()
# def myname(name,lastname):
#     print(f"hello {name}")
#     print(f"hello {lastname}")
#
# myname('dehyami','mahnaz')
#
#
# def sum(a,b):
#     print(a+b)
#
# sum(2,3)

# tasks

# def mypassword(password):
#     if len(password)<8:
#         print("your password must be at last 8 character")
#     elif password.isnumeric():
#         print("you password must ad list one letter")
#     elif password.isalpha():
#         print("your password must ad list one number")
#     else:
#         print("yes your password is correct ")
#
# while True:
#     password = input("entered password: ")
#     mypassword(password)
#---------------------------------------------------------------------------------------------------------------------------
# python functions
# a=input("enter your name :")
# b=input("enter your lastname :")
# def myfunication(a,b):
#     print(f"hellow {a} {b}")
#
# myfunication(a,b)


# def hello(*hams):
#    for n in hams:
#        print(f"hellow {n}")
#
# hello("mahnaz","sara" , "neda" ," sofa")


# def hellow(name,lastname,*names):
#     print(name)
#     print(lastname)
#     print(names)
#
# hellow('ali','zahra')


#برنامه نویس ها این سومی  *names را args به معنای ارگومان مینویسند
# MahnazAtaee24@M23



# def hello(b):
#     for item in b:
#         print(f"hellow {item}")
#
#
# hello(23)

#تابع ما با استفاده از کلمه ریترن تابع ما یک مقدار را میدهد بیرون و ما میتوانیم استفاده کنیم

# def sum(a,b):
#     a+=1
#     b+=5
#     return a,b
#
# result=sum(12,3)
# print(result)
# زمانی که تابع ما برابر میشه با چیزی که داره ریترن میشه


# username=input("enter your username: ")


# def myn(username):
#     if len(username)>8:
#         return False
#     else:
#         return True
#
#     print("helloe")
#
#
# if myn(username):
#     print("your username is ok")
# else:
#     print("your username is wrong")
#
# def hellow():
#     pass

# tasks

# character=input("enter your character: ")


# def myfunc(a):
#     ups=0
#     lows=0
#     for n in a:
#         if n.isupper():
#             ups+=1
#         elif n.islower():
#             lows+=1
#         else:
#             pass
#
#     print(f"upper cases: {ups}")
#     print(f"lower cases: {lows}")
#
# myfunc(character)


# def mynumber(number):
#    if number % 2==0:
#        print("number is even")
#    else:
#        print("number is odd")
#
# number=int(input("enter your number: "))
# mynumber(number)

#---------------------------------------------------------------------------------------------------------------------------
# lesson python 5
# برای ترسیمات عادی هست
#
# import numpy as np
# import seaborn as sb
# import matplotlib.pyplot as plt
# data=np.random.rand(4,6)
# plt.show()
# heat_map=sb.heatmap(data,xticklabels=False,yticklabels=False)
# plt.xlabel("values on X axis")
# data=np.random.rand(4,6)
# heat_map=sb.heatmap(data)
# plt.ylabel('values on Y axis')


#seaborn  مطالعه
#   نصب dgango
# flask +بخوانیم
# pylone
# scikit
#توسط اقای روناچر ساخته شده
#فلاسک یک فریمورک قدرتمند برای توسعه وب که باعث میشه با استفاده از اون کدهامون رو بتونیم منسجم بنویسیم و در زمان صرفه جویی کنیم وهماهنگی با اعضای تیم
#فلسک یک میکرو فریمورک هست چون یک فریمورک سبک هست که بسیاری از ابزارها و کتابخانه های سایر رایج فریمورک ها را ندارد
#فلسک یک کتابخانه کوچک و قدرتمند هست که شرکت های مثل سامسونگ و uber از ان استفاده ممی کنند
#این فریم ورک از دو تا بخش تشکیل شده یک بخش کامپوننت که برای مسیریابی و دیباگ کردن و ارتباط با وب سرور
#بخش دوم که جینجا هست برای داده های مختلف رو در قالب شما نمایش میده یک موتور قالب هست
#---------------------------------------------------------------------------------------------------------------------------
# task Calendar
#برای درست کردن این تقویم ابتدا سال شمسی رو + 622 یا 621 میکنیم.
# اگر تاریخ مدنظر از اول فزوردین تا 10 دی بود عدد 621


# def convertor(day,month,year):
#     if month>10 or day>10 and day==10:
#         berthtey=year+622
#
#     else:
#         berthtey=year+621
#
#     print(f"year milady your is {berthtey}")
#
# day=int(input("enter your day: "))
# month=int(input("enter your day: "))
# year=int(input("enter your day: "))
#
# convertor(day,month,year)
#---------------------------------------------------------------------------------------------------------------------------
# lesssson 6

#bsd
#csv
#simple
# df.index


# def myfuds(a):
#     return a+10
#
#
#
# print(myfuds(30))

# myfund2=myfuds
#
# myfund2(20)
# x=lambda a:a+10
# x(32)
#
#
#
# def myfund(n):
#    return lambda a: a*n

# mydobler=myfund(2)
# print(mydobler(1))

# mylist=[1,3,6,7,8]
# mylist2=[5,8,2,3,4]
#
# x=list(map(lambda a,b:a*b ,mylist,mylist2))
#
# print(x)



#Class
# class MyClass:
#     def __init__(self,name,lastname):
#      self.myname=name
#      self.mylastname=lastname
#
# p1=MyClass("ali","ahmadi")
# p2=MyClass("reza","nadir")
# print(p1.myname)
# print(p1.mylastname)
# print(p2.myname)
# print(p2.mylastname)
#ایجاد دو تا شی ء با دو تا اسم متفاوت با استفاده از یک سری توابع

# class Person:
#     def __init__(self,name,lastname):
#         self.myname=name
#         self.mylastname=lastname
#     def fullname(self):
#         print(f"hi mynames {self.myname} and mylastname {self.mylastname}")
# p1= Person("mahnaz","ataee")
# p1.fullname()
# p1.myname="nazanin"
# p1.fullname()
#
# del p1.myname

# class Car:
#     car_numbers=0
#     def __init__(self,name,price):
#         self.myname=name
#         self.myprice=price
#         self.stutus=False
#         Car.car_numbers+=1
#
#     def start(self):
#         if self.stutus==False:
#                self.stutus=True
#                print(f"car is {self.myname} satarting")
#         else:
#               print("pleases one dont start ")
#
#     def off(self):
#         if self.stutus==True:
#               self.stutus=False
#               print(f"car is {self.myname}  off")
#         else:
#             print("pleases off dont off ")
#
# print(Car.car_numbers)
# c1=Car("toyota","25000")
# c2=Car("mazrati","65000")
# print(Car.car_numbers)
# c1.start()
# c1.start()
#
#
# c1.off()
# c1.off()
#
#
#---------------------------------------------------------------------------------------------------------------------------
# intrehance
# class Person:  #parent
#     def __init__(self,firstname,lastname):
#         self.firstname=firstname
#         self.lastname=lastname
#
#     def printname(self):
#         print(self.firstname,self.lastname)
#
#
#
# class Student(Person): #child
#     def __init__(self,firstname,lastname):
#        Person.__init__(self,firstname,lastname)
#
# s1=Student("sara","asadi")
# print(s1.firstname,s1.lastname)
# s1.printname()


# task
# cs =[
#     {"title":"python",
#      "teacher":"amiri"
#
#     },
#     {
#         "title":"html",
#         "teacher":"Dehyami"
#     },
#     {
#         "title":"php",
#         "teacher":"Enayati"
#
#     }
#
# ]

#
# class User:
#     def __init__(self,firstname,lastname):#parent
#         self.fname=firstname
#         self.lname=lastname
#         self.curses=[]
#
#     def fullname(self):
#         print(f"firstname : {self.fname},lastname: {self.lname}")


#
# class Student(User): #child
#     def __init__(self,firstname,lastname,email):
#         super().__init__(firstname,lastname)
#         self.email=email
#
#
#     def printcurses(self):
#         if self.curses:
#             for curs in self.curses:
#                 print(curs['title'])
#
#         else:
#             print("is user not curses")
#
#
#     def fullname(self):
#         print("i am student")
#         super().fullname()
#
# s1=Student("amir","amiri","amiri@gmail.com")
# s1.curses.append(cs[1])
# s1.curses.append(cs[0])
# s1.printcurses()
# class Teacher:
#     def __init__(self,firstname,lastname,code):
#         super().__init__(firstname,lastname)
#         self.code=code
#
#
#     def fullname(self):
#         print("i am Teacher")
#         super().fullname()
#
#
# t1=Teacher("amir","amiri",22)


#---------------------------------------------------------------------------------------------------------------------------
# python scope
# یک مفهوم جدید
#clobal scope
#یک کلمه کلیدی به اسم global که اگر درون تابع باشد به صورت سراسری است
# c=400
# def test():
#     global c
#     c=200
#
# test()

# python modules
# ما ممکنه که هزار خط کد داشته باشیم و نمیتوانیم توابع را داخل همین فایل بزاریم برای اینکه کار ما اسان شود در داخل یک فایل دیگر توابع را مینویسیم و داخل فایل مورد نظر آن را import می کنیم.

import mymoduole
# from mymoduole import hello,sms
#
#
# hello("mahnaz")
# sms("09136544125")

#ماژول یک فایل پایتونی است که فراخانی میشود.
# برای اینکه کد هامون رو مخفف کنیم از as استفاده میکنیم

# برای فراخانی کردن یک تابع فقط کافیه اول from رو نوشته و بعد اسم ماژول و بعد import و بعد اسم تابع

# علامت * تمام ماژول ها رو میاره



# import pytz
#
# tz=pytz.timezone("Asia/")
#
# x = datetime.now(tz)
#
# print(x)


# x=datetime.datetime(1403,5,25)
#
#
# print(x)



# list=["mina","negar","sara"]
# print(random.randint(10000,99999))
# print(random.randrange(10000,99999))
# print(random.choice(list))

# import platform
# import random
# from random import randint


# from datetime import datetime,timedelta
# start=datetime.now()
# end=start+timedelta(hours=48)
# print(start)
# print(end)
#
# c=end-start
# print(c.days)
# print(int(c.total_seconds()/86400))


# list=[10,22,35,60,89,220]
# b=max(list)
# k=min(list)
# print('max is ',b)
# print('min is ',k)

#abs یک تابع قدر مطلق

# print(abs(-15))
# #pow عدد اول رو به توان عدد دوم می رسونه
#
# print(pow(5,4))
#
# #math یک ماژول ریاضی که یه سری توابع هست
# import  math
# #sqrt جزر هست
# print(math.sqrt(54))
# print(math.ceil(1.5))
# print(math.floor(1.5))

import json
# import json
#
# # some JSON:
# x =  '{ "name":"John", "age":30 , "city" :"New York","isMarried":false,"lastname":"null"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y)

#
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York",
#     "imarrid":None
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)
#
#---------------------------------------------------------------------------------------------------------------------------
# names=['amir','milad','hossain','reza','mahdi']
# newlist=[name for name in names if "a" in name]
# print(newlist)

# for name in names:
#     if "a" in name:
#         newlist.append(name)
# print(names)
# print(newlist)

# newlist1=[x for x in range(12) if x>2]
# print(newlist1)
#---------------------------------------------------------------------------------------------------------------------------
mylist=['mahnaz','jalil','mosen','zahra'] #iterblae to itertor for iter




# class MyIter:
#
#     def __init__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         if self.a>=6:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
#
#
# print(MyIter())

# a="mahnaz"
# print(a)
# b=a
# print(b)

# def test(a):
#     print(a)
#
# b=test
# b("mn")

#---------------------------------------------------------------------------------------------------------------------------
# decorators
# Python program to illustrate functions
# can be treated as objects
# def shout(text):
#     return text.upper()
#
# print(shout('Hello'))
#
# yell = shout
#
# print(yell('Hello'))

# Python program to illustrate functions
# can be passed as arguments to other functions
# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
#
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
#
# greet(shout)
# greet(whisper)
# Python program to illustrate functions
# Functions can return another function

# def create_adder(x):
#     def adder(y):
#         return x+y
#
#     return adder
#
# add_15 = create_adder(15)
#
# print(add_15(10))
# defining a decorator
# def hello_decorator(func):
#     # inner1 is a Wrapper function in
#     # which the argument is called
#
#     # inner function can access the outer local
#     # functions like in this case "func"
#     def inner1():
#         print("Hello, this is before function execution")
#
#         # calling the actual function now
#         # inside the wrapper function.
#         func()
#
#         print("This is after function execution")
#
#     return inner1
#
#
# # defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")
#
#
# # passing 'function_to_be_used' inside the
# # decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)
#
# # calling the function
# function_to_be_used()

#ساخت ربات سایت خزنده ، صفحات را کپی و پست می کند
#web scripting

























