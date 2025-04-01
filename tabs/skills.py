import streamlit as st
import pandas as pd
import plotly.express as px

def skills():
    st.markdown("## Skills")
    st.write("When I was younger, I had a blind typing cursus. I learned to type without looking at the keyboard. This skill has been very useful in my work and studies. I can do 86.4 words per minute, which helps me a lot.")
    st.markdown("There are many more skills I have acquired over the years. Here are some of them:")
    # Load your skill data
    df = pd.read_csv("data/skills.csv")

    # Sort skills by level (optional for nicer visuals)
    df = df.sort_values(by="level", ascending=True)

    # Create horizontal bar chart
    fig = px.bar(
        df,
        x="level",
        y="skill",
        orientation="h",
        range_x=[0, 5],
        color="level",
        color_continuous_scale=px.colors.sequential.Viridis,
        labels={"level": "Proficiency Level", "skill": "Skill"},
        height=700
    )

    fig.update_layout(
        xaxis=dict(dtick=1),  # Show all tick levels from 0 to 5
        margin=dict(l=100, r=40, t=40, b=40),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    fig.update_coloraxes(showscale=False)

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)