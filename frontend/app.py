import streamlit as st
import requests

st.set_page_config(
    page_title="Python Learning Assistant",
    page_icon="🐍"
)

st.title("🐍 Python Learning Assistant")
st.write("Ask questions about Python using the provided documents.")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is a Python function?"
)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )

            if response.status_code == 200:
                data = response.json()

                st.subheader("Answer")
                st.write(data["answer"])

                st.subheader("Sources")

                for source in data["sources"]:
                    st.write(f"- {source}")

            else:
                st.error(
                    f"Backend error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the backend. "
                "Make sure FastAPI is running."
            )