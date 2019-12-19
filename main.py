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

help = Frame(noidung, bg='black', bd=20, width=900, height=200)
help.grid(row=0, column=0)
logo = Frame(noidung, bg='black', bd=20, width=900, height=200)
logo.grid(row=1, column=0)
QA = Frame(noidung, bg='gray', bd=20, width=900, height=200)
QA.grid(row=2, column=0)


LogoImage = PhotoImage(file = 'logo.png')
LogoCenter = Button(logo, image = LogoImage, bg='black')
LogoCenter.grid()
 
Image50_50 = PhotoImage(file = 'help50.png')
Help50_50 = Button(help, image = Image50_50, bg='black')
Help50_50.grid(row=0, column=0)

ImagePhone = PhotoImage(file = 'Phone.png')
HelpPhone = Button(help, image = ImagePhone, bg='black')
HelpPhone.grid(row=0, column=1)

ImagePeople = PhotoImage(file = 'people.png')
HelpPeople = Button(help, image = ImagePeople, bg='black')
HelpPeople.grid(row=0, column=2)

ImageGiaiThuong = PhotoImage(file = 'Picture0.png')
GiaiThuong = Button(giaithuong, image = ImageGiaiThuong, bg='black')
GiaiThuong.grid(row=0, column=0)

root.mainloop()
