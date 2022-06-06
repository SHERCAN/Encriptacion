from base64 import urlsafe_b64encode
import subprocess
import tkinter as tk
from tkinter import messagebox
import sys
try:
    import cryptography
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'cryptography'])
finally:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.hashes import SHA256
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC    
text_to=['Text to encrypt','Text to decrypt','Text encript','Text decrypt']

def ejecutar():
    
    key1=f_key_in.get().encode()
    Key2 =s_key_in.get().encode()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=Key2,
        iterations=390000,
    )
    key = urlsafe_b64encode(kdf.derive(key1))
    fernet = Fernet(key)
    texto=text_box_in.get("1.0", tk.END)
    
    if ch_enc_var.get():
        #Encrypt
        token = fernet.encrypt(texto.encode())
        text_box_out.insert('1.0',token.decode())
        messagebox.showinfo(master=root,title='message', message='Encrypt')
    if ch_dec_var.get():
        #Decrypt
        textDecrypt=fernet.decrypt(texto.encode())
        text_box_out.insert('1.0',textDecrypt.decode())
        messagebox.showinfo(master=root,title='message', message='Decrypt')
    
def state1():
    ch_dec_var.set(value=False)
    text_f.set(text_to[0])
    text_s.set(text_to[2])
    if not ch_dec_var.get() and not ch_enc_var.get():
        ch_enc_var.set(value=False)
        ch_dec_var.set(value=False)
        text_f.set('')
        text_s.set('')
def state2():
    ch_enc_var.set(value=False)
    text_f.set(text_to[1])
    text_s.set(text_to[3])
    if not ch_dec_var.get() and not ch_enc_var.get():
        ch_enc_var.set(value=False)
        ch_dec_var.set(value=False)
        text_f.set('')
        text_s.set('')
if __name__ == '__main__':
    root=tk.Tk()
    root.geometry('810x275')
    root.resizable(height = 0, width =0)
    text_f=tk.StringVar()
    text_s=tk.StringVar()
    ch_enc_var=tk.BooleanVar()
    ch_dec_var=tk.BooleanVar()
    frame = tk.Frame(master=root,relief=tk.RAISED,borderwidth=1)
    frame.grid(row=0, column=0)
    f_key= tk.Label(master=frame, text='First Key:')
    f_key.grid(row=0, column=0,sticky="w")
    s_key = tk.Label(master=frame, text='Second Key:')
    s_key.grid(row=1, column=0,sticky="w")
    f_key_in = tk.Entry(master=frame, text='Your Fisrt Key',width=106)
    f_key_in.grid(row=0,column=1,columnspan=2,sticky="w")
    s_key_in=tk.Entry(master=frame,text='Your Second Key',width=106)
    s_key_in.grid(row=1,column=1,columnspan=2,sticky="w")
    ch_enc=tk.Checkbutton(master=frame,text='Encrypt',command=state1,variable=ch_enc_var)
    ch_enc.grid(row=2,column=0,sticky='w')
    ch_dec=tk.Checkbutton(master=frame,text='Decrypt',command=state2,variable=ch_dec_var)
    ch_dec.grid(row=2,column=1,sticky='e')
    text_f_l = tk.Label(master=frame, textvariable=text_f,width=15)
    text_f_l.grid(row=3, column=0,sticky="w")
    text_s_l = tk.Label(master=frame, textvariable=text_s,width=15)
    text_s_l.grid(row=4, column=0,sticky="w")
    text_box_in=tk.Text(master=frame,height=6)
    text_box_in.grid(row=3,column=1,columnspan=1)
    text_box_out=tk.Text(master=frame,height=6)
    text_box_out.grid(row=4,column=1,columnspan=1)
    boton=tk.Button(master=frame,text='Ejecutar',height=13,command=ejecutar)
    boton.grid(row=3,column=2,rowspan=2)
    root.mainloop()
    