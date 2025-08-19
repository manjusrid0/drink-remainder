import time
import threading
import smtplib
from email.mime.text import MIMEText
import pyttsx3
from datetime import datetime

# Email Config (use a test Gmail ID with App Password)
EMAIL_ADDRESS = "manjusrid0@gmail.com"

TO_EMAIL = "manjusrid0@gmail.com"

# Text-to-Speech Engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Send email
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"Email sent: {subject}")
    except Exception as e:
        print("Email failed:", e)

# Audio alert every 1 hour
def audio_reminder():
    while True:
        speak("Time to drink water!")
        print("Audio reminder: Drink water!")
        time.sleep(60 * 60)  # every 1 hour

# Email at 11AM, 3PM, 7PM
def email_reminder():
    sent_times = set()
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        targets = ["09:54", "15:00", "19:00"]
        if current_time in targets and current_time not in sent_times:
            send_email("Drink Water Reminder", "Stay hydrated! It's time to drink water.")
            sent_times.add(current_time)
        if len(sent_times) == len(targets):
            break
        time.sleep(60)

# Start Threads
t1 = threading.Thread(target=audio_reminder)
t2 = threading.Thread(target=email_reminder)

t1.start()
t2.start()
