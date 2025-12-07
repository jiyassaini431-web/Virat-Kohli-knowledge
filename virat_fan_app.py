# CODE TO BE SAVED AS 'virat_fan_app.py'

import sys
from datetime import date
import streamlit as st 

# --- 1. CONFIGURATION & LOGIC FUNCTIONS ---
BOT_NAME = "Virat Fan"
BIRTH_DATE = date(1988, 11, 5) 

def calculate_age(born):
    """Calculates age based on a datetime.date object."""
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_answer(user_query: str) -> str:
    """Finds the most relevant, detailed answer from the knowledge base."""
    clean_query = user_query.lower().strip()

    if clean_query in ["quit", "exit", "bye", "stop"]:
        return "Thank you for using the bot! The web app stays open, but you can close your browser tab."
    
    for keyword, data_key in KEYWORD_MAP.items():
        if keyword in clean_query:
            if data_key == "business_details":
                return f"{VIRAT_KOHLI_DATA['businesses']}\n{VIRAT_KOHLI_DATA['business_details']}"
            return VIRAT_KOHLI_DATA.get(data_key, "I found the topic, but the detailed data is currently unavailable.")

    return (
        "I'm sorry, I couldn't find an answer to that question about King Kohli. "
        "Try asking specifically about his **Total Runs**, **Businesses/Brands**, **Wife**, **ODI Centuries**, or **Retirement**."
    )

# --- 2. THE ULTIMATE KNOWLEDGE BASE (Verified Facts & Stats as of Dec 2025) ---
VIRAT_KOHLI_DATA = {
    "name": "Virat Kohli",
    "full_name": "Virat Prem Kohli",
    "born": "November 5, 1988, in Delhi, India.",
    "age": f"Virat Kohli is **{calculate_age(BIRTH_DATE)} years old** (as of December 7, 2025).",
    "parents": "His parents were the late **Prem Kohli** (Father, a criminal lawyer, passed away 2006) and **Saroj Kohli** (Mother, a homemaker).",
    "siblings": "He has two elder siblings: a brother, **Vikas Kohli** (a businessman), and a sister, **Bhawna Kohli Dhingra**.",
    "wife": "He is married to the renowned Bollywood actress and producer **Anushka Sharma**.",
    "marriage_date": "They got married on **December 11, 2017**, in a private ceremony in Tuscany, Italy. They are lovingly called 'Virushka'.",
    "children": "They have two children: a daughter, **Vamika Kohli** (born Jan 2021), and a son, **Akaay Kohli** (born Feb 2024).",
    "friends": "His closest friends in cricket include **AB de Villiers** and **Chris Gayle**, and he shares a deep mutual respect with **MS Dhoni**.",
    "role": "Right-handed top-order batsman, universally known as 'King Kohli' and 'Chase Master'.",
    "total_runs": f"His total international runs across all formats (Test, ODI, T20I) is **27,910+ runs**.",
    "runs_test": "His Test career (retired May 2025) concluded with **9,230 runs** in 123 matches at an average of $46.85$ (30 centuries).",
    "runs_odi": "In One Day Internationals, he has scored **14,557+ runs** in 308 matches at an average of over $58.00$, holding the world record for the **most ODI centuries (53)**.",
    "runs_t20i": "His T20I career (retired 2024) finished with **4,188 runs** in 125 matches at an average of $48.69$ (1 century).",
    "runs_ipl": "He is the **leading run-scorer in IPL history** with over **8,661 runs** for the Royal Challengers Bengaluru (RCB).",
    "total_centuries": f"He has a world-class total of **84 international centuries** (30 Tests, 53 ODIs, 1 T20I).",
    "records": "He holds the world record for the **most ODI centuries (53)** and the **most double centuries (7)** as a captain in Test cricket. He is the fastest to $10,000, 11,000, 12,000$ and $13,000$ ODI runs.",
    "retirement": "He has retired from both **Test cricket** (May 2025) and **T20I cricket** (2024 T20 World Cup), focusing solely on ODIs for the national team.",
    "businesses": "Virat Kohli is a significant entrepreneur with interests across fitness, fashion, and hospitality. His key ventures include:",
    "business_details": (
        "* **WROGN:** A popular youth fashion and casual wear brand he co-owns.\n"
        "* **One8 & One8 Commune:** His premium **athleisure brand** (in partnership with PUMA) and a chain of premium restaurants (**One8 Commune**).\n"
        "* **Chisel Fitness:** He has invested in and co-owns this chain of gyms and fitness centers.\n"
        "* **FC Goa:** He holds a minority stake in the **Indian Super League (ISL)** football team.\n"
    ),
    "net_worth": "His estimated net worth is over **₹1,050 Crore** (approximately $127 million USD), driven by his contracts, IPL salary, and business profits.",
}

# --- 3. QUERY MAPPING (Keywords for the logic function) ---
KEYWORD_MAP = {
    "age": "age", "born": "born", "parents": "parents", "siblings": "siblings", "wife": "wife", 
    "marriage": "marriage_date", "children": "children", "friends": "friends", "runs": "total_runs", 
    "test runs": "runs_test", "odi runs": "runs_odi", "t20 runs": "runs_t20i", 
    "ipl runs": "runs_ipl", "centuries": "total_centuries", "odi centuries": "odi_centuries", 
    "records": "records", "retirement": "retirement", "business": "business_details", 
    "brands": "business_details", "wrogn": "business_details", "one8": "business_details", 
    "net worth": "net_worth",
}


# --- 4. STREAMLIT WEB INTERFACE (The App) ---

st.set_page_config(
    page_title="Virat Fan Q&A Bot", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Set the Streamlit UI elements
st.title("👑 The Virat Fan Q&A Bot (Ultimate Edition)")
st.markdown("---")
st.header("Hello, I am a robot who answers **EVERYTHING** about KING KOHLI!")
st.subheader(f"He is currently {VIRAT_KOHLI_DATA['age']}") 

# Input Widget (Text Box)
query = st.text_input("Ask your question here (e.g., 'Who is his wife?', 'What is his total run count?', 'Tell me about WROGN'):", key="user_query")

# Execution Button
if st.button("Get Answer about King Kohli"):
    if query:
        with st.spinner('Searching the records...'):
            answer = get_answer(query)
        
        st.info(f"**Your Question:** {query}")
        st.markdown("### Bot Response:")
        st.success(answer)
    else:
        st.warning("Please enter a question first!")

st.markdown("---")
st.caption("A completely free, single-file Q&A application built with Streamlit.")