import tkinter as tk
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
        button = tk.Button(self.root, text="Submit", command=self.create_gui)
        label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        button.grid(row=1, column=0, columnspan=2)
        self.root.mainloop()

    def create_gui(self) -> None:
        """Create the GUI."""
        self.num_students = int(self.entry.get())
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
        button = tk.Button(self.root, text="Calculate Grades", command=self.calculate_grades)
        button.grid(row=self.num_students, column=0, columnspan=2)
        self.root.mainloop()

    def calculate_grades(self) -> None:
        """Calculate grades based on the scores."""
        scores = [int(entry.get()) for entry in self.entries]
        best_score = max(scores)
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
            self.labels[i].config(text=grade)

if __name__ == "__main__":
    calculator = GradeCalculator()  # Create an instance of the class