import tkinter as tk
from tkinter import ttk
import smtplib
import ssl
from email.message import EmailMessage

def send_email():
    sender_email = sender_email_var.get()
    sender_password = sender_password_var.get()
    recipient_email = recipient_email_var.get()
    email_subject = email_subject_var.get()
    email_body = email_body_var.get("1.0", "end-1c")  # Get text from Text widget

    # Create an EmailMessage object
    message = EmailMessage()
    message.set_content(email_body)
    message["Subject"] = email_subject
    message["From"] = sender_email
    message["To"] = recipient_email
    context=ssl.create_default_context()

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:  # Replace with your SMTP server
        
        smtp.login(sender_email, sender_password)
        smtp.send_message(message)

    # Reset input fields
    sender_email_var.set("")
    sender_password_var.set("")
    recipient_email_var.set("")
    email_subject_var.set("")
    email_body_var.delete("1.0", "end")

# Create the main window
app = tk.Tk()
app.title("Email App")

# Create and place input fields
sender_email_label = ttk.Label(app, text="Sender's Email:")
sender_email_var = tk.StringVar()
sender_email_entry = ttk.Entry(app, textvariable=sender_email_var)

sender_password_label = ttk.Label(app, text="Sender's Password:")
sender_password_var = tk.StringVar()
sender_password_entry = ttk.Entry(app, textvariable=sender_password_var, show="*")

recipient_email_label = ttk.Label(app, text="Recipient's Email:")
recipient_email_var = tk.StringVar()
recipient_email_entry = ttk.Entry(app, textvariable=recipient_email_var)

email_subject_label = ttk.Label(app, text="Subject:")
email_subject_var = tk.StringVar()
email_subject_entry = ttk.Entry(app, textvariable=email_subject_var)

email_body_label = ttk.Label(app, text="Message Body:")
email_body_var = tk.Text(app, height=5, width=40)

send_button = ttk.Button(app, text="Send Email", command=send_email)

# Grid layout for widgets
sender_email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
sender_email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
sender_password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
sender_password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")
recipient_email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
recipient_email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")
email_subject_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
email_subject_entry.grid(row=3, column=1, padx=5, pady=5, sticky="we")
email_body_label.grid(row=4, column=0, padx=5, pady=5, sticky="ne")
email_body_var.grid(row=4, column=1, padx=5, pady=5, sticky="we")
send_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()
