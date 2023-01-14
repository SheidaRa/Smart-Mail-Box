import RPi.GPIO as GPIO
import time
import smtplib

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Set pin 10 as an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Function to send an email
def send_email():
    sender_add='email@gmail.com'
    receiver_add='email@yahoo.com'
    password='mihrbjaxztdvhwic'

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.ehlo()
    smtp_server.login(sender_add,password)
    msg = 'subject: Snail Mail Notification\n\nMail Alert! Mail Alert! Look whos here, a new letter to bring cheer! It could be a invitation to a party, or a package full of treats thats hearty. Could be a note from a long-lost friend or a surprise that will make your weekend. So dont wait, run to the mailbox and check, its waiting for you to take a peek!'
    smtp_server.sendmail(sender_add, receiver_add, msg)
    print("Hey, email has been sent!")
    smtp_server.quit()


# Run a loop to check the status of the mail box
while True:
  if GPIO.input(10) == GPIO.HIGH:
    send_email()
    time.sleep(600)
  else:
    time.sleep(0.5)
