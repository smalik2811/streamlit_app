import streamlit as st

st.header("Triumphant Trio: :blue[Unveiling the Mighty Number!]")
st.subheader("Discover the Ascendancy of Numerical Dominance :sunglasses:", divider = 'rainbow')

main_column, img_column = st.columns(2, gap = "medium")

st.write("###Unleash the Magic of Three! Enter Your Sacred Numbers:")

with main_column:
  num_1 = st.number_input("Enter the Numero Uno of your trio", min_value = 0, step = 1)
  num_2 = st.number_input("Contribute the Second Symphony of Digits", min_value = 0, step = 1)
  num_3 = st.number_input("Complete the Trinity with your Third Marvelous Digit", min_value = 0, step = 1)

with img_column:
  st.write("result here")
  st.image("https://gramener.com/comicgen/v1/comic?name=aavatar&gender=female&character=bindi&facestyle=sketchy&emotion=lookingleft&attire=saree&pose=angry&face=%23f9e6c8&shirt=%23bcd1ec&pant=%233a4e5c&box=&boxcolor=%23000000&boxgap=&mirror=")
