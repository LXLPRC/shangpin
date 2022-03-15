#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymssql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import tkinter.messagebox as messagebox  # 弹窗
# 打包的时候会用到（十进制的一个库）
import decimal

decimal.__version__


class StartPage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 销毁上一个窗口
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('药品销售管理系统')
        self.window.geometry('1300x800+170+50')  # 这里的乘是小x，第一个参数表示窗口的长，第二个表示宽，第三个表示的距离屏幕左边界的距离，第三个为距离上边界的距离
        image_width = 600
        image_height = 500
        canvas = tk.Canvas(self.window, height=1200, width=1200)  # 设置的画布大小
        image_file = tk.PhotoImage(file='../药品销售管理系统/tu2.gif')
        image = canvas.create_image(600, 300, image=image_file)#图片大小
        canvas.place(x=40, y=10)#画布摆放位置

        label = Label(self.window, text="",bg='white')
        label.pack(pady=210)  # pady=210 这个label距离窗口上边界的距离，这里设置为210刚好居中，为了下面界面摆放在图片下面

        # command=lambda:  可以带参数，注意带参数的类不要写括号，否者，这里调用会直接执行(class test:)
        Button(self.window, text=" 管理员登陆", font=tkFont.Font(size=25), command=lambda: AdminPage(self.window), width=20,
               height=1,
               bd='0',
               fg='white', bg='deepskyblue', activebackground='cyan',
               activeforeground='white').pack()  # pack() 方法会使得组件在窗口中自动布局
        Button(self.window, text="用户登陆", font=tkFont.Font(size=25), command=lambda: UserPage(self.window), width=20,
               height=1,
               bd='0',
               fg='white', bg='deepskyblue', activebackground='cyan',
               activeforeground='white').pack()
        Button(self.window, text="卖家登陆", font=tkFont.Font(size=25), command=lambda: SellerPage(self.window), width=20,
               height=1,
               bd='0',
               fg='white', bg='deepskyblue', activebackground='cyan',
               activeforeground='white').pack()
        Button(self.window, text="退出系统", height=1, font=tkFont.Font(size=25), width=20, command=self.window.destroy,
               fg='white',bd='0', bg='deepskyblue', activebackground='cyan', activeforeground='white').pack()
        self.window.mainloop()  # 主消息循环

# 管理员登陆页面
class AdminPage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 销毁上一个界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员登陆页面')
        self.window.geometry('400x300+550+200')# 这里的乘是小x，第一个参数表示窗口的长，第二个表示宽，第三个表示的距离屏幕左边界的距离，第三个为距离上                                         边界的距离

        # 创建画布，这里可以存放照片等组件
        canvas = tk.Canvas(self.window, height=500, width=500)
        image_file = tk.PhotoImage(file='../药品销售管理系统/welcome.gif')
        image = canvas.create_image(50, 0, anchor='nw', image=image_file)  # 前两个参数为画布得坐标，anchor=nw则是把图片的左上角作为锚定点
        canvas.pack(side='top')  # 使用pack将画布进行简单得布局，放到了上半部分

        # 创建提示信息
        tk.Label(self.window, text='登录账号: ').place(x=80, y=150)#摆放位置
        tk.Label(self.window, text='登陆密码: ').place(x=80, y=190)

        self.admin_username = tk.Entry(self.window)#输入的账号
        self.admin_username.place(x=160, y=150)

        self.admin_pass = tk.Entry(self.window,show='*')#输入的密码用*显示
        self.admin_pass.place(x=160, y=190)
        # 登陆和返回首页得按钮
        btn_login = tk.Button(self.window, text='登陆', width=10, command=self.login)
        btn_login.place(x=120, y=230)
        btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
        btn_back.place(x=270, y=230)
        self.window.mainloop()

    # 登陆的函数
    def login(self):
        # 数据库操作 查询管理员表
        db = pymssql.connect(host='localhost',server=r'SQLEXPRESS',port='1433',user='diao',password='123456',database="BUY_system",charset='CP936')
        print("连接成功")
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM users where u_id = '%s'" % (self.admin_username.get())  # 这里得user_name即为u_id，这里是输入的用户账号
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表，这里是返回的二元元组，如(('id','title'),('id','title'))
            results = cursor.fetchall()
            print(results)
            for row in results:
                u_id = row[0]
                u_password = row[1]
                # 打印结果
                print("管理员账号为：%s, \n\n管理员密码为：%s" % (u_id, u_password))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆管理员管理界面.......")
        print(self.admin_username.get())#检验
        print(self.admin_pass.get())
        print(u_id)
        print(u_password)
        print(type(u_password))
        print(type(self.admin_pass.get()))
        print(self.admin_pass.get() == u_password)
        #以上均为检验检验数据类型

        # 判断输入的账号密码与数据库中的信息是否一致a
        if self.admin_pass.get().strip() == u_password.strip():#。strip（）函数清除字符串中的'\n'
            print('进入判断')
            All_admin(self.window)  # 进入管理员子菜单操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')


    # 使得系统点击关闭的x号上返回指定页面，而不是关闭
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 管理员子菜单操作界面
class All_admin:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自定销毁上一个界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('信息管理界面')
        self.window.geometry('1000x700+300+50')
        label = Label(self.window, text="请选择需要进行的操作", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="药品信息管理", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: AdminManage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="药品订单管理", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: ODManage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="用户信息管理", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: USManage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()


        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 药品信息操作界面168--
class AdminManage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=200)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("药品id", "药品名称", "药品价格", "药品数量")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("药品id", width=150, anchor='center')
        self.tree.column("药品名称", width=150, anchor='center')
        self.tree.column("药品价格", width=100, anchor='center')
        self.tree.column("药品数量", width=100, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []
        self.gender = []
        self.age = []

        # 打开数据库连接
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM goods"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
        except:
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="药品信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸

        # 定义下方区域
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = StringVar()  # 声明年龄
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="药品id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="药品名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 商品价格
        self.right_top_gender_label = Label(self.frame_left_top, text="药品价格：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 销售数量
        self.right_top_gender_label = Label(self.frame_left_top, text="药品数量：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新增药品信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中药品信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中药品信息', width=20, command=self.del_row)

        # 定义下方区域，查询功能块
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        # 右上角按钮的位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环

    # 将查到的信息放到中间的表格中
    def put_data(self):
        self.delButton()  # 先将表格内的内容全部清空

        # print(self.chaxun.get())	# 输入框内的内容
        # 打开数据库连接，准备查找指定的信息
        db = pymssql.connect(host='localhost',server=r'SQLEXPRESS',port='1433',user='diao',password='123456',database="BUY_system",charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT *FROM goods where g_name= '%s'" % (self.chaxun.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print('&&&&&&')
            print(results)

            # 再次进行初始化，进行首行数据的插入
            self.id = []
            self.name = []
            self.gender = []
            self.age = []
            # 向表格中插入数据
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])

        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            db.close()  # 关闭数据库连接

        print("进行数据的插入")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

    # 清空表格中的所有信息
    def delButton(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

    # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

    # 点击中间的表格的表头，可以将那一列进行排序
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):#插入新的商品信息
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该药品已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != '':
                # 打开数据库连接
                db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao',password='123456', database="BUY_system", charset='CP936')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO goods(g_id, g_name, g_price, g_number) \
				       VALUES ('%s', '%s', '%s', '%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                    self.age[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写药品信息')

    def updata_row(self):#更新数据
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "UPDATE goods SET g_id = '%s', g_name = '%s', g_price = '%s', g_number = '%s' where g_id = '%s'" % (
            self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(), self.var_id.get())  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            self.name[id_index] = self.var_name.get()
            self.gender[id_index] = self.var_gender.get()
            self.age[id_index] = self.var_age.get()

            self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                self.var_age.get()))  # 修改对于行信息

    # 删除行
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print('*****')
            print(self.tree.selection()[0])  # 行号
            print('*****')
            print(self.tree.get_children())  # 所有行
            print('*****')
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM goods WHERE g_id='%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')

            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.name[id_index]
            del self.gender[id_index]
            del self.age[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())

    def back(self):
        All_admin(self.window)  # 进入管理员子菜单操作界面
#####################################################################################################################################
class ODManage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=250)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=800, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("药品id", "药品名称", "药品总价格", "购买药品数量","购买人")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=15, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("药品id", width=150, anchor='center')
        self.tree.column("药品名称", width=150, anchor='center')
        self.tree.column("药品总价格", width=100, anchor='center')
        self.tree.column("购买药品数量", width=100, anchor='center')
        self.tree.column("购买人", width=100, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.buyer = []

        # 打开数据库连接
        db = pymssql.connect(host='localhost',server=r'SQLEXPRESS',port='1433',user='diao',password='123456',database="BUY_system",charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM orderss"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        print("!!!!!!!!!!!!!!!")
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.buyer.append(row[4])
        except:
            print(sql)
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age),len(self.buyer))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i],self.buyer[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="药品订单信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸

        # 定义下方区域
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put1_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = StringVar()  # 声明年龄
        self.var_buyer = StringVar()
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="药品id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="药品名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 商品价格
        self.right_top_gender_label = Label(self.frame_left_top, text="药品总价格：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 销售数量
        self.right_top_gender_label = Label(self.frame_left_top, text="购买药品数量：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="购买人： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_buyer, font=('Verdana', 15))
        self.right_top_id_label.grid(row=5, column=0)
        self.right_top_id_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建药品订单信息', width=20, command=self.new1_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中药品订单信息', width=20, command=self.updata1_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中药品订单信息', width=20, command=self.del1_row)

        # 定义下方区域，查询功能块
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询订单', width=20, command=self.put1_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        # 右上角按钮的位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环

    # 将查到的信息放到中间的表格中
    def put1_data(self):
        self.delButton()  # 先将表格内的内容全部清空

        # print(self.chaxun.get())	# 输入框内的内容
        # 打开数据库连接，准备查找指定的信息
        db = pymssql.connect(host='localhost',server=r'SQLEXPRESS',port='1433',user='diao',password='123456',database="BUY_system",charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT *FROM orderss where o_name= '%s'" % (self.chaxun.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()

            # 再次进行初始化，进行首行数据的插入
            self.id = []
            self.name = []
            self.gender = []
            self.age = []
            self.buyer= []
            # 向表格中插入数据
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.buyer.append(row[4])

        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            db.close()  # 关闭数据库连接

        print("进行数据的插入")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age),len(self.buyer))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i],self.buyer[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

    # 清空表格中的所有信息
    def delButton(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

    # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.var_buyer.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

    # 点击中间的表格的表头，可以将那一列进行排序
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new1_row(self):#插入新的商品信息
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该药品已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != ''and self.var_buyer.get():
                # 打开数据库连接
                db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao',password='123456', database="BUY_system", charset='CP936')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO orderss(o_id, o_name, o_price, o_number,o_buyer) \
				       VALUES ('%s', '%s', '%s', '%s','%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(),self.var_buyer.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.buyer.append(self.var_buyer.get())
                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                    self.age[len(self.id) - 1],self.buyer[len(self.id)-1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写药品信息')

    def updata1_row(self):#更新数据
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "UPDATE orderss SET o_id = '%s', o_name = '%s', o_price = '%s', o_number = '%s',o_buyer='%s' where o_id = '%s'" % (
            self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(), self.var_id.get(), self.var_buyer.get())  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            self.name[id_index] = self.var_name.get()
            self.gender[id_index] = self.var_gender.get()
            self.age[id_index] = self.var_age.get()
            self.buyer[id_index] = self.var_buyer.get()

            self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                self.var_age.get(),self.var_buyer.get()))  # 修改对于行信息

    # 删除行
    def del1_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print('*****')
            print(self.tree.selection()[0])  # 行号
            print('*****')
            print(self.tree.get_children())  # 所有行
            print('*****')
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM orderss WHERE o_id='%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')

            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.name[id_index]
            del self.gender[id_index]
            del self.age[id_index]
            del self.buyer[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())

    def back(self):
        All_admin(self.window)  # 进入管理员子菜单操作界面

#################################################################################################################################
class USManage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=200)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("用户id", "用户密码")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("用户id", width=150, anchor='center')
        self.tree.column("用户密码", width=150, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []


        # 打开数据库连接
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM users"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])

        except:
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="用户信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸

        # 定义下方区域
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='用户id查询', width=20, command=self.put2_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名

        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="用户id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="用户密码：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)


        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建用户信息', width=20, command=self.new2_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中用户信息', width=20, command=self.updata2_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中用户信息', width=20, command=self.del2_row)

        # 定义下方区域，查询功能块
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='用户id查询', width=20, command=self.put2_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        # 右上角按钮的位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环

    # 将查到的信息放到中间的表格中
    def put2_data(self):
        self.delButton()  # 先将表格内的内容全部清空

        # print(self.chaxun.get())	# 输入框内的内容
        # 打开数据库连接，准备查找指定的信息
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT *FROM users where u_id= '%s'" % (self.chaxun.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print('&&&&&&')
            print(results)

            # 再次进行初始化，进行首行数据的插入
            self.id = []
            self.name = []

            # 向表格中插入数据
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])


        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            db.close()  # 关闭数据库连接

        print("进行数据的插入")
        for i in range(min(len(self.id), len(self.name))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

    # 清空表格中的所有信息
    def delButton(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

    # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])

        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

    # 点击中间的表格的表头，可以将那一列进行排序
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new2_row(self):  # 插入新的商品信息
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该用户已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' :
                # 打开数据库连接
                db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao',
                                     password='123456', database="BUY_system", charset='CP936')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO users(u_id, u_password) \
    				       VALUES ('%s', '%s')" % \
                      (self.var_id.get(), self.var_name.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())

                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写用户信息')

    def updata2_row(self):  # 更新数据
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "UPDATE users SET u_id = '%s', u_password = '%s' where u_id = '%s'" % (
                self.var_id.get(), self.var_name.get(), self.var_id.get())  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            self.name[id_index] = self.var_name.get()


            self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get()))  # 修改对于行信息

    # 删除行
    def del2_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print('*****')
            print(self.tree.selection()[0])  # 行号
            print('*****')
            print(self.tree.get_children())  # 所有行
            print('*****')
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM goods WHERE g_id='%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')

            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.name[id_index]

            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())

    def back(self):
        All_admin(self.window)  # 进入管理员子菜单操作界面



#################################################################################################################################
#用户界面
class UserPage:
    user=0
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 销毁上一个界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('用户登陆页面')
        self.window.geometry('400x300+550+200')# 这里的乘是小x，第一个参数表示窗口的长，第二个表示宽，第三个表示的距离屏幕左边界的距离，第三个为距离上边界的距离

        # 创建画布，这里可以存放照片等组件
        canvas = tk.Canvas(self.window, height=500, width=500)
        image_file = tk.PhotoImage(file='../商品管理系统/welcome.gif')
        image = canvas.create_image(50, 0, anchor='nw', image=image_file)  # 前两个参数为画布得坐标，anchor=nw则是把图片的左上角作为锚定点
        canvas.pack(side='top')  # 使用pack将画布进行简单得布局，放到了上半部分

        # 创建提示信息
        tk.Label(self.window, text='登录账号: ').place(x=80, y=150)#摆放位置
        tk.Label(self.window, text='登陆密码: ').place(x=80, y=190)

        self.admin_username = tk.Entry(self.window)#输入的账号
        self.admin_username.place(x=160, y=150)

        self.admin_pass = tk.Entry(self.window, show='*')#输入的密码用*显示
        self.admin_pass.place(x=160, y=190)
        # 登陆和返回首页得按钮
        btn_login = tk.Button(self.window, text='登陆', width=10, command=self.login1)
        btn_login.place(x=120, y=230)
        btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
        btn_back.place(x=270, y=230)
        self.window.mainloop()
        #########
    # 登陆的函数
    def login1(self):
        # 数据库操作 查询管理员表
        db = pymssql.connect(host='localhost',server=r'SQLEXPRESS',port='1433',user='diao',password='123456',database="BUY_system",charset='CP936')
        print("连接成功")
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM users where u_id = '%s'" % (self.admin_username.get())  # 这里得user_name即为u_id，这里是输入的用户账号
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表，这里是返回的二元元组，如(('id','title'),('id','title'))
            results = cursor.fetchall()
            print(results)
            for row in results:
                u_id = row[0]
                u_password = row[1]
                # 打印结果
                print("用户账号为：%s, \n\n用户密码为：%s" % (u_id, u_password))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆用户界面.......")
        print(self.admin_username.get())#检验
        print(self.admin_pass.get())
        print(u_id)
        print(u_password)
        print(type(u_password))
        print(type(self.admin_pass.get()))
        print(self.admin_pass.get() == u_password)
        #以上均为检验检验数据类型
        user1 = self.admin_username.get()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        UserPage.user = user1
        print(UserPage.user)

        # 判断输入的账号密码与数据库中的信息是否一致a
        if self.admin_pass.get().strip() == u_password.strip():#。strip（）函数清除字符串中的'\n'
            print('进入判断')
            All1_admin(self.window)  # 进入用户子菜单操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')


    # 使得系统点击关闭的x号上返回指定页面，而不是关闭

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
 ###用户子菜单操作界面
class All1_admin:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自定销毁上一个界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('用户操作界面')
        self.window.geometry('1000x700+300+50')
        label = Label(self.window, text="请选择需要进行的操作", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="购买药品", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: Admin1Manage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="个人药品订单查看", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: OD1Manage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="个人信息管理", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: US1Manage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()


        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

        # 使得系统点击关闭的x号上返回指定页面，而不是关闭
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

#$$$$$$$$$$$$$$进入用户购买界面
class Admin1Manage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('用户操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=250)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=800, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("药品id", "药品名称", "药品价格", "药品数量")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=15, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("药品id", width=150, anchor='center')
        self.tree.column("药品名称", width=150, anchor='center')
        self.tree.column("药品价格", width=100, anchor='center')
        self.tree.column("药品数量", width=100, anchor='center')


        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.buyer=0
        print("1111111111111111111111111111111100000000000000000000000000000001111111111111111111111111111111111111")
        print(UserPage.user)
        print(self.buyer)
        self.buyer = UserPage.user
        print(self.buyer)
        print("111111111111111111111111111111111111111111111111111111111111111111111")

        # 打开数据库连接
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM goods"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        print("!!!!!!!!!!!!!!!")
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
        except:
            print(sql)
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="购买操作:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸

        # 定义下方区域
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put3_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = StringVar()  # 声明年龄
        self.var_nu = StringVar()
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="药品id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="药品名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 商品价格
        self.right_top_gender_label = Label(self.frame_left_top, text="药品价格：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 销售数量
        self.right_top_gender_label = Label(self.frame_left_top, text="药品数量：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="购买数量： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_nu, font=('Verdana', 15))
        self.right_top_id_label.grid(row=5, column=0)
        self.right_top_id_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)

        self.right_top_button1 = ttk.Button(self.frame_right_top, text='购买药品', width=20, command=self.updata3_row)

        # 定义下方区域，查询功能块
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put3_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        # 右上角按钮的位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环





    def put3_data(self):
        self.delButton()  # 先将表格内的内容全部清空

        # print(self.chaxun.get())	# 输入框内的内容
        # 打开数据库连接，准备查找指定的信息
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT *FROM goods where g_name= '%s'" % (self.chaxun.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print('&&&&&&')
            print(results)

            # 再次进行初始化，进行首行数据的插入
            self.id = []
            self.name = []
            self.gender = []
            self.age = []
            self.buyer = 0
            print("1111111111111111111111111111111100000000000000000000000000000001111111111111111111111111111111111111")
            print(UserPage.user)
            print(self.buyer)
            self.buyer = UserPage.user
            print(self.buyer)
            print("111111111111111111111111111111111111111111111111111111111111111111111")
            # 向表格中插入数据
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])

        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            db.close()  # 关闭数据库连接

        print("进行数据的插入")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

    # 清空表格中的所有信息
    def delButton(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

    # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

    # 点击中间的表格的表头，可以将那一列进行排序
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def updata3_row(self):  # 更新数据
        res = messagebox.askyesnocancel('提示！', '是否购买？')
        if res == True:
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标

            sql1 = "UPDATE goods SET g_id = '%s', g_name = '%s', g_price = '%s', g_number = '%s' where g_id = '%s'" % (
                self.var_id.get(), self.var_name.get(), self.var_gender.get(), str(int(self.var_age.get())-int(self.var_nu.get())),
                self.var_id.get())  # SQL 插入语句
            sql2 =  "INSERT INTO orderss(o_id, o_name, o_price, o_number,o_buyer) \
				       VALUES ('%s', '%s', '%s', '%s','%s')" % \
                      (self.var_id.get(), self.var_name.get(), str(int(self.var_gender.get())*int(self.var_nu.get())), self.var_nu.get(),self.buyer)
            try:
                cursor.execute(sql1)  # 执行sql1语句
                cursor.execute(sql2)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '购买成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '购买失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            self.name[id_index] = self.var_name.get()
            self.gender[id_index] = self.var_gender.get()
            print('\n\n*************')#检查
            print(self.var_id.get())
            print(self.var_name.get())
            print(self.var_gender.get())
            print(self.var_age.get())#商品数量
            print(type(self.var_age.get()))
            print(self.var_nu.get())
            #print(int(self.var_id.get())-int(self.var_nu.get()))
            #print(str(int(self.var_id.get())-int(self.var_nu.get())))#检查
            self.age[id_index] = self.var_id.get()#检查

            self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                str(int(self.var_age.get())-int(self.var_nu.get()))))  # 修改对于行信息

        # 使得系统点击关闭的x号上返回指定页面，而不是关闭

    def back(self):
        All1_admin(self.window)

#￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
#进入查看订单页面
class OD1Manage(UserPage):
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('用户操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=250)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=800, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("药品id", "药品名称", "药品订单总价格", "购买药品数量", "购买人")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=15, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("药品id", width=150, anchor='center')
        self.tree.column("药品名称", width=150, anchor='center')
        self.tree.column("药品订单总价格", width=100, anchor='center')
        self.tree.column("购买药品数量", width=100, anchor='center')
        self.tree.column("购买人", width=100, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.buyer = []
        #

        print("111111111111111111111111111111111111111111111111111111111111111111111")
        print(UserPage.user)
        self.user_username= UserPage.user
        print(self.user_username)
        print("111111111111111111111111111111111111111111111111111111111111111111111")
        # 打开数据库连接
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM orderss WHERE o_buyer = '%s'" % (self.user_username)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        print("!!!!!!!!!!!!!!!")
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.buyer.append(row[4])
        except:
            print(sql)
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age), len(self.buyer))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i], self.buyer[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="药品订单信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = StringVar()  # 声明年龄
        self.var_buyer = StringVar()
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="药品id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="药品名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 商品价格
        self.right_top_gender_label = Label(self.frame_left_top, text="药品订单总价格：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 销售数量
        self.right_top_gender_label = Label(self.frame_left_top, text="购买药品数量：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="购买人： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_buyer, font=('Verdana', 15))
        self.right_top_id_label.grid(row=5, column=0)
        self.right_top_id_entry.grid(row=5, column=1)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环
        #点击出现
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.var_buyer.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))
    def back(self):
        All1_admin(self.window)
###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#进入用户信息页面
class US1Manage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('用户操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=200)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("用户id", "用户密码")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("用户id", width=150, anchor='center')
        self.tree.column("用户密码", width=150, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []
        self.t=0
        print("XXXXXXXXXXXXXXXXXXXXXXXX11111111111111111111")
        print(UserPage.user)
        self.t = UserPage.user
        print(self.t)
        print("111111111111111111111111111111111111111111111111111111111111111111111")

        # 打开数据库连接
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM users WHERE u_id ='%s'" % (self.t)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])

        except:
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="用户信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸



        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名

        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="用户id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="用户密码：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)

        self.right_top_button1 = ttk.Button(self.frame_right_top, text='更新个人信息', width=20, command=self.updatause_row)



        # 右上角按钮的位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环

    # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        #self.var_gender.set(self.row_info[2])
       # self.var_age.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

    # 点击中间的表格的表头，可以将那一列进行排序
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def updatause_row(self):  # 更新数据
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "UPDATE users SET u_id = '%s', u_password = '%s' where u_id = '%s'" % (
                self.var_id.get(), self.var_name.get(), self.var_id.get())  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            self.name[id_index] = self.var_name.get()

            self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get()))  # 修改对于行信息
    def back(self):
        All1_admin(self.window)


#############卖家登陆页面
class SellerPage:
    seller=0
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 销毁上一个界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('卖家登陆页面')
        self.window.geometry('400x300+550+200')# 这里的乘是小x，第一个参数表示窗口的长，第二个表示宽，第三个表示的距离屏幕左边界的距离，第三个为距离上边界的距离

        # 创建画布，这里可以存放照片等组件
        canvas = tk.Canvas(self.window, height=500, width=500)
        image_file = tk.PhotoImage(file='../商品管理系统/welcome.gif')
        image = canvas.create_image(50, 0, anchor='nw', image=image_file)  # 前两个参数为画布得坐标，anchor=nw则是把图片的左上角作为锚定点
        canvas.pack(side='top')  # 使用pack将画布进行简单得布局，放到了上半部分

        # 创建提示信息
        tk.Label(self.window, text='登录账号: ').place(x=80, y=150)#摆放位置
        tk.Label(self.window, text='登陆密码: ').place(x=80, y=190)

        self.admin_username = tk.Entry(self.window)#输入的账号
        self.admin_username.place(x=160, y=150)

        self.admin_pass = tk.Entry(self.window, show='*')#输入的密码用*显示
        self.admin_pass.place(x=160, y=190)
        # 登陆和返回首页得按钮
        btn_login = tk.Button(self.window, text='登陆', width=10, command=self.login2)
        btn_login.place(x=120, y=230)
        btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
        btn_back.place(x=270, y=230)
        self.window.mainloop()

    # 登陆的函数
    def login2(self):
        # 数据库操作 查询管理员表
        db = pymssql.connect(host='localhost',server=r'SQLEXPRESS',port='1433',user='diao',password='123456',database="BUY_system",charset='CP936')
        print("连接成功")
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM users where u_id = '%s'" % (self.admin_username.get())  # 这里得user_name即为u_id，这里是输入的用户账号
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表，这里是返回的二元元组，如(('id','title'),('id','title'))
            results = cursor.fetchall()
            print(results)
            for row in results:
                u_id = row[0]
                u_password = row[1]
                # 打印结果
                print("卖家账号为：%s, \n\n卖家密码为：%s" % (u_id, u_password))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆卖家管理界面.......")
        print(self.admin_username.get())#检验
        print(self.admin_pass.get())
        print(u_id)
        print(u_password)
        print(type(u_password))
        print(type(self.admin_pass.get()))
        print(self.admin_pass.get() == u_password)
        seller1=self.admin_username.get()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        SellerPage.seller = seller1
        print(SellerPage.seller)

        #以上均为检验检验数据类型

        # 判断输入的账号密码与数据库中的信息是否一致a
        if self.admin_pass.get().strip() == u_password.strip():#。strip（）函数清除字符串中的'\n'
            print('进入判断')
            All33_admin(self.window)  # 进入管理员子菜单操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')


# 使得系统点击关闭的x号上返回指定页面，而不是关闭
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

class All33_admin:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自定销毁上一个界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('信息管理界面')
        self.window.geometry('1000x700+300+50')
        label = Label(self.window, text="请选择需要进行的操作", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="药品信息管理", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: Admin33Manage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="药品订单信息管理", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: OD33Manage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="个人信息管理", font=tkFont.Font(size=25), width=30, height=2,
               command=lambda: US33Manage(self.window),
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()


        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
#……………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………
# 商品信息操作界面
class Admin33Manage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=200)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("药品id", "药品名称", "药品价格", "药品数量")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("药品id", width=150, anchor='center')
        self.tree.column("药品名称", width=150, anchor='center')
        self.tree.column("药品价格", width=100, anchor='center')
        self.tree.column("药品数量", width=100, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []
        self.gender = []
        self.age = []

        # 打开数据库连接
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM goods"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
        except:
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="药品信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸

        # 定义下方区域
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = StringVar()  # 声明年龄
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="药品id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="药品名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 商品价格
        self.right_top_gender_label = Label(self.frame_left_top, text="药品价格：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 销售数量
        self.right_top_gender_label = Label(self.frame_left_top, text="药品数量：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建药品信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中药品信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中药品信息', width=20, command=self.del_row)

        # 定义下方区域，查询功能块
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        # 右上角按钮的位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环

    # 将查到的信息放到中间的表格中
    def put_data(self):
        self.delButton()  # 先将表格内的内容全部清空

        # print(self.chaxun.get())	# 输入框内的内容
        # 打开数据库连接，准备查找指定的信息
        db = pymssql.connect(host='localhost',server=r'SQLEXPRESS',port='1433',user='diao',password='123456',database="BUY_system",charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT *FROM goods where g_name= '%s'" % (self.chaxun.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print('&&&&&&')
            print(results)

            # 再次进行初始化，进行首行数据的插入
            self.id = []
            self.name = []
            self.gender = []
            self.age = []
            # 向表格中插入数据
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])

        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            db.close()  # 关闭数据库连接

        print("进行数据的插入")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

    # 清空表格中的所有信息
    def delButton(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

    # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

    # 点击中间的表格的表头，可以将那一列进行排序
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):#插入新的商品信息
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该药品已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != '':
                # 打开数据库连接
                db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao',password='123456', database="BUY_system", charset='CP936')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO goods(g_id, g_name, g_price, g_number) \
				       VALUES ('%s', '%s', '%s', '%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                    self.age[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写药品信息')

    def updata_row(self):#更新数据
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "UPDATE goods SET g_id = '%s', g_name = '%s', g_price = '%s', g_number = '%s' where g_id = '%s'" % (
            self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(), self.var_id.get())  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            self.name[id_index] = self.var_name.get()
            self.gender[id_index] = self.var_gender.get()
            self.age[id_index] = self.var_age.get()

            self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                self.var_age.get()))  # 修改对于行信息

    # 删除行
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print('*****')
            print(self.tree.selection()[0])  # 行号
            print('*****')
            print(self.tree.get_children())  # 所有行
            print('*****')
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM goods WHERE g_id='%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')

            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.name[id_index]
            del self.gender[id_index]
            del self.age[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())

    def back(self):
        All33_admin(self.window)  # 进入管理员子菜单操作界面
#分割线
class OD33Manage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=250)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=800, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("药品id", "药品名称", "药品总价格", "购买药品数量", "购买人")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=15, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("药品id", width=150, anchor='center')
        self.tree.column("药品名称", width=150, anchor='center')
        self.tree.column("药品总价格", width=100, anchor='center')
        self.tree.column("购买药品数量", width=100, anchor='center')
        self.tree.column("购买人", width=100, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.buyer = []

        # 打开数据库连接
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM orderss"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        print("!!!!!!!!!!!!!!!")
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.buyer.append(row[4])
        except:
            print(sql)
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age), len(self.buyer))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i], self.buyer[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="药品订单信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸

        # 定义下方区域
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put1_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = StringVar()  # 声明年龄
        self.var_buyer = StringVar()
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="药品id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="药品名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 商品价格
        self.right_top_gender_label = Label(self.frame_left_top, text="药品总价格：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 销售数量
        self.right_top_gender_label = Label(self.frame_left_top, text="购买药品数量：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="购买人： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_buyer, font=('Verdana', 15))
        self.right_top_id_label.grid(row=5, column=0)
        self.right_top_id_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建药品信息', width=20, command=self.new1_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中药品信息', width=20, command=self.updata1_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中药品信息', width=20, command=self.del1_row)

        # 定义下方区域，查询功能块
        self.chaxun = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.chaxun, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='药品名称查询', width=20, command=self.put1_data)
        self.right_bottom_button.grid(row=0, column=0, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=1)

        # 右上角按钮的位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环

        # 将查到的信息放到中间的表格中

    def put1_data(self):
        self.delButton()  # 先将表格内的内容全部清空

        # print(self.chaxun.get())	# 输入框内的内容
        # 打开数据库连接，准备查找指定的信息
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT *FROM orderss where o_name= '%s'" % (self.chaxun.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()

            # 再次进行初始化，进行首行数据的插入
            self.id = []
            self.name = []
            self.gender = []
            self.age = []
            self.buyer = []
            # 向表格中插入数据
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.buyer.append(row[4])

        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
            db.close()  # 关闭数据库连接

        print("进行数据的插入")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age), len(self.buyer))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i], self.buyer[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 清空表格中的所有信息

    def delButton(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

        # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.var_buyer.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

        # 点击中间的表格的表头，可以将那一列进行排序

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new1_row(self):  # 插入新的商品信息
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该药品已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != '' and self.var_buyer.get():
                # 打开数据库连接
                db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao',
                                     password='123456', database="BUY_system", charset='CP936')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO orderss(o_id, o_name, o_price, o_number,o_buyer) \
    				       VALUES ('%s', '%s', '%s', '%s','%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(),
                       self.var_buyer.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.buyer.append(self.var_buyer.get())
                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                    self.age[len(self.id) - 1], self.buyer[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写药品信息')

    def updata1_row(self):  # 更新数据
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "UPDATE orderss SET o_id = '%s', o_name = '%s', o_price = '%s', o_number = '%s',o_buyer='%s' where o_id = '%s'" % (
                self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(), self.var_id.get(),
                self.var_buyer.get())  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            self.name[id_index] = self.var_name.get()
            self.gender[id_index] = self.var_gender.get()
            self.age[id_index] = self.var_age.get()
            self.buyer[id_index] = self.var_buyer.get()

            self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                self.var_age.get(), self.var_buyer.get()))  # 修改对于行信息

        # 删除行

    def del1_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print('*****')
            print(self.tree.selection()[0])  # 行号
            print('*****')
            print(self.tree.get_children())  # 所有行
            print('*****')
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM orderss WHERE o_id='%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')

            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.name[id_index]
            del self.gender[id_index]
            del self.age[id_index]
            del self.buyer[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())


    def back(self):
        All33_admin(self.window)  # 进入管理员子菜单操作界面
        ##############卖家改密码

##########
class US33Manage:
    def __init__(self, parent_window):
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        self.window = Tk()  # 初始框的声明
        self.window.title('用户操作界面')
        self.window.geometry("1000x700+300+50")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=200)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=350)
        self.frame_bottom = tk.Frame(width=650, height=70)

        # 定义下方中心列表区域
        self.columns = ("用户id", "用户密码")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0

        # 表格的标题
        self.tree.column("用户id", width=150, anchor='center')
        self.tree.column("用户密码", width=150, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备
        self.id = []
        self.name = []
        self.n = 0
        print("XXXXXXXXXXXXXXXXXXXXXXXX11111111111111111111")
        print(SellerPage.seller)
        self.n = SellerPage.seller
        print(self.n)
        print("111111111111111111111111111111111111111111111111111111111111111111111")

        # 打开数据库连接
        db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                             database="BUY_system", charset='CP936')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM users WHERE u_id ='%s'" % (self.n)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])

        except:
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="用户信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)  # NSEW表示允许组件向4个方向都可以拉伸

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名

        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="用户id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="用户密码：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)

        self.right_top_button1 = ttk.Button(self.frame_right_top, text='更新个人信息', width=20, command=self.updatause_row)

        # 右上角按钮的位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环

        # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 通过tree.identify_column()函数可以直接获取到列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        # self.var_gender.set(self.row_info[2])
        # self.var_age.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

        # 点击中间的表格的表头，可以将那一列进行排序

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def updatause_row(self):  # 更新数据
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            # 打开数据库连接
            db = pymssql.connect(host='localhost', server=r'SQLEXPRESS', port='1433', user='diao', password='123456',
                                 database="BUY_system", charset='CP936')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "UPDATE users SET u_id = '%s', u_password = '%s' where u_id = '%s'" % (
                self.var_id.get(), self.var_name.get(), self.var_id.get())  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            self.name[id_index] = self.var_name.get()

            self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get()))  # 修改对于行信息
    def back(self):
        All33_admin(self.window)



##################################################################################################################################

if __name__ == '__main__':
    # 实例化Application
    window = tk.Tk()
    StartPage(window)
#真难