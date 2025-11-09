import streamlit as st
from pathlib import Path
from openai import OpenAI
import os

# --- Page Configuration ---
st.set_page_config(page_title="AI Code Reviewer", page_icon="🧠", layout="wide")

# --- Load Custom CSS ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/theme_green.css")

# --- Initialize OpenAI Client ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)
else:
    client = None
    st.warning("OpenAI API key not found. Add it in Streamlit secrets to enable AI code analysis.")

# --- Function: AI Code Analysis ---
def analyze_code_with_ai(code):
    if not client:
        return "OpenAI API key not found. Please add it to Streamlit secrets first."

    prompt = f"""
    You are an expert Python developer and code reviewer.
    Analyze the following Python code:

    {code}

    Provide:
    - Syntax or logic errors (if any)
    - Suggestions to improve readability and performance
    - Code quality rating (0–100)
    - Best practices or naming improvements
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during AI analysis: {str(e)}"

# --- App Header ---
st.markdown("""
    <h1 style='text-align:center;'>AI Code Reviewer</h1>
    <p style='text-align:center; font-size:18px; opacity:0.85;'>
        Analyze, Format, and Improve Your Python Code Instantly
    </p>
""", unsafe_allow_html=True)

# --- Tabs for Input and Output ---
tab1, tab2 = st.tabs(["Code Input", "Analysis Results"])

# --- Custom Tab Styling ---
st.markdown("""
    <style>
    section[data-testid="stTabs"] div[data-baseweb="tab-list"] {
        border-bottom: none !important;
        box-shadow: none !important;
    }
    section[data-testid="stTabs"] div[data-baseweb="tab-panel"] {
        border-top: none !important;
    }
    [data-testid="stTabs"] button[aria-selected="true"] {
        position: relative;
    }
    [data-testid="stTabs"] button[aria-selected="true"]::after {
        content: "";
        position: absolute;
        bottom: -4px;
        left: 15%;
        width: 70%;
        height: 3px;
        background: #00ff80;
        border-radius: 4px;
        box-shadow: 0 0 8px rgba(0, 255, 128, 0.5);
        animation: glowMove 2s ease-in-out infinite alternate;
    }
    @keyframes glowMove {
        from { box-shadow: 0 0 6px rgba(0, 255, 128, 0.4); }
        to { box-shadow: 0 0 14px rgba(0, 255, 128, 0.6); }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================
# TAB 1 - CODE INPUT
# ==========================
with tab1:
    st.markdown("<h2 style='margin-bottom:10px;'>Upload or Paste Your Python Code</h2>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload your .py file", type=["py"])
    code_input = st.text_area("Or paste your Python code here:", height=150)

    if uploaded_file:
        code_input = uploaded_file.read().decode("utf-8")

    if code_input:
        st.markdown("### Your Code:")
        st.code(code_input, language="python")

        if st.button("Analyze Code"):
            st.session_state["code"] = code_input
            with st.spinner("Analyzing your code with AI..."):
                ai_feedback = analyze_code_with_ai(code_input)
                st.session_state["ai_feedback"] = ai_feedback
            st.success("Analysis complete! Go to the 'Analysis Results' tab.")

# ==========================
# TAB 2 - RESULTS
# ==========================
with tab2:
    st.markdown("<h2>Analysis Results</h2>", unsafe_allow_html=True)

    if "code" in st.session_state:
        st.markdown("### AI Code Review Report")
        if "ai_feedback" in st.session_state:
            st.write(st.session_state["ai_feedback"])
        else:
            st.info("Run analysis from the 'Code Input' tab to see results here.")
    else:
        st.warning("Please upload or paste your code in the first tab to proceed.")

# ==========================
# FOOTER
# ==========================
st.markdown("""
    <footer style='
        text-align:center;
        color:#00ff80;
        margin-top:40px;
        font-size:14px;
        opacity:0.85;
        letter-spacing:0.5px;
    '>
        Developed by <b>Sandhya</b> | Elevate Labs Internship Project © 2025
    </footer>
""", unsafe_allow_html=True)

