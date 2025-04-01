import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime

def work():
    st.markdown("## 💪 Work Experience Timeline")

    df = pd.read_csv("data/workexperience.csv")
    df['Start Date'] = pd.to_datetime(df['Start Date'], format="%b %Y")
    df['End Date'] = df['End Date'].replace("present", datetime.today().strftime("%b %Y"))
    df['End Date'] = pd.to_datetime(df['End Date'], format="%b %Y")

    df['Date Range'] = "📅 From " + df['Start Date'].dt.strftime("%b %Y") + " until " + df['End Date'].dt.strftime("%b %Y")

    # Role label for y-axis
    df['Role'] = df['job title'] + " at " + df['company']

    # Sort by start date
    df = df.sort_values(by='Start Date', ascending=True)

    fig = px.timeline(
        df,
        x_start="Start Date",
        x_end="End Date",
        y="Role",
        color="company",
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