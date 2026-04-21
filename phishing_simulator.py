import tkinter as tk
from tkinter import messagebox

# Email dataset
emails = [
    {"subject": "Urgent: Verify Your Bank Account", "is_phishing": True},
    {"subject": "Project Meeting at 10 AM", "is_phishing": False},
    {"subject": "Reset Your Password Now!", "is_phishing": True},
    {"subject": "Happy Birthday! ", "is_phishing": False},
    {"subject": "You have won the lottery", "is_phishing": True}
]

class PhishingSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Awareness Simulator")
        self.root.geometry("500x350")

        self.index = 0
        self.score = 0
        self.results = []

        self.label = tk.Label(root, text="", font=("Arial", 16), wraplength=450)
        self.label.pack(pady=40)

        tk.Button(root, text="Mark as Phishing", width=20,
                  command=lambda: self.check(True)).pack(pady=5)

        tk.Button(root, text="Mark as Safe", width=20,
                  command=lambda: self.check(False)).pack(pady=5)

        self.load_email()

    def load_email(self):
        if self.index < len(emails):
            self.label.config(text=f"Email: {emails[self.index]['subject']}")
        else:
            self.show_report()

    def check(self, choice):
        correct = emails[self.index]["is_phishing"]

        if choice == correct:
            self.score += 1
            result = "Correct"
        else:
            result = "Wrong"

        self.results.append({
            "email": emails[self.index]["subject"],
            "result": result
        })

        self.index += 1
        self.load_email()

    def show_report(self):
        report = f"Score: {self.score}/{len(emails)}\n\nDetails:\n"
        for r in self.results:
            report += f"{r['email']} → {r['result']}\n"

        messagebox.showinfo("Report", report)
        self.root.quit()

# Run app
root = tk.Tk()
app = PhishingSimulator(root)
root.mainloop()
