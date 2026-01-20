from fastapi import FastAPI, UploadFile, Form
import pandas as pd
import numpy as np
import os
import smtplib
from email.message import EmailMessage

app = FastAPI()

UPLOAD_DIR = "../uploads"
OUTPUT_DIR = "../outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# TOPIS_LOGIC
def topsis(df, weights, impacts):
    matrix = df.iloc[:, 1:].values.astype(float)
    weights = np.array(weights)

    norm = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted = norm * weights

    ideal_best = np.where(impacts == "+", weighted.max(axis=0), weighted.min(axis=0))
    ideal_worst = np.where(impacts == "+", weighted.min(axis=0), weighted.max(axis=0))

    d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = d_worst / (d_best + d_worst)
    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    return df

# EMAIL_SETUP
def send_email(receiver_email, attachment_path):
    sender_email = "your_email@gmail.com"
    sender_password = "YOUR_APP_PASSWORD"


    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Attached is your TOPSIS result file.")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="output.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# API_ENDPT
@app.post("/run-topsis/")
async def run_topsis(
    file: UploadFile,
    weights: str = Form(...),
    impacts: str = Form(...),
    email: str = Form(...)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    df = pd.read_csv(file_path)

    w = list(map(float, weights.split(",")))
    i = impacts.split(",")

    result = topsis(df, w, i)

    output_path = os.path.join(OUTPUT_DIR, "output.csv")
    result.to_csv(output_path, index=False)

    send_email(email, output_path)

    return {
        "message": "TOPSIS completed. Result sent to email.",
        "data": result.to_dict(orient="records")
    }

