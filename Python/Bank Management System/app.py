import streamlit as st
from main import Bank

bank = Bank()

st.title("🏦 Bank Management System")

menu = [
    "Create Account",
    "Deposit Money",
    "Withdraw Money",
    "View Account Details",
    "Update Account Details",
    "Delete Account"
]

choice = st.sidebar.selectbox("Select an operation", menu)

if choice == "Create Account":
    st.subheader("Open New Bank Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        if not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be a 4-digit number.")
        else:
            success, result = bank.create_account(name, int(age), email, int(pin))
            if success:
                st.success("✅ Account Created Successfully!")
                st.json(result)
            else:
                st.error(result)

elif choice == "Deposit Money":
    st.subheader("Deposit Funds")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, user = bank.deposit_money(acc_no, int(pin), int(amount))
        if success:
            st.success("💰 Amount deposited successfully!")
            st.json(user)
        else:
            st.error("❌ Failed to deposit money. Check details or amount limit (<= 10000).")

elif choice == "Withdraw Money":
    st.subheader("Withdraw Funds")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, user = bank.withdraw_money(acc_no, int(pin), int(amount))
        if success:
            st.success("💸 Amount withdrawn successfully!")
            st.json(user)
        else:
            st.error("🚫 Insufficient balance or invalid credentials.")

elif choice == "View Account Details":
    st.subheader("Your Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View Details"):
        user = bank.show_details(acc_no, int(pin))
        if user:
            st.success("🔍 Account Found")
            st.json(user)
        else:
            st.error("❌ No account found with the given details.")

elif choice == "Update Account Details":
    st.subheader("Update Account Information")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name")
    email = st.text_input("New Email")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update Details"):
        new_pin_int = int(new_pin) if new_pin.isdigit() else None
        success = bank.update_details(acc_no, int(pin), name or None, email or None, new_pin_int)
        if success:
            st.success("✅ Details updated successfully!")
        else:
            st.error("❌ Could not update. Invalid account or PIN.")

elif choice == "Delete Account":
    st.subheader("Delete Your Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        success = bank.delete_account(acc_no, int(pin))
        if success:
            st.success("🗑️ Account deleted successfully.")
        else:
            st.error("❌ Account not found or PIN incorrect.")
