import tkinter as tk
import re
#root object for the window
root = tk.Tk()
#attribute title and geometry
root.title("Email Splicer")
root.geometry("800x600")

# Create the output labels once
username_list = tk.Label(root, text="")
domain_list = tk.Label(root, text="")

#function to splice emails after button clicked
def splice_emails():
    emails = email_input.get(1.0, tk.END)

    all_emails = re.findall(r'\S+@\S+', emails)
    
    usernames = []
    domains = []
    
    # Use a simpler and more efficient method to splice emails
    for email in all_emails:
        parts = email.split('@')
        if len(parts) == 2:
            usernames.append(parts[0])
            domains.append(parts[1])

    # Update the text of the existing labels instead of creating new ones
    username_list.config(text="Usernames: " + str(usernames))
    domain_list.config(text="Domains: " + str(domains))


#create top label
label = tk.Label(root, text = "Enter your list of emails:")
label.pack(pady=20)

#create text box
email_input = tk.Text(root, height=2, width=30)
email_input.pack(pady=5)

#create button to splice emails
splice_button = tk.Button(root, text="Splice Emails", command=splice_emails)
splice_button.pack(pady=10)

# Place the output labels in the UI
username_list.pack(pady=10)
domain_list.pack(pady=10)

#to keep window open
root.mainloop()