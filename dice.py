import tkinter as tk
from random import randint
from PIL import Image, ImageTk
import pygame

def roll_dice():
    dice_result = randint(1, 6)
    result_label.config(text=f"{dice_result}")
    dice_image = dice_images[dice_result - 1]
    image_label.config(image=dice_image)
    image_label.image = dice_image  

    sound_index = randint(0, 7)
    dice_sounds[sound_index].play()

pygame.mixer.init()

root = tk.Tk()
root.title("Roll Dice")

dice_images = []
for i in range(1, 7):
    img = Image.open(f"dice{i}.png")
    img = img.resize((100, 100)) 
    dice_images.append(ImageTk.PhotoImage(img))

root.geometry("300x300")

dice_sounds = []
for i in range(1, 9):
    sound = pygame.mixer.Sound(f"diceroll{i}.wav")
    dice_sounds.append(sound)

result_label = tk.Label(root, text="Result: ", font=('Times New Roman', 18))
result_label.pack(pady=20)

image_label = tk.Label(root)
image_label.pack(pady=20)

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=('Times New Roman', 14))
roll_button.pack(pady=20)

root.mainloop()