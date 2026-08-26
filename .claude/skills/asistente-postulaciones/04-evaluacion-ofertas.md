---
framework_version: 1.0.0
---

# Evaluación y Puntuación de Ofertas de Empleo (Fit Scoring)

Antes de redactar un CV o carta de presentación, el asistente debe realizar una evaluación rigurosa de la vacante contra el perfil del postulante.

---

## 1. Compuertas Previas de Elegibilidad (Hard Gates)

Si la vacante falla en cualquiera de estas compuertas, se detiene el proceso y se avisa al usuario:

### A. Compuerta de Idioma (Language Gate)
- Si la vacante exige un idioma **no declarado** en el perfil (ej. *"Alemán fluido excluyente"*): **FALLO DIRECTO (FAIL)**.
- Si exige un idioma declarado pero a un nivel superior al que posee el candidato (ej. el candidato tiene B1 y la oferta pide C1/Nativo): **ALERTA (FLAG)**. Se informa al usuario para que decida si desea postularse igual.
- Si el nivel del candidato cumple o supera el requisito: **APROBADO (PASS)**.

### B. Compuerta de Modalidad y Ubicación
- Si la oferta requiere presencialidad en una ciudad o país fuera del radio de residencia del candidato y sin soporte de reubicación: **FALLO DIRECTO (FAIL)**.
- Ofertas 100% remotas o híbridas compatibles: **APROBADO (PASS)**.

---

## 2. Dimensiones de Puntuación (0 a 100)

Toda vacante que supera las compuertas se puntúa en 5 dimensiones ponderadas:

| Dimensión | Ponderación | Criterio de Evaluación |
|---|---|---|
| **1. Match Técnico** | 35% | Coincidencia de lenguajes, frameworks, bases de datos y arquitectura requeridos. |
| **2. Nivel de Seniority y Experiencia** | 25% | Años de experiencia real, liderazgo técnico y complejidad de proyectos previos. |
| **3. Modalidad y Compensación** | 20% | Ajuste al rango salarial deseado (ARS Bruto/Neto o USD Contractor) y beneficios. |
| **4. Reputación y Estabilidad de Empresa** | 10% | Análisis de cultura, valoraciones en Glassdoor/Openqube y modelo de negocio. |
| **5. Proyección Profesional** | 10% | Posibilidad de aprendizaje de nuevas tecnologías y crecimiento en la carrera. |

### Veredicto Global:
- **80 - 100 puntos (Excelente Match)**: Prioridad máxima. Generar CV y carta altamente adaptados.
- **60 - 79 puntos (Buen Match)**: Brechas menores aprendibles. Postular destacando transferibilidad de habilidades.
- **Menos de 60 puntos (Bajo Match)**: Advertir al usuario sobre brechas significativas antes de avanzar.
