from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from plyer import notification

def send_notification(medication_name, dosage):
    notification.notify(
        title="Medication Reminder",
        message=f"Time to take {dosage} of {medication_name}!",
        timeout=10  
    )

def schedule_reminders(medication):
    # Mapping frequency to reminder times
    freq = medication["frequency"].lower()

    if freq == "every night":
        reminder_times = [(21, 0)]  # 9 PM
    elif freq == "every morning":
        reminder_times = [(8, 0)]  # 8 AM
    elif freq == "every afternoon":
        reminder_times = [(14, 0)]  # 2 PM
    elif freq == "every morning and night":
        reminder_times = [(8, 0), (21, 0)]  # 8 AM and 9 PM
    elif freq == "every morning and afternoon":
        reminder_times = [(8, 0), (14, 0)]  # 8 AM and 2 PM
    elif freq == "every afternoon and night":
        reminder_times = [(14, 0), (21, 0)]  # 2 PM and 9 PM
    elif freq == "every morning, afternoon, and night":
        reminder_times = [(8, 0), (14, 0), (21, 0)]  # 8 AM, 2 PM, 9 PM
    else:
        reminder_times = [(12, 0)]  # default to noon

    # Setting up the scheduler
    scheduler = BackgroundScheduler()
    start_time = datetime.now()

    for day in range(medication["duration_days"]):
        for i, (hour, minute) in enumerate(reminder_times):
            reminder_time = (start_time + timedelta(days=day)).replace(
                hour=hour, minute=minute, second=0, microsecond=0
            )

            job_id = f"{medication['medication_name'].lower()}-{day}-{i}"

            scheduler.add_job(
                func=lambda name=medication["medication_name"], dose=medication["dosage"]:
                    send_notification(name, dose),
                trigger='date',
                run_date=reminder_time,
                id=job_id
            )

    scheduler.start()
    print("Reminders scheduled!")
    return scheduler