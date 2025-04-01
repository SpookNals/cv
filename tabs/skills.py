import streamlit as st
import pandas as pd
import plotly.express as px

def skills():
    st.markdown("## 🎯 Skill Levels (0-5)")

    df = pd.read_csv("data/skills.csv")
    df = df.sort_values(by="level", ascending=False)

    df["level_label"] = df["level"].apply(lambda x: f"Level {x}")

    fig = px.bar_polar(
        df,
        r="level",
        theta="skill",
        color="level_label",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        template="plotly_dark",
        range_r=[0, 5]
    )

    fig.update_traces(
        marker_line_color="black",
        marker_line_width=1.5,
        hovertemplate='%{theta}: <b>%{r}</b><extra></extra>'
    )

    fig.update_layout(
    showlegend=False,
    margin=dict(t=60, b=30, l=30, r=30),
    height=600,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    polar=dict(
        bgcolor="rgba(255,255,255,0.1)",
        radialaxis=dict(
            showticklabels=False,           # 👈 hides the 0–5 labels
            ticks='',                       # optional: removes small ticks
            showline=False,                 # optional: removes radial axis line
            gridcolor="rgba(200,200,200,0.1)",
        ),
        angularaxis=dict(
            tickfont=dict(color="white"),
            gridcolor="rgba(200,200,200,0.3)"
        )
    )
)

    st.plotly_chart(fig, use_container_width=True)
