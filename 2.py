import tkinter as tk
def check():
    score = int(entry1.get())
    if score<10:
        label1.config(text="مردود" , fg="red")
        entry1.delete(0, tk.END)
    elif 10<=score<=15:
        label1.config(text="قابل قبول" , fg="#FFC02C")
        entry1.delete(0, tk.END)
    elif 15<score<=20:
        label1.config(text="عالی" , fg="green")
        entry1.delete(0, tk.END)
    else:
        label1.config(text="نمره را به درستی وارد کنید" , fg="red")
        entry1.delete(0, tk.END)
root = tk.Tk()
root.config(background='#f0ddff')
root.title("سیستم نمره دهی هنرستان")
root.geometry('300x170')
root.resizable(width=False,height=False)
label1 = tk.Label(root, text= "نمره دانش آموز را وارد کنید" , font=('B titr' , 15) , background='#f0ddff')
label1.pack(pady=10)
entry1 = tk.Entry(root , width=6 , font=(15) , background="#f0ddff")
entry1.pack(pady=10)
btn1 = tk.Button(root , text="نمایش وضعیت دانش آموز" ,font= ('B titr' , 8), background="#D1D1D1", command=lambda:check())
btn1.pack(pady=10)
root.mainloop()

