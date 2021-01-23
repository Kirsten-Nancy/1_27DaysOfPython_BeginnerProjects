from tkinter import *

window = Tk()
window.title('Hello Tkinter')
window.minsize(width=400, height=200)
window.configure(padx=20, pady=20)

def convert_miles_to_km():
    ans = 1.60934 * int(user_input.get())
    answer_label.configure(text=f'{ans}')


user_input = Entry()
user_input.grid(column=1, row=0)

miles_label = Label(text='Miles', padx=10)
miles_label.grid(column=2, row=0)

equal_label = Label(text='is equal to', padx=10, pady=10)
equal_label.grid(column=0, row=1)

answer_label = Label(text='0')
answer_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

calculate_btn = Button(text='Calculate',  command=convert_miles_to_km, background='plum4')
calculate_btn.grid(column=1, row=2)

window.mainloop()