import tkinter as tk
def check():
    temperature = int(entry1.get())
    if temperature<=0:
        label1.config(text="Ice")
        entry1.delete(0, tk.END)
    elif 1<=temperature<=99:
        label1.config(text="Water")
        entry1.delete(0, tk.END)
    else:
        label1.config(text="Steam")
        entry1.delete(0, tk.END)
root = tk.Tk()
root.config(background='#f0ddff')
root.title("سماور هوشمند هنرستان")
root.geometry('300x170')
root.resizable(width=False,height=False)
label1 = tk.Label(root, text= "دمای آب سماور چقدر است؟" , font=('B titr' , 15) , background='#f0ddff')
label1.pack(pady=10)
entry1 = tk.Entry(root , width=6 , font=(15) , background="#f0ddff")
entry1.pack(pady=10)
btn1 = tk.Button(root , text="دما را بررسی کن" ,font= ('B titr' , 8), background="#D1D1D1", command=lambda:check())
btn1.pack(pady=10)
root.mainloop()

