import streamlit as st

st.write("""
# Triumphant Trio: Unveiling the Mighty Number!
## Discover the Ascendancy of Numerical Dominance
""")

st.header("Unleash the Magic of Three! Enter Your Sacred Numbers.")

num_1 = st.number_input("Enter the Numero Uno of your trio", min_value = 0, step = 1)
num_2 = st.number_input("Contribute the Second Symphony of Digits", min_value = 0, step = 1)
num_3 = st.number_input("Complete the Trinity with your Third Marvelous Digit", min_value = 0, step = 1)
