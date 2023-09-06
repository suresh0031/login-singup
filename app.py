import streamlit as st

def main():
  st.title("Simple Login App")
  menu = ["Home","Login","Signup"]
  choice = st.sidebar.selectbox("Menu",menu)

  if choice == "Home":
    st.subheader("Home")
    
  elif choice == "Login":
    st.subheader("Login Selection")
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.button("Login"):
      st.success("Logged In as {}".format(username))
    

  elif choice == "Signup":
    st.subheader("Create New Account")


if __name__ =='__main__':
  main()
