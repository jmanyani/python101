from scenes import story_generator

def main():
    print("\nWelcome to: The Lazy Chronicles 🐍")
    print("A memory-efficient tale, revealed one scene at a time.\n")
    print("Press [Enter] to see the next scene. Type 'q' to quit.\n")

    story = story_generator()
    
    while True:
        user_input = input("→ ")
        if user_input.lower() == 'q':
            print("\nYou left the story unfinished... the mystery continues!\n")
            break
        try:
            print(next(story))
        except StopIteration:
            print("\n[End] The story has ended. Hope you enjoyed this memory-efficient tale!\n")
            break

if __name__ == "__main__":
    main()
