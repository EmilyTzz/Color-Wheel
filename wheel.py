import customtkinter as ctk
from CTkColorPicker import *
import colorsys

window = ctk.CTk()
window.geometry("550x550")
window.title("Color Picker")

options = ['Complementary', 'Monochromatic', 'Analogous', 'Triadic', 'Tetradic']

def complementary(comp_h, comp_s, comp_v):
    comp_h = ((comp_h + 180) % 360)/360
    comp_r, comp_g, comp_b = colorsys.hsv_to_rgb(comp_h, comp_s, comp_v)
    comp_r = f"{int(comp_r * 255):02x}"
    comp_g = f"{int(comp_g * 255):02x}"
    comp_b = f"{int(comp_b * 255):02x}"
    hex_color = f"#{comp_r}{comp_g}{comp_b}"
    return hex_color


def combobox(choice):
    print("combobox dropdown clicked:", choice)
    hue, sat, val = conversion()
    if choice == 'Complementary':
        comp_color = complementary(hue, sat, val)
        print(f"This is the complementary color: {comp_color}")
        empty_label = ctk.CTkLabel(window, text="", fg_color=comp_color, width=20, height=2)
        empty_label.grid(row = 2, padx=1, pady=1)
    elif choice == 'Monochromatic':
        pass
    elif choice == 'Analogous':
        pass
    elif choice == 'Triadic':
        pass
    elif choice == 'Tetradic':
        pass

def choose_color():
    pick_color = colorpicker.get()
    print(f"You have picked {pick_color}")
    #print(conversion())
    options_box.grid()

def conversion():
    pick_color = colorpicker.get()
    # Convert hexadecimal to decimal
    r = int(pick_color[1:3], 16)/255
    g = int(pick_color[3:5], 16)/255
    b = int(pick_color[5:7], 16)/255
    #print(r, g, b)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    angle = round(h*360,1)
    return angle, s, v

options_box = ctk.CTkComboBox(master = window,
                              values = options,
                              command = combobox
                              )

colorpicker = CTkColorPicker(window,
                             width=350,
                             fg_color="#fdfdfd",
                             bg_color="#010106",
                             slider_border=5,
                             button_color="#010106",
                             button_hover_color="#010106",
                             corner_radius=10,
                             orientation="horizontal"
                             )


colorpicker.grid(row=0, padx=180, pady=(80,0))

button = ctk.CTkButton(window,
                     width=220,
                     height=50,
                     text_color='#010106',
                     text="Choose Color",
                     fg_color= "#fdfdfd",
                     corner_radius = 10,
                     font=("Arial", 20),
                     command=choose_color
                     )

options_box.set("Complementary")
options_box.grid(row=2, pady=40)
options_box.grid_remove()   # hide initially
button.grid(row=1, padx=150, pady=20)

window.mainloop()


