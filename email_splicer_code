import tkinter as tk
import re

# root object for the window
root = tk.Tk()
# attribute title and geometry
root.title("Email Splicer")
root.geometry("800x600")

#main frame
frame = tk.Frame(root)
frame.pack(pady=10)
#header frame
header_frame = tk.Frame(frame)
header_frame.pack(pady=10)

#Frame for the output listboxes
output_frame = tk.Frame(frame)
output_frame.pack(pady=20)

#header
index_label = tk.Label(header_frame, text="Index", font=("Helvetica", 10, "bold"), width=5)
username_label = tk.Label(header_frame, text="Username", font=("Helvetica", 10, "bold"), width=30)   
domain_label = tk.Label(header_frame, text="Domain", font=("Helvetica", 10, "bold"), width=30)

#creating scrollbar
scrollbar = tk.Scrollbar(output_frame, orient="vertical")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#orienting the labels side by side
index_label.pack(side=tk.LEFT, padx=5)
username_label.pack(side=tk.LEFT, padx=5)
domain_label.pack(side=tk.LEFT, padx=5)

#creating 3 objects of listboxes for index, username, and domain of emails.
index_listbox = tk.Listbox(output_frame, height=15, width=5, yscrollcommand=scrollbar.set)
username_listbox = tk.Listbox(output_frame, height=15, width=30, yscrollcommand=scrollbar.set)
domain_listbox = tk.Listbox(output_frame, height=15, width=30, yscrollcommand=scrollbar.set)

# orienting the listboxes side by side
index_listbox.pack(side=tk.LEFT, padx=5)
username_listbox.pack(side=tk.LEFT, padx=5)
domain_listbox.pack(side=tk.LEFT, padx=5)

#controls of scrollbar
scrollbar.config(command=lambda *args: (
    index_listbox.yview(*args),
    username_listbox.yview(*args),
    domain_listbox.yview(*args)
))

def splice_emails():
    emails = email_input.get(1.0, tk.END)
    
    #reset the listboxes
    index_listbox.delete(0, tk.END)
    username_listbox.delete(0, tk.END)
    domain_listbox.delete(0, tk.END)

    all_emails = re.findall(r'\S+@\S+', emails)
    print(all_emails)

    temp_email = ""
    temp_username = []
    temp_domain = []
    usernames = []
    domains = []
    temp = False
    temp_string = ""
    for i in range(len(all_emails)):
        temp_email = ""
        temp_username = []
        temp_domain = []
        temp_string = ""
        temp_email = list(all_emails[i])
        print(temp_email)
        for j in range(len(temp_email)):
            if temp:
                temp_domain.append(temp_email[j])
            else:
                temp_username.append(temp_email[j])
            if temp_email[j]=='@':
                temp = True
            print(j)
        temp_username.pop()
        temp_string = ""
        for j in range(len(temp_username)):
            temp_string += temp_username[j]
        usernames.append(temp_string)
        temp_string = ""
        for j in range(len(temp_domain)):
            temp_string += temp_domain[j]
        domains.append(temp_string)
        temp = False
    print(usernames)
    print(domains)
    
    # reinput data into the listboxes
    # loop through the usernames and domains lists, and add each item
    # to the corresponding listbox at the same index.
    if usernames:
        for i in range(len(usernames)):
            index_listbox.insert(tk.END, i + 1)
            username_listbox.insert(tk.END, usernames[i])
            domain_listbox.insert(tk.END, domains[i])
    else:
        username_listbox.insert(tk.END, "No emails found.")


# create top label
label = tk.Label(root, text = "Enter your list of emails:")
label.pack(pady=20)

# create text box
email_input = tk.Text(root, height=2, width=30)
email_input.pack(pady=5)

# create button to splice emails
splice_button = tk.Button(root, text="Splice Emails", command=splice_emails)
splice_button.pack(pady=10)

#to keep window open
root.mainloop()