def show_messages(unsent_messages, sent_messages):
    while unsent_messages:
        current_message = unsent_messages.pop(0)
        print(f"\n{current_message}")
        sent_messages.append(current_message)

text_messages = ['Hi', 'This is a message.', 'Wow, uWu, XD']
sent_messages = []
show_messages(text_messages, sent_messages=sent_messages)

print(text_messages)
print(sent_messages)