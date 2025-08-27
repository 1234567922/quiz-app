import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("light")


answer =  [
    {"question": "Capital of France?", "options": ["Berlin", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "5 x 6 =", "options": ["30", "36", "25"], "answer": "30"},
    {"question": "Largest ocean?", "options": ["Atlantic", "Indian", "Pacific"], "answer": "Pacific"},
 
    {"question": "Capital of France?", "options": ["Berlin", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "5 x 6 =", "options": ["30", "36", "25"], "answer": "30"},
    {"question": "Largest ocean?", "options": ["Atlantic", "Indian", "Pacific"], "answer": "Pacific"},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "Thailand"], "answer": "Japan"},
    {"question": "What is the tallest mountain in the world?", "options": ["K2", "Mount Everest", "Kangchenjunga"], "answer": "Mount Everest"},
    {"question": "Which planet has the most moons?", "options": ["Saturn", "Jupiter", "Mars"], "answer": "Saturn"},
    {"question": "What gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen"], "answer": "Carbon Dioxide"},
    {"question": "Smallest bones in the body are found in the?", "options": ["Ear", "Hand", "Foot"], "answer": "Ear"},
    {"question": "H2O is?", "options": ["Salt", "Water", "Hydrogen"], "answer": "Water"},
    {"question": "Square root of 64?", "options": ["6", "8", "10"], "answer": "8"},
    {"question": "12 x 11?", "options": ["121", "132", "144"], "answer": "132"},
    {"question": "Which number is prime?", "options": ["9", "15", "13"], "answer": "13"},
    {"question": "Dark Knight is?", "options": ["Superman", "Batman", "Iron Man"], "answer": "Batman"},
    {"question": "Game with creepers?", "options": ["Minecraft", "Fortnite", "Roblox"], "answer": "Minecraft"},
    {"question": "Ship called Titanic appears in?", "options": ["Titanic", "Poseidon", "The Perfect Storm"], "answer": "Titanic"},
    {"question": "First US President?", "options": ["Lincoln", "Washington", "Jefferson"], "answer": "Washington"},
    {"question": "WWII ended in?", "options": ["1945", "1939", "1950"], "answer": "1945"},
    {"question": "Who discovered gravity?", "options": ["Einstein", "Newton", "Galileo"], "answer": "Newton"},
    {"question": "Fastest land animal?", "options": ["Lion", "Cheetah", "Horse"], "answer": "Cheetah"},]
    
class QuizApp(ctk.CTk):
    def __init__(app):
        super().__init__()
        app.title("🧠 Quiz Master")
        app.geometry("600x500")
        app.resizable(False, False)

        app.q_index = 0
        app.score = 0

        # Frames
        app.top_frame = ctk.CTkFrame(app, fg_color="dimgrey", height=80)
        app.top_frame.pack(fill="x", pady=5)

        app.middle_frame = ctk.CTkFrame(app, fg_color="dimgrey")
        app.middle_frame.pack(fill="both", expand=True)

        app.bottom_frame = ctk.CTkFrame(app, fg_color="dimgrey", height=100)
        app.bottom_frame.pack(fill="x")

        # Top Frame Content
        app.title_label = ctk.CTkLabel(app.top_frame, text="Quiz App", font=("Cascadia Code", 22, "bold"), text_color="white")
        app.title_label.pack(pady=20)

        # Middle Frame Content
        app.answer_label = ctk.CTkLabel(app.middle_frame, text="", font=("Arial", 18), )
        app.answer_label.pack(pady=30)

        app.option_buttons = []
        for i in range(3):
            btn = ctk.CTkButton(app.middle_frame, text="", command=lambda i=i: app.check_answer(i))
            btn.pack(pady=10)
            app.option_buttons.append(btn)

        # Bottom Frame Content
        app.status_label = ctk.CTkLabel(app.bottom_frame, text="Score: 0", font=("Arial", 16), text_color="white")
        app.status_label.pack(pady=20)

        app.load_answer()

    def load_answer(app):
        q = answer[app.q_index]
        app.answer_label.configure(text=q["question"])
        for i, opt in enumerate(q["options"]):
            app.option_buttons[i].configure(text=opt)

    def check_answer(app, index):
        selected = app.option_buttons[index].cget("text")
        correct = answer[app.q_index]["answer"]
        if selected == correct:
            app.score += 1
        app.q_index += 1
        app.status_label.configure(text=f"Score: {app.score}")
        if app.q_index < len(answer):
            app.load_answer()
        else:
           messagebox.showinfo("Quiz Finished", f"You scored {app.score} out of {len(answer)}!")(
        app.quit())

app = QuizApp()
app.mainloop()