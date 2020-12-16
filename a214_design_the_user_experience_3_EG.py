import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")

frame1 = tk.Frame(root, height=100, width=130, background="blue" )
frame2 = tk.Frame(root, height=100, width=70, background="lime")
frame3 = tk.Frame(root, height=100, width=130, background="red")
frame4 = tk.Frame(root, height=100, width=70, background="yellow")

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0)
frame4.grid(row=1, column=1)

'''
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
'''
root.mainloop()