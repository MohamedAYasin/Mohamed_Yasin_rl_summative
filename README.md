# **Reinforcement Learning for Personalized Education**  

## **🎯 Project Mission**

My mission at ALU is to transform the education system of Somalia by empowering youth through emerging technologies. This initiative aims to build a Business Innovation Hub, bringing together entrepreneurs, innovators, leaders, and students for collaboration and creativity. This RL-powered Personalized Learning & Skill Development system adjusts dynamically to student progress, ensuring they receive tailored challenges and resources.

 <img src="https://github.com/user-attachments/assets/81a4e848-515c-4443-96ed-a0f52aca585a" width="800">

## **🌟 Features**  
- **Custom Gym Environment** for RL-based education tracking  
- **Personalized Learning & Skill Development** using adaptive RL algorithms  
- **PyOpenGL + Pygame Rendering** for interactive visualization  
- **Multi-Step Decision Making** (Assess, Guide, Challenge, Adapt)  

## **🔗 Links to Explore**

- Document: [Project Report Document](https://docs.google.com/document/d/17oI4Mv7mgviua3miv2alk2-DyxYpnEJnKxDQEuukd3I/edit?tab=t.0#heading=h.a6l59bpcgjnq)

- Simulation Video: [Simulation Agent Video on Loom](https://www.loom.com/share/e264ac14759a476da1a8f035ce1dfecd)

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

## **📈 Plots**

![Image](https://github.com/user-attachments/assets/011c94e6-75e0-439a-8fed-525a03453884)

![Image](https://github.com/user-attachments/assets/67c35f4d-c460-4ee6-ad5d-443b23720911)

## **🔍 Key Findings**

🔹DQN took around 500 episodes to reach stable performance.
🔹PPO took around 300 episodes to stabilize.
🔹DQN performed well but took longer to find the optimal path.
🔹PPO adapted more quickly to new starting positions.

## **📈 Future Improvements**  
🔹 Fine-tune RL hyperparameters for better adaptation.  
🔹 Improve curriculum learning for gradual difficulty adjustments.   
🔹 Extend the action space with more personalized interventions.  
🔹 Add real-world integration with educational platforms.  

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


---

©👤 **[Mohamed Ahmed Yasin](https://github.com/mohamedAYasin/)**

---
