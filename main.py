import streamlit as safoo  #  for web application UI
import random    # for random pic 
import time

# Headings
safoo.title("QUIZ APPLICATION")

# creates list with multiple dictionary 
questions  = [
    {
        "question": "what is the capital india?",
        "option": ["Karachi", "lahore", "delhi", "other"],
        "answer": "delhi",
    },
{
     "question": "what is the currency of pakistan?",
        "option": ["rupees", "dollor", "pound", "other"],
        "answer": "rupees",
},
{
     "question": "what is the capital city of Pakistan?",
        "option": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
},
{
     "question": "which language is widely spoken in Pakistan?",
        "option": ["Hindi", "Urdu", "Punjabi", "Bengali"],
        "answer": "Urdu"
},
{
     "question": "what is the national animal of Pakistan?",
        "option": ["Tiger", "Markhor", "Lion", "Elephant"],
        "answer": "Markhor"
},
{
     "question": "which river is the longest in Pakistan?",
        "option": ["Indus River", "Ravi River", "Chenab River", "Kabul River"],
        "answer": "Indus River"
},
{
        "question": "what is the national sport of India?",
        "option": ["Cricket", "Hockey", "Football", "Kabaddi"],
        "answer": "Hockey"
},
{
        "question": "which river is considered holy in India?",
        "option": ["Ganges", "Yamuna", "Brahmaputra", "Narmada"],
        "answer": "Ganges"
},
{
        "question": "what is the famous monument in India?",
        "option": ["Eiffel Tower", "Great Wall", "Taj Mahal", "Big Ben"],
        "answer": "Taj Mahal"
},
{
        "question": "which festival is known as the festival of colors in India?",
        "option": ["Diwali", "Holi", "Eid", "Christmas"],
        "answer": "Holi"
},
{
        "question": "what is the capital of the USA?",
        "option": ["New York", "Los Angeles", "Washington, D.C.", "Chicago"],
        "answer": "Washington, D.C."
},
{
        "question": "which currency is used in the USA?",
        "option": ["Euro", "Pound", "Dollar", "Yen"],
        "answer": "Dollar"
},
{
        "question": "what is the national bird of the USA?",
        "option": ["Eagle", "Peacock", "Sparrow", "Flamingo"],
        "answer": "Eagle"
},
{
        "question": "which famous statue is located in New York City?",
        "option": ["Statue of Liberty", "Big Ben", "Eiffel Tower", "Christ the Redeemer"],
        "answer": "Statue of Liberty"
},
]

# intialize a random question (if none exists in the session state)
if "current_question" not in safoo.session_state:
    # create a varible
    safoo.session_state.current_question = random.choice(questions) # memorize all question in the list and randomize it  

#session state is a streamlit feature,  to store memory or in simple words memory for streamlit app

#get the current question from the session_state (is a streamlit features)
question = safoo.session_state.current_question   # generated question added in a variable of question

# new heading with 
safoo.subheader(question["question"])  

# create the radio button to select answer
selected_option = safoo.radio("choose your answer", question["option"], key="answer")

# submit the button to check answer
if safoo.button("submit answer"):
    if selected_option == question["answer"]:
     safoo.success("correct") 
     safoo.balloons()   # correct answer will pop up ballons on screen
    else: 
       safoo.error("incorrect, correct answer is "+ question["answer"])

# heading       Question will change after every 10 seconds with html attributes  
safoo.markdown(
    "<h3 style='font-size:15px;'>Question will change after every 10 seconds</h3>", 
    unsafe_allow_html=True
)
# question reload after 10 seconds
time.sleep(10)  # after 10 seconds new question appear

# auto generated question randomly
safoo.session_state.current_question = random.choice(questions)



# re run app or from the begining,  to display the next question
safoo.rerun()
