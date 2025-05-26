#  The Lazy Chronicles – A Story Generator Powered by Python Generators

This project is a creative demonstration of how Python generators can be used to build something both memory-efficient and interactive. Instead of loading an entire story at once, this program reveals one scene at a time only when the user asks for it. The goal here is to make the experience smooth and efficient using the `yield` keyword.

##  Purpose of the Project

The idea behind this was to explore how generators work in Python, especially in scenarios where we don’t want to store a lot of data in memory. By creating a lazy-loading story, I was able to apply what I’ve learned about the `yield` statement, `next()` function, and how generator functions behave differently than regular ones.

##  Key Concepts Implemented

- Use of `yield` to pause and resume a function
- Generator-based iteration using `next()`
- Handling `StopIteration` gracefully when the story ends
- Keeping the memory footprint low by generating scenes only when needed

##  How the Program Works

When you run the script, the story unfolds scene by scene. The generator produces one scene at a time, and the user simply presses [Enter] to move forward. This is a simple but effective way to demonstrate lazy evaluation in a real-world-style interaction.

## Controls

- `Enter` → Show the next scene in the story  
- `q` + `Enter` → Exit the story early
