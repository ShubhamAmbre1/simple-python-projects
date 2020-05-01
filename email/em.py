from tkinter import *
import smtplib


def main():

	screen = Tk()

	sender_email = StringVar()
	password = StringVar()
	message = StringVar()
	receiver_email = StringVar()
	count = IntVar()

	sender_label = Label(screen, text = "Your email:").grid(row = 1, column = 1)
	sender_entry = Entry(screen, textvariable = sender_email,width = 35).grid(row = 1, column = 2)
	extra = Label(screen).grid(row = 2)

	password_label = Label(screen, text = "Password").grid(row = 3, column = 1)
	password_entry = Entry(screen, show = "*",textvariable = password,width = 35).grid(row = 3, column = 2)
	extra = Label(screen).grid(row = 4)

	receiver_label = Label(screen, text = "receiver email: ").grid(row = 5, column = 1)
	receiver_entry = Entry(screen, textvariable = receiver_email, width = 35).grid(row = 5, column = 2)
	extra = Label(screen).grid(row = 6)

	message_label = Label(screen, text = "Message").grid(row = 7, column = 1)
	message_entry = Entry(screen, textvariable = message, width = 50).grid(row = 7, column = 2)
	extra = Label(screen).grid(row = 8)	

	count_label = Label(screen, text = "spam count").grid(row = 9, column = 1)
	count_entry = Entry(screen, textvariable = count).grid(row = 9, column = 2)
	extra = Label(screen).grid(row = 10)


	login = Button(screen, text = "send", command = lambda: send_mail(sender_email, password, message, receiver_email, count), padx = 20, pady = 10).grid(row = 11, column = 2,columnspan = 2)
	extra = Label(screen).grid(row = 12)	

	screen.mainloop()



def send_mail(sender_email, password, message, receiver_email, count):
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(sender_email.get(), password.get())
	for i in range(count.get()):
		server.sendmail(sender_email.get(), receiver_email.get(), message.get())
	server.quit()


	
if __name__ == '__main__':
	main()


