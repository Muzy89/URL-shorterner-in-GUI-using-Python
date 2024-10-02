import tkinter as tk
from tkinter import messagebox
import pyshorteners
#1) Function to shorten the URL
def shorten_url():
    url = url_entry.get()
    if url:
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(url)
            result_entry.delete(0, tk.END)
            result_entry.insert(0, short_url)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
#2) Create the main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")

#3) Create a label and entry for the URL input
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

#4) Create a button to trigger the URL shortening
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

#5) Create an entry to display the shortened URL
result_label = tk.Label(root, text="Shortened URL:")
result_label.pack(pady=10)

result_entry = tk.Entry(root, width=50)
result_entry.pack(pady=5)

#Run the main event loop
root.mainloop()