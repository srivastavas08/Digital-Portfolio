#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 09:31:25 2023

@author: kiranchandra
"""

from pathlib import Path
import streamlit as st
from PIL import Image


#----Declaring Paths--------

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

NAME = "Kiran Chandra"
EMAIL = "srivastavaskc@gmail.com"

# ------ Page Config ----------

st.set_page_config(page_title="Digital Resume | Kiran Chandra", page_icon=":wave:", layout="wide")



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)



# --- HERO SECTION ---
col1, col2= st.columns([2,4], gap="small")
with col1:
    st.image(profile_pic, width=300)


    
with col2:
    st.title(NAME)
    st.write("Experienced Data Analyst adept at analysing and interpreting data, performing statistical analysis,creating data visualisations, utilising SQL and NoSQL databases, developing automations and REST APIs, collaborating cross-functionally, and delivering presentations and reports. Strong skills in Tableau, Excel, and Python.")
    st.write("📧", EMAIL)
    col3, col4, col5, col6 =st.columns(4)
    with col3:
        st.write("[LinkedIn](https://www.linkedin.com/in/kcsrivastava/)")
    with col4:
        st.write("[Github](https://github.com/srivastavas08)")
    

    
# --- EXPERIENCE & QUALIFICATIONS ---

st.write('\n')
st.subheader("PROFESSIONAL EXPERIENCE")
col1, col2 = st.columns([4,1])
with col1:
    st.write("Data Analyst, Tata Consultancy Services")
with col2:
    st.write("06/2021 – Present, Bangalore, India")
st.write(###
    """
- ✔️ Analysed and interpreted data to identify trends, patterns, and insights to support business decisions.
- ✔️ Performed statistical analysis to validate data, identify outliers, and ensure data accuracy.
- ✔️ Created data visualisations using tools such as Tableau and Excel to communicate insights to stakeholders.
- ✔️ Utilised SQL and NoSQL databases to extract data and perform data manipulation.
- ✔️ Developed automations and REST APIs to streamline data workflows, improving efficiency and reducing errors
- ✔️ Collaborated cross-functionally with teams to provide data-driven solutions to meet business needs.
- ✔️ Delivered presentations and reports to communicate findings and recommendations to clients and stakeholders.
"""
)

st.write('\n')
col1, col2 = st.columns([4,1])
with col1:
    st.write("Automation Engineer, Tata Consultancy Services")
with col2:
    st.write("11/2020 – 06/2021, Bangalore, India")
st.write(###
    """
- ✔️ Developed and maintained automations using Python and Veeva to streamline workflows.
- ✔️ Utilised ServiceNow to manage incidents and requests.
- ✔️ Worked collaboratively with team members to troubleshoot and resolve issues.
- ✔️ Communicated updates and recommendations to clients.

"""
)


st.write('\n')
st.subheader("SKILLS")
col1, col2 = st.columns(2)

st.write(
    """
- ✔️ Programming: Python, SQL, VQL, Streamlit
- ✔️ Data Visulization: Tableau, MS Excel, Plotly
- ✔️ Web Scrapping and Automations : Selenium, Beautiful Soup, REST API (Veeva API, ServiceNow)
- ✔️ CRM Softwares: Veeva Vault, Servicenow Automations.
- ✔️ Modeling: Logistic regression, linear regression, decition trees
- ✔️ Databases: Postgres, MongoDB, MySQL
- ✔️ Additional: Data Analysis and Interpretation, Statistical Analysis, Cross-functional collaboration, Root cause analysis, Presentations and reports.
"""
)

st.write('\n')
st.subheader('PROJECTS')

tab1, tab2, tab3, tab4 = st.tabs(["Project 1", "Project 2", "Project 3", "Project 4" ])

