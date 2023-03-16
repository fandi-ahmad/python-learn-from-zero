# import program_print

# print(program_print.data)
# print(program_print.angka)

# hasil = program_print.tambah(12, 3)
# print(hasil)

# import my_module as op

# hasil_tambah = op.tambah(10,20,3,5)
# hasil_kali = op.kali(3,2,5)
# pangkat = op.pangkat(3)

# print('=============')
# print(hasil_tambah)
# print(hasil_kali)
# print(pangkat(2))

# from my_module import tambah
# hasil_tambah = tambah(10,3)
# print('=============')
# print(hasil_tambah)

# from my_module import tambah as add
# hasil_tambah = add(10,3)
# print('=============')
# print(hasil_tambah)


# ===== PACKAGE =====
# import time
# t_start = time.time()
# import sains.matematika

# hasil_tambah = sains.matematika.tambah(12,5)
# print(hasil_tambah)

# t_end = time.time()
# print(t_end - t_start)


# ===== INIT =====
# __init__.py dijalankan saat import folder 'sains'
# import sains
# import datetime

# data_waktu = datetime.datetime

# hasil_tambah = sains.matematika.tambah(12,5)
# print(hasil_tambah)


# ===== GUI =====
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()

window.configure(bg='white')
window.geometry('600x400')
# window.resizable(False, False)
window.title('python app')


# frame
input_frame = ttk.Frame(window)

# penempatan grid, pack, place
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# komponen
# 1. label nama depan
nama_depan = ttk.Label(input_frame, text='Nama Depan')
nama_depan.pack(padx=10, fill='x', expand=True)

# 2. entry nama depan
NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, pady=10, fill='x', expand=True)

# 3. label nama belakang
nama_belakang = ttk.Label(input_frame, text='Nama Belakang')
nama_belakang.pack(padx=10, fill='x', expand=True)

# 4. entry nama belakang
NAMA_belakang = tk.StringVar()
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_belakang)
nama_belakang_entry.pack(padx=10, pady=10, fill='x', expand=True)

# 5. button
def btn_click():
    # print(NAMA_DEPAN.get())
    pesan = f'halo {NAMA_DEPAN.get()} {NAMA_belakang.get()}, apa kabar?'
    showinfo(title='pesan', message=pesan)

hay_btn = ttk.Button(input_frame, text='click me', command=btn_click)
hay_btn.pack(padx=10, fill='x', expand=True, pady=10)


window.mainloop()

# pypi.org      => package

# pip install ...       => install package
# pip uninstall ...     => uninstall package