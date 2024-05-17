import csv
import os
from datetime import datetime

class AttendanceTracker:
    def __init__(self, student_file='students.csv', attendance_file='attendance.csv'):
        self.student_file = student_file
        self.attendance_file = attendance_file
        self.student_fields = ['Student ID', 'Name']
        self.attendance_fields = ['Student ID', 'Name', 'Date', 'Present']

        # Create the student file with headers if it doesn't exist
        if not os.path.exists(self.student_file):
            with open(self.student_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.student_fields)
                writer.writeheader()
        
        # Create the attendance file with headers if it doesn't exist
        if not os.path.exists(self.attendance_file):
            with open(self.attendance_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.attendance_fields)
                writer.writeheader()

    def add_student(self, student_id, name):
        with open(self.student_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.student_fields)
            writer.writerow({'Student ID': student_id, 'Name': name})
        print(f"Student {name} added.")

    def mark_attendance(self, student_id, present=True):
        date_str = datetime.now().strftime('%Y-%m-%d')
        student_name = None
        
        # Check if student exists
        with open(self.student_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Student ID'] == student_id:
                    student_name = row['Name']
                    break
        
        if not student_name:
            print(f"No student found with ID {student_id}.")
            return

        # Add attendance record
        with open(self.attendance_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.attendance_fields)
            writer.writerow({'Student ID': student_id, 'Name': student_name, 'Date': date_str, 'Present': 'Yes' if present else 'No'})
        print(f"Attendance marked for student ID {student_id} ({student_name}) on {date_str}.")

    def view_attendance(self):
        with open(self.attendance_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)

if __name__=='__main__':
    tracker = AttendanceTracker()
    
    # Example usage:
    # Add students
    tracker.add_student('1', 'Alice')
    tracker.add_student('2', 'Bob')
    
    # Mark attendance
    tracker.mark_attendance('1', present=True)
    tracker.mark_attendance('2', present=False)
    
    # View attendance
    tracker.view_attendance()