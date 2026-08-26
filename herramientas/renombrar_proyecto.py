import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

EXTENSIONES = {".md", ".py", ".tex", ".cls", ".json", ".yml", ".yaml", ".txt", ".sh", ".bat", ".csv"}
IGNORAR_DIRS = {".git", "venv", ".venv", "__pycache__", "node_modules", "fonts"}

REEMPLAZOS = [
    ("Maldito ATS", "Maldito ATS"),
    ("Maldito ATS", "Maldito ATS"),
    ("maldito ats", "maldito ats"),
    ("MalditoATS", "MalditoATS"),
    ("maldito-ats", "maldito-ats"),
    ("maldito_ats", "maldito_ats"),
    ("MalditoATSBot", "MalditoATSBot"),
]

modificados = []

for root, dirs, files in os.walk(RAIZ):
    dirs[:] = [d for d in dirs if d not in IGNORAR_DIRS]
    for file in files:
        ruta = Path(root) / file
        if ruta.suffix.lower() in EXTENSIONES or file in {"LICENSE", ".gitignore"}:
            try:
                contenido_original = ruta.read_text(encoding="utf-8")
                contenido_nuevo = contenido_original
                for viejo, nuevo in REEMPLAZOS:
                    contenido_nuevo = contenido_nuevo.replace(viejo, nuevo)
                if contenido_nuevo != contenido_original:
                    ruta.write_text(contenido_nuevo, encoding="utf-8")
                    modificados.append(str(ruta.relative_to(RAIZ)))
            except Exception as e:
                print(f"Error procesando {ruta}: {e}")

print(f"Archivos actualizados con 'Maldito ATS': {len(modificados)}")
for m in modificados:
    print(f"- {m}")
