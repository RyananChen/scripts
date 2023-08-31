from tkinter import *
import tkinter.messagebox as messagebox


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.result = StringVar()
        self.history = []

        self.display = Entry(self.master, textvariable=self.result, width=40, bd=5, insertwidth=5, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.result.set("0")

        self.create_button("1", self.press, 1, 0)
        self.create_button("2", self.press, 1, 1)
        self.create_button("3", self.press, 1, 2)
        self.create_button("+", self.press, 1, 3)

        self.create_button("4", self.press, 2, 0)
        self.create_button("5", self.press, 2, 1)
        self.create_button("6", self.press, 2, 2)
        self.create_button("-", self.press, 2, 3)

        self.create_button("7", self.press, 3, 0)
        self.create_button("8", self.press, 3, 1)
        self.create_button("9", self.press, 3, 2)
        self.create_button("*", self.press, 3, 3)

        self.create_button("0", self.press, 4, 0)
        self.create_button(".", self.press, 4, 1)
        self.create_button("C", self.clear, 4, 2)
        self.create_button("/", self.press, 4, 3)

        self.create_button("=", self.calculate, 5, 0, 1, 4)
        self.create_button("History", self.show_history, 6, 0, 1, 4)

    def create_button(self, text, command, row, col, rowspan=1, columnspan=1):
        button = Button(self.master, text=text, command=lambda: command(text), width=10, height=3)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)

    def press(self, button):
        if self.result.get() == "0" and button.isdigit():
            self.result.set("")

        if button == "." and "." in self.result.get().split()[-1]:
            return
        else:
            if not button.isdigit() and button != ".":
                if len(self.result.get()) == 0:
                    return
                elif not self.result.get()[-1].isdigit():
                    return
                else:
                    button = " " + button + " "

            self.result.set(self.result.get() + button)

    def clear(self):
        self.result.set("0")

    def calculate(self):
        try:
            result = eval(self.result.get())
            self.result.set(result)
            self.history.append(self.result.get() + " = " + str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero not allowed")
            self.result.set("0")
        except:
            messagebox.showerror("Error", "Invalid expression")
            self.result.set("0")

    def show_history(self):
        history_window = Toplevel(self.master)
        history_window.title("History")

        scrollbar = Scrollbar(history_window)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(history_window, yscrollcommand=scrollbar.set, width=50, height=10, font=("Arial", 14))
        listbox.pack()

        for item in self.history:
            listbox.insert(END, item)

        scrollbar.config(command=listbox.yview)

root = Tk()
calculator = Calculator(root)
root.mainloop()