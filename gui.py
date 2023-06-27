from tkinter import Tk, Button, filedialog, Entry, Label
from main import BeadPattern


def create_pattern():
    image_path = filedialog.askopenfilename()
    size = int(size_entry.get())
    output_file_name = name_entry.get()
    n_colors = 20  # The number of unique colors (beads) you have available
    pattern = BeadPattern(image_path, output_file_name, size, n_colors)
    pattern.create_pattern()
    result_label.config(text="Pattern saved as bead_pattern.jpg")


root_tk = Tk()
root_tk.title('Image to Bead Pattern')

Label(root_tk, text='File name:').pack()
name_entry = Entry(root_tk)
name_entry.pack()

Label(root_tk, text='Pixel Size:').pack()
size_entry = Entry(root_tk)
size_entry.pack()

select_button = Button(root_tk, text='Select Image', command=create_pattern)
select_button.pack()

result_label = Label(root_tk, text='')
result_label.pack()

root_tk.mainloop()
