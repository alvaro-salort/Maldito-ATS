# /postular - Flujo Integral de Postulación a Empleo

Analiza una vacante de empleo, evalúa la compatibilidad con el perfil, redacta un CV adaptado en LaTeX con la **Fórmula Google XYZ** y genera una carta de presentación de 1 página.

## Parámetros
- URL de la vacante (ej. enlace de LinkedIn, Bumeran, Get on Board, Computrabajo) o texto completo de la oferta.

## Pasos de Ejecución
1. **Extracción y Evaluación**: Extraer requisitos clave, verificar compuertas de idioma y ubicación, y calcular puntuación de compatibilidad (Fit Score 0-100).
2. **Generación de CV**: Crear `cv/cv_<empresa>_<puesto>.tex` adaptando viñetas con logros y palabras clave.
3. **Generación de Carta**: Crear `cartas_presentacion/carta_<empresa>_<puesto>.tex` con mensaje persuasivo.
4. **Verificación de PDF y ATS**: Compilar y validar que no haya desbordes y que la capa de texto sea limpia.
5. **Preparación de Entrevista**: Generar puntos clave para la entrevista técnica.
