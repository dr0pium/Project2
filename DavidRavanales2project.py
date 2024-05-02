import tkinter as tk
import tkinter.messagebox as mb
import json
from typing import List, Tuple

class GradeCalculator:
    def __init__(self):
        """Initialize the grade calculator."""
        self.create_student_selection_gui()

    def create_student_selection_gui(self) -> None:
        """Create the GUI for student number selection."""
        self.root = tk.Tk()
        label = tk.Label(self.root, text="Enter the number of students: ")
        self.entry = tk.Entry(self.root)
        button = tk.Button(self.root, text="Submit", command=self.validate_input)
        label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        button.grid(row=1, column=0, columnspan=2)
        self.root.mainloop()

    def validate_input(self) -> None:
        """Validate the input for number of students."""
        try:
            self.num_students = int(self.entry.get())
            if self.num_students <= 0:
                raise ValueError
            self.create_gui()
        except ValueError:
            mb.showerror("Invalid Input", "Please enter a positive integer.")
            self.entry.delete(0, 'end')

    def create_gui(self) -> None:
        """Create the GUI."""
        self.root.destroy()
        self.root = tk.Tk()
        self.entries = []
        self.labels = []
        for i in range(self.num_students):
            label = tk.Label(self.root, text=f"Student {i+1}: ")
            entry = tk.Entry(self.root)
            grade_label = tk.Label(self.root, text="")
            label.grid(row=i, column=0)
            entry.grid(row=i, column=1)
            grade_label.grid(row=i, column=2)
            self.entries.append(entry)
            self.labels.append(grade_label)
        calculate_button = tk.Button(self.root, text="Calculate Grades", command=self.calculate_grades)
        calculate_button.grid(row=self.num_students, column=0, columnspan=2)
        save_button = tk.Button(self.root, text="Save Data", command=self.save_data)
        save_button.grid(row=self.num_students+1, column=0, columnspan=2)

    def calculate_grades(self) -> None:
        """Calculate the grades based on the input."""
        scores = []
        for i in range(self.num_students):
            try:
                score = float(self.entries[i].get())
                if score < 0 or score > 100:
                    raise ValueError
                scores.append(score)
            except ValueError:
                mb.showerror("Invalid Input", f"Please enter a valid grade for Student {i+1}.")
                self.entries[i].delete(0, 'end')

        best_score = max(scores) if scores else 0
        grades = []
        for i, score in enumerate(scores):
            if score >= best_score - 10:
                grade = "A"
            elif score >= best_score - 20:
                grade = "B"
            elif score >= best_score - 30:
                grade = "C"
            elif score >= best_score - 40:
                grade = "D"
            else:
                grade = "F"
            grades.append((i+1, score, grade))
            self.labels[i].config(text=grade)

    def save_data(self) -> None:
        """Save the student data to a file."""
        data = {f"Student {i+1}": self.entries[i].get() for i in range(self.num_students)}
        with open("student_data.json", "w") as f:
            json.dump(data, f)

def main():
    """Main function to start the program."""
    GradeCalculator()

if __name__ == "__main__":
    main()