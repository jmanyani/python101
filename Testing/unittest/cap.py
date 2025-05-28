def cap_text(text):
    words = text.split(' ')           # Split the input into words
    capitalized_words = []            # List to store capitalized words

    for word in words:
        if word:                      # Make sure it's not an empty string
            capitalized = word[0].upper() + word[1:]  # Capitalize first letter
            capitalized_words.append(capitalized)
        else:
            capitalized_words.append('')  # Preserve spacing if needed

    return ' '.join(capitalized_words)   # Join the list back into a single string
