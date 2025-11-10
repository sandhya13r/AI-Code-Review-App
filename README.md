# AI Code Reviewer

An AI-powered web application that analyses Python code and provides detailed feedback on logic, style and efficiency.  
This project was built as part of the Elevate Labs Python Internship submission.

---

## Project Concept

The **AI Code Reviewer** helps developers quickly review their Python code for logical issues, stylistic improvements and performance suggestions.  
It’s designed for students, beginners and professionals who want to write cleaner, more efficient code without waiting for manual reviews.

---

## Why I Made This

As part of my Elevate Labs Python Internship, I wanted to build something practical that demonstrates both my Python and Streamlit skills.  
This project bridges the gap between writing code and receiving AI-powered review, enabling users to instantly receive feedback and improve their code quality.

---

## Features

- Upload or paste Python code for instant analysis  
- AI-powered code review using a Streamlit interface  
- Feedback on:
  - Logic correctness and readability  
  - Optimization and performance suggestions  
  - Pythonic best-practices  
- Clean and simple UI  
- Fully deployed online for immediate use  

---

## Tech Stack

- **Python**  
- **Streamlit**  
- **OpenAI API**  
- HTML / CSS (via Streamlit components)  

---

## Live Demo

[AI Code Reviewer – Streamlit App](https://sandhya13r-ai-code-review-app-app-monoau.streamlit.app/)  

---

## Run Locally

### 1. Clone the repository  

git clone https://github.com/sandhya13r/AI-Code-Review-App.git
cd AI-Code-Review-App 

### 2.Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add your OpenAI API key

Create a file named .streamlit/secrets.toml in the project root and add:

OPENAI_API_KEY = "your_api_key_here"

### 5. Run the Streamlit app
streamlit run app.py

## Screenshots
### Home Page
<img width="1900" height="732" alt="image" src="https://github.com/user-attachments/assets/72b2201d-7533-4d79-b524-8a32d72f65a1" />
<img width="1903" height="792" alt="image" src="https://github.com/user-attachments/assets/a97f91e6-55ab-4ae3-a9bd-92fedd533034" />

### Code Review Output
<img width="1855" height="789" alt="image" src="https://github.com/user-attachments/assets/4677d528-b887-45ad-8510-aaf17543e652" />
<img width="1800" height="744" alt="image" src="https://github.com/user-attachments/assets/fe314acd-1883-4d06-aeba-5798f9c5b4e4" />
<img width="1820" height="769" alt="image" src="https://github.com/user-attachments/assets/2fe7aadc-a5a5-427f-9989-7d645f61922a" />


