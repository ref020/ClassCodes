###############
#Ray Favaza
#2/14/23
#Input Analyzer
###############

import tkinter as tk
import enchant

# initialize the PyEnchant dictionary
d = enchant.Dict("en_US")

# function to analyze the input string
def analyze_input():
    input_str = input_field.get()
    try:
        # check if the input is a number
        num = float(input_str)
        is_integer = num.is_integer()
        is_prime = isprime(int(num))
        if is_integer:
            num_type = "integer"
        else:
            num_type = "decimal"
            
        if num % 2 == 0 and num_type != "decimal":
            num_parity = "even"
        else:
            num_parity = "odd"
            
        if is_prime:
            num_prime = "prime"
        else:
            num_prime = "not prime"
            
        if num_type == "integer":
            result_label.config(text=f"The input is a {num_type} number, {num_parity}, and {num_prime}.")
        else:
            result_label.config(text=f"The input is a {num_type} number.")
            
    except ValueError:
        # check if the input is a valid English word
        if d.check(input_str):
            result_label.config(text=f"The input is a string with {len(input_str)} characters and is a valid English word.")
        else:
            # provide suggested English words in case the input is not a valid English word
            suggested_words = d.suggest(input_str)
            result_label.config(text=f"The input is a string with {len(input_str)} characters and is not a valid English word. Did you mean {', '.join(suggested_words)}?")

# function to switch frames
def switch_frame(frame):
    frame.tkraise()

# function to check if a number is prime
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# create the main window
root = tk.Tk()
root.geometry("800x600")
root.title("Input Analyzer")

# create the input frame
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.BOTH, expand=True)

#The text at the top, the instructions
input_label = tk.Label(input_frame, text="Enter any kind of string:")
input_label.config(font=("Arial", 36))
input_label.pack(pady=10)

#entry box for the text to be analyzed
input_field = tk.Entry(input_frame, width=100, font=("Arial", 36))
input_field.pack(padx=10, pady=5)

#the button to activate the program
analyze_button = tk.Button(input_frame, text="Analyze", font=("Arial", 20), command=analyze_input, width=10, height=2)
analyze_button.pack(pady=10)


# create the result frame
result_frame = tk.Frame(root)

result_label = tk.Label(result_frame, text="", font=("Arial", 20), wraplength=800)
result_label.pack(pady=10)

result_frame.pack(fill=tk.BOTH, expand=True)

switch_frame(input_frame)

root.mainloop()
