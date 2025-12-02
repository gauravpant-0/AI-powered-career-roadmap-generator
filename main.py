import time
import numpy as np
import pandas as pd
import streamlit as st

from model import generate_roadmap

st.title(":blue[AI-Powered] Student Career Roadmap Generator :streamlit:")
st.header("Project Overview:", divider="blue")
st.subheader("*This project is an intelligent web-based application designed to generate personalized career roadmaps for students*")

st.subheader("Enter your details below: ")

name = st.text_input("Your name")
experience_level = st.text_input("Current Experience Level")
target_job_role = st.text_input("Target Job Role")
career_goal = st.text_input("Career Goal")

if st.button("Generate Roadmap"):
    if name and experience_level and target_job_role and career_goal:
        with st.spinner("Generating your personalized roadmap:male_detective:..."):
            output = generate_roadmap(
                name,
                experience_level,
                target_job_role,
                career_goal
            )
        st.success("Roadmap generated successfully!:cowboy_hat_face:")
        st.write(output)

    else:
        st.error("Please fill all fields before generating.")