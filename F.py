import os
import fitz
import tkinter as tk
from tkinter import filedialog
import seaborn as sns
import matplotlib.pyplot as plt
import torch



def generate_and_display_plot():
    
    torch_tensor = torch.randn(100)

 
    sns.lineplot(x=range(len(torch_tensor)), y=torch_tensor.numpy())
    plt.title('Seaborn Plot of Torch Tensor')
    plt.show()


def select_files():
    files_selected = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files_selected:
        entry_paths.delete(0, tk.END)
        entry_paths.insert(0, ', '.join(files_selected))

def merge_and_display():
    file_paths = entry_paths.get().split(', ')
    if len(file_paths) < 2:
        status_label.config(text="Select at least two PDF files.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_file:
        merge_pdfs(file_paths, output_file)
        status_label.config(text=f"PDFs merged and saved to {output_file}")
        generate_and_display_plot()

root = tk.Tk()
root.title("PDF Merging with GUI")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)

label_paths = tk.Label(frame, text="Select PDF Files:")
label_paths.grid(row=0, column=0, sticky='e')

entry_paths = tk.Entry(frame, width=50)
entry_paths.grid(row=0, column=1, padx=5)

button_browse = tk.Button(frame, text="Browse", command=select_files)
button_browse.grid(row=0, column=2, padx=5)

button_merge = tk.Button(frame, text="Merge PDFs", command=merge_and_display)
button_merge.grid(row=1, column=1, pady=10)

status_label = tk.Label(frame, text="")
status_label.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
