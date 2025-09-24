from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.travelagent.config.config import GROQ_API_KEY
from src.travelagent.logging import logger
from src.travelagent.exception import ChatbotException
import os,sys

try:
    logger.info("Creating an LLM")
    llm = ChatGroq(
        groq_api_key = GROQ_API_KEY,
        model_name = "llama-3.3-70b-versatile",
        temperature = 0.7
    )
    logger.info("LLM created Successfully")
except Exception as e:
    logger.error(e)
    raise ChatbotException(e,sys)

itinerary_prompt = ChatPromptTemplate([
    ("system","""You are an expert AI Travel Agent specializing in creating customized travel itineraries. Your task is to generate a detailed, budget-friendly travel plan based on the input: {city}, {number_of_days}, and key places or interests: {interest}.For each itinerary, follow these rules: 
                 1. Organize the plan accoring to {number_of_days} days, with recommended sightseeing spots, activities, and time slots for morning, afternoon, and evening. 
                 2. Suggest realistic travel routes, transportation options (e.g., local transport, taxis, walking), and approximate travel times between places. 
                 3. Recommend budget-friendly hotels, restaurants, cafes, and street food options.
                 4. Provide estimated costs for accommodation, food, transport, activities, and entry tickets. Break down the daily cost and also provide a total trip cost(in USD and INR).
                 5. Show expenses in both USD and INR (assume 1 USD = 87.75 INR unless otherwise specified).
                 6. Include cultural tips, safety advice, and local experiences (festivals, markets, hidden gems, nightlife, etc.).
                 7. Format the response in a clear, structured way with headers for each day and a final summary including the total estimated cost.
                 8. Keep the explanation concise but detailed enough for real travelers to follow and use directly."""),
    
    ("human","Create a itinerary for my trip")
])

def generate_itinerary(city:str , interests:list[str], num_of_days:int) -> str:
    try:
        logger.info("Invoking the LLM with the custom prompt")
        response = llm.invoke(
            itinerary_prompt.format_messages(city=city,number_of_days = num_of_days, interest=', '.join(interests))
        )
        
        logger.info("Returning the generated content")
        return response.content
    
    except Exception as e:
        logger.error(e)
        raise ChatbotException(e,sys)

