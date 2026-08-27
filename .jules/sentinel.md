## 2026-08-26 - Validación de Esquemas URL en Herramientas de Verificación
**Vulnerability:** Falta de restricción de esquema URL en `verificar_acceso` (`herramientas/verificar_robots.py`), lo cual permitía esquemas como `file://`, `ftp://` o URIs arbitrarias.
**Learning:** Al construir verificadores o scrapers que utilicen `urllib.parse.urlparse`, comprobar únicamente la existencia de `parsed.scheme` y `parsed.netloc` no previene la inserción de esquemas no deseados o vectores SSRF.
**Prevention:** Validar explícitamente mediante una lista blanca de esquemas permitidos (`http`, `https`) antes de procesar URLs o construir peticiones secundarias.
