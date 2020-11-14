# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
import datetime
from rasa_sdk.executor import CollectingDispatcher
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

class ActionCleanRoom(Action):
    def name(self):
        return "action_clean_room_time"
    def run(self, dispatcher, tracker,domain):
        currentDT = datetime.datetime.now()
        x=currentDT.hour
        ti=tracker.get_slot("number")
        print(tracker.slots)
        print(x)
        print(ti)
        stri="Sure, I have scheduled a cleaning at "+str(int(x)+int(ti))+" today. "
        dispatcher.utter_message(text=stri)
        
