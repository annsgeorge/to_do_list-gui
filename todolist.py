import tkinter
from tkinter import *

root=Tk()
root.title("To_do_List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task :
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("taskfile.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task!='\n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file=open("tasklist.txt","w")
        file.close()

    
#icon
#Image_icon=PhotoImage(file="C:\Users\annmo\Downloads\todo\icon 1.png")
#root.iconphoto(False,Image_icon)

#top bar
#TopImage=PhotoImage(file ="C:\Users\annmo\Downloads\todo\topbar.png")
#Label(root,image=TopImage).pack()

heading=Label(root,text="Tasks",font="arial 30 bold",fg="teal")
heading.place(x=140,y=20)

#main
frame=Frame(root,width=400,height=60,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button =Button(frame,text="Enter",font="arial 20 bold",width=6,bg="teal",fg="white",command=addTask)
button.place(x=300,y=0)

#listbox
frame1=Frame(root,bd=3,width=700,height=300,bg="teal")
frame1.pack(pady=(250,0))

listbox =   Listbox(frame1,font=('arial', 12),width=40,height=16,bg="teal")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
delete =Button(root,text="Delete",font="arial 20 bold",width=10,bg="teal",fg="white",command=deleteTask)
delete.pack(side=BOTTOM,pady=30)



root.mainloop()
