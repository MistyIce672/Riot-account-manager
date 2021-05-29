import pyautogui
from time import sleep
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
import os.path
from functools import partial

def auto():
	global filename
	if os.path.exists("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/VALORANT.lnk") == True:
		filename = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/VALORANT.lnk"
		print("is real")
	elif os.path.exists("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/riot games/VALORANT.lnk") == True:
		filename = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/riot games/VALORANT.lnk"
		print("fantac")
	else:
			tk.messagebox.showerror(title="file not found", message="File not found pls select manuly")

def add():
	display = DNE.get()
	user = UNE.get()
	passw = PSE.get()
	print (display)
	print (user)
	print (passw)
	if display == "":
		print("denied")
	elif user == "":
		print("denied")
	elif passw == "":
		print("denied")
	else:	
		datas.insert(-1, display)
		users.insert(-1, user)
		pases.insert(-1, passw)
		fh = open('data.txt', 'w')
		strin = ",".join(datas)
		fh.write(strin)
		strin = ",".join(users)
		fh.write(strin)
		strin = ",".join(pases)
		fh.write(strin)
		strin = ",".join(path)
		fh.write(strin)

def clrall():
	global datas
	global users
	global pases
	datas = ['\n']
	users = ['\n']
	pases = ['\n']
	fh = open('data.txt', 'w')
	fh.write(",\n")
	fh.write(",\n")
	fh.write(",\n")
	strin = ",".join(path)
	fh.write(strin)

def get_data():
	with open('data.txt') as f:
		lines = f.readlines()
	datas = lines[0].split(',')
	return datas

def get_user():
	with open('data.txt') as f:
		lines = f.readlines()
	print (lines)
	users = lines[1].split(',')
	return users

def get_pass():
	with open('data.txt') as f:
		lines = f.readlines()
	pases = lines[2].split(',')
	return pases

def get_path():
	with open('data.txt') as f:
		lines = f.readlines()
	path = lines[3].split(',')
	return path

def fill(user, pas):
	c = 0
	userlocation = pyautogui.locateOnScreen('user.png', confidence=0.7)
	while userlocation == None:
		userlocation = pyautogui.locateOnScreen('user.png', confidence=0.7)
		if userlocation == None:
			userlocation = pyautogui.locateOnScreen('us.png', confidence=0.9)
		sleep(1)
		c = c+1
		if c > 30:
			window.destroy()
	c = 0
	userx, usery = pyautogui.center(userlocation)
	pyautogui.click(userx, usery)
	pyautogui.write(user)
	pasloaction = pyautogui.locateOnScreen('pass.png', confidence=0.7)
	while pasloaction == None:	
		pasloaction = pyautogui.locateOnScreen('pass.png', confidence=0.7)
		sleep(1)
		c = c+1
		if c > 30:
			window.destroy()
	c = 0
	passx, passy = pyautogui.center(pasloaction)
	pyautogui.click(passx, passy)
	sleep(1)
	pyautogui.write(pas)
	finlocation = pyautogui.locateOnScreen('fin.png', confidence=0.7)
	while finlocation == None:
		finlocation = pyautogui.locateOnScreen('fin.png', confidence=0.7)
		sleep(1)
		c = c+1
		if c > 30:
			window.destroy()
	c = 0
	finx, finy = pyautogui.center(finlocation)
	pyautogui.click(finx, finy)
	playlocation = pyautogui.locateOnScreen('play.png', confidence=0.7)
	while playlocation == None:
		playlocation = pyautogui.locateOnScreen('play.png', confidence=0.7)
		sleep(1)
		c = c+1
		if c > 30:
			window.destroy()
	c = 0
	playx, play = pyautogui.center(playlocation)
	pyautogui.click(playx, play)
	window.destroy()

def fileselect():
	print ("iniated")
	global filename
	filename = filedialog.askopenfilename(initialdir="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VALORANT", title='Select file',filetypes=(('executables', '*.lnk'), ('all files', '*.*')))
	print (filename)

datas = get_data()
users = get_user()
pases = get_pass()
path = get_path()
def function(count):
	os.startfile(path[0])
	fill(users[count], pases[count])


def setupb():
	filename = None
	mainframe.destroy()
	global setupframe
	setupframe = Frame(root,bg = '#1C252E',height= '350',width='350')
	setupframe.pack()
	label = Label(setupframe,text='Set VALORANT short cut for launch',bg = '#1C252E',fg='#ff4654')
	label.pack(padx=10,pady=10)
	btn = Button(setupframe, text='Select file', relief="flat", bg="#ff4654",width=15, command=fileselect)
	btn.pack(padx=10,pady=10)
	btn = Button(setupframe, text='Auto detect', relief="flat", bg="#ff4654",width=15, command=auto)
	btn.pack(padx=10,pady=10)
	btn = Button(setupframe, text='Next', relief="flat", bg="#ff4654",width=15, command=nex)
	btn.pack(padx=100,pady=10)
	btn = Button(setupframe, text='Skip', relief="flat", bg="#ff4654",width=15, command=skip)
	btn.pack(padx=100,pady=10)


def nex():
	if filename == None:
		tk.messagebox.showerror(title="error", message="use select or auto else skip")
	else:
		fh = open('data.txt', 'w')
		strin = ",".join(datas)
		fh.write(strin)
		strin = ",".join(users)
		fh.write(strin)
		strin = ",".join(pases)
		fh.write(strin)
		path[0] = filename
		print (path)
		strin = ",".join(path)
	fh.write(strin)
	global dis
	dis = True
	setupframe.destroy()
	global addframe 
	addframe = Frame(root,bg = '#1C252E',height= '350',width='350')
	addframe.grid()
	DN = Label(addframe, text="Display Name",bg = '#1C252E',fg='#ff4654')
	DN.grid(padx=10,pady=10)
	global DNE
	DNE = Entry(addframe, bd =5,bg = '#1C252E',fg='#ffffff')
	DNE.grid(row=0,column=2,padx=10,pady=10)
	UN = Label(addframe, text="User Name",bg = '#1C252E',fg='#ff4654')
	UN.grid(row=3,column=0,padx=10,pady=10)
	global UNE
	UNE = Entry(addframe, bd =5,bg = '#1C252E',fg='#ffffff')
	UNE.grid(row=3,column=2,padx=10,pady=10)
	PS = Label(addframe, text="Password",bg = '#1C252E',fg='#ff4654')
	PS.grid(row=4,column=0,padx=10,pady=10)
	global PSE
	PSE = Entry(addframe, bd =5,bg = '#1C252E',fg='#ffffff')
	PSE.grid(row=4,column=2,padx=10,pady=10)
	addac = Button(addframe,text='Add account', relief="flat", bg="#ff4654",width=15, command=add)
	addac.grid(row=5,padx=25,pady=5,columnspan=3)
	addac = Button(addframe,text='Clear all accounts', relief="flat", bg="#ff4654",width=15, command=clrall)
	addac.grid(row=6,padx=25,pady=5,columnspan=3)
	addac = Button(addframe,text='Next', relief="flat", bg="#ff4654",width=15, command=bm)
	addac.grid(row=7,padx=25,pady=5,columnspan=3)

def bm():
	if dis == True:
		addframe.destroy()
		dis == False
	global mainframe
	mainframe = Frame(root,bg = '#1C252E',height= '350',width='350')
	mainframe.pack()
	datas = get_data()
	print (datas)
	ct = 10
	c = 0
	for data in datas:
		if data == datas[-1]:
			print ("deniHelloMeed")
		else:
			print('lol')
			btn = Button(mainframe, text=data, relief="flat", bg="#ff4654",width=15, command=partial(function, c))
			btn.pack(padx=10,pady=10)
			c = c + 1
			ct = ct+ 10
	btn = Button(mainframe, text="setup", relief="flat", bg="#ff4654",width=15, command=setupb)
	btn.pack(padx=100,pady=10)

def skip():
	global dis
	dis = True
	setupframe.destroy()
	global addframe 
	addframe = Frame(root,bg = '#1C252E',height= '350',width='350')
	addframe.grid()
	DN = Label(addframe, text="Display Name",bg = '#1C252E',fg='#ff4654')
	DN.grid(padx=10,pady=10)
	global DNE
	DNE = Entry(addframe, bd =5,bg = '#1C252E',fg='#ffffff')
	DNE.grid(row=0,column=2,padx=10,pady=10)
	UN = Label(addframe, text="User Name",bg = '#1C252E',fg='#ff4654')
	UN.grid(row=3,column=0,padx=10,pady=10)
	global UNE
	UNE = Entry(addframe, bd =5,bg = '#1C252E',fg='#ffffff')
	UNE.grid(row=3,column=2,padx=10,pady=10)
	PS = Label(addframe, text="Password",bg = '#1C252E',fg='#ff4654')
	PS.grid(row=4,column=0,padx=10,pady=10)
	global PSE
	PSE = Entry(addframe, bd =5,bg = '#1C252E',fg='#ffffff')
	PSE.grid(row=4,column=2,padx=10,pady=10)
	addac = Button(addframe,text='Add account', relief="flat", bg="#ff4654",width=15, command=add)
	addac.grid(row=5,padx=25,pady=5,columnspan=3)
	addac = Button(addframe,text='Clear all accounts', relief="flat", bg="#ff4654",width=15, command=clrall)
	addac.grid(row=6,padx=25,pady=5,columnspan=3)
	addac = Button(addframe,text='Next', relief="flat", bg="#ff4654",width=15, command=bm)
	addac.grid(row=7,padx=25,pady=5,columnspan=3)

root = tk.Tk()
root.iconbitmap(default='icon.ico')
dis = False
bm()

root.mainloop()
