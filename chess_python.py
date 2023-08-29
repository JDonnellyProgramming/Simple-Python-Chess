import tkinter as tk
import math

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800, bg='white')
canvas.pack()

canvas.create_rectangle(50, 50, 750, 750)
sq1a = canvas.create_rectangle(50, 50, 137.5, 137.5)
sq1b = canvas.create_rectangle(137.5, 50, 225, 137.5, fill='black')
sq1c = canvas.create_rectangle(225, 50, 312.5, 137.5)
sq1d = canvas.create_rectangle(312.5, 50, 400, 137.5, fill='black')
sq1e = canvas.create_rectangle(400, 50, 487.5, 137.5)
sq1f = canvas.create_rectangle(487.5, 50, 575, 137.5, fill='black')
sq1g = canvas.create_rectangle(575, 50, 662.5, 137.5)
sq1h = canvas.create_rectangle(662.5, 50, 750, 137.5, fill='black')

sq2a = canvas.create_rectangle(50, 137.5, 137.5, 225, fill='black')
sq2b = canvas.create_rectangle(137.5, 137.5, 225, 225)
sq2c = canvas.create_rectangle(225, 137.5, 312.5, 225, fill='black')
sq2d = canvas.create_rectangle(312.5, 137.5, 400, 225)
sq2e = canvas.create_rectangle(400, 137.5, 487.5, 225, fill='black')
sq2f = canvas.create_rectangle(487.5, 137.5, 575, 225)
sq2g = canvas.create_rectangle(575, 137.5, 662.5, 225, fill='black')
sq2h = canvas.create_rectangle(662.5, 137.5, 750, 225)

sq3a = canvas.create_rectangle(50, 225, 137.5, 312.5)
sq3b = canvas.create_rectangle(137.5, 225, 225, 312.5, fill='black')
sq3c = canvas.create_rectangle(225, 225, 312.5, 312.5)
sq3d = canvas.create_rectangle(312.5, 225, 400, 312.5, fill='black')
sq3e = canvas.create_rectangle(400, 225, 487.5, 312.5)
sq3f = canvas.create_rectangle(487.5, 225, 575, 312.5, fill='black')
sq3g = canvas.create_rectangle(575, 225, 662.5, 312.5)
sq3h = canvas.create_rectangle(662.5, 225, 750, 312.5, fill='black')

sq4a = canvas.create_rectangle(50, 312.5, 137.5, 400, fill='black')
sq4b = canvas.create_rectangle(137.5, 312.5, 225, 400)
sq4c = canvas.create_rectangle(225, 312.5, 312.5, 400, fill='black')
sq4d = canvas.create_rectangle(312.5, 312.5, 400, 400)
sq4e = canvas.create_rectangle(400, 312.5, 487.5, 400, fill='black')
sq4f = canvas.create_rectangle(487.5, 312.5, 575, 400)
sq4g = canvas.create_rectangle(575, 312.5, 662.5, 400, fill='black')
sq4h = canvas.create_rectangle(662.5, 312.5, 750, 400)

sq5a = canvas.create_rectangle(50, 400, 137.5, 487.5)
sq5b = canvas.create_rectangle(137.5, 400, 225, 487.5, fill='black')
sq5c = canvas.create_rectangle(225, 400, 312.5, 487.5)
sq5d = canvas.create_rectangle(312.5, 400, 400, 487.5, fill='black')
sq5e = canvas.create_rectangle(400, 400, 487.5, 487.5)
sq5f = canvas.create_rectangle(487.5, 400, 575, 487.5, fill='black')
sq5g = canvas.create_rectangle(575, 400, 662.5, 487.5)
sq5h = canvas.create_rectangle(662.5, 400, 750, 487.5, fill='black')

sq6a = canvas.create_rectangle(50, 487.5, 137.5, 575, fill='black')
sq6b = canvas.create_rectangle(137.5, 487.5, 225, 575)
sq6c = canvas.create_rectangle(225, 487.5, 312.5, 575, fill='black')
sq6d = canvas.create_rectangle(312.5, 487.5, 400, 575)
sq6e = canvas.create_rectangle(400, 487.5, 487.5, 575, fill='black')
sq6f = canvas.create_rectangle(487.5, 487.5, 575, 575)
sq6g = canvas.create_rectangle(575, 487.5, 662.5, 575, fill='black')
sq6h = canvas.create_rectangle(662.5, 487.5, 750, 575)

sq7a = canvas.create_rectangle(50, 575, 137.5, 662.5)
sq7b = canvas.create_rectangle(137.5, 575, 225, 662.5, fill='black')
sq7c = canvas.create_rectangle(225, 575, 312.5, 662.5)
sq7d = canvas.create_rectangle(312.5, 575, 400, 662.5, fill='black')
sq7e = canvas.create_rectangle(400, 575, 487.5, 662.5)
sq7f = canvas.create_rectangle(487.5, 575, 575, 662.5, fill='black')
sq7g = canvas.create_rectangle(575, 575, 662.5, 662.5)
sq7h = canvas.create_rectangle(662.5, 575, 750, 662.5, fill='black')

sq8a = canvas.create_rectangle(50, 662.5, 137.5, 750, fill='black')
sq8b = canvas.create_rectangle(137.5, 662.5, 225, 750)
sq8c = canvas.create_rectangle(225, 662.5, 312.5, 750, fill='black')
sq8d = canvas.create_rectangle(312.5, 662.5, 400, 750)
sq8e = canvas.create_rectangle(400, 662.5, 487.5, 750, fill='black')
sq8f = canvas.create_rectangle(487.5, 662.5, 575, 750)
sq8g = canvas.create_rectangle(575, 662.5, 662.5, 750, fill='black')
sq8h = canvas.create_rectangle(662.5, 662.5, 750, 750)

s1a = 'c1w'
s2a = 'h1w'
s3a = 'b1w'
s4a = 'kw'
s5a = 'qw'
s6a = 'b2w'
s7a = 'h2w'
s8a = 'c2w'
s1b = 'p1w'
s2b = 'p2w'
s3b = 'p3w'
s4b = 'p4w'
s5b = 'p5w'
s6b = 'p6w'
s7b = 'p7w'
s8b = 'p8w'
s1c = ''
s2c = ''
s3c = ''
s4c = ''
s5c = ''
s6c = ''
s7c = ''
s8c = ''
s1d = ''
s2d = ''
s3d = ''
s4d = ''
s5d = ''
s6d = ''
s7d = ''
s8d = ''
s1e = ''
s2e = ''
s3e = ''
s4e = ''
s5e = ''
s6e = ''
s7e = ''
s8e = ''
s1f = ''
s2f = ''
s3f = ''
s4f = ''
s5f = ''
s6f = ''
s7f = ''
s8f = ''
s1g = 'p1b'
s2g = 'p2b'
s3g = 'p3b'
s4g = 'p4b'
s5g = 'p5b'
s6g = 'p6b'
s7g = 'p7b'
s8g = 'p8b'
s1h = 'c1b'
s2h = 'h1b'
s3h = 'b1b'
s4h = 'kb'
s5h = 'gb'
s6h = 'b2b'
s7h = 'h2b'
s8h = 'c2b'


def on_enter_b(event):
    event.widget.configure(bg='lightblue')


def on_leave_b(event):
    event.widget.configure(bg="black")


def on_enter_w(event):
    event.widget.configure(bg='lightblue')


def on_leave_w(event):
    event.widget.configure(bg="white")


def on_click_p_b(event):
    pass


label_c1_w = tk.Label(root, text='C', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_c1_w.place(x=76, y=63)
label_c1_w.bind("<Enter>", on_enter_w)
label_c1_w.bind("<Leave>", on_leave_w)
label_h1_w = tk.Label(root, text='H', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_h1_w.place(x=163.5, y=63)
label_h1_w.bind("<Enter>", on_enter_w)
label_h1_w.bind("<Leave>", on_leave_w)
label_b1_w = tk.Label(root, text='B', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_b1_w.place(x=251, y=63)
label_b1_w.bind("<Enter>", on_enter_w)
label_b1_w.bind("<Leave>", on_leave_w)
label_k_w = tk.Label(root, text='K', bg='white', highlightthickness=1,
                     highlightbackground='black', width=4,
                     height=4, cursor='hand2')
label_k_w.place(x=338.1, y=63)
label_k_w.bind("<Enter>", on_enter_w)
label_k_w.bind("<Leave>", on_leave_w)
label_q_w = tk.Label(root, text='Q', bg='white', highlightthickness=1,
                     highlightbackground='black', width=4,
                     height=4, cursor='hand2')
label_q_w.place(x=426, y=63)
label_q_w.bind("<Enter>", on_enter_w)
label_q_w.bind("<Leave>", on_leave_w)
label_b2_w = tk.Label(root, text='B', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_b2_w.place(x=513.5, y=63)
label_b2_w.bind("<Enter>", on_enter_w)
label_b2_w.bind("<Leave>", on_leave_w)
label_h2_w = tk.Label(root, text='H', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_h2_w.place(x=601, y=63)
label_h2_w.bind("<Enter>", on_enter_w)
label_h2_w.bind("<Leave>", on_leave_w)
label_c2_w = tk.Label(root, text='C', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_c2_w.place(x=688.5, y=63)
label_c2_w.bind("<Enter>", on_enter_w)
label_c2_w.bind("<Leave>", on_leave_w)
label_p1_w = tk.Label(root, text='P', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_p1_w.place(x=76, y=150.1)
label_p1_w.bind("<Enter>", on_enter_w)
label_p1_w.bind("<Leave>", on_leave_w)
label_p2_w = tk.Label(root, text='P', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_p2_w.place(x=163.5, y=150.1)
label_p2_w.bind("<Enter>", on_enter_w)
label_p2_w.bind("<Leave>", on_leave_w)
label_p3_w = tk.Label(root, text='P', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4)
label_p3_w.place(x=251, y=150.1)
label_p3_w.bind("<Enter>", on_enter_w)
label_p3_w.bind("<Leave>", on_leave_w)
label_p4_w = tk.Label(root, text='P', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_p4_w.place(x=338.1, y=150.1)
label_p4_w.bind("<Enter>", on_enter_w)
label_p4_w.bind("<Leave>", on_leave_w)
label_p5_w = tk.Label(root, text='P', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_p5_w.place(x=426, y=150.1)
label_p5_w.bind("<Enter>", on_enter_w)
label_p5_w.bind("<Leave>", on_leave_w)
label_p6_w = tk.Label(root, text='P', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_p6_w.place(x=513.5, y=150.1)
label_p6_w.bind("<Enter>", on_enter_w)
label_p6_w.bind("<Leave>", on_leave_w)
label_p7_w = tk.Label(root, text='P', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_p7_w.place(x=601, y=150.1)
label_p7_w.bind("<Enter>", on_enter_w)
label_p7_w.bind("<Leave>", on_leave_w)
label_p8_w = tk.Label(root, text='P', bg='white', highlightthickness=1,
                      highlightbackground='black', width=4,
                      height=4, cursor='hand2')
label_p8_w.place(x=688.5, y=150.1)
label_p8_w.bind("<Enter>", on_enter_w)
label_p8_w.bind("<Leave>", on_leave_w)

label_c1_b = tk.Label(root, text='C', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_c1_b.place(x=76, y=675.5)
label_c1_b.bind("<Enter>", on_enter_b)
label_c1_b.bind("<Leave>", on_leave_b)
label_h1_b = tk.Label(root, text='H', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_h1_b.place(x=163.5, y=675.5)
label_h1_b.bind("<Enter>", on_enter_b)
label_h1_b.bind("<Leave>", on_leave_b)
label_b1_b = tk.Label(root, text='B', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_b1_b.place(x=251, y=675.5)
label_b1_b.bind("<Enter>", on_enter_b)
label_b1_b.bind("<Leave>", on_leave_b)
label_k_b = tk.Label(root, text='K', bg='black', highlightthickness=1,
                     highlightbackground='white', width=4,
                     height=4, fg='white', cursor='hand2')
label_k_b.place(x=338.1, y=675.5)
label_k_b.bind("<Enter>", on_enter_b)
label_k_b.bind("<Leave>", on_leave_b)
label_q_b = tk.Label(root, text='Q', bg='black', highlightthickness=1,
                     highlightbackground='white', width=4,
                     height=4, fg='white', cursor='hand2')
label_q_b.place(x=426, y=675.5)
label_q_b.bind("<Enter>", on_enter_b)
label_q_b.bind("<Leave>", on_leave_b)
label_b2_b = tk.Label(root, text='B', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_b2_b.place(x=513.5, y=675.5)
label_b2_b.bind("<Enter>", on_enter_b)
label_b2_b.bind("<Leave>", on_leave_b)
label_h2_b = tk.Label(root, text='H', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_h2_b.place(x=601, y=675.5)
label_h2_b.bind("<Enter>", on_enter_b)
label_h2_b.bind("<Leave>", on_leave_b)
label_c2_b = tk.Label(root, text='C', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_c2_b.place(x=688.5, y=675.5)
label_c2_b.bind("<Enter>", on_enter_b)
label_c2_b.bind("<Leave>", on_leave_b)
label_p1_b = tk.Label(root, text='P', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_p1_b.place(x=76, y=588)
label_p1_b.bind("<Enter>", on_enter_b)
label_p1_b.bind("<Leave>", on_leave_b)
label_p2_b = tk.Label(root, text='P', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_p2_b.place(x=163.5, y=588)
label_p2_b.bind("<Enter>", on_enter_b)
label_p2_b.bind("<Leave>", on_leave_b)
label_p3_b = tk.Label(root, text='P', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_p3_b.place(x=251, y=588)
label_p3_b.bind("<Enter>", on_enter_b)
label_p3_b.bind("<Leave>", on_leave_b)
label_p4_b = tk.Label(root, text='P', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_p4_b.place(x=338.5, y=588)
label_p4_b.bind("<Enter>", on_enter_b)
label_p4_b.bind("<Leave>", on_leave_b)
label_p5_b = tk.Label(root, text='P', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_p5_b.place(x=426, y=588)
label_p5_b.bind("<Enter>", on_enter_b)
label_p5_b.bind("<Leave>", on_leave_b)
label_p6_b = tk.Label(root, text='P', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_p6_b.place(x=513.5, y=588)
label_p6_b.bind("<Enter>", on_enter_b)
label_p6_b.bind("<Leave>", on_leave_b)
label_p7_b = tk.Label(root, text='P', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_p7_b.place(x=601, y=588)
label_p7_b.bind("<Enter>", on_enter_b)
label_p7_b.bind("<Leave>", on_leave_b)
label_p8_b = tk.Label(root, text='P', bg='black', highlightthickness=1,
                      highlightbackground='white', width=4,
                      height=4, fg='white', cursor='hand2')
label_p8_b.place(x=688.5, y=588)
label_p8_b.bind("<Enter>", on_enter_b)
label_p8_b.bind("<Leave>", on_leave_b)

root.mainloop()

