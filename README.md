# **Reinforcement Learning for Personalized Education**  

This project uses **Reinforcement Learning (RL)** to create an AI-powered **Personalized Learning System** that adapts dynamically to students' progress. The agent learns to **assess student understanding**, **provide tailored challenges**, and **adjust learning materials** to optimize learning outcomes.  

 <img src="https://github.com/user-attachments/assets/81a4e848-515c-4443-96ed-a0f52aca585a" width="800">

## **🌟 Features**  
- **Custom Gym Environment** for RL-based education tracking  
- **Personalized Learning & Skill Development** using adaptive RL algorithms  
- **PyOpenGL + Pygame Rendering** for interactive visualization  
- **Multi-Step Decision Making** (Assess, Guide, Challenge, Adapt)  

## **🔗 Links to Explore**

Document: 
Simulation Video:

## **🧠 Reinforcement Learning in Education**  

### **📌 State Space (Minimum 4 States)**  
The RL model tracks student progress through four states:  

1️⃣ **Struggling Learner** – Needs extra support and guidance.  
2️⃣ **Steady Learner** – Making gradual progress but requires assistance.  
3️⃣ **Independent Learner** – Can solve problems with minimal help.  
4️⃣ **Adaptive Learner** – Highly competent, applying skills across challenges.  

### **🎮 Action Space (Minimum 4 Actions)**  
The AI tutor selects actions to guide the student’s learning:  

🔹 **Action 1:** Simplify Content – Adjusts material difficulty.  
🔹 **Action 2:** Provide a Challenge – Increases complexity for skill growth.  
🔹 **Action 3:** Offer Immediate Feedback – Gives hints or corrections.  
🔹 **Action 4:** Introduce Alternative Learning Path – Uses different methods for better understanding.  

### **🏆 Reward Criteria**  
✅ **Positive Rewards:** When a student successfully progresses or completes tasks.  
❌ **Negative Rewards:** If a student struggles repeatedly without improvement or disengages.  

### **🔚 Terminal Conditions**  
The learning session ends when:  
- **Mastery Achieved:** Student reaches the **Adaptive Learner** state.  
- **Completion:** Student finishes the learning cycle.  
- **Persistent Struggle:** Student stays stuck in **Struggling Learner** state too long.  
- **Disengagement:** Student stops participating.  



## **🚀 Setup Instructions**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/MohamedAYasin/Mohamed_Yasin_rl_summative.git
cd Mohamed_Yasin_rl_summative
```

### **2️⃣ Create and Activate a Virtual Environment**  
```bash
python -m venv venv  

# Activate the virtual environment
# On Windows:
venv\Scripts\activate  

# On macOS/Linux:
source venv/bin/activate
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```



## **🖥️ Running the RL Agent**  

Run the environment without training:  
```bash
python play.py  
```


## **📈 Future Improvements**  
🔹 Fine-tune RL hyperparameters for better adaptation.  
🔹 Improve curriculum learning for gradual difficulty adjustments.  
🔹 Implement additional RL algorithms (SAC, TRPO) for better performance.  
🔹 Extend the action space with more personalized interventions.  
🔹 Add real-world integration with educational platforms.  

---

©👤 **[Mohamed Ahmed Yasin](https://github.com/mohamedAYasin/)**

---
