import streamlit as st
from src.travelagent.core.planner import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Travel Agent",layout="wide")
st.title(f"\N{airplane departure} AI Travel Itineray Planner")

with st.form("Planeer_Form"):
    city = st.text_input("Enter the City Name for your Trip")
    interests = st.text_input("Enter your interests(comma-seperated) for your Trip")
    num_of_days = st.number_input("Enter the number of days you will be on your trip",min_value=1,max_value=100,step=1)
    
    submitted = st.form_submit_button("Generate Itinerary")
    
    if submitted:
        if city and interests and num_of_days:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            planner.set_numOfDays(num_of_days)
            
            itinerary = planner.create_itinerary()
            
            st.subheader(f"\N{newspaper} Your Itinerary")
            st.markdown(itinerary)
        
        else:
            st.warning("Please city, interest and Number of days to Proceed")

