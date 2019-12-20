from tkinter import *
import pygame
from PIL import*
from idlelib.idle_test.test_configdialog import root
from django.utils.termcolors import background

pygame.init()
root = Tk()
root.title("Who wants to be a Millionaire")
root.geometry('1352x652+0+0')
root.configure(background='black')

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

LogoImage = PhotoImage(file='logo.png')
LogoCenter = Button(logo, image=LogoImage, bg='black')
LogoCenter.grid()
 ##################################################################################################################
def click50_50():
    cavans = Canvas(help, bg='black',width = 160, height = 80)
    cavans.grid(row=0, column=0)
    cavans.delete('all')
    image = PhotoImage(file = 'help50X.png')
    cavans.create_image(90,40,image = image)
    cavans.image = image
def clickPeople():
    cavans = Canvas(help, bg='black',width = 160, height = 80)
    cavans.grid(row=0, column=2)
    cavans.delete('all')
    image = PhotoImage(file = 'peopleX.png')
    cavans.create_image(90,40,image = image)
    cavans.image = image
def clickFriend():
    cavans = Canvas(help, bg='black',width = 160, height = 80)
    cavans.grid(row=0, column=1)
    cavans.delete('all')
    image = PhotoImage(file = 'PhoneX.png')
    cavans.create_image(90,40,image = image)
    cavans.image = image
    
Image50_50 = PhotoImage(file='help50.png')
Help50_50 = Button(help, image=Image50_50, bg='black', command = click50_50)
Help50_50.grid(row=0, column=0)

ImagePhone = PhotoImage(file='Phone.png')
HelpPhone = Button(help, image=ImagePhone, bg='black', command = clickFriend)
HelpPhone.grid(row=0, column=1)

ImagePeople = PhotoImage(file='people.png')
HelpPeople = Button(help, image=ImagePeople, bg='black', command = clickPeople)
HelpPeople.grid(row=0, column=2)

ImageGiaiThuong = PhotoImage(file='Picture0.png')
GiaiThuong = Button(giaithuong, image=ImageGiaiThuong, bg='black')
GiaiThuong.grid(row=0, column=0)

txtQuestion = Entry(QA, font=('arial', 18, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER)
txtQuestion.grid(row=0, column=0, columnspan=4, pady=4)

lblAnswerA = Label(QA, font=('arial', 14, 'bold'), text='A: ', bg='black', fg='white', bd=5, justify=CENTER)
lblAnswerA.grid(row=1, column=0, pady=4, sticky=W)

btnAnswerA = Button(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER)
btnAnswerA.grid(row=1, column=1 , pady=4)

lblAnswerB = Label(QA, font=('arial', 14, 'bold'), text='B: ', bg='black', fg='white', bd=5, justify=CENTER)
lblAnswerB.grid(row=1, column=2, pady=4, sticky=W)

btnAnswerB = Button(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER)
btnAnswerB.grid(row=1, column=3 , pady=4)

lblAnswerC = Label(QA, font=('arial', 14, 'bold'), text='C: ', bg='black', fg='white', bd=5, justify=CENTER)
lblAnswerC.grid(row=2, column=0, pady=4, sticky=W)

btnAnswerC = Button(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER)
btnAnswerC.grid(row=2, column=1 , pady=4)

lblAnswerD = Label(QA, font=('arial', 14, 'bold'), text='D: ', bg='black', fg='white', bd=5, justify=CENTER)
lblAnswerD.grid(row=2, column=2, pady=4, sticky=W)

btnAnswerD = Button(QA, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER)
btnAnswerD.grid(row=2, column=3 , pady=4)

root.mainloop()
