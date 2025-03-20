# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os

# Lista de colores de Minecraft
colors = [
    "white", "orange", "magenta", "light_blue", "yellow", "lime", "pink",
    "gray", "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black"
]

# Directorio de salida
output_dir = "spaceship_jsons"
os.makedirs(output_dir, exist_ok=True)

# Plantilla JSON
json_template = '''{
"parent": "item/generated",
"textures": {
"layer0": "comicsafio:item/navebolsillo_{color}"
}
}'''

# Generar archivos JSON para cada color
for color in colors:
    filename = f"spaceship_{color}.json"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(json_template.replace("{color}", color))

print(f"Generados {len(colors)} archivos en la carpeta '{output_dir}'.")

print("Programa creado por HubDEV")