from bardapi import Bard
import streamlit as st
from streamlit_chat import message

import os
import re


os.environ['_BARD_API_KEY'] = "bQg9X_g2XOKyrXaHAbBSxsx9RbgN9VYI4ydpxAsWsJngx-NwcjIaJny2ZYz6kZpwOq8BBQ."

subject_options = {
    "1": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "2": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "3": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "4": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "5": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "6": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science"],
    "7": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science"],
    "8": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science"],
    "9": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science", "Health and Physical Education"],
    "10": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science", "Health and Physical Education"],
    "11": ['All', 'Sanskrit', 'Accountancy', 'Chemistry', 'Mathematics', 'Biology', 'Psychology', 'Geography', 'Physics', 'Hindi', 'Sociology', 'English', 'Political Science', 'History', 'Economics', 'Business Studies', 'Home Science', 'Creative Writing and Translation', 'Fine Art', 'Informatics Practices', 'Computer Science', 'Health and Physical Education', 'Biotechnology', 'Sangeet', 'Knowledge Traditions Practices of India'],
    "12": ['All', 'Mathematics', 'Physics', 'Accountancy', 'Sanskrit', 'Hindi', 'English', 'Biology', 'History', 'Geography', 'Psychology', 'Sociology', 'Chemistry', 'Political Science', 'Economics', 'Business Studies', 'Home Science', 'Urdu', 'Creative Writing & Translation', 'Fine Art', 'Computer Science', 'Informatics Practices', 'Biotechnology']
}

sensitive_content_regex = re.compile(r"[\(\[](sex|porn|nude|naked|violence|drugs|alcohol)[\)\]]")

@st.cache_data
def response_api(prompt):
    message = Bard().get_answer(prompt)['content']
    # Filter out sensitive content
    message = sensitive_content_regex.sub('', message)
    return message

st.title("GreatMinds Genie by Prastara")

user_grade = st.selectbox("Select your grade:",
                           subject_options.keys(), index=None)

if user_grade:
    subject_options_for_grade = subject_options[user_grade]

    user_subject = st.selectbox("Choose your subject",
                                subject_options_for_grade, index=None)

    if user_subject:
        user_text = st.text_input("What are looking for now: ")
        if user_text:
            if 'generate' not in st.session_state:
                st.session_state['generate'] = []
            if 'past' not in st.session_state:
                st.session_state['past'] = []
            
            output = response_api(f"Restrict responses only to NCERT textbooks and materials. Refer Grade {user_grade} subject {user_subject} and give answer to {user_text}")
            st.session_state.generate.append(output)
            st.session_state.past.append(user_text)

            if st.session_state['generate']:
                for i in range(len(st.session_state['generate']) - 1, -1, -1):
                    message(st.session_state['past'][i],
                            is_user=True, key=str(i) + '_user')
                    message(st.session_state['generate'][i], key=str(i))
