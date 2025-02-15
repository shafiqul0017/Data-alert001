from telegram import Bot
import schedule
import time

# আপনার BotFather থেকে প্রাপ্ত API টোকেনটি এখানে বসান
TOKEN = '7780487272:AAF7DHhTx2S0WszcB5dR8k4karsRou-9Au4'
CHAT_ID = '-1002272580765'  # আপনার গ্রুপের Chat ID

# বট তৈরি
bot = Bot(token=TOKEN)

# মেসেজ পাঠানোর ফাংশন
def send_alert():
    message = """Assalamu Alaikum,
The time is now 9:10 PM. Please check your MW account. If the Extension/Software is running, kindly close it, remove any corrupted data, and then restart the Extension/Software before resuming work.
Thank you.
Best regards,
Shafiqul Islam"""
    bot.send_message(chat_id=CHAT_ID, text=message)
    print("এলার্ট মেসেজ পাঠানো হয়েছে!")

# শিডিউল সেট করা (প্রতিদিন রাত ৯:১০ মিনিটে)
schedule.every().day.at("21:10").do(send_alert)

# শিডিউল চালু রাখা
while True:
    schedule.run_pending()
    time.sleep(60)
