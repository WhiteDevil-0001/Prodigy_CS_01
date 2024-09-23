import tkinter as tk
from tkinter import messagebox

# Caesar Cipher function
def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
            
    return result

# Encrypt/Decrypt button handler
def process_text():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return
    
    mode = var_mode.get()
    
    if mode == "encrypt":
        result = caesar_cipher(text, shift, "encrypt")
    elif mode == "decrypt":
        result = caesar_cipher(text, shift, "decrypt")
    
    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

# Create main window
root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("400x300")
root.resizable(False, False)

# Text Input
label_text = tk.Label(root, text="Enter your message:")
label_text.pack(pady=10)

entry_text = tk.Entry(root, width=50)
entry_text.pack(pady=5)

# Shift Input
label_shift = tk.Label(root, text="Enter shift value:")
label_shift.pack(pady=10)

entry_shift = tk.Entry(root, width=10)
entry_shift.pack(pady=5)

# Mode Selection (Encrypt/Decrypt)
var_mode = tk.StringVar(value="encrypt")

frame_mode = tk.Frame(root)
frame_mode.pack(pady=10)

radio_encrypt = tk.Radiobutton(frame_mode, text="Encrypt", variable=var_mode, value="encrypt")
radio_encrypt.pack(side=tk.LEFT, padx=10)

radio_decrypt = tk.Radiobutton(frame_mode, text="Decrypt", variable=var_mode, value="decrypt")
radio_decrypt.pack(side=tk.LEFT, padx=10)

# Process Button
button_process = tk.Button(root, text="Process", command=process_text)
button_process.pack(pady=10)

# Result Output
label_result = tk.Label(root, text="Result:")
label_result.pack(pady=10)

entry_result = tk.Entry(root, width=50)
entry_result.pack(pady=5)

# Run the application
root.mainloop()
