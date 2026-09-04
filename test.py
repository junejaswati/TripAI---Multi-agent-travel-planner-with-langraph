from tools.flight_tool import search_flights
from tools.tavily_tool import tavily_search
from backend import run_travel_agent


user_input = input("Enter your travel query: ")

res = run_travel_agent(user_input = user_input,thread_id="test_user1")
print("\nFINAL RESPONSE:\n")
print(res["itinerary"])



