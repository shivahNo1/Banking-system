# Banking system

This Project is a simple banking application built using Streamlit and MongoDB. It allows users to register, login, deposit money, withdraw money, and view their balance. 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

GUVI BANK is a web application that simulates basic banking operations. It is designed for learning purposes and demonstrates how to integrate a web framework (Streamlit) with a NoSQL database (MongoDB).

## Features

- User Registration
- User Login
- Deposit Money
- Withdraw Money
- View Account Balance

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x
- MongoDB Atlas account or a local MongoDB server
- Streamlit library
- pymongo library

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/shivahNo1/Banking-system.git
   

2. **Install Required Python Libraries**

   ```shh
   pip install streamlit pymongo

3. **Update MongoDB URI**

   Update the MongoDB URI in the code (uri variable) with your connection string:
    ```shh
    uri = "your_mongodb_connection_string"

**Run the Streamlit app:**
 ```shh
 streamlit run app.py
  ```


## Usage

**Register**

Visit the registration page and fill in the required details to create a new account.

**Login**

Use your registered credentials to log in to your account.

**Deposit Money**

Navigate to the deposit section, enter the amount you wish to deposit, and confirm the transaction.

**Withdraw Money**

Navigate to the withdraw section, enter the amount you wish to withdraw, and confirm the transaction. Ensure you have sufficient balance before attempting to withdraw.

**View Account Balance**

Go to the balance section to view your current account balance.

## Project Structure

- **banking_code.py**: Main application file containing the Streamlit code.
- **requirements.txt**: List of Python libraries required for the project.


 


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.





## Support

For any inquiries, please contact the repository owner at email shivashankaranofficial@gmail.com 
