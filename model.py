import time
import numpy as np
import pandas as pd
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

f = open('newapi.txt')
GOOGLE_API_KEY = f.read()

model = ChatGoogleGenerativeAI(
    api_key=GOOGLE_API_KEY,
    model="gemini-2.0-flash",
    temperature=1)

WRITER_SYS_PROMPT = """
You are a career strategy assistant and an expert learning-path designer.
You take the student's inputs and produce a clear, structured, step-by-step career plan to help them reach their target role.

Your output must:
- Analyze their current experience level.
- Understand their target job role and long-term career goal.
- Provide a realistic, actionable roadmap they can follow.
- Break the plan into stages (short-term, mid-term, long-term).
- Include recommended skills, courses, tool recommendations, projects, and milestones.
- Ensure the plan is personalized to the student.

Write in a simple, organized, and motivating manner.
"""


HUMAN_PROMPT_1 = """
Create a personalized career roadmap for the student based on the following details:

Name: {name}
Current Experience Level: {experience_level}
Target Job Role: {target_job_role}
Career Goal: {career_goal}

Provide a detailed, structured plan with clear steps and milestones.
"""


writer_chat_template = ChatPromptTemplate.from_messages([
    ("system", WRITER_SYS_PROMPT),
    ("human", HUMAN_PROMPT_1)
])

def generate_roadmap(name, experience_level, target_job_role, career_goal):
    chain = writer_chat_template | model | StrOutputParser()
    return chain.invoke({
        "name": name,
        "experience_level": experience_level,
        "target_job_role": target_job_role,
        "career_goal": career_goal
    })

