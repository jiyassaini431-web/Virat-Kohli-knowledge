# CODE TO BE SAVED AS 'virat_fan_app.py' (The Final Updated Version)

import sys
from datetime import date
import streamlit as st 

# --- 1. CONFIGURATION & LOGIC FUNCTIONS ---
BOT_NAME = "Virat Fan"
BIRTH_DATE = date(1988, 11, 5) 

def calculate_age(born):
    """Calculates age based on a datetime.date object."""
    today = date.today()
    # Subtract 1 if the birthday hasn't occurred yet this year
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_answer(user_query: str) -> str:
    """Finds the most relevant, detailed answer from the knowledge base."""
    clean_query = user_query.lower().strip()

    if clean_query in ["quit", "exit", "bye", "stop"]:
        return "Thank you for using the bot! The web app stays open, but you can close your browser tab."
    
    # Check for direct keyword matches (e.g., age, height)
    for keyword, data_key in KEYWORD_MAP.items():
        if keyword in clean_query:
            if data_key == "business_details":
                return f"{VIRAT_KOHLI_DATA['businesses']}\n{VIRAT_KOHLI_DATA['business_details']}"
            elif data_key == "ipl_details":
                 return f"{VIRAT_KOHLI_DATA['ipl_team']}\n{VIRAT_KOHLI_DATA['runs_ipl']}\n{VIRAT_KOHLI_DATA['ipl_records']}"
            elif data_key == "debut_details":
                return f"{VIRAT_KOHLI_DATA['odi_debut']}\n{VIRAT_KOHLI_DATA['t20i_debut']}\n{VIRAT_KOHLI_DATA['test_debut']}"
            elif data_key == "trophies_details":
                return f"{VIRAT_KOHLI_DATA['trophies_international']}\n{VIRAT_KOHLI_DATA['trophies_ipl']}\n{VIRAT_KOHLI_DATA['trophies_other']}"
            return VIRAT_KOHLI_DATA.get(data_key, "I found the topic, but the detailed data is currently unavailable.")

    return (
        "I'm sorry, I couldn't find an answer to that question about King Kohli. "
        "Try asking specifically about his **Debut**, **Trophies**, **IPL**, **Records**, **Marks**, or **Height**."
    )

# --- 2. THE ULTIMATE KNOWLEDGE BASE (Verified Facts & Stats as of Dec 2025) ---
VIRAT_KOHLI_DATA = {
    # --- Personal & General ---
    "name": "Virat Kohli",
    "full_name": "Virat Prem Kohli",
    "born": "November 5, 1988, in Delhi, India.",
    "age": f"Virat Kohli is **{calculate_age(BIRTH_DATE)} years old** (as of December 8, 2025).", # Age updated to 37
    "nickname": "His most famous nicknames are **Cheeku** (given by his Delhi state coach) and the global names **King Kohli** and **The Chase Master**.",
    "height": "Virat Kohli stands at **5 feet 9 inches (175 cm)**.", 
    "country": "He is an **Indian** international cricketer and plays for the **Indian National Cricket Team** (Team India) in ODIs.",
    "current_living": "Although he is an Indian citizen, he has recently been confirmed to be living and training in **London, UK**, during his breaks to maintain his elite physical condition.",
    "wife": "He is married to the renowned Bollywood actress and producer **Anushka Sharma**. They have two children: a daughter, Vamika, and a son, Akaay.",
    
    # --- Debut & First Match Details ---
    "odi_debut": (
        "**ODI Debut:** August 18, 2008, against **Sri Lanka** at Dambulla.\n"
        "**First Innings:** He scored **12 runs** off 22 balls, opening the innings."
    ),
    "t20i_debut": (
        "**T20I Debut:** June 12, 2010, against **Zimbabwe** at Harare.\n"
        "**First Innings:** He scored an unbeaten **26* runs** off 21 balls."
    ),
    "test_debut": (
        "**Test Debut:** June 20, 2011, against the **West Indies** at Kingston.\n"
        "**First Innings:** He scored **4 runs** off 10 balls, batting at No. 5."
    ),
    "debut_details": "Here are his debut details for all three formats:",
    
    # --- Cricket Stats & Records ---
    "role": "Right-handed top-order batsman.",
    "total_runs": f"His total international runs across all formats (Test, ODI, T20I) is **27,975+ runs**.", 
    "total_centuries": "He has a world-class total of **84 international centuries** (30 Tests, 53 ODIs, 1 T20I).",
    "runs_odi": "In One Day Internationals, he has scored **14,557+ runs** in 308 matches, holding the world record for the **most ODI centuries (53)**.", 
    "records": (
        "**World Records & Firsts (Non-IPL):**\n"
        "* **Most ODI Centuries (53):** Surpassing Sachin Tendulkar (49) to hold the all-time record.\n"
        "* **Fastest to 8k, 9k, 10k, 11k, 12k, 13k ODI Runs.**\n"
        "* **First Player** to score 500+ ODI runs at **6 different international venues**.\n"
        "* **Most Centuries in ODIs (53) and T20Is (1) by an Indian in World Cups.**\n"
        "* **Most Double Centuries (7)** as a Captain in Test Cricket (World Record)."
    ),
    "all_centuries_date": (
        "Providing all 84 centuries dates is too long for a chat, but you can search for them using his format-specific century count:\n"
        "* **ODI (53):** His first was **107 vs Sri Lanka** on Dec 24, 2009. His 53rd was **102 vs South Africa** on Dec 3, 2025.\n"
        "* **Test (30):** His first was **116 vs Australia** on Jan 24, 2012.\n"
        "* **T20I (1):** His only century was **122* vs Afghanistan** on Sep 8, 2022."
    ),
    
    # --- IPL Details ---
    "ipl_team": "He plays for the **Royal Challengers Bengaluru (RCB)** and is the only player to have played for a single franchise throughout his entire IPL career (since 2008).",
    "runs_ipl": (
        "**IPL Stats (As of IPL 2025):**\n"
        "* **Total Runs:** He is the all-time leading run-scorer in IPL history with **8,661+ runs**.\n"
        "* **Total Centuries:** He holds the record for the **most IPL Centuries (8)**."
    ),
    "ipl_records": (
        "**Key IPL Records:**\n"
        "* **Most Runs in a Single IPL Season (973 runs in 2016).**\n"
        "* **Most Centuries (8) in IPL History.**\n"
        "* **First Player** to reach 7,000 and 8,000 IPL runs."
    ),
    
    # --- Trophies & Awards ---
    "trophies_international": (
        "**Major International Trophies (As Player):**\n"
        "* **ICC ODI World Cup:** Winner (2011)\n"
        "* **ICC Champions Trophy:** Winner (2013)\n"
        "* **ICC T20 World Cup:** Winner (2024)\n"
        "* **ICC Under-19 World Cup:** Winner (2008 - As Captain)"
    ),
    "trophies_ipl": (
        "**IPL Trophy:** Winner of the **2025 Indian Premier League (IPL)** with Royal Challengers Bengaluru (RCB)."
    ),
    "trophies_other": (
        "**National/Other Major Awards:**\n"
        "* **Padma Shri** (India's fourth-highest civilian award)\n"
        "* **Rajiv Gandhi Khel Ratna Award** (Highest sporting honour in India)\n"
        "* **ICC Cricketer of the Decade** (2011-2020)"
    ),
    "trophies_details": "Here are his major national and international trophies:",

    # --- Educational Details ---
    "marks_10th_12th": (
        "**Academic Details (Known Facts):**\n"
        "* **Formal Education:** He studied at the Saviour Convent and later at West Delhi Cricket Academy.\n"
        "* **Class 10 (CBSE 2004):** His marks are publicly known, but the focus was on cricket from a young age. He scored a pass with A1 in English and A2 in Social Science, but C grades in Maths and Science.\n"
        "* **Class 12:** He did not formally complete his 12th standard, as he focused on his burgeoning domestic and international cricket career after the Under-19 World Cup."
    ),
    
    # --- Business & Finance ---
    "businesses": "Virat Kohli is a significant entrepreneur with interests across fitness, fashion, and hospitality. His key ventures include:",
    "business_details": (
        "* **WROGN:** A popular youth fashion and casual wear brand he co-owns.\n"
        "* **One8 & One8 Commune:** His premium **athleisure brand** and a chain of premium restaurants (**One8 Commune**).\n"
        "* **Chisel Fitness:** He has invested in and co-owns this chain of gyms and fitness centers."
    ),
}

# --- 3. QUERY MAPPING (Keywords for the logic function) ---
KEYWORD_MAP = {
    "age": "age", "born": "born", "birth": "born", "wife": "wife", "marriage": "wife", "children": "wife", 
    "runs": "total_runs", "centuries date": "all_centuries_date", "all centuries": "all_centuries_date",
    "centuries": "total_centuries", "odi centuries": "runs_odi", 
    "records": "records", "first player": "records", "indian player": "records",
    "business": "business_details", "brands": "business_details", "wrogn": "business_details", "one8": "business_details", 
    "height": "height", "how tall": "height", "nickname": "nickname", "cheeku": "nickname",
    
    # New Mappings for Detailed Info
    "debut": "debut_details", "opponent": "debut_details", "first match": "debut_details", "first runs": "debut_details",
    "trophies": "trophies_details", "trophy": "trophies_details", "awards": "trophies_details",
    "country": "country", "play for": "country", 
    "ipl team": "ipl_details", "ipl records": "ipl_details", "rcb": "ipl_details",
    "marks": "marks_10th_12th", "10th": "marks_10th_12th", "12th": "marks_10th_12th", 
    "living country": "current_living", "london": "current_living",
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

# Image Code 
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Virat_Kohli_at_Chinnaswamy.jpg/640px-Virat_Kohli_at_Chinnaswamy.jpg"
st.image(image_url, caption=f"The Chase Master | Nickname: {VIRAT_KOHLI_DATA['nickname'].split(' ')[-1]}", use_column_width=True)

# Input Widget (Text Box)
query = st.text_input("Ask your question here (e.g., 'What are his debut dates?', 'Which IPL records does he hold?', 'Tell me about his trophies'):", key="user_query")

# Execution Button
if st.button("Get Answer about King Kohli"):
    if query:
        with st.spinner('Searching the ultimate records...'):
            answer = get_answer(query)
        
        st.info(f"**Your Question:** {query}")
        st.markdown("### Bot Response:")
        st.success(answer)
    else:
        st.warning("Please enter a question first!")

st.markdown("---")
st.caption("An updated, single-file Q&A application built with Streamlit. Data accurate as of December 2025.")
