def check_string(text):
    if text.startswith('a') or text.startswith('A'):
        return True
    elif text.endswith('a') or text.endswith('A'):
        return True
    else:
        return False


text = input("Enter a word: ")

print(check_string(text))