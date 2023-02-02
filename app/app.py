"""GUI Implementation."""


import tkinter as tk

root = tk.Tk()
root.geometry("700x500")

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack()

# Create a scrollbar and associate it with the frame
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox to hold the buttons
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Add buttons to the listbox
for i in range(20):
    listbox.insert(tk.END, f'Button {i}')

# Configure the scrollbar to scroll the listbox
scrollbar.config(command=listbox.yview)

# center the list of buttons
listbox.pack(expand=True, fill=tk.BOTH)

# Create the "Add" button
add_button = tk.Button(root, text="Add")
add_button.grid(row=0, column=1, sticky="n")

# Create the "Remove" button
remove_button = tk.Button(root, text="Remove")
remove_button.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()
