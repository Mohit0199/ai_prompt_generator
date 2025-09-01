import streamlit as st
import time
from engine import PromptEngine
import threading

st.set_page_config(page_title="AI Prompt Generator", page_icon="⚡", layout="wide")


# Custom CSS
st.markdown(
    """
    <style>
        /* Make sidebar wider, but still collapsible */
        [data-testid="stSidebar"] {
            width: 350px !important;
        }
        /* Ensure when sidebar is collapsed, main content takes full width */
        [data-testid="stSidebar"][aria-expanded="false"] {
            width: 0px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Sidebar Info ---
st.sidebar.title("ℹ️ About this App")
st.sidebar.write(
    """
    **AI Prompt Generator** helps you transform simple, vague ideas into 
    **robust, structured, role-based prompts** you can copy directly into any LLM.

    ✅ Write in plain English.  
    ✅ Choose your preferred **tone** (Professional, Casual, Humorous, Persuasive).
    ✅ Get polished prompts instantly.

    ---
    **How to use:**  
    1. Enter your idea in the text box.  
    2. Pick your **tone**.  
    3. Click *Generate Optimized Prompt*.  
    4. Copy the ready-to-use prompt for your LLM.  

    ---
    **Pro tip:**  
    The more **specific details** you provide (e.g., target audience, format, or constraints),  
    the more **robust and tailored** your optimized prompt will be.
    """
)


# --- Main App ---
st.title("⚡ AI Prompt Generator")
st.write("Turn simple input into robust, structured prompts for any LLM.")

engine = PromptEngine()

# User input
user_text = st.text_area("✍️ Enter your idea, task, or request:", height=150)

# --- Tone Selector ---
tone = st.radio(
    "🎭 Select Tone:",
    ["Professional", "Casual", "Humorous", "Persuasive"],
    index=0,
    horizontal=True
)

# Button
if st.button("🚀 Generate Optimized Prompt"):
    if user_text.strip():
        spinner_messages = [
            "⚡ Crafting your optimized prompt...",
            "🛠️ Building the perfect structure...",
            "✨ Polishing the details...",
            "📦 Almost ready..."
        ]

        # Create a placeholder for dynamic spinner text
        status_placeholder = st.empty()
        result = {}

        # --- Run engine.ask in a background thread ---
        def run_engine():
            result["output"] = engine.ask(user_text, tone=tone)

        t = threading.Thread(target=run_engine)
        t.start()

        # --- Show spinner messages evenly until engine finishes ---
        msg_count = len(spinner_messages)
        i = 0
        while t.is_alive():
            msg = spinner_messages[i % msg_count]  # pick message
            with status_placeholder, st.spinner(msg):
                # wait a fraction of total time
                time.sleep(2.2)  
            i += 1

        # Ensure thread joined
        t.join()

        # --- Show final result ---
        optimized = result.get("output", "❌ Something went wrong.")
        st.success("Here's your optimized prompt:")
        st.code(optimized, language="markdown")

    else:
        st.warning("⚠️ Please enter some input first.")


