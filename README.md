# 💧 Drink Water Reminder (Python Project)

This is a simple **Drink Water Reminder** built with Python.  
It reminds you to stay hydrated using:

- 🗣 **Audio Alerts** (via Text-to-Speech every 1 hour)  
- 📧 **Email Reminders** (sent at fixed times like 11 AM, 3 PM, and 7 PM)  



## 🚀 Features
- Automatic **hourly audio alerts** to remind you to drink water.  
- Scheduled **email notifications** at specified times.  
- Uses `pyttsx3` for offline text-to-speech.  
- Secure email sending with **Gmail SMTP + App Passwords**.  
- Runs in the background with **multithreading**.



## 🛠 Requirements
Install dependencies before running the script:

```bash
pip install pyttsx3
(Optional) If you don’t have smtplib, it comes pre-installed with Python.

⚙️ Setup
Clone this repository:

bash
Copy
Edit
git clone https://github.com/manjusrid0/drink-reminder.git
cd drink-water-reminder
Open the Python file and update with your Gmail credentials:

python
Copy
Edit
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # Generate from Google Account > Security > App Passwords
TO_EMAIL = "receiver-email@gmail.com"
⚠️ Note: Use an App Password, not your normal Gmail password.

Run the script:

python reminder.py
📌 How it Works
Audio Reminder: Every hour, a voice says "Time to drink water!".

Email Reminder: Sends hydration emails at 11:00, 15:00, and 19:00.

Both reminders run in separate threads, so they work simultaneously.

📸 Example Output

Audio reminder: Drink water!
Email sent: Drink Water Reminder
🔒 Security Note
Do NOT hardcode your real password in the script.

Use environment variables or .env files in production.

For Gmail, enable 2FA and create an App Password.

📄 License
This project is licensed under the MIT License – feel free to use and improve it!
