import customtkinter as ctk
from CTkColorPicker import *
import colorsys

window = ctk.CTk()
window.geometry("600x680")
window.title("Color Picker")

options = ['Complementary', 'Monochromatic', 'Analogous', 'Triadic', 'Tetradic']

def hex_conversion(r, g, b):
    rr = f"{int(r * 255):02x}"
    gg = f"{int(g * 255):02x}"
    bb = f"{int(b * 255):02x}"
    hex_color = f"#{rr}{gg}{bb}"
    return hex_color

def complementary(comp_h, comp_s, comp_v):
    comp_h = ((comp_h + 180) % 360)/360
    comp_r, comp_g, comp_b = colorsys.hsv_to_rgb(comp_h, comp_s, comp_v)
    color = hex_conversion(comp_r, comp_g, comp_b)
    return color

def analogous(ana_h, ana_s, ana_v):
    ana_h1 = ((ana_h + 30) % 360)/360
    ana_h2 = ((ana_h + 60) % 360)/360
    r1, g1, b1 = colorsys.hsv_to_rgb(ana_h1, ana_s, ana_v)
    r2, g2, b2 = colorsys.hsv_to_rgb(ana_h2, ana_s, ana_v)
    color1 = hex_conversion(r1, g1, b1)
    color2 = hex_conversion(r2, g2, b2)
    return color1, color2

def triadic(tria_h, tria_s, tria_v):
    tria_h1 = ((tria_h + 120)%360)/360 
    tria_h2 = ((tria_h + 240)%360)/360
    r1, g1, b1 = colorsys.hsv_to_rgb(tria_h1, tria_s, tria_v)
    r2, g2, b2 = colorsys.hsv_to_rgb(tria_h2, tria_s, tria_v)
    color1 = hex_conversion(r1, g1, b1)
    color2 = hex_conversion(r2, g2, b2)
    return color1, color2

def tetradic(tetra_h, tetra_s, tetra_v):
    tetra_h1 = ((tetra_h + 90)%360)/360
    tetra_h2 = ((tetra_h + 180)%360)/360
    tetra_h3 = ((tetra_h + 270)%360)/360
    r1, g1, b1 = colorsys.hsv_to_rgb(tetra_h1, tetra_s, tetra_v)
    r2, g2, b2 = colorsys.hsv_to_rgb(tetra_h2, tetra_s, tetra_v)
    r3, g3, b3 = colorsys.hsv_to_rgb(tetra_h3, tetra_s, tetra_v)
    color1 = hex_conversion(r1, g1, b1)
    color2 = hex_conversion(r2, g2, b2)
    color3 = hex_conversion(r3, g3, b3)
    return color1, color2, color3

cur_label = ctk.CTkLabel(window, text="", width=25, height=15)
cur_label.grid_remove()

comp_label = ctk.CTkLabel(window, text="", width=25, height=15)
comp_label.grid_remove()

ana_label1 = ctk.CTkLabel(window, text="", width=25, height=15)
ana_label1.grid_remove()

ana_label2 = ctk.CTkLabel(window, text="", width=25, height=15)
ana_label2.grid_remove()

tria_label1 = ctk.CTkLabel(window, text="", width=25, height=15)
tria_label1.grid_remove()

tria_label2 = ctk.CTkLabel(window, text="", width=25, height=15)
tria_label2.grid_remove()

tetra_label1 = ctk.CTkLabel(window, text="", width=25, height=15)
tetra_label1.grid_remove()

tetra_label2 = ctk.CTkLabel(window, text="", width=25, height=15)
tetra_label2.grid_remove()

tetra_label3 = ctk.CTkLabel(window, text="", width=25, height=15)
tetra_label3.grid_remove()

def comp_display(color):
    comp_label.configure(fg_color=color)
    comp_label.place(x=315, y=510)
    cur_label.configure(fg_color=colorpicker.get())
    cur_label.place(x=290, y=510)

def ana_display(color1, color2):
    cur_label.configure(fg_color=colorpicker.get())
    cur_label.place(x=277.5, y=510)
    ana_label1.configure(fg_color=color1)
    ana_label1.place(x=302.5, y=510)
    ana_label2.configure(fg_color=color2)
    ana_label2.place(x=327.5, y=510)

def tria_display(color1, color2):
    cur_label.configure(fg_color=colorpicker.get())
    cur_label.place(x=277.5, y=510)
    tria_label1.configure(fg_color=color1)
    tria_label1.place(x=302.5, y=510)
    tria_label2.configure(fg_color=color2)
    tria_label2.place(x=327.5, y=510)

def tetra_display(color1, color2, color3):
    cur_label.configure(fg_color=colorpicker.get())
    cur_label.place(x=265, y=510)
    tetra_label1.configure(fg_color=color1)
    tetra_label1.place(x=290, y=510)
    tetra_label2.configure(fg_color=color2)
    tetra_label2.place(x=315, y=510)
    tetra_label3.configure(fg_color=color3)
    tetra_label3.place(x=340, y=510)

def combobox(choice):
    print("combobox dropdown clicked:", choice)
    hue, sat, val = conversion()
    if choice == 'Complementary':
        cur_label.place_forget()
        ana_label1.place_forget()
        ana_label2.place_forget()
        tria_label1.place_forget()
        tria_label2.place_forget()
        tetra_label1.place_forget()
        tetra_label2.place_forget()
        tetra_label3.place_forget()
        comp_color = complementary(hue, sat, val)
        comp_display(comp_color)

    elif choice == 'Monochromatic':
        pass

    elif choice == 'Analogous':
        cur_label.place_forget()
        comp_label.place_forget()
        tria_label1.place_forget()
        tria_label2.place_forget()
        tetra_label1.place_forget()
        tetra_label2.place_forget()
        tetra_label3.place_forget()
        ana_color1, ana_color2 = analogous(hue, sat, val)
        ana_display(ana_color1, ana_color2)

    elif choice == 'Triadic':
        cur_label.place_forget()
        comp_label.place_forget()
        ana_label1.place_forget()
        ana_label2.place_forget()
        tetra_label1.place_forget()
        tetra_label2.place_forget()
        tetra_label3.place_forget()
        tria_color1, tria_color2 = triadic(hue, sat, val)
        tria_display(tria_color1, tria_color2)

    elif choice == 'Tetradic':
        cur_label.place_forget()
        comp_label.place_forget()
        ana_label1.place_forget()
        ana_label2.place_forget()
        tria_label1.place_forget()
        tria_label2.place_forget()
        tetra_color1, tetra_color2, tetra_color3 = tetradic(hue, sat, val)
        tetra_display(tetra_color1, tetra_color2, tetra_color3)

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


