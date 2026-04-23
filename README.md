# Cyber-Range-Phishing-Attack-Awareness-Simulator
A Python-based GUI application that simulates real-world phishing attacks in a cyber range environment to train users in identifying and preventing cyber threats.

# 🛡️ Cyber Range Simulation: Phishing Attack Awareness System

## 📖 Abstract

This project presents a GUI-based Cyber Range simulation designed to model real-world phishing attacks and evaluate user awareness. The system provides an interactive environment where users are exposed to simulated attack scenarios and must identify whether they are legitimate or malicious. The application delivers immediate feedback, explanatory insights, and a final risk assessment, thereby enhancing cybersecurity awareness in a controlled setting.

## 🎯 Objectives

* To simulate phishing attack scenarios in a controlled environment
* To analyze user decision-making in identifying cyber threats
* To demonstrate attack-defense interaction using a Cyber Range model
* To improve user awareness and understanding of phishing techniques

## 🧠 System Overview

The application operates as a **Cyber Range as a Service (CRaaS)** simulation, where:

* **Attack Layer:** Generates realistic phishing attempts such as fake emails, malicious links, and credential harvesting pages
* **Defense Layer:** Represents the user, who analyzes and responds to threats
* **Simulation Layer:** Provides a safe and controlled GUI-based environment for interaction

## ⚙️ Key Features

* **Graphical User Interface (GUI):** Built using Tkinter for interactive simulation
* **Phishing Scenario Engine:** Multiple realistic attack scenarios
* **Credential Harvesting Simulation:** Fake login interface to demonstrate data theft
* **Time-Constrained Decision Making:** Timer-based responses to simulate real-world pressure
* **Alert Mechanism:** Audio indication of incoming threats
* **Real-Time Feedback:** Immediate evaluation and explanation of user actions
* **Security Awareness Scoring:** Tracks performance across scenarios
* **Risk Classification:** Categorizes users as High Risk, Moderate, or Security Aware

## 🛠️ Technologies Used

| Component     | Technology         |
| ------------- | ------------------ |
| Programming   | Python 3           |
| GUI Framework | Tkinter            |
| Alert System  | Winsound (Windows) |


## 🚀 Execution Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/phishing-simulator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd phishing-simulator
   ```

3. Execute the application:

   ```bash
   python phishing_simulator.py
   ```

## 🔄 Workflow

1. The user initiates the simulation
2. The system generates an attack scenario
3. The user evaluates and classifies the scenario
4. The system provides feedback with justification
5. The process repeats for multiple scenarios
6. A final score and security assessment are generated

## 📊 Output

* **Security Awareness Score** (based on correct identifications)
* **Risk Level Classification:**

  * High Risk User
  * Moderate Awareness
  * Security Aware User

## 🔮 Future Scope

* Integration with cloud-based cyber range platforms
* Expansion of attack scenarios using real-world datasets
* Machine learning-based phishing detection
* Multi-user simulation and analytics dashboard
* Cross-platform compatibility improvements

## 📌 Conclusion

The project successfully demonstrates a simplified Cyber Range environment for phishing attack simulation. It highlights the importance of user awareness in cybersecurity and provides an interactive approach to understanding and mitigating phishing threats.
