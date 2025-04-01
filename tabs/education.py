import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime

def education():
    st.markdown("## 🎓 Education Timeline")

    df = pd.read_csv("data/education.csv")
    df['Start Date'] = pd.to_datetime(df['Start Date'], format="%b %Y")
    df['End Date'] = df['End Date'].replace("present", datetime.today().strftime("%b %Y"))
    df['End Date'] = pd.to_datetime(df['End Date'], format="%b %Y")

    df['Date Range'] = "📅 From " + df['Start Date'].dt.strftime("%b %Y") + " until " + df['End Date'].dt.strftime("%b %Y")

    # Role label for y-axis
    df['Track'] = df['Program'] + " at " + df['Institution']

    # Sort by start date
    df = df.sort_values(by='Start Date', ascending=True)

    fig = px.timeline(
        df,
        x_start="Start Date",
        x_end="End Date",
        y="Track",
        color="Institution",
        color_continuous_scale=px.colors.sequential.Viridis,
        custom_data=['Date Range']
    )

    # Reverse Y-axis to show most recent on top
    fig.update_yaxes(autorange="reversed")

    # Calculate the full year range
    start_year = df["Start Date"].dt.year.min()
    end_year = df["End Date"].dt.year.max()
    year_ticks = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq="YS")

    # Apply year-based ticks to x-axis
    fig.update_xaxes(
        tickvals=year_ticks,
        tickformat="%Y",
        tickangle=0,
        showgrid=True,
        gridcolor="rgba(200,200,200,0.2)"
    )

    # Final layout styling
    fig.update_layout(
        height=300,
        margin=dict(l=60, r=40, t=40, b=40),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title=None,
        yaxis_title=None,
        font=dict(size=12),
        bargap=0.4
    )
    fig.update_traces(
    hovertemplate="%{y}<br>%{customdata[0]}<extra></extra>"
)
    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    # markdown for projects
    st.markdown("## 📂 School Projects")
    # hyperlink to my website
    st.markdown('### HBO:ICT Cyber Security - Data Science Minor')
    st.markdown("- **Flightscase**: In a group of four students, we developed a Streamlit app that visualizes airport delays and individual flight information. The app is in Dutch. [Flightscase Streamlit App](https://flightscase3hvagroup1.streamlit.app/)")
    st.markdown("- **Titanic**: We created a Streamlit app with various visualizations based on the Titanic disaster dataset. This project was particularly interesting because it was a follow-up assignment to improve our very first project. As a result, the app combines elements from the original version with an improved version, incorporating the skills we learned throughout the course. The app is also in Dutch. [Titanic Streamlit App](https://titanic2dashboardhvagroup1.streamlit.app/)")
    st.markdown("- **Machine Learning**: During the minor, we also had lessons about machine learning. We learned about various algorithms and how to implement them in Python. We also had to create a machine learning model for a specific dataset. One of the datasets we used was the Titanic dataset. We had to create a model that could predict whether a passenger would survive or not based on various features. We used various algorithms, including logistic regression, decision trees, Gradient Boosting, and Random Forest. We also learned about the importance of feature selection and how to evaluate the performance of our models. This project was a great way to learn about machine learning and its applications in real-world scenarios.")
    st.markdown("- **Motion Amplification**: In a group of three students, we wrote a python notebook that uses OpenCV to analyze video footage of a vibrating object. The goal was to amplify the motion of the object and visualize it in a way that makes it easier to understand. We used various techniques. It looked really cool, but I don't have a link to it.")
    
    st.markdown("### HBO:ICT Cyber Security")
    st.markdown("- **Captive Portal**: This was my first school project in a team. We created a login page by using Python and Flask. The goal was to create a captive portal that would allow users to log in to a network. We used various techniques, including HTML, CSS, and several configurations within Linux to create the login page. We also learned about the importance of security and how to protect user data. This project was a great way to learn about web development and security. But more importantly, I learned to work with a team. It was tuff, because most of my teammates didn't do much.")
    st.markdown("- **Capture the Flag**: In a group of five students, we developed an interactive Capture the Flag (CTF) game using Python and Flask. The game is designed to teach students about cybersecurity concepts and techniques in a fun and engaging way. Unfortunately, the website was not online, so I cannot provide a link to it.")
    st.markdown("- **Anomaly Detection**: As an idividual project, I had to implement an anomaly detection algorithm within PFsense (a firewall/router) to detect potential threats. The project was a bit of a challenge, but I learned a lot about network security and how to identify unusual patterns in network traffic.")
    st.markdown("- **Math**: In middle school I had mathematics for social studies. For this study, I had to learn about Mathematics for scientific studies.")
    st.markdown("- **Internship**: During my internship, I massively improved my skills in Python. I had to work more with python classes, which I rarely did before. I also learned about docker, APIs, Django, CVEs and much more!")

    st.markdown("### HBO:ICT Cyber Security - Theme Semester Mobile Development")
    st.markdown("- **Kotlin**: During this theme semester, I had to learn Kotlin and make tons of android apps. I learned a lot about APIs, JSON, and how to work with them. I created a rock paper scissors game and an cocktail app, that uses the cocktaildb API to get cocktail recipes based on the ingredients you have. It was a lot of fun to work with Kotlin, but if I'm being honest, my apps were visually not that great.")
    st.markdown("- **.NET MAUI**: I had to make a .NET MAUI app for a group project. I learned much about C# and how to work with .NET MAUI. This language was a bit tuff because it was really new and there was no documentation about it.")