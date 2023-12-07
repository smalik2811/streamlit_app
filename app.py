import streamlit as st

st.header("Triumphant Trio: :blue[Unveiling the Mighty Number!]")
# st.subheader("Discover the Ascendancy of Numerical Dominance :sunglasses:", divider='rainbow')

st.write("### Unleash the Magic of Three! Enter Your Sacred Numbers:")

main_column, result_column = st.columns(2, gap="medium")

with main_column:
    with st.container(border=True):
        num_1 = st.number_input("Enter the Numero Uno of your trio", min_value=0, step=1)
        num_2 = st.number_input("Contribute the Second Symphony of Digits", min_value=0, step=1)
        num_3 = st.number_input("Complete the Trinity with your Third Marvelous Digit",
                                   min_value=0, step=1)

def find_greatest(num_1, num_2, num_3):
    return max(num_1, num_2, num_3)

with result_column:
    if st.button("Ascend to Greatness!", type="primary"):
        greatest_num = find_greatest(num_1, num_2, num_3)
        st.write("#### Behold the Champion: The Supreme Number is Revealed!")
        with st.container(border = True):
            st.write("# {}".format(greatest_num))
st.write("__Why was the number six afraid of seven? Because seven, eight (ate), nine! Remember, numbers have appetites too!__")
