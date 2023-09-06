import stremlit as st

def main():
  st.title("Simple Login App")
  menu = ["Home","Login","Signup"]
  choice = st.sidebar.selectbox("Menu",menu)

  if choice == "Home":
    st.subheader("Home")
  elif choice == "Login":
    st.subheader("Login Selection")

  elif choice == "Signup":
    st.subheader("Create New Account")


if __name__ =='__main__':
  main()
