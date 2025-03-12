import random
'''import random'''
# is used to include the random module in your script. This module provides functions to generate random numbers 
# and make random selections, which can be quite useful in various scenarios like simulations, games, and data analysis.
'''whenever randomness or unpredictability is required in your programs'''

print(random.randint(1, 10))  # Output: 7 (example) every time new

colors = ['red', 'blue', 'green']
print(random.choice(colors))  # Output: 'blue' (example), next time you run you will get new answer

deck = [1, 2, 3, 4]
random.shuffle(deck)
print(deck)  # Output: [3, 1, 4, 2] (example), next time you run you will get new answer


'''import Stramlit'''
import streamlit as st
#The import streamlit command is used to include the Streamlit library in your Python script. 
# Streamlit is a Python framework that allows you to quickly build and share interactive, data-driven web applications 
# directly from your Python code. It is especially popular in the fields of data analysis, machine learning, and scientific visualization.

import streamlit as st

# Simple app example
st.title("Welcome to Streamlit!")
st.write("This is a simple web app built using Streamlit.")
number = st.slider("Choose a number", 0, 100)
st.write(f"You selected: {number}")


'''session state'''
#Since Streamlit re-executes the script from top to bottom whenever an interaction occurs 
# (like clicking a button or changing a slider), Session State becomes essential to store and persist data, 
# such as user inputs, counters, or application states.

# application current state stores in the web browser, when restart it will re renders from the browser

'''useState hook'''  # same as session state in streamlit 
# it memorize the UI or app or function etc..... to re use in react 