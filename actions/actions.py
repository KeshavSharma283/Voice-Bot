import time
import re
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

    
class SlotStatusAction(Action):
    def name(self) -> Text:
        return "action_name_given_or_not"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve the value of the slot
        slot_value = tracker.get_slot("name")

        if slot_value is not None:
            # Slot is filled
            dispatcher.utter_message(f"Your name has been recorded as: {slot_value}.")
        else:
            # Slot is not filled
            dispatcher.utter_message("Sure your identity is safe with me.")

        return []
    
    
class SlotStatusAction(Action):
    def name(self) -> Text:
        return "action_violater_name_given_or_not"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve the value of the slot
        slot_value = tracker.get_slot("violaterName")

        if slot_value is not None:
            # Slot is filled
            dispatcher.utter_message(f"The violater's name has been recorded as: {slot_value}.")
        else:
            # Slot is not filled
            dispatcher.utter_message("Try to find the name of the violater and report it.")

        return []



class PauseAction(Action):
    def name(self) -> Text:
        return "action_pause"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        time.sleep(1)  # Sleep for 1 seconds
        
        return []
    


# class AskEmployeeIDAction(Action):
#     def name(self) -> Text:
#         return "action_ask_employee_id"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         dispatcher.utter_message(template="utter_ask_employee_id")
#         return []

class ValidateEmployeeIDAction(Action):
    def name(self) -> Text:
        return "action_validate_employee_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        employee_id = next(tracker.get_latest_entity_values("employeeId"), None)

        # Define the regex pattern to match the employee ID format
        pattern = "[0-9]{4}[A][0-9][P][S][0-9]{4}[PGH]"

        if employee_id and re.fullmatch(pattern, employee_id):
            # Valid employee ID provided
            dispatcher.utter_message(template="utter_employee_id")
            return [SlotSet("employeeId", employee_id)]
        else:
            # Invalid or no employee ID provided
            dispatcher.utter_message("Invalid employee ID format. Please try again.")
            return [SlotSet("employeeId", None)]


class TimeAndDateAction(Action):
    def name(self) -> Text:
        return "action_date_and_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        time_entity = next(tracker.get_latest_entity_values("time"), None)
        date_entity = next(tracker.get_latest_entity_values("date"), None)

        if time_entity:
            # Process the time entity
            dispatcher.utter_message(f"Time: {time_entity}")

        if date_entity:
            # Process the date entity
            dispatcher.utter_message(f"Date: {date_entity}")

        return []