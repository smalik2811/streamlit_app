import streamlit as st

st.header("Triumphant Trio: :blue[Unveiling the Mighty Number!]")
st.subheader("Discover the Ascendancy of Numerical Dominance :sunglasses:", divider = 'rainbow')

st.write("### Unleash the Magic of Three! Enter Your Sacred Numbers:")

main_column, img_column = st.columns(2, gap = "medium")

with main_column:
  with st.container(border = True):
    num_1 = st.number_input("Enter the Numero Uno of your trio", min_value = 0, step = 1)
    num_2 = st.number_input("Contribute the Second Symphony of Digits", min_value = 0, step = 1)
    num_3 = st.number_input("Complete the Trinity with your Third Marvelous Digit", min_value = 0, step = 1)

with img_column:
  st.write("result here")
