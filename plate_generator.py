from random import randint, choice
from PIL import Image
import matplotlib.pyplot as plt

number_of_plates_to_generate = 1

letters = "ABCDEFGHIJKLMNOPRSTUVWXY" #no 'Q','Z'
symbol_positions = [
    (82,  17), 
    (143, 17),
    (203, 17),
    (314, 17),
    (385, 17),
    (455, 17)
    ]


def random_plate() -> list:
    char_list = []
    for i in range(3):
        char_list.append(str(randint(0, 9)))

    for i in range(3):
        char_list.append(choice(letters))

    return char_list


def image_from_plate(plate: list, show=False):
    background = Image.open("symbols/blank.png")
    file_name = ''
    for index, char in enumerate(plate):
        file_name += char
        symbol = f"symbols/{char}.png"
        
        img = Image.open(symbol)
        background.paste(img, symbol_positions[index])

    background = background.convert("RGB")
    background.save(f"output/{file_name}.jpg")
    
    if show:
        plt.imshow(background)
        plt.show()


def main(number_of_plates: int) -> None:
    for i in range(number_of_plates):
        plate = random_plate()
        image_from_plate(plate)
        

if __name__=="__main__":
    main(number_of_plates_to_generate)