from pymongo import MongoClient
import streamlit as st
import re

uri = "mongodb+srv://shivano1:shivaips32567@cluster0.h1pqbge.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.Guvi_atm

# Define the title text
title_text = "GUVI BANK"

# Use HTML/CSS to center align the title
st.markdown(
    f"""
    <h1 style='text-align: center; color: black;'>{title_text}</h1>
    """,
    unsafe_allow_html=True
)
# Define a function to get or create session state
def get_session_state():
    session_state = st.session_state
    if "logged_in" not in session_state:
        session_state.logged_in = False
    return session_state

def register():
    st.subheader("Register")
    name = st.text_input("Enter your name:", key="register_name_input")
    email = st.text_input("Enter your email:", key="register_email_input")
    ph = st.text_input("Enter your phone number:", key="register_ph_input")
    city = st.text_input("Enter your city name:", key="register_city_input")
    password = st.text_input("Create your 4 Digit PIN number:", type='password', key="register_pass_input")
    re_pass = st.text_input("Re-enter your PIN number:", type='password', key="register_repass_input")

    if st.button("Register"):
        if not re.match(r"[^@]+@gmail\.com$", email):
            st.error("Invalid email format. Please enter a valid email address.")
            return

        if not ph.isdigit() or len(ph) != 10:
            st.error("Invalid phone number. Please enter a 10-digit number.")
            return

        if not ph.isdigit() or len(password) != 4:
            st.error("Invalid PIN number. Please set 4 digit PIN number")
            return

        if re_pass != password:
            st.error("Passwords do not match. Please re-enter.")
            return

        # Create a collection with the user's name
        customer_name = name.replace(' ', '_') + '_data'
        records = db[customer_name]

        # Storing user data in MongoDB
        biodata = {
            "Name": name,
            "Email": email,
            "Phone Number": ph,
            "Password": password,
            "Balance": 0
        }
        records.insert_one(biodata)

        st.success("Registration successful!")

def login(customer_name, x, y):
    session_state = get_session_state()
    if session_state.logged_in:
        return True

    st.info("New user? Please register.")

    if st.button("Login"):
        records = db[customer_name]
        user_data = records.find_one({"$or": [{"Email": x}, {"Phone Number": x}]})
        collection_names = db.list_collection_names()

        if customer_name in collection_names:
            if user_data:
                email = user_data.get("Email")
                pwd = user_data.get("Password")
                user_name = user_data.get("Name")
                ph = user_data.get("Phone Number")
                bal = user_data.get("Balance")

                if (x == email or x == ph) and y == pwd:
                    st.success("Login Successful")
                    st.subheader("WELCOME TO GUVI BANK")
                    st.markdown("*****{}*****".format(user_name.upper()))

                    session_state.logged_in = True
                    return True  # Return True if login successful
                else:
                    st.error("Invalid credentials. Please check your email/password")
            else:
                st.error("Invalid credentials. Please check your email/phone number.")
        else:
            st.error("Invalid name! Use registered name")

    return False  # Return False if login failed

def deposit(customer_name, x, y):
    records = db[customer_name]
    user_data = records.find_one({"$or": [{"Email": x}, {"Phone Number": x}]})
    bal = user_data.get("Balance")

    amount = st.number_input("Enter amount to deposit:")
    if st.button("Deposit"):
        new_balance = bal + amount
        records.update_one({"$or": [{"Email": x}, {"Phone Number": x}]}, {"$set": {"Balance": new_balance}})
        st.success("Deposit successful. Current balance: {}".format(new_balance))

def withdraw(customer_name, x, y):
    records = db[customer_name]
    user_data = records.find_one({"$or": [{"Email": x}, {"Phone Number": x}]})
    bal = user_data.get("Balance")

    amount = st.number_input("Enter amount to withdraw:")
    if st.button('Withdraw'):
        if amount > bal:
            st.error("Insufficient balance.")
        else:
            new_balance = bal - amount
            records.update_one({"$or": [{"Email": x}, {"Phone Number": x}]}, {"$set": {"Balance": new_balance}})
            st.success("Withdrawal successful. Current balance: {}".format(new_balance))

def view_balance(customer_name, x):
    records = db[customer_name]
    user_data = records.find_one({"$or": [{"Email": x}, {"Phone Number": x}]})
    bal = user_data.get("Balance")

    pwd = user_data.get("Password")
    pin = st.text_input("Please enter your PIN: ", type='password')
    proceed_button = st.button("Proceed")
    if proceed_button and pwd == pin:
        st.info("Account Balance : {}".format(bal))
    elif proceed_button:
        st.error("Invalid PIN")

def main():
    choice = st.sidebar.radio("Login/Register/Exit", ["Login", "Register", "Exit"])
    if choice == 'Register':
        register() 
    elif choice == 'Login':
        name = st.text_input("Enter your full name:", key="login_name_input")
        customer_name = name.replace(' ', '_') + '_data'
        x = st.text_input("Enter your email address / Phone number:", key="login_mail_input")
        y = st.text_input("Enter your pin number:", type='password', key="login_pass_input")
        
        if login(customer_name, x, y):  
            service = st.selectbox("Select Service", ["None", "Deposit", "Withdraw", "View Balance"])
            if service == 'None':
                st.error("Please select a service!")
            elif service == 'Deposit':
                deposit(customer_name, x, y)
            elif service == 'Withdraw':
                withdraw(customer_name, x, y)
            elif service == 'View Balance':
                view_balance(customer_name, x)
    elif choice == 'Exit':
        st.subheader("Thank you for choosing Guvi Bank! Have a great day ")

main()
