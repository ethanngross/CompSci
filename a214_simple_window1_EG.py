##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

def test_my_button():
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_expose = tk.Label(frame_auth, text=password)
    lbl_expose.pack()

# main window
root = tk.Tk()
root.title('Authorization')
root.wm_geometry("200x100")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
lbl_password = tk.Label(frame_login,text="Password:")
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(padx=5)
btn_login = tk.Button(frame_login, text="login", command=test_my_button)
btn_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")
netbeans = tk.Label(frame_auth, text="netbeans")


frame_login.tkraise()

root.mainloop()