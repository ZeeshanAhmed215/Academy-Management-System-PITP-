try:

        import  tkinter as tk
        import customtkinter as cu
        from tkinter import ttk,messagebox as msg
        from fpdf import FPDF
        from PIL import Image
        import mysql.connector
except ModuleNotFoundError:
        msg.showerror("Database Not Found","Please! Check the connection of your database...........")
                  


try:

        db=mysql.connector.connect(
        host="your host name",
        user="your user name",
        password="your password of Mysql",
        database="your name of database"
        )
except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
             msg.showerror("Database Not Found","Please! Check the connection of your database...........")
                                       

# cursor=db.cursor()
# cursor.execute(f"select * from admin")
# data=cursor.fetchall()
# for result in data:
#         print(result)
        


# db.commit()
# cursor.close()
# db.close()
cu.set_appearance_mode("dark")
cu.set_default_color_theme("dark-blue")

def switch_option(switch_to):
    match switch_to:
        case "Home":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                home()
                home_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ============
                register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

                
        case "Registration":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                registration()
                register_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ================
                home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

                
        case "View":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                view()
                view_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ===============
                home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

               
              

def registration():
        

              wig_frame=cu.CTkFrame(big_frame,corner_radius=20)
              wig_frame.grid(row=0,column=1,pady=20,padx=50)

              page_frame=cu.CTkFrame(big_frame,width=1300,height=600,corner_radius=20,)
              page_frame.grid(row=1,column=1,padx=60)

              head_lab=cu.CTkLabel(wig_frame,text="Admission Form",font=("Arial Rounded MT Bold",60))
              head_lab.grid(row=0,column=1,padx=170)

#             Form labels=========================
        #       Column 1
              st_name_lab=cu.CTkLabel(page_frame,text="Student Name:",font=("Arial Rounded MT Bold",22,"bold"))
              st_name_lab.grid(row=1,column=0,pady=5,padx=15)
              st_cnic_lab=cu.CTkLabel(page_frame,text="Student Cnic:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold"))
              st_cnic_lab.grid(row=2,column=0,pady=5)
              st_dob_lab=cu.CTkLabel(page_frame,text="Student DOB:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold"))
              st_dob_lab.grid(row=3,column=0,pady=5)
              st_gen_lab=cu.CTkLabel(page_frame,text="Gender:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold"))
              st_gen_lab.grid(row=4,column=0,pady=5)
              course_lab=cu.CTkLabel(page_frame,text="Course:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold"))
              course_lab.grid(row=5,column=0,pady=5)
        #       Column 2
              father_name_lab=cu.CTkLabel(page_frame,text=" Father`s Name:",font=("Arial Rounded MT Bold",22,"bold"))
              father_name_lab.grid(row=1,column=2,pady=5)
              father_cnic_lab=cu.CTkLabel(page_frame,text="Father`s Cnic:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold"))
              father_cnic_lab.grid(row=2,column=2,pady=5)
              f_pro_lab=cu.CTkLabel(page_frame,text="F/Profession",anchor="ne",font=("Arial Rounded MT Bold",22,"bold"))
              f_pro_lab.grid(row=3,column=2,pady=5)
              phone_lab=cu.CTkLabel(page_frame,text=" Phone No:",font=("Arial Rounded MT Bold",22,"bold"))
              phone_lab.grid(row=4,column=2,pady=5)
              address_lab=cu.CTkLabel(page_frame,text="Address:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold"))
              address_lab.grid(row=5,column=2,pady=5)


#               Form Entries==============================
#               Column 1
              st_name_ent=cu.CTkEntry(page_frame,placeholder_text="Hussain Raza",width=250,font=("Cambria (Headings)", 20))
              st_name_ent.grid(row=1,column=1,padx=15,pady=5)
              st_cnic_ent=cu.CTkEntry(page_frame,placeholder_text="45502-7073113-3",width=250,font=("Cambria (Headings)", 20))
              st_cnic_ent.grid(row=2,column=1,padx=10,pady=5)
              st_dob_ent=cu.CTkEntry(page_frame,placeholder_text="27-4-2006",width=250,font=("Cambria (Headings)", 20))
              st_dob_ent.grid(row=3,column=1,padx=10,pady=5)
              gen_combo=cu.CTkOptionMenu(page_frame,values=["Select Gender","Male","Female","Other"],width=245,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
              gen_combo.grid(row=4,column=1,pady=10,padx=5)
              course_list=["Select Course","Python Development","Java Development","C++ Programming","C# Programming","Web Development","PHP Web Development","SQL Database","Data Science","Machine Learning","Cyber Security","Data Structures"]
              course_combo=cu.CTkOptionMenu(page_frame,values=course_list,width=245,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
              course_combo.grid(row=5,column=1,pady=10,padx=5)
        #     Column 2   

              f_name_ent=cu.CTkEntry(page_frame,placeholder_text="Hassan Raza",width=250,font=("Cambria (Headings)", 20))
              f_name_ent.grid(row=1,column=4,pady=5,padx=10)
              f_cnic_ent=cu.CTkEntry(page_frame,placeholder_text="45502-8976982-7",width=250,font=("Cambria (Headings)", 20))
              f_cnic_ent.grid(row=2,column=4,pady=5,padx=10)
              f_pro_ent=cu.CTkEntry(page_frame,placeholder_text="Teacher",width=250,font=("Cambria (Headings)", 20))
              f_pro_ent.grid(row=3,column=4,pady=5,padx=10)

              phone_ent=cu.CTkEntry(page_frame,placeholder_text="+923473228701",width=250,font=("Cambria (Headings)", 20))
              phone_ent.grid(row=4,column=4,pady=5,padx=10)
              address_ent=cu.CTkEntry(page_frame,placeholder_text="Sukkur Sindh Pakistan",width=250,font=("Cambria (Headings)", 20))
              address_ent.grid(row=5,column=4,pady=5,padx=10)



              book_image=cu.CTkImage(dark_image=Image.open("images/fill_ph.png"),light_image=Image.open("images/fill_ph.png"),size=(350,350))

              image_label=cu.CTkLabel(big_frame,text="",image=book_image)
              image_label.grid(row=1,column=2)
#             Button of register=====================

              def admission():
                        # Column one==============
                        st_name=st_name_ent.get().title().strip()
                        st_cnic=st_cnic_ent.get().strip()
                        st_dob=st_dob_ent.get().strip()
                        gen=gen_combo.get()
                        course=course_combo.get()
                        # Column two==============
                        f_name=f_name_ent.get().title().strip()
                        f_cnic=f_cnic_ent.get().strip()
                        f_pro=f_pro_ent.get().title().strip()
                        phone=phone_ent.get().strip()
                        address=address_ent.get().title().strip()
                        import datetime
                        Tim=datetime.datetime.now()
                        Time=Tim.strftime(f"%d-%m-%Y")
                        date_formate=f"%d-%m-%Y"
                        from datetime import datetime,timedelta
                        date=datetime.strptime(Time,date_formate)
                        passing_date=date+timedelta(days=6*30)
                        passing_date=str(passing_date)
                       
                        
                        
                        # Make a list==============
                        form_data=[st_name,f_name,st_cnic,f_cnic,gen,st_dob,phone,address,f_pro,course,Time,"Six Months",passing_date,"Unpaid"]
                                        # msg.showerror("Missing Fields Error","Please! Fill out all required fields.\nThis will help us process your request.\nYou have some missing information.\nPlease! Review and complete the form. ")
                        def data_verify(data_list):
                                data_list=list(data_list)
                                for element in data_list:
                                        if element=="":
                                                msg.showerror("Missing Fields Error","Please! Fill out all required fields.\nThis will help us process your request.\nYou have some missing information.\nPlease! Review and complete the form. ")
                                                return  None
                                        
                                                
                                import re               
                                cnic_pattern=re.compile(r"^\d{5}-\d{7}-\d$")
                                dob_pattern=re.compile(r"^\d{2}-\d{2}-\d{4}$")
                                phone_pattern=re.compile(r"^(\+92|0)?3\d{9}$")
                                if  cnic_pattern.match(str(data_list[2])) and cnic_pattern.match(str(data_list[3])) and dob_pattern.match(str(data_list[5])) and phone_pattern.match(str(data_list[6])):
                                        if str(data_list[4])=="Select Gender" or str(data_list[9])=="Select Course":
                                                msg.showerror("Data Validation Error","Please! Select Course and Gender\nThis will help us process your request.\nYou have not selected them.\nPlease! Review and complete the form with correct data. ")
                                                return  None 
                                        else:
                                            
                                            return data_list
                                        
                                else:
                                        msg.showerror("Data Validation Error","Please! Fill out all required fields with correct data.\nThis will help us process your request.\nYou have entered some wrong information.\nPlease! Review and complete the form with correct data. ")
                                        return  None        
                        verify_data=data_verify(form_data)
                        
                        if verify_data != None:
                                verify_data=tuple(verify_data)
                                
                                try:
                                        cursor=db.cursor()
                                        cursor.execute(f"insert into admin(Student_Name,Father_Name,CNIC,Father_CNIC,Gender,DOB,Phone,Address,Father_pro,Course,Admission_Date,Course_Duration,Passing_Date,Fee_Status) values{verify_data} ")
                                        db.commit()
                                        cursor.close()

                                        msg.showinfo("Form Submitted Successfully","Congratulations! Your admission form has been submitted successfully.\nTo confirm your seat, Please! processed to pay the admission fee as per the instructions provide.\nWe look forward to Welcoming you to our institution! ")
                                        st_name_ent.delete(0, "end")
                                        st_cnic_ent.delete(0, "end")
                                        st_dob_ent.delete(0, "end")
                                        # Column two==============
                                        f_name_ent.delete(0, "end")
                                        f_cnic_ent.delete(0, "end")
                                        f_pro_ent.delete(0, "end")
                                        phone_ent.delete(0, "end")
                                        address_ent.delete(0, "end") 
                                except (mysql.connector.errors.OperationalError,
                                        mysql.connector.errors.ProgrammingError,
                                        mysql.connector.errors.IntegrityError,
                                        mysql.connector.errors.ConnectionTimeoutError,
                                        ):
                                        msg.showerror("Database Not Found","Please! Check the connection of database...........")
                                       
                                          

              register_btn=cu.CTkButton(page_frame,text="Register!",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#1F6AA5",command=admission)
              register_btn.grid(row=6,column=0,padx=10,ipadx=20,columnspan=10,pady=50)
        #        Image Books======================

              

def home():

        # Making table area=================================================
        tb_frame1=cu.CTkFrame(big_frame,corner_radius=20,height=250,width=800)
        tb_frame1.grid(row=1,column=1)
        table_frame1 = tk.Frame(tb_frame1, bg="#000000", bd=2, relief="ridge")
        table_frame1.place(x=5,y=10,width=790,height=220,)
        scroll_x_bottom1=tk.Scrollbar(table_frame1,orient="horizontal")
        scroll_x_top1=tk.Scrollbar(table_frame1,orient="horizontal")
        scroll_y_left1=tk.Scrollbar(table_frame1,orient="vertical")
        scroll_y_right1=tk.Scrollbar(table_frame1,orient="vertical")
        col_names1=("st_name","f_name","st_cnic","gen","cou","fee_status")
        col_heading_names1=("Student Name","Father`s Name","CNIC","Gender","Course","Fees Status")
        Customer_table1=ttk.Treeview(table_frame1,columns=(col_names1),xscrollcommand=scroll_x_bottom1.set and scroll_x_top1,yscrollcommand=scroll_y_left1.set and scroll_y_right1.set)
        scroll_x_bottom1.pack(side="bottom",fill="x")
        scroll_x_top1.pack(side="top",fill="x")
        scroll_y_left1.pack(side="left",fill="y")
        scroll_y_right1.pack(side="right",fill="y")
        scroll_x_bottom1.config(command=Customer_table1.xview)
        scroll_x_top1.config(command=Customer_table1.xview)
        scroll_y_left1.config(command=Customer_table1.yview)
        scroll_y_right1.config(command=Customer_table1.yview)
        for x,y in zip(col_names1,col_heading_names1):
              Customer_table1.heading(x,text=y)
        Customer_table1['show']='headings'

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                background="#313030",  
                fieldbackground="#363636", 
                foreground="#ffffff",   
                ) 
        style.configure("Treeview.Heading",
                background="#4a4a4a",
               
                )
        
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"),)
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table1.pack(fill="both",expand=1)
        # Inserting data in the table=======================


        try:
                cursor=db.cursor()
                cursor.execute(f"SELECT Student_Name, Father_Name,CNIC,Gender,Course,Fee_Status FROM admin")
                data=cursor.fetchall()
                for row in data:
                        Customer_table1.insert("","end",values=row)
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                         msg.showerror("Database Not Found","Please! Check the connection of database...........")
        def remove():
                for rows in Customer_table1.get_children():
                        Customer_table1.delete(rows)
        def refresh():
                for rows in Customer_table1.get_children():
                        Customer_table1.delete(rows)
                
                try:
                        cursor=db.cursor()
                        cursor.execute(f"SELECT Student_Name, Father_Name,CNIC,Gender,Course,Fee_Status FROM admin")
                        data=cursor.fetchall()
                        for row in data:
                                Customer_table1.insert("","end",values=row)
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                        mysql.connector.errors.ProgrammingError,
                        mysql.connector.errors.IntegrityError,
                        mysql.connector.errors.ConnectionTimeoutError,
                        ):
                             msg.showerror("Database Not Found","Please! Check the connection of database...........")
        def search():
                select_by=search_combo.get()
                user_search=search_ent.get().title().strip()
               
               
                match select_by:
                        case "Search By":
                               msg.showinfo("Select Search By","Please! Select option (Name, CNIC) to find the student information you are looking for.")
                
                        case "Name":
                                        # home_table_data=[Customer_table1.item(row,"values") for row in Customer_table1.get_children()]
                                        # print(home_table_data)
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select Student_Name, Father_Name,CNIC,Gender,Course,Fee_Status from admin where Student_Name=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table1.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "CNIC":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select Student_Name, Father_Name,CNIC,Gender,Course,Fee_Status from admin where CNIC=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table1.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
        def B_delete():
                selected=Customer_table1.selection()
                if selected:
                        qti=msg.askquestion("Delete!",f"Do you want to delete selected student data ?")
                        if qti=="yes":
                        
                                for item in selected:
                                     values= Customer_table1.item(item,"values")
                                val=list(values)
                                selected_cnic=val[2]
                                try:
                                        
                                        cursor=db.cursor()
                                        quarry="DELETE FROM admin WHERE CNIC=%s"
                                        cursor.execute(quarry,(selected_cnic,))                                                                                                                       
                                
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
    
                                
                                msg.showinfo("Admission canceled Successfully!",f"Registration Detail\n\n1.Name: {values[0]}\n2.Father`s Name: {values[1]}\n3.CNIC: {values[2]}\n4.Course: {values[3]}\n5.Fee Status: {values[4]}")
                                for item2 in selected:
                                   Customer_table1.delete(item2)
                        else:
                                 msg.showinfo("Not Selected!",f"Please! Select student data from given table for deleting.")

        def Challan():
                        def generate_challan(data_list,fee,roll_no):
                                data_list=list(data_list)
                                # fee=str(fee)
                                fee_50=float(fee)*50/100
                                fee_5=float(fee)*5/100
                                fee_15=float(fee)*15/100
                                fee_10=float(fee)*10/100
                                pdf = FPDF()
                                pdf.add_page()
                                pdf.image("images/CMIT.png", x=0, y=0, w=50)
                                
                                pdf.set_font("Times","B", size=30)
                                pdf.cell(200, 20, txt="CodeMasters Institute of Technology", ln=True, align='R')

                                
                                pdf.set_font("Times","B", size=24)
                                pdf.cell(200, 10, txt="Admission Challan", ln=True, align='C')
                                

                                pdf.set_font("Times", size=20, style='B')
                                pdf.cell(190, 10, txt="Student Information", border=1,ln=True, align='C')
                                # pdf.ln(5)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(50, 10, txt="Student Name", border=1, align='L')
                                pdf.set_font("Times", size=18,style="BI")
                                pdf.cell(140, 10, txt=data_list[0], border=1, align='L')
                                pdf.ln(10)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(50, 10, txt="Father's Name", border=1, align='L')
                                pdf.set_font("Times", size=18,style="BI")
                                pdf.cell(140, 10, txt=data_list[1], border=1, align='L')
                                pdf.ln(10)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(50, 10, txt="CNIC", border=1, align='L')
                                pdf.set_font("Times", size=18,style="BI")
                                pdf.cell(140, 10, txt=data_list[2], border=1, align='L')
                                pdf.ln(10)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(50, 10, txt="Gender", border=1, align='L')
                                pdf.set_font("Times", size=18,style="BI")
                                pdf.cell(140, 10, txt=data_list[3], border=1, align='L')
                                pdf.ln(10)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(50, 10, txt="Course", border=1, align='L')
                                pdf.set_font("Times", size=18,style="BI")
                                pdf.cell(140, 10, txt=data_list[4], border=1, align='L')
                                pdf.ln(10)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(50, 10, txt="Roll Number", border=1, align='L')
                                pdf.set_font("Times", size=18,style="BI")
                                pdf.cell(140, 10, txt=str(roll_no), border=1, align='L')
                                pdf.ln(10)

                                pdf.ln(10)
                                pdf.set_font("Times", size=20, style='B')
                                pdf.cell(95, 10, txt="Fee Details", border=1, align='C')
                                pdf.set_font("Times", size=20,style="B")
                                pdf.cell(95, 10, txt="Amount", border=1, align='C')
                                pdf.ln(10)

                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(95, 10, txt="Admission Fee", border=1, align='L')
                                pdf.set_font("Times", size=18, style='BI')
                                pdf.cell(95, 10, txt=str(float(fee_10)), border=1, align='R')
                                pdf.ln(10)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(95, 10, txt="Tuition Fee", border=1, align='L')
                                pdf.set_font("Times", size=18, style='BI')
                                pdf.cell(95, 10, txt=str(float(fee_50)), border=1, align='R')
                                pdf.ln(10)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(95, 10, txt="Library Fee", border=1, align='L')
                                pdf.set_font("Times", size=18, style='BI')
                                pdf.cell(95, 10, txt=str(float(fee_10)), border=1, align='R')
                                pdf.ln(10)

                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(95, 10, txt="Books Fee", border=1, align='L')
                                pdf.set_font("Times", size=18, style='BI')
                                pdf.cell(95, 10, txt=str(float(fee_15)), border=1, align='R')
                                pdf.ln(10)

                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(95, 10, txt="Exam Fee", border=1, align='L')
                                pdf.set_font("Times", size=18, style='BI')
                                pdf.cell(95, 10, txt=str(float(fee_10)), border=1, align='R')
                                pdf.ln(10)
                                pdf.set_font("Times", size=18,style="B")
                                pdf.cell(95, 10, txt="Other Fee", border=1, align='L')
                                pdf.set_font("Times", size=18, style='BI')
                                pdf.cell(95, 10, txt=str(fee_5), border=1, align='R')
                                pdf.ln(10)

                                pdf.set_font("Times", size=18, style='B')
                                pdf.cell(95, 10, txt="Total Fee", border=1, align='L')
                                pdf.set_font("Times", size=18,style="BI")

                                pdf.cell(95, 10, txt=str(float(fee)), border=1, align='R')
                                pdf.ln(10)
                                pdf.set_text_color(255,0,0)
                                pdf.set_font("Times", size=18, style='B')
                                pdf.cell(20, 10, txt="Note:",  align='L')
                                pdf.set_font("Times", size=16, style='B')
                                pdf.cell(95, 10, txt="Fee is Non Refundable / Non Transferable.",  align='C')

                                pdf.image("images/fee_status.png", x=3, y=243, w=50)
                                pdf.image("images/signature.png", x=150, y=250, w=60)
                                try:
                                     pdf.output(f"Generated Materrial/Challan_{data_list[2]}.pdf")
                                except:
                                         msg.showerror("Folder not found error","Please! Check the path of your 'Generated Matrrial' folder and try again.")
                                                
                        selected=Customer_table1.selection()
                        if selected:
                                qti=msg.askquestion("Generate Challan",f"Do you want to print challan of selected student?")
                                if qti=="yes":
                                        for item in selected:
                                               values= Customer_table1.item(item,"values")
                                        val=list(values)
                                        selected_cnic=val[2]
                                        selected_course=val[4]
                                        
                                        fee_dic={'SQL Database': 25000, 'Web Development': 45000, 'Python Development': 30000, 'Java Development': 30000, 'C++ Programming': 30000, 'C# Programming': 30000, 'PHP Web Development': 30000, 'Data Structures': 45000, 'Data Science': 105000, 'Machine Learning': 105000,"Cyber Security":105000}
                                        selected_fee=  fee_dic.get(selected_course) 
                                        try:
                                        
                                                        cursor=db.cursor()
                                                        quarry="select StudentId from admin where CNIC=%s"
                                                        cursor.execute(quarry,(selected_cnic,))  
                                                        data=cursor.fetchall()
                                                        for da in data:
                                                                for d in da:
                                                                        roll_no=d
                                                                                                                      
                                                        db.commit()
                                                        cursor.close() 
                                        except (mysql.connector.errors.OperationalError,
                                                                mysql.connector.errors.ProgrammingError,
                                                                mysql.connector.errors.IntegrityError,
                                                                mysql.connector.errors.ConnectionTimeoutError,
                                                                ):
                                                                     msg.showerror("Database Not Found","Please! Check the connection of database...........")
                                                      
                                        if val[-1]!="Paid":
                                                try:
                                        
                                                        cursor=db.cursor()
                                                        quarry="UPDATE admin SET Fee_Status='Paid' WHERE CNIC=%s"
                                                        cursor.execute(quarry,(selected_cnic,))                                                                                                                       
                                                        db.commit()
                                                        cursor.close() 
                                                except (mysql.connector.errors.OperationalError,
                                                                mysql.connector.errors.ProgrammingError,
                                                                mysql.connector.errors.IntegrityError,
                                                                mysql.connector.errors.ConnectionTimeoutError,
                                                                ):
                                                             msg.showerror("Database Not Found","Please! Check the connection of database...........")
                                                generate_challan(val,selected_fee,roll_no)
                                                refresh()
                                                msg.showinfo("Challan Generated Successfully!",f"Please! Check your challan with this name '{val[2]}.pdf' in 'Generated folder'")

                                        else:
                                                 msg.showerror("Paid Challan",f"Please! Select another student to print his challan this student has already paid challan...")

                                              
                                
                                        
                        else:
                                msg.showerror("Paid Challan",f"Please! Select another student to print his challan this student has already paid challan...")
                  
        # operations on table================================
        op_frame=cu.CTkFrame(big_frame,corner_radius=20)
        op_frame.grid(row=1,column=2,padx=80)
  

        # Search options=============
        search_lab=cu.CTkLabel(op_frame,text="Get Student`s Fee Slip",font=("Arial Rounded MT Bold",22,"bold"))
        search_lab.grid(row=0,column=0,pady=10,columnspan=2)
        search_ent=cu.CTkEntry(op_frame,placeholder_text="Search!🔍",width=250,font=("Cambria (Headings)", 20),corner_radius=30)
        search_ent.grid(row=1,column=0,pady=10,padx=10)
        search_combo=cu.CTkOptionMenu(op_frame,values=["Search By","Name","CNIC"],width=130,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        search_combo.grid(row=1,column=1,padx=20,pady=10,)

        #   Creating Buttons======================= 
        search_btn=cu.CTkButton(op_frame,text="Search🔎",corner_radius=100,font=("Cambria (Headings)",20),command=search)
        search_btn.grid(row=2,column=0,pady=10,)
        delete_btn=cu.CTkButton(op_frame,text="Delete❌",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#8D0707",command=B_delete)
        delete_btn.grid(row=2,column=1,pady=10,)
        refresh_btn=cu.CTkButton(op_frame,text="Refresh🔃",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=refresh)
        refresh_btn.grid(row=3,column=0,pady=10)
        fee_print_btn=cu.CTkButton(op_frame,text="Fee Slip📄",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#410A88",command= Challan)
        fee_print_btn.grid(row=3,column=1,pady=10)
        
        # Data insert area=================================
    





def view():

        # Making table area=================================================
        tb_frame=cu.CTkFrame(big_frame,corner_radius=20,height=250,width=1500)
        tb_frame.grid(row=1,column=1)
        table_frame = tk.Frame(tb_frame, bg="#000000", bd=2, relief="ridge")
        table_frame.place(x=5,y=10,width=1350,height=220,)
        scroll_x=tk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=tk.Scrollbar(table_frame,orient="vertical")
        col_names=("Rol","st_name","f_name","st_cnic","f_cnic","DOB","gen","prof","ph_no","add","course","adm_date","dur","pas_date")
        col_heading_names=("Roll NO","Student Name","Father`s Name","Student CNIC","Father`s CNIC","Date of Birth","Gender","Father`s Profession","Phone No","Address","Course","Admission Date","Course Duration","Passing Date")
        Customer_table=ttk.Treeview(table_frame,columns=(col_names),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="left",fill="y")
        scroll_x.config(command=Customer_table.xview)
        scroll_y.config(command=Customer_table.yview)
        for x,y in zip(col_names,col_heading_names):
              Customer_table.heading(x,text=y)
        Customer_table['show']='headings'

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                background="#313030",  
                fieldbackground="#363636", 
                foreground="#ffffff",   
                ) 
        style.configure("Treeview.Heading",
                background="#4a4a4a",
                #foreground="#FFFFFF",
                )
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"))
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table.pack(fill="both",expand=1)
        # Data insert area=================================
        try:
                cursor=db.cursor()
                quarry="SELECT * FROM admin where Fee_Status=%s"
                cursor.execute(quarry,("Paid",))
                data=cursor.fetchall()
                for row in data:
                        Customer_table.insert("","end",values=row)
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")

        def refresh():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
                
                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM admin where Fee_Status=%s"
                        cursor.execute(quarry,("Paid",))
                        data=cursor.fetchall()
                        for row in data:
                                Customer_table.insert("","end",values=row)
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
        def remove():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
        def search():
                select_by=search_combo.get()
                user_search=search_ent.get().title().strip()
               
               
                match select_by:
                        case "Search By":
                               msg.showinfo("Select Search By","Please! Select option (Name, CNIC) to find the student information you are looking for.")
                
                        case "Name":
                                        # home_table_data=[Customer_table1.item(row,"values") for row in Customer_table1.get_children()]
                                        # print(home_table_data)
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where Fee_Status='Paid' and Student_Name=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "CNIC":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where Fee_Status='Paid' and CNIC=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "Course":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from admin  where Fee_Status='Paid' and Course=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")


        def B_delete():
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Delete!",f"Do you want to delete selected student data ?")
                        if qti=="yes":
                        
                                for item in selected:
                                     values= Customer_table.item(item,"values")
                                val=list(values)
                                selected_cnic=val[3]
                                try:
                                        
                                        cursor=db.cursor()
                                        quarry="DELETE FROM admin WHERE CNIC=%s"
                                        cursor.execute(quarry,(selected_cnic,))                                                                                                                       
                                
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
    
                                
                                msg.showinfo("Admission canceled Successfully!",f"Registration Detail\n\n1.Name: {values[0]}\n2.Father`s Name: {values[1]}\n3.CNIC: {values[2]}\n4.Course: {values[3]}\n5.Fee Status: {values[4]}")
                                for item2 in selected:
                                   Customer_table.delete(item2)
                        else:
                                 msg.showinfo("Not Selected!",f"Please! Select student data from given table for deleting.")
        def Generate_Card():
                def gen_card(card_for,data_list):
                     
                        pdf = FPDF('P', 'mm', (89, 55)) 
                        pdf.add_page()
                        pdf.image(card_for, x=0, y=0, w=89, h=55)
                        pdf.set_font("Times", size=8)
                        pdf.set_xy(24, 18)
                        pdf.cell(27, 5, txt=str(data_list[0]), align='L')  # keep width small, align left
                        pdf.set_xy(24, 27)
                        pdf.cell(27, 0, txt=str(data_list[1]), align='L')
                        pdf.set_xy(24, 34)  
                        pdf.cell(20, 0, txt=str(data_list[2]), align='L')
                        pdf.set_xy(65, 11)
                        pdf.cell(27, 5, txt=str(data_list[3]), align='L')
                        pdf.output(f"Generated Materrial/ID_Card{data_list[1]}.pdf")

                        

                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Generate Student ID Card",f"Do you want to generate student ID Card of  selected student ?")
                        if qti=="yes":
                                for item in selected:
                                     values= Customer_table.item(item,"values")
                                val=list(values)
                                data_list_s=[val[1],val[3],val[10],val[0]]
                                selected_gender=val[5]
                                if selected_gender=="Female":
                                        gen_card("images/girl_card.png",data_list_s)
                                else:
                                        gen_card("images/boy_card.png",data_list_s)
                else:
                         msg.showinfo("Not Selected!",f"Please! Select student from given table for generating student ID Card!")
        
        def Generate_Certificate():
                def gen_certificate(data_list):
                        pdf = FPDF("L", "mm", "A4")  
                        pdf.add_page()
                        pdf.image("images/certi.png", x=0, y=0, w=300)

                        pdf.set_font("Times", size=30,style="B")
                        pdf.cell(280,175 , txt=str(data_list[0]),  align='C')
                        pdf.ln(10)
                        pdf.set_xy(100,60)
                        pdf.set_font("Times", size=14)
                        pdf.cell( 100,100, txt="has successfully completed 6-month skill development course of ",  align='C')
                                                                        
                        pdf.set_xy(100,70)
                        pdf.set_font("Times", size=20,style="B")
                        pdf.cell( 100,100, txt=f'"{data_list[1]}"',  align='C')
                        pdf.set_xy(100,77)
                        pdf.set_font("Times", size=14)
                        pdf.cell( 100,100, txt=f'from {data_list[2]} to {data_list[3]} at',  align='C')
                        pdf.set_xy(100,85)
                        pdf.set_font("Times", size=15,style="B")
                        pdf.cell( 100,100, txt='CodeMasters Institute of Technology',  align='C')
                        pdf.output(f"Generated Materrial/Certificate_of_{data_list[0]}.pdf")
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Generate Student Certificate",f"Do you want to generate Certificate of  selected student ?")
                        if qti=="yes":
                                for item in selected:
                                     values= Customer_table.item(item,"values")
                                val=list(values)
                                
                                passing_date=val[-2][0:10]
                                data_list_s=[val[1],val[10],val[-4],passing_date]
                                gen_certificate(data_list_s)
                                
                else:
                         msg.showinfo("Not Selected!",f"Please! Select student from given table for generating student Certificate")
        
                     








        op_frame=cu.CTkFrame(big_frame,corner_radius=20)
        op_frame.grid(row=10,column=1,pady=20)
  

        # Search options=============
        search_lab=cu.CTkLabel(op_frame,text="Get Student`s ID Card and Certificate",font=("Arial Rounded MT Bold",22,"bold"))
        search_lab.grid(row=0,column=0,pady=10,columnspan=2)
        search_ent=cu.CTkEntry(op_frame,placeholder_text="Search!🔍",width=250,font=("Cambria (Headings)", 20),corner_radius=30)
        search_ent.grid(row=1,column=0,pady=10,padx=10)
        search_combo=cu.CTkOptionMenu(op_frame,values=["Search By","Name","CNIC","Course"],width=200,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        search_combo.grid(row=1,column=1,padx=20,pady=10,)
        search_btn=cu.CTkButton(op_frame,text="Search🔎",corner_radius=100,font=("Cambria (Headings)",20),command=search)
        search_btn.grid(row=2,column=0,pady=10,ipadx=35)
        
        delete_btn=cu.CTkButton(op_frame,text="Delete❌",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#8D0707",command=B_delete)
        delete_btn.grid(row=2,column=1,pady=10,ipadx=28)
        refresh_btn=cu.CTkButton(op_frame,text="Refresh🔃",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=refresh)
        refresh_btn.grid(row=3,column=0,pady=10,ipadx=35)
        st_idcard_print_btn=cu.CTkButton(op_frame,text="Student ID Card",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#410A88",command=Generate_Card)
        st_idcard_print_btn.grid(row=3,column=1,pady=10,ipadx=10)
        st_certi_print_btn=cu.CTkButton(op_frame,text="Student Certificate",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#410A88",command=Generate_Certificate)
        st_certi_print_btn.grid(row=4,column=0,pady=10,ipadx=10,columnspan=3)





Windows=cu.CTk()
Windows.title("CodeMasters Institute of Technology")
Windows.geometry("1500x650")
tabs_frame=cu.CTkFrame(Windows)
tabs_frame.pack(pady=20)
big_frame=cu.CTkFrame(Windows,width=1300,height=600,corner_radius=20,)
big_frame.pack(pady=20,fill="both",expand=1)


home()

home_tab=cu.CTkButton(tabs_frame,text="Home",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("Home"))
home_tab.grid(row=0,column=0,padx=10)
register_tab=cu.CTkButton(tabs_frame,text="Registration",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("Registration"))
register_tab.grid(row=0,column=1,padx=10)
view_tab=cu.CTkButton(tabs_frame,text="View",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("View"))
view_tab.grid(row=0,column=2,padx=10)

Windows.mainloop()






















































































































































































































































































































































    # if switch_to=="Home":
    #     home_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ============
    #     register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     setting_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    
    
    # elif switch_option=="Registration":
    #     register_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ================
    #     home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     setting_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    
    # elif switch_option=="View":
    #     view_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ===============
    #     home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     setting_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

    
    # elif switch_option=="Setting":
    #     setting_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # =================
    #     home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

