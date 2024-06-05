
GUVI BANK
Overview
GUVI BANK is a simple web application for managing basic banking activities such as registration, login, deposit, withdrawal, and balance inquiry. The application is built using Streamlit for the frontend and MongoDB for the backend database.

Features
User Registration: Users can register by providing their name, email, phone number, city, and a 4-digit PIN.
User Login: Users can log in using their registered email or phone number along with the 4-digit PIN.
Deposit: Users can deposit a specified amount into their account.
Withdraw: Users can withdraw a specified amount from their account, provided they have sufficient balance.
View Balance: Users can check their current account balance after entering their PIN.
Technologies Used
Frontend: Streamlit
Backend Database: MongoDB
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/guvi-bank.git
cd guvi-bank
Install the required packages:

sh
Copy code
pip install streamlit pymongo
Run the Streamlit application:

sh
Copy code
streamlit run app.py
Usage
Registration
Select "Register" from the sidebar.
Fill in the registration form with your name, email, phone number, city, and a 4-digit PIN.
Click the "Register" button to complete the registration process.
Login
Select "Login" from the sidebar.
Enter your full name, registered email or phone number, and 4-digit PIN.
Click the "Login" button.
Banking Services
Once logged in, you can select any of the following services:

Deposit: Enter the amount to deposit and click the "Deposit" button.
Withdraw: Enter the amount to withdraw and click the "Withdraw" button.
View Balance: Enter your PIN and click the "Proceed" button to view your balance.
Exit
Select "Exit" from the sidebar to log out and end your session.

Code Explanation
Title and Styling
python
Copy code
title_text = "GUVI BANK"
st.markdown(
    f"""
    <h1 style='text-align: center; color: black;'>{title_text}</h1>
    """,
    unsafe_allow_html=True
)
Session State
python
Copy code
def get_session_state():
    session_state = st.session_state
    if "logged_in" not in session_state:
        session_state.logged_in = False
    return session_state
Registration
python
Copy code
def register():
    st.subheader("Register")
    # Code to get user input and validate
    # Code to insert user data into MongoDB
    st.success("Registration successful!")
Login
python
Copy code
def login(customer_name, x, y):
    session_state = get_session_state()
    if session_state.logged_in:
        return True
    st.info("New user? Please register.")
    # Code to validate login credentials
    return False
Deposit
python
Copy code
def deposit(customer_name, x, y):
    records = db[customer_name]
    # Code to handle deposit
    st.success("Deposit successful. Current balance: {}".format(new_balance))
Withdraw
python
Copy code
def withdraw(customer_name, x, y):
    records = db[customer_name]
    # Code to handle withdrawal
    st.success("Withdrawal successful. Current balance: {}".format(new_balance))
View Balance
python
Copy code
def view_balance(customer_name, x):
    records = db[customer_name]
    # Code to view balance
    st.info("Account Balance : {}".format(bal))
Main Function
python
Copy code
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
Notes
Ensure that MongoDB Atlas is properly configured and accessible using the provided URI.
Modify the URI in the script to match your MongoDB connection string if necessary.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any questions or feedback, please contact [your email].
