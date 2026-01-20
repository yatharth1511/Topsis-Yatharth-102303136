import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="TOPSIS Tool", layout="centered")

st.markdown(
    "<h1 style='text-align: center;'>TOPSIS Decision Making Tool</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Upload CSV, enter weights & impacts, get result via email and instantly on screen</p>",
    unsafe_allow_html=True
)

file = st.file_uploader("Upload CSV file", type=["csv"])
weights = st.text_input("Weights (comma separated)", "1,1,1,1,2")
impacts = st.text_input("Impacts (comma separated)", "+,+,-,+,+")
email = st.text_input("Email address")

if st.button("Run TOPSIS"):
    if file and email:
        with st.spinner("Running TOPSIS..."):
            files = {"file": file}
            data = {
                "weights": weights,
                "impacts": impacts,
                "email": email
            }

            response = requests.post(
                "http://127.0.0.1:8000/run-topsis/",
                files=files,
                data=data
            )

        if response.status_code == 200:
            res = response.json()

            st.success("✅ TOPSIS completed! Result sent to email 📧")

            # convert JSON to DataFrame
            df_result = pd.DataFrame(res["data"])

            st.subheader("📊 TOPSIS Result")
            st.dataframe(df_result, use_container_width=True)

            # download button
            csv = df_result.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download output.csv",
                data=csv,
                file_name="output.csv",
                mime="text/csv"
            )

        else:
            st.error("❌ Something went wrong. Please try again.")
    else:
        st.warning("Please upload a CSV file and enter an email address.")

