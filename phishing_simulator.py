import tkinter as tk
from tkinter import messagebox
import winsound

scenarios = [
    {
        "type": "Phishing Email",
        "text": "Your bank account is suspended! Click immediately:\nhttp://secure-bank-login.xyz",
        "answer": "Phishing",
        "explanation": "Fake URL + urgency indicates phishing."
    },
    {
        "type": "Credential Harvesting Attack",
        "text": "Session expired! Login again to continue.",
        "answer": "Phishing",
        "explanation": "Fake login page used to steal credentials.",
        "login": True
    },
    {
        "type": "Legitimate Notification",
        "text": "Your university results are published:\nhttps://jainuniversity.edu",
        "answer": "Safe",
        "explanation": "Official domain with no suspicious signs."
    },
    {
        "type": "Phishing Scam",
        "text": "You won ₹10,00,000! Claim now:\nhttp://lottery-win-free.com",
        "answer": "Phishing",
        "explanation": "Too good to be true + fake link."
    },
    {
        "type": "E-commerce Notification",
        "text": "Amazon: Your order shipped.\nhttps://amazon.in/orders",
        "answer": "Safe",
        "explanation": "Trusted platform."
    }
]

current_question = 0
score = 0
time_left = 10


def start_simulation():
    start_frame.pack_forget()
    main_frame.pack()
    load_question()


def load_question():
    global current_question, time_left

    if current_question < len(scenarios):
        scenario = scenarios[current_question]

      
        winsound.Beep(1000, 300)

        question_label.config(
            text=f"⚠️ Incoming Attack Simulation\n\n"
                 f"Attack Type: {scenario['type']}\n\n"
                 f"{scenario['text']}"
        )

        score_label.config(text=f"Security Awareness Score: {score}")

      
        time_left = 10
        start_timer()

      
        if "login" in scenario and scenario["login"]:
            root.after(1500, open_fake_login)

    else:
        show_final_result()


def check_answer(user_choice):
    global current_question, score

    scenario = scenarios[current_question]
    correct = scenario["answer"]

    if user_choice == correct:
        score += 1
        result_text = "✅ Threat Successfully Identified"
    else:
        result_text = "❌ You Fell for the Attack"

    explanation = scenario["explanation"]

    question_label.config(
        text=f"{result_text}\n\nReason:\n{explanation}"
    )

    current_question += 1
    root.after(2500, load_question)


def start_timer():
    global time_left

    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left}s")
        time_left -= 1
        root.after(1000, start_timer)
    else:
        check_answer("No Answer")


def open_fake_login():
    login_window = tk.Toplevel(root)
    login_window.title("Secure Login")
    login_window.geometry("350x250")

    tk.Label(login_window, text="Login to Continue", font=("Arial", 14)).pack(pady=10)

    tk.Label(login_window, text="Username").pack()
    username = tk.Entry(login_window)
    username.pack()

    tk.Label(login_window, text="Password").pack()
    password = tk.Entry(login_window, show="*")
    password.pack()

    def submit_login():
        messagebox.showwarning(
            "Phishing Attack!",
            "⚠️ This was a fake login page!\nYour credentials could have been stolen."
        )
        login_window.destroy()

    tk.Button(login_window, text="Login", command=submit_login).pack(pady=15)


def show_final_result():
    phishing_btn.pack_forget()
    safe_btn.pack_forget()

    if score <= 2:
        level = "⚠️ High Risk User"
    elif score <= 4:
        level = "⚠️ Moderate Awareness"
    else:
        level = "✅ Security Aware User"

    question_label.config(
        text=f"🎯 Simulation Completed\n\n"
             f"Final Score: {score}/{len(scenarios)}\n\n"
             f"Assessment: {level}"
    )

    messagebox.showinfo(
        "Simulation Result",
        f"Score: {score}/{len(scenarios)}\n{level}"
    )


root = tk.Tk()
root.title("Cyber Range - Phishing Attack Simulator")
root.geometry("700x500")
root.config(bg="#e6f2ff")

start_frame = tk.Frame(root, bg="#e6f2ff")

title = tk.Label(
    start_frame,
    text="Cyber Range Simulation",
    font=("Arial", 20, "bold"),
    bg="#e6f2ff"
)
title.pack(pady=20)

desc = tk.Label(
    start_frame,
    text="Simulating Real-World Phishing Attacks\nAnalyze and Defend Against Threats",
    font=("Arial", 12),
    bg="#e6f2ff"
)
desc.pack(pady=10)

start_btn = tk.Button(
    start_frame,
    text="Start Simulation",
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
    command=start_simulation
)
start_btn.pack(pady=20)

start_frame.pack(expand=True)

main_frame = tk.Frame(root, bg="#e6f2ff")

score_label = tk.Label(
    main_frame,
    text="Security Awareness Score: 0",
    font=("Arial", 12),
    bg="#e6f2ff"
)
score_label.pack(pady=5)

timer_label = tk.Label(
    main_frame,
    text="Time Left: 10s",
    font=("Arial", 12),
    bg="#e6f2ff"
)
timer_label.pack()

question_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 12),
    wraplength=600,
    justify="center",
    bg="white",
    padx=15,
    pady=15,
    relief="solid"
)
question_label.pack(pady=20)

phishing_btn = tk.Button(
    main_frame,
    text="Mark as Phishing",
    font=("Arial", 12),
    bg="#ff6666",
    width=20,
    command=lambda: check_answer("Phishing")
)
phishing_btn.pack(pady=5)

safe_btn = tk.Button(
    main_frame,
    text="Mark as Safe",
    font=("Arial", 12),
    bg="#66cc66",
    width=20,
    command=lambda: check_answer("Safe")
)
safe_btn.pack(pady=5)

root.mainloop()
