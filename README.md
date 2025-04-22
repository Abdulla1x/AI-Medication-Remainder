# AI Medication Reminder

An AI-powered Streamlit application that extracts medication details, schedules reminders, and answers medication-related questions using Gemini LLM and APScheduler.

* * *

## Project Overview

Built to help users manage their medication schedules effectively, this app leverages LLM-driven parsing to extract medication name, dosage, and timing, schedules notifications, and provides a Q&A interface for medication inquiries.

* * *

## ✅ Features

- **Medication Extraction**  
  Parse medication name, dosage, and schedule from freeform input using Gemini LLM chains.

- **Reminder Scheduling**  
  Schedule and manage notifications with APScheduler, including timezone support and grace periods.

- **Interactive Streamlit UI**  
  Add, view, and remove medications, see upcoming reminders in a dashboard.

- **Asynchronous LLM Calls**  
  Ensure smooth UI by handling async tasks with `nest_asyncio`.

- **Q&A Interface**  
  Ask medical or medication-related questions directly within the app.

* * *

## ️ Technologies Used

- Python 3  
- Streamlit  
- Gemini LLM  
- APScheduler  
- nest_asyncio

* * *

## Example Use Case

1. Run the Streamlit app:
   ```bash
   streamlit run streamlitApp.py
   ```
2. Enter medication details in the form (e.g., "Take 2 tablets of Ibuprofen every 6 hours").
3. View scheduled reminders in the dashboard.
4. Receive notifications at specified times.
5. Ask questions like "What are common side effects of Ibuprofen?" in the Q&A section.

* * *

## What I Learned

- Integrating LLMs for natural language parsing.  
- Managing scheduled tasks in Python with APScheduler.  
- Handling async operations within Streamlit using `nest_asyncio`.

* * *

## Future Improvements

- Add support for multiple timezones per medication.  
- Implement user authentication and data persistence.  
- Integrate push notifications (e.g., email or SMS).  
- Extend Q&A with additional medical resources and validation.

* * *

## File Structure

```plaintext
AI-Medication-Reminder/
├── main.py                 # Defines Gemini LLM chains and async functions for parsing and Q&A
├── remainder_scheduler.py  # Configures and manages reminder schedules
├── streamlitApp.py         # Streamlit UI and async task orchestration
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation
```

---

