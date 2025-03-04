import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Function to perform translation
def translate_text():
    source_text = text_input.get("1.0", tk.END).strip()
    source_lang = source_lang_combo.get()
    target_lang = target_lang_combo.get()
    
    if not source_text:
        messagebox.showerror("Error", "Please enter text to translate")
        return
    
    translator = Translator()
    try:
        translated = translator.translate(source_text, src=source_lang, dest=target_lang)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Initialize main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")
root.configure(bg="lightblue")

# Dropdown lists for language selection
languages = LANGUAGES
lang_codes = list(languages.keys())
lang_names = [languages[code].capitalize() for code in lang_codes]

# Labels
tk.Label(root, text="Enter text:", bg="lightblue").pack(pady=5)

# Text input
text_input = tk.Text(root, height=5, width=60)
text_input.pack(pady=5)

# Language selection
frame = tk.Frame(root, bg="lightblue")
frame.pack()

tk.Label(frame, text="From Language:", bg="lightblue").grid(row=0, column=0, padx=5, pady=5)
source_lang_combo = ttk.Combobox(frame, values=lang_codes, width=20)
source_lang_combo.grid(row=0, column=1, padx=5, pady=5)
source_lang_combo.set("auto")

tk.Label(frame, text="To Language:", bg="lightblue").grid(row=1, column=0, padx=5, pady=5)
target_lang_combo = ttk.Combobox(frame, values=lang_codes, width=20)
target_lang_combo.grid(row=1, column=1, padx=5, pady=5)
target_lang_combo.set("en")  # Default to English

# Translate button
tk.Button(root, text="Translate", command=translate_text, bg="green", fg="white").pack(pady=10)

# Output text area
tk.Label(root, text="Translated text:", bg="lightblue").pack(pady=5)
text_output = tk.Text(root, height=5, width=60)
text_output.pack(pady=5)

# Run the application
root.mainloop()