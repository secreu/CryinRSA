# -*- coding: UTF-8 -*-

from tkinter import Message
from ttkbootstrap.constants import *
from PIL import ImageTk, Image
from tkinter import filedialog
import ttkbootstrap as ttk

from cryinrsa import *

ki = 0
# 存储文件名
pub_key_filename = ""
priv_key_filename = ""
op_filename = ""
temp_window = None


def get_op_filename():
    global op_filename
    op_filename = filedialog.askopenfilename(title='选择文件',
                                         filetypes=[("所有文件", "*.*")],
                                         initialdir='./',
                                         parent=temp_window)


def decrypt_op_file():
    get_op_filename()
    # 解密文件
    Message(temp_window, text="已开始解密")
    decrypt(op_filename, "dec.txt", ki)
    Message(temp_window, text="已完成解密，在当前目录下生成文件dec.txt").place(x=400, y=100, width=200, height=100)



def encrypt_op_file():
    get_op_filename()
    # 加密文件
    encrypt(op_filename, "enc.txt", ki)
    Message(temp_window, text="已完成加密，在当前目录下生成文件enc.txt").place(x=400, y=100, width=200, height=100)


def get_pub_key_filename():
    global pub_key_filename
    pub_key_filename = filedialog.askopenfilename(title='选择文件',
                                         filetypes=[("所有文件", "*.*")],
                                         initialdir='./',
                                         parent=temp_window)
    print("pub")

def get_priv_key_filename():
    global priv_key_filename
    priv_key_filename = filedialog.askopenfilename(title='选择文件',
                                         filetypes=[("所有文件", "*.*")],
                                         initialdir='./',
                                         parent=temp_window)
    print("priv")


def home():
    global temp_window
    win_home = ttk.Toplevel(root)
    win_home.geometry('1000x600+460+240')
    win_home.title('主页')
    temp_window = win_home

    # 设置背景图片
    canvas_home = ttk.Canvas(win_home, width=1000, height=600)

    canvas_home.create_image(500, 300, image=im_home)
    canvas_home.grid()

    # 选择公钥加密
    global obj_file
    btn_pub = ttk.Button(win_home, text="选择公钥文件", bootstyle=(PRIMARY, "outline-toolbutton"), command=get_pub_key_filename)
    btn_pub.place(x=210, y=250, width=150, height=40)

    # 选择加密文件
    btn_encrypt = ttk.Button(win_home, text="选择加密文件", bootstyle=(PRIMARY, "outline-toolbutton"), command=encrypt_op_file)
    btn_encrypt.place(x=210, y=315, width=150, height=40)
    # btn_encrypt.bind("<Button-2>", open_filename("op_file"))

    # 选择私钥解密
    btn_priv = ttk.Button(win_home, text="选择私钥文件", bootstyle=(PRIMARY, "outline-toolbutton"), command=get_priv_key_filename)
    btn_priv.place(x=595, y=250, width=150, height=40)
    # btn_priv.bind("<Button-2>", open_filename("priv_key"))

    # 选择解密文件
    btn_decrypt = ttk.Button(win_home, text="选择解密文件", bootstyle=(PRIMARY, "outline-toolbutton"), command=decrypt_op_file)
    btn_decrypt.place(x=595, y=315, width=150, height=40)
    # btn_decrypt.bind("<Button-2>", open_filename("op_file"))




def get_img(filename, width, height):
    im = Image.open(filename).resize((width, height))
    im = ImageTk.PhotoImage(im)
    return im


def login():
    # 设置背景图片
    canvas_root = ttk.Canvas(root, width=1000, height=600)
    canvas_root.create_image(500, 300, image=im_root)
    canvas_root.grid()


    # 输入框
    entry_account = ttk.Entry(root, show=None)
    entry_account.insert('0', '请输入账号')
    entry_account.place(x=180, y=260, width=200, height=30)
    entry_pwd = ttk.Entry(root, show='*')
    entry_pwd.insert('0', '请输入密码')
    entry_pwd.place(x=180, y=310, width=200, height=30)

    # 登录按钮
    btn = ttk.Button(root, text="登录", bootstyle=(PRIMARY, "outline-toolbutton"))
    btn.place(x=180, y=380, width=150, height=40)
    btn.bind("<Button-1>", lambda e: home())

    root.mainloop()


if __name__ == '__main__':
    ki = gen_key(32)

    root = ttk.Window(title="RSA加解密系统")
    root.geometry('1000x600+460+240')
    root.resizable(False, False)

    im_root = get_img('./img/login.jpg', 1000, 600)
    im_home = get_img('./img/home.jpg', 1000, 600)
    login()

