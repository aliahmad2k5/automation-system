import csv
import os
from datetime import datetime

FILE = "leads.csv"

# ----------------------------
# INIT FILE (create if not exists)
# ----------------------------
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "email", "status", "time", "note"])


# ----------------------------
# AUTOMATION LOGIC
# ----------------------------
def auto_status(email):
    if "@gmail.com" in email:
        return "verified"
    return "unverified"


def fake_email_send(name, email, status):
    print("\n--- EMAIL SYSTEM ---")
    print(f"To: {email}")
    print("Subject: Welcome to our system")
    print(f"Hi {name}, your lead status is: {status}")
    print("Email sent (simulated)")
    print("--------------------\n")


def add_lead(name, email):
    status = auto_status(email)
    time = datetime.now()

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, status, time, "new lead"])

    print("\nLead saved ✔")
    print(f"Auto status: {status}")

    fake_email_send(name, email, status)


def view_leads():
    print("\n--- ALL LEADS ---")
    with open(FILE, "r") as f:
        print(f.read())


# ----------------------------
# MAIN LOOP
# ----------------------------
print("CRM AUTOMATION SYSTEM STARTED")

while True:
    print("\n1. Add Lead")
    print("2. View Leads")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        add_lead(name, email)

    elif choice == "2":
        view_leads()

    elif choice == "3":
        print("System shutting down...")
        break

    else:
        print("Invalid option")