
---

# 📚 **Academy Management System – PITP**

A **CustomerTkinter-based Desktop Application** for educational institutes to manage student data and generate official documents including **Challans, ID Cards, and Course Certificates** in PDF format.

---

## ✅ **Features**

### 🎓 **Student Management**

* Add, update, and manage student records
* Store student details such as personal info, course info, fee details, and more

### 🧾 **PDF Document Generation**

* **Student Challan Generator**

  * Automatically generates student fee challans
  * Customizable fields (fee amount, due date, student info)
  * Exports clean and professional PDF documents

* **Student ID Card Generator**

  * Creates official-looking student ID cards
  * Includes Name, ID, batch, department
  * Saves output as PDF

* **Student Course Certificate Generator**

  * Generates course completion certificates
  * Includes institute name, student name, course title, and signatures
  * Output as high-quality printable PDF

### 🖥 **Modern CustomTkinter GUI**

* Built with **CustomTkinter** for a modern look
* Dark/light mode theme
* User-friendly interface for administrators
* Organized menus and multi-window structure

---

## 🛠 **Technologies Used**

* **Python**
* **CustomTkinter (Modern UI)**
* **FPDF (PDF Generation)**
* **MySQL** Data storage

---


## 🚀 **How to Run the Academy Management System**

Follow these steps to properly set up and run the application.

---

## **1️⃣ Create the MySQL Database**

Open **MySQL Workbench / XAMPP phpMyAdmin / Terminal** and create a new database:

```sql
CREATE DATABASE academy_management;
```

---

## **2️⃣ Create Required Table**

After creating the database, run this SQL command to create the **admin** table:

```sql
CREATE TABLE admin (
    StudentId INT AUTO_INCREMENT PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL,
    Father_Name VARCHAR(100) NOT NULL,
    CNIC VARCHAR(100) UNIQUE NOT NULL,
    Father_CNIC VARCHAR(100) UNIQUE NOT NULL,
    Gender VARCHAR(100) NOT NULL,
    DOB VARCHAR(100) NOT NULL,
    Phone VARCHAR(100) NOT NULL,
    Address VARCHAR(300) NOT NULL,
    Father_pro VARCHAR(100) NOT NULL,
    Course VARCHAR(100) NOT NULL,
    Admission_Date VARCHAR(100) NOT NULL,
    Course_Duration VARCHAR(100) NOT NULL,
    Passing_Date VARCHAR(100) NOT NULL,
    Fee_Status VARCHAR(100) NOT NULL
);
```

---

## **3️⃣ Connect Your MySQL Database to the App**

In your project, open your database connection file (like `db.py`, `connection.py`, or wherever you handled DB).

Update your credentials:

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="academy_management"
)
```



---

## **4️⃣ Install Required Python Libraries**

Run these commands in terminal:

```bash
pip install customtkinter
pip install pillow
pip install fpdf
pip install mysql-connector-python
```

---

## **5️⃣ Run the Application**

After installing the requirements, run:

```bash
main.py
``
---

## 📄 **Generated PDFs**

This system automatically generates:

| Document Type      | Format | Description                            |
| ------------------ | ------ | -------------------------------------- |
| Student Challan    | PDF    | Fee challan with institute details     |
| Student ID Card    | PDF    | Printable ID card (single or batch)    |
| Course Certificate | PDF    | Official course completion certificate |

---

## 🎨 **UI Preview**

*(Add screenshots here if available)*

* Modern CustomTkinter Windows
* Regeisteration Form
* Challan Preview
* ID Card Template
* Certificate Template

---

## 🤝 **Contributions**

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

---

## 📌 **Future Improvements**


* QR code on ID cards
* Attendance management module
* Export/Import student data (CSV/Excel)

---




