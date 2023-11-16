import streamlit as st
import random

names = {
    0: "Vaičaitis",
    1: "Rugilė",
    2: "Simas",
    3: "Pijus",
    4: "Repečka",
    5: "Patricija",
    6: "Plungė",
    7: "Rūta",
}

random.seed(2023)

random_numbers = random.sample(range(0, 8), 8)

while (
    any([random_numbers[i] == i for i in range(0, len(names))])
    or random_numbers[1] == 3
    or random_numbers[3] == 1
    or random_numbers[4] == 7
    or random_numbers[7] == 4
):
    random_numbers = random.sample(range(0, len(names)), len(names))

st.title("Kas su kuo?")

for key, value in names.items():
    if st.button(value, key=key):
        st.success(names[random_numbers[key]])
