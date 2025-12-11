import json
import os
from datetime import datetime

class SimpleStudentSystem:
    def __init__(self, file_name="student_results.json"):
        self.file_name = file_name
        self.data = self.load_file()
    
    def load_file(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_file(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(f"\n✓ Data saved to {self.file_name}")
    
    def calc_percent(self, marks_dict, total_possible):
        return (sum(marks_dict.values()) / total_possible) * 100
    
    def calc_grade(self, percent):
        if percent >= 90:
            return 'A+'
        elif percent >= 80:
            return 'A'
        elif percent >= 70:
            return 'B'
        elif percent >= 60:
            return 'C'
        elif percent >= 50:
            return 'D'
        else:
            return 'F'
    
    def add_marks_for_student(self):
        print("\n" + "="*50)
        print("ADD STUDENT MARKS")
        print("="*50)
        
        stud_id = input("Enter Student ID: ").strip()
        stud_name = input("Enter Student Name: ").strip()
        
        if not stud_id or not stud_name:
            print("✗ Student ID and Name cannot be empty!")
            return
        
        print("\nEnter marks for subjects (enter subject name and marks)")
        print("Type 'done' when finished")
        
        marks_dict = {}
        while True:
            subject_name = input("\nSubject name (or 'done'): ").strip()
            if subject_name.lower() == 'done':
                break
            
            if not subject_name:
                print("✗ Subject name cannot be empty!")
                continue
            
            try:
                mark_val = float(input(f"Marks for {subject_name}: "))
                if mark_val < 0:
                    print("✗ Marks cannot be negative!")
                    continue
                marks_dict[subject_name] = mark_val
            except ValueError:
                print("✗ Invalid marks! Please enter a number.")
        
        if not marks_dict:
            print("✗ No marks entered!")
            return
        
        total_obtained = sum(marks_dict.values())
        max_total = len(marks_dict) * 100
        percent = self.calc_percent(marks_dict, max_total)
        grade_val = self.calc_grade(percent)
        
        self.data[stud_id] = {
            'name': stud_name,
            'marks': marks_dict,
            'total_marks': total_obtained,
            'max_marks': max_total,
            'percentage': round(percent, 2),
            'grade': grade_val,
            'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print("\n" + "-"*50)
        print("✓ Student marks added successfully!")
        print(f"Student: {stud_name} (ID: {stud_id})")
        print(f"Total Marks: {total_obtained}/{max_total}")
        print(f"Percentage: {percent:.2f}%")
        print(f"Grade: {grade_val}")
        print("-"*50)
    
    def show_student_result(self):
        print("\n" + "="*50)
        print("VIEW STUDENT RESULT")
        print("="*50)
        
        if not self.data:
            print("✗ No students found in the system!")
            return
        
        stud_id = input("Enter Student ID: ").strip()
        
        if stud_id not in self.data:
            print(f"✗ Student with ID '{stud_id}' not found!")
            return
        
        record = self.data[stud_id]
        
        print("\n" + "-"*50)
        print(f"Student ID: {stud_id}")
        print(f"Name: {record['name']}")
        print(f"Date Added: {record['date_added']}")
        print("\nSubject-wise Marks:")
        print("-"*50)
        
        for subject, mark in record['marks'].items():
            print(f"  {subject:<30} {mark:>6.2f}/100")
        
        print("-"*50)
        print(f"Total Marks: {record['total_marks']}/{record['max_marks']}")
        print(f"Percentage: {record['percentage']}%")
        print(f"Grade: {record['grade']}")
        print("-"*50)
    
    def show_all_students(self):
        print("\n" + "="*50)
        print("ALL STUDENTS RESULTS")
        print("="*50)
        
        if not self.data:
            print("✗ No students found in the system!")
            return
        
        print(f"\n{'ID':<10} {'Name':<20} {'Percentage':<12} {'Grade':<6}")
        print("-"*50)
        
        for stud_id, rec in self.data.items():
            print(f"{stud_id:<10} {rec['name']:<20} {rec['percentage']:<12.2f} {rec['grade']:<6}")
        
        print("-"*50)
        print(f"Total Students: {len(self.data)}")
    
    def delete_student_record(self):
        print("\n" + "="*50)
        print("DELETE STUDENT RECORD")
        print("="*50)
        
        if not self.data:
            print("✗ No students found in the system!")
            return
        
        stud_id = input("Enter Student ID to delete: ").strip()
        
        if stud_id not in self.data:
            print(f"✗ Student with ID '{stud_id}' not found!")
            return
        
        stud_name = self.data[stud_id]['name']
        confirm = input(f"Are you sure you want to delete {stud_name}? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            del self.data[stud_id]
            print(f"✓ Student {stud_name} deleted successfully!")
        else:
            print("✗ Deletion cancelled.")
    
    def start(self):
        while True:
            print("\n" + "="*50)
            print("STUDENT RESULT MANAGEMENT SYSTEM")
            print("="*50)
            print("1. Add Student Marks")
            print("2. View Student Result")
            print("3. View All Students")
            print("4. Delete Student Record")
            print("5. Save Data to File")
            print("6. Exit")
            print("="*50)
            
            user_choice = input("Enter your choice (1-6): ").strip()
            
            if user_choice == '1':
                self.add_marks_for_student()
            elif user_choice == '2':
                self.show_student_result()
            elif user_choice == '3':
                self.show_all_students()
            elif user_choice == '4':
                self.delete_student_record()
            elif user_choice == '5':
                self.save_file()
            elif user_choice == '6':
                print("\nSaving data before exit...")
                self.save_file()
                print("Thank you for using Student Result Management System!")
                print("Goodbye!\n")
                break
            else:
                print("✗ Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    app = SimpleStudentSystem()
    app.start()
