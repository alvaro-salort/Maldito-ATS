---
framework_version: 1.0.0
---

# Guía de Plantillas de CV y Optimización para ATS

Esta guía establece las reglas técnicas y de diseño para la confección de CVs que superen los sistemas de seguimiento de postulantes (**ATS**) y capturen la atención del reclutador en los primeros 6 segundos.

---

## 1. Reglas de Formato ATS-Friendly

1. **Estructura limpia en una o dos columnas simples**:
   - Evitar tablas anidadas complejas, cuadros de texto flotantes, gráficos de barras de habilidades (ej. "Python 80%") o íconos que contengan texto embebido invisible para los parsers.
2. **Capa de texto limpia y extraíble**:
   - Todo el contenido esencial (nombre, email, teléfono, ciudad, experiencia, educación, palabras clave) debe ser texto plano seleccionable.
   - Probar con `python herramientas/verificar_pdf.py cv/cv_<empresa>.pdf`.
3. **Encabezados estándar en español**:
   - `\section{Resumen Profesional}` o `\section{Perfil}`
   - `\section{Experiencia Laboral}`
   - `\section{Educación}`
   - `\section{Habilidades Técnicas}`
   - `\section{Proyectos Destacados}`
   - `\section{Certificaciones e Idiomas}`

---

## 2. Regla de Extensión Estricta

- **1 página** para profesionales Junior o Semi-Senior (menos de 5 años de experiencia).
- **2 páginas exactas** para profesionales Senior, Líderes Técnicos o con más de 5 años de trayectoria relevante.
- **Nunca 1.25 ni 2.1 páginas**: Un CV que desborda 3 líneas a una página adicional daña la presentación visual.

---

## 3. Estructura de Secciones

### Encabezado
- Nombre completo en tamaño prominente.
- Titular profesional conciso (*ej. "Senior Backend Engineer | Go · Python · Cloud"*).
- Contacto: Ciudad/País, Email, Teléfono, LinkedIn, GitHub/Portfolio.

### Resumen Profesional (3-4 líneas máximo)
- Resumen conciso que une tu experiencia principal, stack dominante y principal valor que aportas al puesto postulado.

### Experiencia Laboral
- Empresa, Ubicación, Puesto y Fechas (Mes Año - Mes Año).
- 3 a 5 viñetas por puesto redactadas con la **Fórmula Google XYZ** (*"Logré X medido por Y haciendo Z"*).

### Habilidades Técnicas
- Agrupadas por categoría: *Lenguajes, Frameworks, Bases de Datos, Cloud & DevOps, Metodologías*.
