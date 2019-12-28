from tkinter import *
from tkinter import messagebox
import pygame
from PIL import*
from idlelib.idle_test.test_configdialog import root
from django.utils.termcolors import background
import random
import question
from django.conf.locale import lv

pygame.init()
root = Tk()
root.title("Who wants to be a Millionaire")
root.geometry('1352x652+0+0')
root.configure(background='black')
gt = ["image/Picture0.png","image/Picture1.png","image/Picture2.png","image/Picture3.png","image/Picture4.png","image/Picture5.png",
      "image/Picture6.png","image/Picture7.png","image/Picture8.png","image/Picture9.png","image/Picture10.png","image/Picture11.png",
      "image/Picture12.png","image/Picture13.png","image/Picture14.png","image/Picture15.png"]
answer =StringVar()
lv=0
dem=0
correct_answer = ""
q = StringVar()
a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()

ABC = Frame(root, bg='black')
ABC.grid()

noidung = Frame(root, bg='black', bd=20, width=900, height=600)
noidung.grid(row=0, column=0)
giaithuong = Frame(root, bg='black', bd=20, width=452, height=600)
giaithuong.grid(row=0, column=1)

help = Frame(noidung, bg='black', bd=20, width=900, padx = 130, height=200)
help.grid(row=0, column=0)
logo = Frame(noidung, bg='black', bd=20, width=900, height=200)
logo.grid(row=1, column=0)
QA = Frame(noidung, bg='black', bd=20, width=900, height=200)
QA.grid(row=2, column=0)

LogoImage = PhotoImage(file='image/logo.png')
LogoCenter = Button(logo, image=LogoImage, bg='black')
LogoCenter.grid()
##################################################################################################################
def click50_50():
    cavans = Canvas(help, bg='black',width = 160, height = 80)
    cavans.grid(row=0, column=0)
    cavans.delete('all')
    image = PhotoImage(file = 'image/help50X.png')
    cavans.create_image(90,40,image = image)
    cavans.image = image
    temp =0
    global  dem
    while(dem<2):
        hide = random.randint(1,4)
        if(dem ==0):
            temp = hide
        else:
            if(hide == temp):
                hide = random.randint(1,4)
        if(hide == 1):
            if(a1.get() != correct_answer):
                a1.set("")
                dem +=1
        elif(hide == 2):
            if(a2.get() != correct_answer):
                a2.set("")
                dem +=1
        elif(hide == 3):
            if(a3.get() != correct_answer):
                a3.set("")
                dem +=1
        elif(hide == 4):
            if(a4.get() != correct_answer):
                a4.set("")
                dem +=1  
def clickPeople():
    cavans = Canvas(help, bg='black',width = 160, height = 80)
    cavans.grid(row=0, column=2)
    cavans.delete('all')
    image = PhotoImage(file = 'image/peopleX.png')
    cavans.create_image(90,40,image = image)
    cavans.image = image
def clickFriend():
#     cavans = Canvas(help, bg='black',width = 160, height = 80)
#     cavans.grid(row=0, column=1)
#     cavans.delete('all')
#     image = PhotoImage(file = 'image/PhoneX.png')
#     cavans.create_image(90,40,image = image)
#     cavans.image = image
    getquestion(lv)
def change(lv):
    cavans = Canvas(giaithuong, bg='black',width = 452, height = 600)
    cavans.grid(row=0, column=0)
    cavans.delete('all')
    image = PhotoImage(file = gt[lv])
    cavans.create_image(230,305,image = image)
    cavans.image = image
def getquestion(lv):
    qnum = int (random.random() * 10)
    global quest    
    quest = question.get_question(lv, qnum)    
    q.set(quest[0])
    a1.set(quest[1])
    a2.set(quest[2])
    a3.set(quest[3])
    a4.set(quest[4])
    global correct_answer
    correct_answer = quest[5]
    if(lv > 6):
        cavans = Canvas(help, bg='black',width = 160, height = 80)
        cavans.grid(row=0, column=1)
        cavans.delete('all')
        image = PhotoImage(file = 'PhoneX.png')
        cavans.create_image(90,40,image = image)
        cavans.image = image

def checkAnswer(str):
    global correct_answer,lv
    if(str == correct_answer):
        if(lv == 14):
            messagebox.showinfo('congratulation', 'Chúc mừng ! Bạn đã đạt được 1 million $!')
            root.destroy()
        else:
            lv+=1
            change(lv)
            getquestion(lv)
    else:
        if(lv <5):
            messagebox.showinfo('game over', 'Bạn đã thua cuộc!')
        elif(lv <10):
            messagebox.showinfo('game over', 'Số tiền bạn nhận được là 1.000$')
        elif(lv <15):
            messagebox.showinfo('game over', 'Số tiền bạn nhận được là 32.000$')
        root.destroy()
    
##################################################################################################################
Image50_50 = PhotoImage(file='image/help50.png')
Help50_50 = Button(help, image=Image50_50, bg='black', command = click50_50)
Help50_50.grid(row=0, column=0)

ImagePhone = PhotoImage(file='image/Phone.png')
HelpPhone = Button(help, image=ImagePhone, bg='black', command = clickFriend)
HelpPhone.grid(row=0, column=1)

ImagePeople = PhotoImage(file='image/people.png')
HelpPeople = Button(help, image=ImagePeople, bg='black', command = clickPeople)
HelpPeople.grid(row=0, column=2)

ImageGiaiThuong = PhotoImage(file=gt[lv])
GiaiThuong = Button(giaithuong, image=ImageGiaiThuong, bg='black')
GiaiThuong.grid(row=0, column=0)

lblQuestion = Label(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER, wraplength = 500 , textvariable = q)
lblQuestion.grid(row=0, column=0, columnspan=4, pady=4)

lblAnswerA = Label(QA, font=('arial', 14, 'bold'), text='A: ', bg='black', fg='white', bd=5, justify=CENTER)
lblAnswerA.grid(row=1, column=0, pady=4, sticky=W)

btnAnswerA = Button(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER
                    , textvariable = a1, command = lambda: checkAnswer(a1.get()) )
btnAnswerA.grid(row=1, column=1 , pady=4)

lblAnswerB = Label(QA, font=('arial', 14, 'bold'), text='B: ', bg='black', fg='white', bd=5, justify=CENTER)
lblAnswerB.grid(row=1, column=2, pady=4, sticky=W)

btnAnswerB = Button(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER
                    , textvariable = a2, command = lambda: checkAnswer(a2.get()))
btnAnswerB.grid(row=1, column=3 , pady=4)

lblAnswerC = Label(QA, font=('arial', 14, 'bold'), text='C: ', bg='black', fg='white', bd=5, justify=CENTER)
lblAnswerC.grid(row=2, column=0, pady=4, sticky=W)

btnAnswerC = Button(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER
                    , textvariable = a3, command = lambda: checkAnswer(a3.get()))
btnAnswerC.grid(row=2, column=1 , pady=4)

lblAnswerD = Label(QA, font=('arial', 14, 'bold'), text='D: ', bg='black', fg='white', bd=5, justify=CENTER)
lblAnswerD.grid(row=2, column=2, pady=4, sticky=W)

btnAnswerD = Button(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER
                    , textvariable = a4, command = lambda: checkAnswer(a4.get()))
btnAnswerD.grid(row=2, column=3 , pady=4)

    
getquestion(0)
root.mainloop()
