
from tkinter import *
root = Tk()
root.geometry('500x500')
root.config(bg = 'SlateGray3')
root.resizable()
root.title('Mercy-AddressBook')
contactlist = [
    ['Parv Maheswari',  '0176738493', 'alh close', 'parv@gmail.com'],
    ['David Sharma',  '2684430000', 'alh close', 'parv@gmail.com'],
    ['Mandish Kabra',   '4338354432', 'alh close', 'parv@gmail.com'],
    ['Prisha Modi','6834552341', 'alh close', 'parv@gmail.com'],
    ['Rahul kaushik',   '1234852689', 'alh close', 'parv@gmail.com'],
    ['Johena Shaa' , '2119876543', 'alh close', 'parv@gmail.com'],
    ]
Name = StringVar()
Number = StringVar()
Address = StringVar()
Email= StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

def Selected():
    return int(select.curselection([0]))
def AddContact():
    contactlist.append([Name.get(), Number.get(), Address.get(), Email.get()])
    Select_set()
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get(), Address.get(), Email.get()]
    Select_set()
def DELETE():
    del contactlist[Selected()]
    Select_set()
def VIEW():
    NAME, PHONE, ADDRESS, EMAIL= contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Address. set(ADDRESS)
    Email.set(EMAIL)

def EXIT():
    root.destroy()
def RESET():
    Name.set('')
    Number.set('')
    Address.set('')
    Email.set('')
def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,Address,Email in contactlist :
        select.insert (END, name)
Select_set()

Label(root, text = 'NAME', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 100, y=20)
Label(root, text = 'PHONE NO.', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Number).place(x= 130, y=70)
Label(root, text = 'ADDRESS', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Address).place(x= 100, y=20)
Label(root, text = 'EMAIL', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Email).place(x= 130, y=70)
Button(root,text=" ADD", font='arial 12 bold',bg='SlateGray4', command = AddContact).place(x= 50, y=110)
Button(root,text="EDIT", font='arial 12 bold',bg='SlateGray4',command = EDIT).place(x= 50, y=260)
Button(root,text="DELETE", font='arial 12 bold',bg='SlateGray4',command = DELETE).place(x= 50, y=210)
Button(root,text="VIEW", font='arial 12 bold',bg='SlateGray4', command = VIEW).place(x= 50, y=160)
Button(root,text="EXIT", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 300, y=320)
Button(root,text="RESET", font='arial 12 bold',bg='SlateGray4', command = RESET).place(x= 50, y=310)
root.mainloop()
'''


name = ("input full name: ")
address = ("input address: ")
Phone_number = ("input phone: ")
email = ("input email: ")
data=[]
data=data.append([name, address, Phone_number, email])

def write_to_file(data):
    with open('contact_book.txt', mode='a') as database:  # a to append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = contact_book.write(f"\n{name},{address},{Phone_number}, {email}")  # \n for new line anytime we get an entry
        
    
write_to_file(data)
'''