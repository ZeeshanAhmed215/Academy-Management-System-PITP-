# import tkinter as tk
# from tkcalendar import DateEntry

# root = tk.Tk()
# root.title("DOB Form Example")

# tk.Label(root, text="Enter Your DOB:").pack(pady=5)

# dob_entry = DateEntry(root, width=12, background="#7D87A7",
#                       foreground="#000000", borderwidth=10, year=2000, date_pattern="dd-mm-yyyy")
# dob_entry.pack(pady=5)

# def submit():
#     dob = dob_entry.get_date()   # returns datetime.date
#     result_label.config(text=f"Your DOB is: {dob.strftime('%d-%m-%Y')}")

# tk.Button(root, text="Submit", command=submit).pack(pady=10)

# result_label = tk.Label(root, text="")
# result_label.pack()

# root.mainloop()
# import customtkinter
# from tkinter import ttk

# app = customtkinter.CTk()
# app.geometry("400x300")

# # Define a custom style
# style = ttk.Style()

# # Configure the 'Treeview' and 'Treeview.Heading' styles
# style.configure("Treeview",
#                 background="#333333",  # Background color of the entire widget
#                 foreground="white",    # Default text color
#                 fieldbackground="#333333", # Background color for the data area
#                 rowheight=25,
#                 bordercolor="#555555" # border color
#                 )

# # Change the selection color (requires mapping)
# style.map('Treeview',
#           background=[('selected', '#0078d7')], # Highlight color when selected
#           foreground=[('selected', 'white')]
#           )

# # Headings styling
# style.configure("Treeview.Heading",
#                 background="#555555",
#                 foreground="white",
#                 font=("Arial", 10, "bold")
#                 )
# style.map("Treeview.Heading",
#           background=[('active', '#666666')] # Color when heading is active (hovered)
#           )

# tree = ttk.Treeview(app, columns=('Name', 'Size'), show='headings')
# tree.pack(fill="both", expand=True, padx=10, pady=10)

# tree.heading('Name', text='File Name')
# tree.heading('Size', text='Size (bytes)')

# # Insert some data
# tree.insert('', 'end', values=('file1.txt', '850 bytes'))
# tree.insert('', 'end', values=('file2.txt', '1200 bytes'))

# app.mainloop()




# from CTkTreeview import CTkTreeview
# import customtkinter

# app = customtkinter.CTk()

# tree = CTkTreeview(app, columns=["First", "Last", "Age"], show="headings",
#                    header_fg_color="blue",
#                    fg_color=["#D3D3D3", "#404040"], # Use different colors for light/dark mode
#                    bg_color="transparent",
#                    text_color="white",
#                    hover_color="green")

# tree.pack(fill="both", expand=True)

# # Example of changing a specific row's color
# tree.insert("", "end", values=("John", "Doe", "30"), tags=("my_color_tag",))
# tree.tag_configure("my_color_tag", background="red")

# app.mainloop()



import customtkinter 
from tkinter import ttk

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.title("Styled Treeview")
app.geometry("400x300")

# 1. Create a Style object
style = ttk.Style(app)

# 2. Set the theme to "clam" (most flexible for styling)
style.theme_use("clam")

# 3. Configure the "Treeview" style
style.configure("Treeview",
                background="#2a2a2a",  # Row background color
                fieldbackground="#2a2a2a", # Background color of the unused area
                foreground="white",    # Text color
                rowheight=25)          # Optional: adjust row height

# Optional: Change selected item color
style.map('Treeview', background=[('selected', '#5a5a5a')])

# Create the Treeview widget
tree = ttk.Treeview(app, columns=('Name', 'Size'), show='headings', style="Treeview")
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Configure headings (headings have separate styling)
style.configure("Treeview.Heading",
                background="#4a4a4a",
                foreground="#FFFFFF",
                font=("Arial", 10, "bold"))
tree.heading('Name', text='File Name')
tree.heading('Size', text='Size (bytes)')

# Insert some data
tree.insert('', 'end', text='Folder A', values=('850 bytes'))
tree.insert('', 'end', text='Folder B', values=('1200 bytes'))

app.mainloop()



