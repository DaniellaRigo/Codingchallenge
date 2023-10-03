text_input = input(f"Enter a string: ")
reversed_text = ""
for i in range(len(text_input)):
  reversed_text = text_input[i] + reversed_text

print(f"Reversed string: {reversed_text}")
