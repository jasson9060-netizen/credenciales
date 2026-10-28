import os
import json

def generar_datos():
    ruta_fotos = "fotos"
    if not os.path.exists(ruta_fotos):
        print("Error: No se encontró la carpeta 'fotos'.")
        return

    estructura = {}
    
    for grado in range(1, 7):
        for grupo in ["A", "B", "C", "D"]:
            nombre_carpeta = f"{grado}{grupo}"
            ruta_carpeta = os.path.join(ruta_fotos, nombre_carpeta)
            
            estructura[nombre_carpeta] = []
            
            if os.path.exists(ruta_carpeta):
                archivos = os.listdir(ruta_carpeta)
                for archivo in sorted(archivos):
                    if archivo.lower().endswith((".jpg", ".jpeg", ".png")):
                        estructura[nombre_carpeta].append(archivo)

    contenido_js = f"const baseDatosAlumnos = {json.dumps(estructura, indent=4, ensure_ascii=False)};"
    with open("datos.js", "w", encoding="utf-8") as f:
        f.write(contenido_js)

    print("¡Listo! Archivo 'datos.js' generado con éxito con todos tus alumnos.")

if __name__ == "__main__":
    generar_datos()