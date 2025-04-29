import streamlit as st
import asyncio
import pandas as pd
import os
import csv
from main import extract_medication_details, answer_medical_question
from reminder_scheduler import schedule_reminders, send_notification
from prolog_interface import check_interaction, check_long_term_risk

st.title("AI Medication Reminder 💊")

tab1, tab2, tab3, tab4 = st.tabs(["📋 Schedule Reminders", "🧠 Ask a Medical Question", "🔔 Test Notification", "⚠️ Medication Safety Check"])

with tab1:
    st.subheader("Enter your medication details:")
    st.info("Include the medication name, dosage, frequency (e.g., every morning/afternoon/night), and duration in your input.")
    natural_input = st.text_area("Example: 'Remind me to take 1 tablet of Paracetamol every night for 5 days.'")

    if st.button("Submit Medication Details"):
        if natural_input.strip():
            with st.spinner("Processing your input..."):
                try:
                    medication_details = asyncio.run(extract_medication_details(natural_input))
                    st.success("Medication details extracted successfully!")
                    
                    if isinstance(medication_details, dict):
                        # Convert single dict to list
                        medication_details = [medication_details]

                    # Check if the result is a list
                    if isinstance(medication_details, list):

                        # Iterate over each medication and schedule reminders
                        for medication in medication_details:
                            st.markdown(f"#### Medication: {medication['medication_name']}")
                            st.write(f"**Dosage:** {medication['dosage']}")
                            st.write(f"**Frequency:** {medication['frequency']}")
                            st.write(f"**Duration:** {medication['duration_days']} days")

                            # Schedule reminders
                            schedule_reminders(medication)
                        st.success("Reminders have been scheduled!")

                    # Convert to DataFrame and save to CSV
                    df = pd.DataFrame(medication_details)
                    csv_file = "medications.csv"

                    if os.path.exists(csv_file):
                        df.to_csv(csv_file, mode='a', header=False, index=False)
                    else:
                        df.to_csv(csv_file, index=False)

                    st.success("✅ Saved to medications.csv")
                    with open(csv_file, 'rb') as f:
                        st.download_button("⬇️ Download CSV", f, file_name="medications.csv")

                except ValueError as e:
                    st.error(f"Error: {e}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")
        else:
            st.warning("Please enter valid medication details.")

with tab2:
    st.subheader("Ask a health-related question:")
    user_question = st.text_input("Your question")

    if st.button("Ask AI"):
        if not user_question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                answer = asyncio.run(answer_medical_question(user_question))
                st.success("Answer:")
                st.write(answer)
            
with tab3:
    # Test Notification Section
    st.markdown("---")
    st.markdown("## 🔔 Test Notification")
    st.info("Click the button below to send a test notification.")

    if st.button("Send Test Notification"):
        try:
            send_notification("Test Medication", "1 tablet")
            st.success("Test notification sent successfully!")
        except Exception as e:
            st.error(f"Notification failed: {e}")

with tab4:
    st.subheader("⚠️ Medication Safety Check using Prolog")
    st.info("This tool checks for harmful drug interactions and long-term usage risks using Prolog rules.")

    csv_file = "medications.csv"

    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)

        if not df.empty:
            st.write("### Current Medications:")
            st.dataframe(df)

            medications = []
            try:
                with open(csv_file, mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        medication = {
                            'medication_name': row['medication_name'].strip(),
                            'dosage': row['dosage'].strip(),
                            'frequency': row['frequency'].strip(),
                            'duration_days': int(row['duration_days'].strip())
                        }
                        medications.append(medication)
            except Exception as e:
                st.error(f"Failed to read CSV file: {e}")

            st.markdown("### 🚨 Drug Interactions")
            found_interaction = False
            for i in range(len(medications)):
                for j in range(i + 1, len(medications)):
                    med1 = medications[i]["medication_name"]
                    med2 = medications[j]["medication_name"]
                    try:
                        if check_interaction(med1, med2):
                            st.warning(f"⚠️ Interaction detected between **{med1}** and **{med2}**")
                            found_interaction = True
                    except Exception as e:
                        st.error(f"Error checking interaction between {med1} and {med2}: {e}")
            if not found_interaction:
                st.success("✅ No harmful interactions detected.")

            st.markdown("### 🧪 Long-Term Usage Risk")
            for med in medications:
                name = med["medication_name"]
                duration = int(med["duration_days"])
                try:
                    if check_long_term_risk(name, duration):
                        st.warning(f"⚠️ **{name}** taken for **{duration} days** may pose long-term health risks.")
                    else:
                        st.info(f"✅ **{name}** is safe for {duration} days.")
                except Exception as e:
                    st.error(f"Error checking risk for {name}: {e}")
        else:
            st.warning("No medications found in CSV. Please enter medication details first.")
    else:
        st.warning("No medication data found. Submit details in the first tab to run safety checks.")
