import os

# la lista de colores
colors = [
    "white", "orange", "magenta", "light_blue", "yellow", "lime", "pink",
    "gray", "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black"
]

# el directorio de los archivos
output_dir = "spaceship_jsons"
os.makedirs(output_dir, exist_ok=True)

# la estructura del json
json_template = '''{
"parent": "item/generated",
"textures": {
"layer0": "comicsafio:item/navebolsillo_{color}"
}
}'''

# se generan los archivos bien pros
for color in colors:
    filename = f"spaceship_{color}.json"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(json_template.replace("{color}", color))

print(f"Creado {len(colors)} archivos en la carpeta '{output_dir}'")
print("Programa creado por HubDEV")
