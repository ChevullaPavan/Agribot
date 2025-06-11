 🌾 AgriBot Project Plan Report

    👥 1.1 Team Information

  👨‍🌾 Team Name:** AgriNova

  👨‍💻 Team Members & Roles:**

- 👑 M. Sridhar Goud – Project Lead  
- 🤖 C. Pavan – AI Engineer  
- 💻 Y. Sai Teja – Frontend Developer  
- 📊 Y. Chandu – Data Scientist  
- 🎨 Shiva Kiran – UX Designer  

  📌 Planned Individual Contributions:**

- 👑 Sridhar: Oversees coordination, planning & deadlines.  
- 🤖 Pavan: Implements AI models for crop recommendations, disease detection, chatbot.  
- 💻 Sai Teja: Builds responsive, fast, and accessible frontend for users.  
- 📊 Chandu: Handles data collection, validation & performance testing.  
- 🎨 Shiva: Designs clean, accessible, and user-friendly UX based on user behavior.

---

   🌱 1.2 Application Overview

   📱 Application Name:** AgriBot – AI-Powered Agriculture Assistant

  🎯 Problem Statement:**  
AgriBot supports farmers facing a lack of real-time guidance by offering AI-driven crop recommendations, pest/disease diagnosis, and localized farming advice – especially helpful for rural areas with limited connectivity.

**✨ Key Features:**

- 🤖 AI chatbot for smart crop planning and pest control  
- 🌦 Weather-based sowing/irrigation suggestions  
- 🗣 Multilingual support (e.g., Telugu, Hindi)  
- 📴 Offline-first design for rural access  

**💡 Motivation:**  
Many farmers rely solely on outdated traditional methods. AgriBot aims to democratize access to expert agricultural knowledge using modern AI, improving livelihoods and sustainability.

---

 🧠 1.3 AI Integration Details

**🧪 Planned AI Models:**

- ✨ Text-based: `flan-t5-large` / `mistralai/Mistral-7B-Instruct-v0.2`  
- 🌿 Image-based: MobileNet + PlantVillage dataset for disease diagnosis  

**🔄 AI Workflow:**

1. Collect input (text/image) via frontend  
2. Use prompt-engineered LLM or image classifier  
3. Output localized suggestions or diagnosis  

**📝 Example Prompts:**

- “Suggest crops suitable for [district] with [soil type].”  
- “Diagnose this pest from the uploaded image.”  
- “Give organic fertilizer tips for [crop].”

---

 🏗 1.4 Technical Architecture & Development

🧩 Architecture Diagram: (to be inserted after AI/backend integration)

**🛠 Technology Stack:**

- 🧾 Frontend: Streamlit (or React)  
- 🧠 Backend: Hugging Face Transformers, TensorFlow  
- 🐍 Language: Python  
- 🧬 Deployment: Hugging Face Spaces / Gradio  
- 🛡 Version Control: GitLab  

**⚠ Expected Challenges & Solutions:**

| Challenge 🌪 | Solution 🌈 |
|-------------|-------------|
| Poor connectivity | Offline caching & light UI |
| Scarce crop data | Use PlantVillage, Krishikosh datasets |
| Prompt translation issues | Localized prompt fine-tuning |

🪪 License: MIT Open Source

---

👨‍🔬 1.5 User Testing & Feedback (Planned)

**🧪 Testing Strategy:**

- 🧑‍🌾 Share beta app with real farmers & agri-students  
- 📋 Google Forms for multilingual feedback  

**📊 Target:**
- 15–20 users initially  

**🔁 Iteration Plan:**
- Revise prompts & UI based on common user suggestions  
- Improve language accuracy & cultural relevance

---

 🚀 1.6 Future Roadmap & Adoption Plan

📆 Rollout Timeline:

 ⏳ Phase 1 (Weeks 1–2):
- Fix bugs  
- Expand to 3 languages  
- Add voice input support  

 🌦 Phase 2 (Weeks 3–4):
- Integrate weather API  
- Add crop prices, scheme info  
- Launch SMS version  

 🤝 Phase 3 (Weeks 5–6):
- Community forum for farmers  
- Mandi price prediction  

📈 Adoption Strategy:

- 🧑‍🌾 Target Users: Rural farmers, agri-students, NGOs  
- 🎁 Value: Free, localized, easy to use, expert-powered  
- 📣 Promotion: WhatsApp videos, YouTube Shorts, agri-university booths  
- 👥 NGO Collaboration: Field-testing and deployment  

📲 Onboarding:

- 🧭 In-app guided tutorial in local language  
- ❓ FAQ & “How it works” walkthrough  
- 📸 Visual instructions and tooltips

🔁 Feedback Loop:

- 🔘 Built-in “Give Feedback” button  
- 📤 Optional voice/text form  
- 🙏 Acknowledgement screens and follow-up

👨‍👩‍👧 Community Engagement:

- 🔗 Open GitLab repo with CONTRIBUTING.md  
- 🏆 Feature contributors in-app & README  
- 🤝 Encourage data & question sharing by local users



 


