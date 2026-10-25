import ollama

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
        messages=state.visible_message_history
    )

    state.visible_message_history.append(response.message)

    return response.message.content

