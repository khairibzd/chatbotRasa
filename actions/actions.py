# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from pymongo import MongoClient
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from actions.database.database_connection import DataUpdate
from rasa_sdk.events import SlotSet
import requests
import json
import random




from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests



# client = MongoClient("mongodb+srv://khairiBZ1:kingragnar@cluster0.r4fmbkw.mongodb.net/")
# db = client.test  # Replace 'test' with your database name
# collection = db.places  # Replace 'users' with your collection name
# collection2 = db.restaurants  # Replace 'users' with your collection name
from typing import Any, Dict, List, Text
from pymongo import MongoClient
import random



class ActionGetPlaceByType(Action):
    def name(self) -> Text:
        return "action_fetch_place"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            affirm = tracker.get_slot('aff')
            deny = tracker.get_slot('dny')
            print("utter_already_run::",affirm , deny)
            if not affirm and not deny:
              dispatcher.utter_message(response="utter_continue_or_skip")
            else:
               type = tracker.get_slot('type')  # <--- Variable referenced here
               location = tracker.get_slot('location')
               restaurant_type = tracker.get_slot('Restauranttype')
           
               print(f"Received type: {type}, location: {location}, restaurantType: {restaurant_type}")
   
               client = MongoClient("mongodb+srv://khairiBZ1:kingragnar@cluster0.r4fmbkw.mongodb.net/")
               db = client["test"]
               collection = db["places"]
               if restaurant_type and not location:
                   # collection = db["restaurants"]
                   query = {"type": restaurant_type}
               elif restaurant_type and location:
                   query = {"location": location, "type": restaurant_type}
           
               elif location and not type:
                       dispatcher.utter_message(text="What type of place do you like?")
                       return []  # Clear location slot
               # elif type and location:
               #         print("Both type and location provided, continuing with the existing logic...")
   
               elif type and location:
                   query = {"location": location, "type": type}
               elif type and not location:
                   query = {"type": type}
               elif location and not type:
                   query = {"location": location}
               else:
                       dispatcher.utter_message(text="Please provide either type or location.")
                       return []
   
               print(f"Querying with parameters: {query}")
               places = collection.find(query)
               places = list(places)
   
               if places:
                   selected_place = random.choice(places)
                   place_name = selected_place.get('name')
                   place_image = selected_place.get('placeImage')
                   dispatcher.utter_message(text=place_name)
                   dispatcher.utter_message(image=place_image)
               else:
                   dispatcher.utter_message(text="No places found matching your criteria.")
        except Exception as e:
            print('Error fetching place data:', e)
            dispatcher.utter_message(text="An error occurred while fetching place data.")
            raise e  

        # Set all slots to null
        return []
    
#       # Clear slots
# class ActionGetRestaurantByType(Action):
#     def name(self) -> Text:
#         return "action_fetch_restaurant"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         try:
#             Restauranttype = tracker.get_slot('Restauranttype')
#             # location = tracker.get_slot('location')

#             print(f"Received type: {Restauranttype}")
#             query = {}
            
#             if Restauranttype:
#                 query = {"type": Restauranttype}
           
#             else:
#                 dispatcher.utter_message(text=" i can give you a best recommendation about  an Italian , romantic or fast food restaurant?!")
#                 return []

#             print(f"Querying with parameters: {query}")
#             places = collection2.find(query)
#             places = list(places)

#             if places:
#                 selected_place = random.choice(places)
#                 place_name = selected_place.get('name')
#                 place_image = selected_place.get('placeImage')
#                 dispatcher.utter_message(text=place_name)
#                 dispatcher.utter_message(image=place_image)
#             else:
#                 dispatcher.utter_message(text="No places found matching your criteria.")
#         except Exception as e:
#             print('Error fetching place data:', e)
#             dispatcher.utter_message(text="An error occurred while fetching place data.")
#             raise e  

#         # Set all slots to null
#         return [SlotSet("Restauranttype", None)]  # Clear type and location slots



# class ActionGetPlaceByLocation(Action):
#     def name(self) -> Text:
#         return "action_get_place_by_location"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         try:
#             location = tracker.get_slot('location')
#             print('test location',location)
#             places = collection.find({"location": location})
#             filtered_places = list(places)
#             if filtered_places:
#                 # Randomly select a place from the filtered list
#                 selected_place = random.choice(filtered_places)
#                 place_name = selected_place.get('name')
#                 place_image = selected_place.get('placeImage')
#                 dispatcher.utter_message(text=place_name)
#                 dispatcher.utter_message(image=place_image)
#             else:
#                 dispatcher.utter_message(text="I can give you a recommendation about restaurants, places, hotels, or beaches. Please tell me what you want.")
#         except requests.exceptions.RequestException as e:
#             print('Error fetching restaurant data:', e)
#             dispatcher.utter_message(text="i can give you a recommendation about restaurants , place ,hotels or beaches tell me what you want")
#             raise e  

#         # Set all slots to null
        
#         return []






# def name(self):

#     return "action_reset_all_slots"

# def run(self, dispatcher, tracker, domain):

#     return [AllSlotsReset()]




# class ActionAskLastName(Action):
#     def name(self) -> Text:
#         return "action_ask_last_name"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_ask_state")
#         return [SlotSet('lastName', tracker.latest_message.get('text'))]



# class ActionAskAge(Action):
#     def name(self) -> Text:
#         return "action_ask_age"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_ask_phone")
#         return [SlotSet('age', tracker.latest_message.get('text'))]


# class ActionAskSalary(Action):
#     def name(self) -> Text:
#         return "action_ask_salary"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_ask_social_status")
#         return [SlotSet('salary', tracker.latest_message.get('text'))]



# class ActionAskState(Action):
#     def name(self) -> Text:
#         return "action_ask_state"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_ask_email")
#         return [SlotSet('state', tracker.latest_message.get('text'))]




# class ActionAskEmail(Action):
#     def name(self) -> Text:
#         return "action_ask_email"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_ask_gender")
#         return [SlotSet('email', tracker.latest_message.get('text'))]




# class ActionAskGender(Action):
#     def name(self) -> Text:
#         return "action_ask_gender"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_continue_or_skip")
#         return [SlotSet('gender', tracker.latest_message.get('text'))]




# class ActionAskPhone(Action):
#     def name(self) -> Text:
#         return "action_ask_phone"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_ask_salary")
#         return [SlotSet('phone', tracker.latest_message.get('text'))]


# class ActionAskSocialStatus(Action):
#     def name(self) -> Text:
#         return "action_ask_social_status"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_thank_user")
#         return [SlotSet('socialStatus', tracker.latest_message.get('text'))]


# class ActionSubmit(Action): 
#     def name(self) -> Text: 
#         """Unique identifier of the form""" 
#         return "action_submit"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#         DataUpdate(
#             tracker.get_slot("name"),
#             tracker.get_slot("lastName"),
#             tracker.get_slot("email"),
#             tracker.get_slot("gender"),
#             tracker.get_slot("age"),
#             tracker.get_slot("state"),
#             tracker.get_slot("phone"),
#             tracker.get_slot("salary"),
#             tracker.get_slot("socialStatus")
#         )

#         dispatcher.utter_message("Thanks for the valuable feedback.")
#         return []





















# class ActionSessionStart(Action):
#     def name(self):
#         return "greeting_action"  # Replace with your actual action name
    
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         dispatcher.utter_message("Hi! Welcome to my Rasa chatbot. What would you like to know?")

#         return []
    


# class ActionGetLoc(Action):

#     def name(self) -> Text:
#         return "action_get_loc"

#     def run(self, dispatcher: CollectingDispatcher,;
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         slot_name = tracker.get_slot("state")

#         print("slotname", slot_name)

#         dispatcher.utter_message(
#             text="So You Live In " + slot_name.title() + " , Here is the best close restaurant to you: \n")

#         return []
    

# class ActionGetName(Action):

#     def name(self) -> Text:
#         return "action_get_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         slot_name = tracker.get_slot("name")

        

#         dispatcher.utter_message(
#             text="Hey Mr " + slot_name.title() + " its good to see you how can i help you today?")

#         return []
    
# class Actiongetrestaurant(Action):

#     def name(self) -> Text:
#         return "action_get_restaurant"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         responses = "saif fast Food" #here instead of put it static we can fetch from an api or database to make it realtime response
#         print(responses)
#         dispatcher.utter_message(text = responses)

#         return []
    
# class ActionAskNotifications(Action):
#     def name(self) -> Text:
#         return "action_ask_notifications"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         # Get the user's response from the tracker
#         user_response = tracker.latest_message['text']

#         if user_response.lower() == 'yes':
#             dispatcher.utter_message(text="Okay, you want notifications.")
#         elif user_response.lower() == 'no':
#             dispatcher.utter_message(text="Okay, you don't want notifications.")
#         else:
#             dispatcher.utter_message(text="I didn't understand your response.")

#         return []