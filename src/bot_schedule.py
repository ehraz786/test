import telebot, schedule, time
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual bot API key


# Chat ID to which you want to send messages


def send_scheduled_message():
    message_text = f"Scheduled message sent at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    bot.send_message(CHAT_ID, message_text)
    print("Message sent")

# Schedule the message to be sent every day at a specific time
schedule.every().day.at("20:00").do(send_scheduled_message)  # Change "09:00" to your desired time

# Function to run the scheduler
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduler
run_scheduler()
