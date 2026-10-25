import time

import ollama
from ollama import ResponseError

from ..state import AppState

def increase_stat(stat, value):
    if stat.get() < 80:
        stat.set(clamp(stat.get() + value, 0, 100))
        return True
    else:
        return False

def tick_stat(root, stat, deduction, delay):
    root.after(delay, _tick_stat, root, stat, deduction, delay)

def _tick_stat(root, stat, deduction, delay):
    stat.set(
        clamp(stat.get() - deduction, 0, 100)
    )

    root.after(delay, _tick_stat, root, stat, deduction, delay)

def clamp(num, lower, upper):
    return min(max(num, lower), upper)

def get_ai_response(state):
    state.visible_message_history.append(
        {
            "role": "user",
            "content": state.last_sent_user.get()
        }
    )

    response = ollama.chat(
        model="gemma4:e4b",
        messages= [build_system_message(state)] + state.visible_message_history
    )

    state.visible_message_history.append(response.message)

    return response.message.content

def generate_history(_, state: AppState):
    while len(state.backstories) <= 2:
        try:
            response = ollama.chat(
                model="smollm2:135m",
                messages= [
                    {
                        "role":"system",
                        "content":
                            f'''
                                You are a grandma. Keep everything short (max 1 word)
                                Your name is: {state.grandma_name}
                                Your age is: {state.grandma_age}
                                Your traits are: {state.grandma_traits}
                                Your backstories are: {state.backstories}
                                Give a summary of your backstory based on the information provided. Who did you marry, what did you study, how did you live your life?
                            '''
                    }
                ]
            )
            state.backstories.append(response.message.content)
        except ConnectionError:
            print("Couldn't connect to Ollama.")
        except ResponseError:
            print("Couldn't find smollm2:135m model.")
        finally:
            time.sleep(10)

def build_system_message(state):
    return {
        "role": "system",
        "content":
            f'''
            You are a grandma. Short messages. No actions.
            Your name is: {state.grandma_name}
            Your age is: {state.grandma_age}
            Your traits are: {state.grandma_traits}
            Your health is: {state.grandma_health.get()}/100
            Your satiation is: {state.grandma_satiation.get()}/100
            Your hydration is: {state.grandma_hydration.get()}/100
            Your happiness is: {state.grandma_happiness.get()}/100
            Make your current status obvious, whether you are unhealthy, starving, thirsty, unhappy.
            
            Your backstory is (THAT IS JUST SOMETHING YOU KNOW):
            {"\n".join(state.backstories)}
            '''
    }