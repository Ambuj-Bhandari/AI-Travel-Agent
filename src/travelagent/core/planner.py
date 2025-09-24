from langchain_core.messages import HumanMessage,AIMessage
from src.travelagent.chains.itinerary_chains import generate_itinerary
from src.travelagent.logging import logger
from src.travelagent.exception import ChatbotException
import sys

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city = ""
        self.interests = []
        self.num_of_days = 1
        self.itinerary = ""
        
        logger.info("Initialized Travel Planner Instance")
    
    def set_city(self,city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City Set Successfully!!")
        except Exception as e:
            logger.error(e)
            raise ChatbotException(e,sys)
    
    def set_interests(self,interests:str):
        try:
            self.interests = [i.strip() for i in interests.split(",")]
            self.messages.append(HumanMessage(content=interests))
            logger.info("Interests Set Successfully!!")
        except Exception as e:
            logger.error(e)
            raise ChatbotException(e,sys)
    
    def set_numOfDays(self,num_of_days:int):
        try:
            self.num_of_days = int(num_of_days)
            self.messages.append(HumanMessage(content=str(num_of_days)))
            logger.info("Number of Days Set Successfully!!")
        except Exception as e:
            logger.error(e)
            raise ChatbotException(e,sys)
    
    def create_itinerary(self):
        try:
            logger.info(f"Creating Itinerary for {self.city} with interests {self.interests} for {self.num_of_days} days")
            itinerary = generate_itinerary(city=self.city,
                                           interests=self.interests,
                                           num_of_days=self.num_of_days)
            
            self.itinerary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            
            logger.info("itinerary generated successfully")
            return itinerary
        except Exception as e:
            logger.error(e)
            raise ChatbotException(e,sys)