import requests

objetivos = ['admin', 'login', 'dashboard', 'config', 'robots.txt']
url_base = input("Ingresá la URL base (ej: http://localhost:8000): ").strip('/')

for path in objetivos:
    url = f"{url_base}/{path}"
    try:
        r = requests.get(url)
        print(f"[{r.status_code}] {url}")
    except:
        print(f"[ERROR] No se pudo acceder a {url}")
