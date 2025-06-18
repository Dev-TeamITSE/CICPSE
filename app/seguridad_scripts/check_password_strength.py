import re

def evaluar_contraseña(pwd):
    if len(pwd) < 6:
        return "Débil"
    if re.search(r"[A-Z]", pwd) and re.search(r"[a-z]", pwd) and re.search(r"[0-9]", pwd):
        return "Fuerte"
    return "Media"

pwd = input("Ingresá una contraseña: ")
print("Nivel de seguridad:", evaluar_contraseña(pwd))
