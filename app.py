from unicodedata import digit
from numpy import number
import streamlit as st
import random
import string

def password_gen(size):
    Characters = string.digits + string.ascii_letters + string.punctuation
    generate_password = "".join(random.choice(Characters) for x in range(size))
    return generate_password

def printStrongNess(input_string):
    
    num = len(input_string)
    #print(num)
    # Checking lower alphabet in string
    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
     
    for i in range(num):
        if input_string[i].islower():
            hasLower = True
        if input_string[i].isupper():
            hasUpper = True
        if input_string[i].isdigit():
            hasDigit = True
        if input_string[i] not in normalChars:
            specialChar = True
 
    # Strength of password
    if (hasLower and hasUpper and
        hasDigit and specialChar and num >= 8):
        Strength = "Strong Password"
         
    elif ((hasLower or hasUpper) and
          specialChar and num >= 6):
          Strength = "Moderate Password"
    else:
          Strength = "Weak Password"
    return Strength

def main() :
    st.title("Password Generator and Classifier")
    
    operations = ["Generate Password","Classify Password","About"]
    choice = st.sidebar.selectbox("Select Operation", operations)

    if choice == "Generate Password":
        st.subheader("Generate Password")
        pass_len = st.number_input("Enter Length of Password",8,25)
        st.write(pass_len)
        if st.button("Generate"):
            custom_password = password_gen(pass_len)
            st.write(custom_password)


    elif choice == "Classify Password":
        st.subheader("Classify Strength of Password")
        password = st.text_input("Enter Password")
        if st.button("Classify"):
            strength_password = printStrongNess(password)
            st.write(strength_password)
            
            

    elif choice == 'About':
        st.subheader("About App")        
        st.markdown("Hello and Welcome guys this is a basic PASSWORD GENERATOR program using python and streamlit. Hope you guys like it!")
if __name__ == "__main__":
  main()
