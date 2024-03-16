import customtkinter as ctk
from tkinter import *
import pandas as pd
from datetime import datetime

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Marking System")
        self.root.geometry("600x400")

        # Variables to store class name, student name, and attendance status
        self.class_name = StringVar()
        self.student_name = StringVar()
        self.attendance_status = StringVar()
        self.attendance_status.set("Present")  # Default value

        # Class name entry
        ctk.CTkLabel(self.root, text="Class Name:", font=("Arial", 12)).pack(pady=5)
        self.class_entry = ctk.CTkEntry(self.root, textvariable=self.class_name, font=("Arial", 12))
        self.class_entry.pack(pady=5)

        # Student name entry
        ctk.CTkLabel(self.root, text="Student Name:", font=("Arial", 12)).pack(pady=5)
        self.student_entry = ctk.CTkEntry(self.root, textvariable=self.student_name, font=("Arial", 12))
        self.student_entry.pack(pady=5)

        # Attendance status selection
        ctk.CTkLabel(self.root, text="Attendance Status:", font=("Arial", 12)).pack(pady=5)
        self.status_combobox = ctk.CTkCombobox(self.root, textvariable=self.attendance_status, font=("Arial", 12))
        self.status_combobox['values'] = ("Present", "Absent")
        self.status_combobox.pack(pady=5)

        # Mark Attendance button
        self.mark_button = ctk.CTkButton(self.root, text="Mark Attendance", command=self.mark_attendance, font=("Arial", 12))
        self.mark_button.pack(pady=10)

        # Done button to export data to Excel
        self.done_button = ctk.CTkButton(self.root, text="Done", command=self.export_to_excel, font=("Arial", 12))
        self.done_button.pack(pady=10)

    def mark_attendance(self):
        class_name = self.class_name.get()
        student_name = self.student_name.get()
        attendance_status = self.attendance_status.get()
        
        # Perform attendance marking here (can be customized)
        print(f"Attendance marked for {student_name} in class {class_name}. Status: {attendance_status}")

    def export_to_excel(self):
        class_name = self.class_name.get()
        student_name = self.student_name.get()
        attendance_status = self.attendance_status.get()
        
        # Export data to Excel (create DataFrame and save to Excel)
        data = {'Class Name': [class_name],
                'Student Name': [student_name],
                'Attendance Status': [attendance_status],
                'Timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
        
        df = pd.DataFrame(data)
        df.to_excel('attendance.xlsx', index=False)
        print("Data exported to Excel.")

if __name__ == "__main__":
    root = Tk()
    app = AttendanceSystem(root)
    root.mainloop()
