# Smart-Mail-Box
In this project, I created an IoT system that uses a Raspberry Pi and a motion sensor to send notifications when a mailbox has received mail. This can be useful for individuals who are unable to check their mailbox regularly or who want to be notified as soon as possible when they receive mail.


![Circuit Diagram](CircuitDiagram.png)


The code begins by importing the RPi.GPIO, time, and smtplib libraries. RPi.GPIO is used to control the General Purpose Input Output (GPIO) pins on a Raspberry Pi, time is used for creating delays, and smtplib is used for sending emails.

The code sets the pin numbering mode to physical pin numbering using the GPIO.setmode() method and passing in GPIO.BOARD as the argument. The code then sets pin 10 as an input pin using the GPIO.setup() method, passing in 10 as the pin number and GPIO.IN as the mode. The pull_up_down argument is set to GPIO.PUD_DOWN, which means the initial value of the pin is pulled low (off).

The send_email() function is used to send an email when mail is detected. The function starts by defining the sender's email address, the recipient's email address, and the email account's password. These values can be changed to any valid email address and password. The function then establishes a connection to the Gmail SMTP server using the smtplib.SMTP() method, passing in 'smtp.gmail.com' as the server address and 587 as the port number.

The email notification message in the code is written in a fun and creative way to make it more engaging for the recipient. The message starts with a catchy subject line "Snail Mail Notification" which immediately grabs the recipient's attention, it continues to have a creative message that describes the excitement of receiving mail. It creates a feeling of anticipation and excitement for the recipient, making them more likely to check their mailbox.

Then The code sleeps for 600 seconds (10 minutes) after the send_email() function is called because it is waiting for a certain amount of time before checking the status of the input pin again. The reason for this is to prevent multiple emails from being sent if the motion sensor is triggered multiple times within a short period of time. By waiting for 10 minutes after an email is sent, the script gives the user enough time to retrieve their mail and prevent multiple unnecessary emails. Additionally, a delay in the code also helps reduce the chances of the server being overloaded with too many requests in a short time. This would prevent the server from crashing and keep the system running smoothly.

