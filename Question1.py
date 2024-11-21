import mood_response

while True:
    mood = input(" How are you feeling today? (happy/sad/excited) or 'exit' to leave system.").lower()
    if mood == 'happy':
        mood_response.mood_responses('happy')
    elif mood == 'sad':
        mood_response.mood_responses('sad')
    elif mood == 'excited':
        mood_response.mood_responses('excited')
    elif mood == 'exit':
        print("Exiting System")
        break
    else:
        print("Invalid input, please respond with the following options: happy/sad/excited")