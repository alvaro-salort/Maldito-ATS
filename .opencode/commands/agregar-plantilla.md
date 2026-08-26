# /agregar-plantilla - Registro y Validación de Nuevas Plantillas de CV

Permite incorporar nuevas plantillas de CV en formato LaTeX o Typst, validando compatibilidad con parsers ATS y reglas de extensión (1 o 2 páginas).

---

## Parámetros
- `nombre`: Nombre descriptivo de la plantilla (ej. `moderna-dos-columnas`, `ejecutiva-simple`).
- `archivo`: Ruta al archivo `.tex` o `.typ` de origen.
- `motor`: Motor de compilación requerido (`lualatex`, `xelatex`, `typst`).

---

## Pasos de Ejecución

1. **Copia y Organización**: Copiar la plantilla a `plantillas/<nombre>/`.
2. **Validación de Secciones en Español**:
   - Verificar que incluya encabezados en español: *Resumen Profesional*, *Experiencia Laboral*, *Educación*, *Habilidades Técnicas*, *Idiomas*.
3. **Prueba de Compilación**:
   - Compilar con datos de prueba y validar que no arroje errores tipográficos.
4. **Validación ATS**:
   - Ejecutar `python herramientas/verificar_pdf.py` sobre el PDF resultante para asegurar que la capa de texto se extraiga limpiamente sin caracteres ilegibles (`cid:*`).
5. **Registro**:
   - Registrar la plantilla en `.claude/skills/asistente-postulaciones/05-plantillas-cv.md` para que esté disponible en `/postular`.
