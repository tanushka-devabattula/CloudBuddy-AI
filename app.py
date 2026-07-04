import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

st.set_page_config(page_title="CloudBuddy AI", page_icon="☁️")

st.title("☁️ CloudBuddy AI")
st.write("### Your AI Learning Buddy for Cloud Computing")

topic = st.text_input("Enter a Cloud Computing Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple choice questions with answers on {topic}."

        else:
            prompt = topic

        try:
            response = client.chat.completions.create(
                model="openrouter/free",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.success("Response Generated Successfully!")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(str(e))
