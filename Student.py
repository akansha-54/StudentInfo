from tkinter import *
from tkinter import ttk
import pymysql
import tkinter.messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1520x780+0+0")
        self.root.configure(bg="navy")

        title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("Times New Roman",40,"bold"),bg="navy",fg="white")
        title.pack(side=TOP,fill=X)

        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Branch_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_No_var = StringVar()
        self.Dob_var = StringVar()
        self.Year_var = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

    # -----------------------------MANAGE FRAME---------------------------------------------------------------
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=20,y=100,width=500,height=660)

        m_title=Label(Manage_Frame,text="Manage Students",bg="black",fg="white",font=("Times New Roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10,padx=30)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="black",fg="white",font=("Times New Roman",15,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,text="Roll No.",textvariable=self.Roll_No_var,width=35,bg="white",fg="black",bd=5,relief=GROOVE,font=("Times New Roman",12,"bold"))
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="black", fg="white", font=("Times New Roman",15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,bg="white",width=35,textvariable=self.Name_var,fg="black", bd=5, relief=GROOVE,font=("Times New Roman", 12, "bold"))
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="black", fg="white", font=("Times New Roman", 15, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame,bg="white", fg="black",textvariable=self.Email_var,width=35,bd=5, relief=GROOVE,
                         font=("Times New Roman", 12, "bold"))
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Branch = Label(Manage_Frame, text="Branch", bg="black", fg="white", font=("Times New Roman",15, "bold"))
        lbl_Branch.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_branch=ttk.Combobox(Manage_Frame,textvariable=self.Branch_var,width=27,font=("Times New Roman",15, "bold"),state="readonly")
        combo_branch['values']=("Select Branch","Computer Science Engineering","Civil Engineering","Chemical Engineering","Mechanical Engineering","Electrical Engineering","Electronics & Communication Engineering","Information Technology Engineering")
        combo_branch.set("Select Branch")
        combo_branch.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_gender = Label(Manage_Frame,text="Gender",bg="black", fg="white", font=("Times New Roman",15, "bold"))
        lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,width=27,font=("Times New Roman",15, "bold"), state="readonly")
        combo_gender['values'] = ("Select Gender","Male","Female","Transgender")
        combo_gender.set("Select Gender")
        combo_gender.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact No.", bg="black", fg="white", font=("Times New Roman", 15, "bold"))
        lbl_contact.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, bg="white", fg="black", width=35,textvariable=self.Contact_No_var, bd=5, relief=GROOVE,
                          font=("Times New Roman", 12, "bold"))
        txt_Contact.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Dob = Label(Manage_Frame, text="D.O.B", bg="black", fg="white", font=("Times New Roman", 15, "bold"))
        lbl_Dob.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_Dob = Entry(Manage_Frame, bg="white", fg="black", width=35, bd=5, relief=GROOVE,textvariable=self.Dob_var,
                          font=("Times New Roman", 12, "bold"))
        txt_Dob.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_Year = Label(Manage_Frame, text="Year", bg="black", fg="white", font=("Times New Roman", 15, "bold"))
        lbl_Year.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        combo_year = ttk.Combobox(Manage_Frame,textvariable=self.Year_var,width=27 ,font=("Times New Roman", 15, "bold"), state="readonly")
        combo_year['values'] = ("Select Year","1st year","2nd year","3rd year","4th year")
        combo_year.set("Select Year")
        combo_year.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="black", fg="white", font=("Times New Roman",15, "bold"))
        lbl_Address.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address= Text(Manage_Frame,width=36,height=4,font=("times new roman",12,"bold"))
        self.txt_Address.grid(row=9, column=1 , pady=10,padx=20,sticky="w")

        # -------------------------------------BUTTON FRAME------------------------------------------------------

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="black")
        btn_Frame.place(x=10, y=580, width=470)

        Addbtn = Button(btn_Frame,text="ADD",width=12,font=("Times New Roman",10,"bold"),command=self.add_students,bg="blue4",fg="white",bd=3,relief=SUNKEN)
        Addbtn.grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame, text="UPDATE",font=("Times New Roman",10,"bold"),width=12,command=self.update_data,bg="blue4",fg="white",bd=3,relief=SUNKEN)
        Updatebtn.grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="DELETE", font=("Times New Roman",10,"bold"),width=12,command=self.delete_data,bg="blue4",fg="white",bd=3,relief=SUNKEN)
        Deletebtn.grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="CLEAR", font=("Times New Roman",10,"bold"),width=12,command=self.clear,bg="blue4",fg="white",bd=3,relief=SUNKEN)
        Clearbtn.grid(row=0, column=3, padx=10, pady=10)

    # -----------------------------DETAIL FRAME--------------------------------------------------------------------
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="black")
        Detail_Frame.place(x=560,y=100, width=930, height=660)

        lblSearch = Label(Detail_Frame, text="Search By", bg="black", fg="white", font=("Times New Roman",20, "bold"))
        lblSearch.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by,font=("Times New Roman", 15, "bold"), state="readonly")
        combo_Search['values'] = ("Select","roll","name","branch","year")
        combo_Search.set("Select")
        combo_Search.grid(row=0, column=1, pady=10, padx=20)

        txt_Search = Entry(Detail_Frame, bg="white", fg="black",textvariable=self.search_txt, width=30, bd=5, relief=GROOVE,font=("Times New Roman", 14, "bold"))
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, text="SEARCH", font=("Times New Roman",10,"bold"),width=12, pady=5,command=self.search_data,bg="blue4",fg="white",bd=3,relief=SUNKEN)
        Searchbtn.grid(row=0, column=3, padx=10, pady=10)
        Showbtn = Button(Detail_Frame, text="SHOW ALL", font=("Times New Roman",10,"bold"),width=12, pady=5,command=self.fetch_data,bg="blue4",fg="white",bd=3,relief=SUNKEN)
        Showbtn.grid(row=0, column=4, padx=10, pady=10)

        #-------------------TABLE FRAME--------------------------------------------------------------------------------

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=10, y=60, width=900, height=580)

        Scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Information_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","branch","gender","contact","dob","year","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.configure(command=self.Information_table.xview)
        Scroll_y.configure(command=self.Information_table.yview)
        self.Information_table.heading("roll",text="Roll No.")
        self.Information_table.heading("name", text="Name")
        self.Information_table.heading("email", text="Email")
        self.Information_table.heading("branch", text="Branch")
        self.Information_table.heading("gender", text="Gender")
        self.Information_table.heading("contact", text="Contact No.")
        self.Information_table.heading("dob", text="D.O.B")
        self.Information_table.heading("year", text="Year")
        self.Information_table.heading("address", text="Address")
        self.Information_table['show'] = 'headings'
        self.Information_table.column("roll",width=100)
        self.Information_table.column("name", width=180)
        self.Information_table.column("email", width=180)
        self.Information_table.column("branch", width=180)
        self.Information_table.column("gender", width=100)
        self.Information_table.column("contact", width=150)
        self.Information_table.column("dob", width=100)
        self.Information_table.column("year", width=100)
        self.Information_table.column("address", width=230)
        self.Information_table.pack(fill=BOTH,expand=1)
        self.Information_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
        if (self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Branch_var.get()=="Select Branch" or self.Gender_var.get()=="Select Gender" or self.Contact_No_var.get()=="" or self.Dob_var.get()=="" or self.Year_var.get()=="Select Year" or self.txt_Address.get('1.0',END)==""):
            tkinter.messagebox.showerror("Error","All fields are required !!!")
        else:
            con = pymysql.connect("localhost","root","rat","student_management")
            cur = con.cursor()
            cur.execute("insert into information values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                      self.Name_var.get(),
                                                                                      self.Email_var.get(),
                                                                                      self.Branch_var.get(),
                                                                                      self.Gender_var.get(),
                                                                                      self.Contact_No_var.get(),
                                                                                      self.Dob_var.get(),
                                                                                      self.Year_var.get(),
                                                                                      self.txt_Address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            tkinter.messagebox.showinfo("Success","Record has been Inserted!")
    def fetch_data(self):
        con = pymysql.connect("localhost", "root", "rat", "student_management")
        cur = con.cursor()
        cur.execute("select * from information")
        data=cur.fetchall()
        if len(data)!=0:
            self.Information_table.delete(*self.Information_table.get_children())
            for row in data:
                self.Information_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Branch_var.set("Select Branch")
        self.Gender_var.set("Select Gender")
        self.Contact_No_var.set("")
        self.Dob_var.set("")
        self.Year_var.set("Select Year")
        self.txt_Address.delete("1.0",END)
    def get_cursor(self,ev):
        cursor_row = self.Information_table.focus()
        content = self.Information_table.item(cursor_row)
        row = content['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Branch_var.set(row[3])
        self.Gender_var.set(row[4])
        self.Contact_No_var.set(row[5])
        self.Dob_var.set(row[6])
        self.Year_var.set(row[7])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END,row[8])
    def update_data(self):
        con = pymysql.connect("localhost", "root", "rat", "student_management")
        cur = con.cursor()
        cur.execute("update information set name=%s,email=%s,branch=%s,gender=%s,contact=%s,dob=%s,year=%s,address=%s where roll=%s",(self.Name_var.get(),self.Email_var.get(),self.Branch_var.get(),self.Gender_var.get(),self.Contact_No_var.get(),self.Dob_var.get(),self.Year_var.get(), self.txt_Address.get('1.0', END),self.Roll_No_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        tkinter.messagebox.showinfo("Success", "Record has been Updated!")
    def delete_data(self):
        con = pymysql.connect("localhost", "root", "rat", "student_management")
        cur = con.cursor()
        cur.execute("delete from information where roll=%s",self.Roll_No_var.get())
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        tkinter.messagebox.showinfo("Success", "Record has been Deleted!")
    def search_data(self):
        if (self.search_by.get()==""):
            tkinter.messagebox.showerror("Search unsuccessful","Search By is Needed !")
        if self.search_txt.get()== "":
            tkinter.messagebox.showerror("Search unsuccessful","Search Text is Needed !")
        else:
            con = pymysql.connect("localhost", "root", "rat", "student_management")
            cur = con.cursor()

            cur.execute("select * from information where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            data=cur.fetchall()
            if len(data)!=0:
                self.Information_table.delete(*self.Information_table.get_children())
                for row in data:
                    self.Information_table.insert('',END,values=row)
                con.commit()
            con.close()
            tkinter.messagebox.showinfo("Success","Search Successful!")

root=Tk()
obj=Student(root)
root.mainloop()