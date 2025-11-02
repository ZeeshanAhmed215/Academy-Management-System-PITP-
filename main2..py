import  tkinter as tk
import customtkinter as cu
from tkinter import ttk
from PIL import Image
cu.set_appearance_mode("dark")
cu.set_default_color_theme("dark-blue")

def switch_option(switch_to):
    match switch_to:
        case "Home":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                home_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ============
                register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

                home()
        case "Registration":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                
                register_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ================
                home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

                registration()
        case "View":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                view_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ===============
                home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

                view()
              

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
              course_list=["Select Course","Class KG","Class One","Class Two","Class Three","Class Four","Class Five","Class Six","Class Seven","Class Eight","Class IX","Class X","Class XI  Pre-Medical","Class XI  Pre-Engineering","Class XII  Pre-Medical","Class XII  Pre-Engineering","Mathematics Specialist","Essential Mathematics","Entry Level Mathematics","Entry Level English","Essential English","English Specialist"]
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
#             Button of register=====================

              register_btn=cu.CTkButton(page_frame,text="Register!",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#1F6AA5",)
              register_btn.grid(row=6,column=0,padx=10,ipadx=20,columnspan=10,pady=50)
        #        Image Books======================
              book_image=cu.CTkImage(dark_image=Image.open("images/fill_ph.png"),light_image=Image.open("images/fill_ph.png"),size=(350,350))

              image_label=cu.CTkLabel(big_frame,text="",image=book_image)
              image_label.grid(row=1,column=2)

def home():

        # Making table area=================================================
        tb_frame=cu.CTkFrame(big_frame,corner_radius=20,height=250,width=1000)
        tb_frame.grid(row=1,column=1)
        table_frame = tk.Frame(tb_frame, bg="#000000", bd=2, relief="ridge")
        table_frame.place(x=5,y=10,width=1000,height=220,)
        scroll_x_bottom=tk.Scrollbar(table_frame,orient="horizontal")
        scroll_x_top=tk.Scrollbar(table_frame,orient="horizontal")
        scroll_y_left=tk.Scrollbar(table_frame,orient="vertical")
        scroll_y_right=tk.Scrollbar(table_frame,orient="vertical")
        col_names=("st_name","f_name","st_cnic","gen","fee_status")
        col_heading_names=("Student Name","Father`s Name","CNIC","Gender","Fees Status")
        Customer_table=ttk.Treeview(table_frame,columns=(col_names),xscrollcommand=scroll_x_bottom.set and scroll_x_top,yscrollcommand=scroll_y_left.set and scroll_y_right.set)
        scroll_x_bottom.pack(side="bottom",fill="x")
        scroll_x_top.pack(side="top",fill="x")
        scroll_y_left.pack(side="left",fill="y")
        scroll_y_right.pack(side="right",fill="y")
        scroll_x_bottom.config(command=Customer_table.xview)
        scroll_x_top.config(command=Customer_table.xview)
        scroll_y_left.config(command=Customer_table.yview)
        scroll_y_right.config(command=Customer_table.yview)
        for x,y in zip(col_names,col_heading_names):
              Customer_table.heading(x,text=y)
        Customer_table['show']='headings'

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"))
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table.pack(fill="both",expand=1)
        # Data insert area=================================
        for i in range(100):
                Customer_table.insert("","end",values=i)
        c=(1,2,3,4,5,6,"jjjjjjjjjjjjjjkkkkkkkk")
        Customer_table.insert("","end",values=c)

#        head_lab=cu.CTkLabel(wig_frame,text="The Strive Educational Academy",font=("Edwardian Script ITC", 90, "bold"))
#        head_lab.grid(row=0,column=0)
       




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
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"))
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table.pack(fill="both",expand=1)
        # Data insert area=================================
        for i in range(100):
                Customer_table.insert("","end",values=i)
        c=(1,2,3,4,5,6,"jjjjjjjjjjjjjjkkkkkkkk")
        Customer_table.insert("","end",values=c)
        # Data operating area===============================
        # sp_frame=cu.CTkFrame(big_frame,corner_radius=20)
        # sp_frame.grid(row=1,column=1,pady=20,padx=50)
        op_frame=cu.CTkFrame(big_frame,corner_radius=20)
        op_frame.grid(row=10,column=1,pady=20,padx=50)
        search_ent=cu.CTkEntry(op_frame,placeholder_text="Search!🔍",width=250,font=("Cambria (Headings)", 20),corner_radius=30)
        search_ent.grid(row=1,column=1,padx=15,pady=5)
        register_btn=cu.CTkButton(op_frame,text="🔍🔎",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#1F6AA5",)
        register_btn.grid(row=1,column=2,)
        gen_combo=cu.CTkOptionMenu(op_frame,values=["Search By","Name","Roll No","CNIC"],width=130,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        gen_combo.grid(row=1,column=3,pady=10,padx=5)








Windows=cu.CTk()
tabs_frame=cu.CTkFrame(Windows)
tabs_frame.pack(pady=20)

big_frame=cu.CTkFrame(Windows,width=1300,height=600,corner_radius=20,)
big_frame.pack(pady=20,fill="both",expand=1)

# image_frame=cu.CTkFrame(big_frame,width=1300,height=600,corner_radius=20,)
# image_frame.grid(row=1,column=2,padx=90)



home()




Windows.title("The Strive Educational Academy")
home_tab=cu.CTkButton(tabs_frame,text="Home",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("Home"))
home_tab.grid(row=0,column=0,padx=10)

register_tab=cu.CTkButton(tabs_frame,text="Registration",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("Registration"))
register_tab.grid(row=0,column=1,padx=10)

view_tab=cu.CTkButton(tabs_frame,text="View",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("View"))
view_tab.grid(row=0,column=2,padx=10)

# setting_tab=cu.CTkButton(tabs_frame,text="Setting",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("Setting"))
# setting_tab.grid(row=0,column=3,padx=10)
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

