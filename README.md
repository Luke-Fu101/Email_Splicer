# Email Splicer

A simple Python GUI application that splits email addresses into their username and domain components. Built with tkinter as a learning project.

## Features

- Paste one or more email addresses into the text box
- Click "Splice Emails" to separate each address into username and domain
- Results displayed in a table with index, username, and domain columns

## Prerequisites

- Python 3.x
- tkinter (included with most Python installations)

On Ubuntu/Debian, if tkinter is not installed:

```bash
sudo apt install python3-tk
```

## Installation

```bash
git clone https://github.com/luketfood101/Email_Splicer.git
cd Email_Splicer
```

No additional dependencies are required.

## Usage

Run the main application:

```bash
python3 email_splicer_code_1.py
```

Or run the simplified version:

```bash
python3 New_Splicer_Code_2.py
```

## Project Structure

- `email_splicer_code_1.py` — Full-featured version with listbox UI, scrollbar, and column headers
- `New_Splicer_Code_2.py` — Simplified rewrite with cleaner parsing logic
