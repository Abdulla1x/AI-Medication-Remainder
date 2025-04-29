# AI Medication Reminder

An AI-powered Streamlit application that extracts medication details, schedules reminders, answers health-related questions using Gemini LLM, and performs medication safety checks using Prolog logic.

---

## Project Overview

Built to help users manage their medication schedules effectively, this app leverages LLM-driven parsing to extract medication name, dosage, and timing, schedules notifications, provides a Q&A interface for medication inquiries, and ensures safety by checking for harmful drug interactions and long-term usage risks using Prolog.

---

## ✅ Features

- **Medication Extraction**  
  Parse medication name, dosage, and schedule from freeform input using Gemini LLM chains.

- **Reminder Scheduling**  
  Schedule and manage notifications with APScheduler, including timezone support and grace periods.

- **Medication Safety Check**  
  Analyze entered medications using SWI-Prolog to:
  - Detect harmful **drug interactions**
  - Flag **long-term usage risks**

- **Interactive Streamlit UI**  
  Add, view, and remove medications, check for safety concerns, and view upcoming reminders in a dashboard.

- **Asynchronous LLM Calls**  
  Ensure smooth UI by handling async tasks with `nest_asyncio`.

- **Q&A Interface**  
  Ask medical or medication-related questions directly within the app.

---

## 🧰 Technologies Used

- Python 3  
- Streamlit  
- Gemini LLM (via LangChain)  
- APScheduler  
- SWI-Prolog (via `pyswip`)  

---

## 💡 Example Use Case

1. Run the Streamlit app:
   ```bash
   streamlit run streamlitApp.py
   ```
2. Enter medication details in the form (e.g., "Take 2 tablets of Ibuprofen every night").
3. View scheduled reminders in the dashboard.
4. Receive notifications at specified times.
5. Ask questions like "What are common side effects of Ibuprofen?" in the Q&A section.
6. Download a CSV report of your medications for reference.
7. Check for harmful drug interactions and long-term usage risks. 

* * *

## What I Learned

- Integrating LLMs for natural language parsing.  
- Managing scheduled tasks in Python with APScheduler.  
- Creating a User-Friendly Interface using Streamlit.
- Communicating with Prolog from Python to perform logical safety checks.
  
* * *

## Future Improvements

- Add support for multiple timezones per medication.  
- Implement user authentication and data persistence.  
- Integrate push notifications (e.g., email or SMS).  
- Extend Q&A with additional medical resources and validation.
- Expand Prolog logic with more rules and drug data.
- Extend Q&A with additional medical resources and validation.

* * *

## File Structure

```plaintext
AI-Medication-Reminder/
├── main.py                 # Defines Gemini LLM chains and async functions for parsing and Q&A
├── reminder_scheduler.py   # Configures and manages reminder schedules
├── prolog_interface.py     # Contains functions to query Prolog for safety checks
├── streamlitApp.py         # Streamlit UI and async task orchestration
├── med_rules.pl            # Prolog rules for medication interactions and long-term usage risks
├── medications.csv         # Stores user medication history
└── README.md               # Project documentation
```

---

