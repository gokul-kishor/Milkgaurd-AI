import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="MilkGuard AI",
    page_icon="🥛",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    selected = option_menu(
        "MilkGuard AI",
        ["Dashboard","Analytics","Reports","Alerts","Profile"],
        icons=["house","graph-up","file-earmark","bell","person"],
        default_index=0
    )

# -----------------------------
# Dummy Data
# -----------------------------

safe = 98
unsafe = 12
borderline = 18

temperature = 4.2
ph = 6.7
density = 1.030
confidence = 98.4

df = pd.DataFrame({
    "Sample":["M001","M002","M003","M004","M005"],
    "Status":["Safe","Safe","Borderline","Unsafe","Safe"],
    "Temperature":[4.2,4.3,9.2,17.8,4.1],
    "pH":[6.7,6.6,6.5,8.1,6.8],
    "Density":[1.030,1.031,1.026,1.020,1.029]
})

# -----------------------------
# Dashboard
# -----------------------------

if selected=="Dashboard":

    st.title("🥛 MilkGuard AI Dashboard")

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Milk Quality","SAFE")
    c2.metric("Temperature",f"{temperature} °C")
    c3.metric("pH",ph)
    c4.metric("Density",density)
    c5.metric("Confidence",f"{confidence}%")

    st.divider()

    col1,col2 = st.columns([2,1])

    with col1:

        st.subheader("Latest Test Result")

        st.success("AI Prediction : SAFE")

        st.dataframe(df,use_container_width=True)

    with col2:

        pie = px.pie(
            names=["Safe","Borderline","Unsafe"],
            values=[safe,borderline,unsafe],
            color=["Safe","Borderline","Unsafe"],
            color_discrete_sequence=["green","orange","red"]
        )

        st.plotly_chart(pie,use_container_width=True)

    st.divider()

    col1,col2 = st.columns(2)

    with col1:

        line = px.line(
            df,
            x="Sample",
            y="Temperature",
            markers=True,
            title="Temperature Trend"
        )

        st.plotly_chart(line,use_container_width=True)

    with col2:

        bar = px.bar(
            df,
            x="Sample",
            y="Density",
            color="Status",
            title="Density Analysis"
        )

        st.plotly_chart(bar,use_container_width=True)

# -----------------------------
# Analytics
# -----------------------------

elif selected=="Analytics":

    st.title("📊 Analytics")

    st.plotly_chart(
        px.bar(
            df,
            x="Sample",
            y="Temperature",
            color="Status"
        ),
        use_container_width=True
    )

# -----------------------------
# Reports
# -----------------------------

elif selected=="Reports":

    st.title("📄 Reports")

    st.dataframe(df,use_container_width=True)

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "Milk_Report.csv"
    )

# -----------------------------
# Alerts
# -----------------------------

elif selected=="Alerts":

    st.title("🚨 Alerts")

    st.error("Sample M004 : Unsafe Milk")

    st.warning("Sample M003 : Borderline Quality")

# -----------------------------
# Profile
# -----------------------------

else:

    st.title("👤 Profile")

    st.text_input("Operator Name","GK")

    st.text_input("Milk Collection Center","MilkGuard AI")

    st.text_input("Device","Raspberry Pi 3B+")

    st.success("Device Connected")