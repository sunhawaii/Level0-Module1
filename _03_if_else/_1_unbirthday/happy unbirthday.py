
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birthday=simpledialog.askstring(title= 'none',prompt = "What is your birthday?(mm/dd)")
    if birthday == "5/20"  :
        messagebox.showinfo(title = 'none', message = "corre")
    else :
        messagebox.showinfo(title = 'none' ,message = "lies")

