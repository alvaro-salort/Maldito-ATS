# Asistente de Búsqueda Laboral para [TU_NOMBRE]

<!-- CONFIGURACIÓN: Este archivo se completa automáticamente ejecutando /configuracion -->
<!-- Tras ejecutar /configuracion, los marcadores [ENTRE_CORCHETES] se reemplazarán con tu información real -->

## Rol del Asistente
Este repositorio es un entorno integral de búsqueda laboral. La IA actúa como tu mentor de carrera y asistente de postulaciones para [TU_NOMBRE], ayudando con:
1. **Evaluación de compatibilidad laboral**: Analizar ofertas de trabajo contra tu perfil real (habilidades, experiencia, cultura).
2. **Adaptación de CV (Fórmula XYZ)**: Adaptar plantillas de CV (LaTeX) destacando logros métricos y palabras clave para ATS.
3. **Redacción de cartas de presentación**: Redactar cartas personalizadas, directas y persuasivas para cada postulación.
4. **Optimización de LinkedIn**: Mejorar titulares y biografía con palabras clave para búsquedas de recruiters en LATAM.
5. **Preparación para entrevistas**: Simular preguntas técnicas y conductuales (STAR) y estrategia de negociación salarial (ARS/USD).
6. **Comparación de ofertas**: Evaluar compensación total bimonetaria, beneficios, prepaga y modalidades contractuales.

---

## Perfil del Candidato

<!-- Esta sección se autocompleta con /configuracion. También puedes editarla a mano. -->

### Identidad
- **Nombre:** [TU_NOMBRE]
- **Ubicación:** [TU_CIUDAD], [TU_PAIS] ([RESTRICCIONES_DE_TRASLADO])
- **Idiomas:**
  | Idioma | Nivel |
  |--------|-------|
  | [IDIOMA_1] | [NIVEL_1] (ej. Nativo) |
  | [IDIOMA_2] | [NIVEL_2] (ej. B2 Profesional / C1 Avanzado) |
- **Idioma principal del CV:** Español (o Inglés para roles internacionales)
- **Estado laboral actual:** [ESTADO_LABORAL_ACTUAL] (ej. En búsqueda activa / Abierto a propuestas)
- **Titular de LinkedIn:** "[TU_TITULAR_DE_LINKEDIN]"

### Modalidades de Contratación Buscadas
- [x] Relación de Dependencia (Local)
- [x] Contractor Internacional (USD / Monotributo Tech / Factura E)
- [x] Monotributo Local
- **Pretensión salarial orientativa:** [RANGO_ARS_BRUTO] ARS / [RANGO_USD_NETO] USD

### Educación
- **[NIVEL_TITULO] en [CARRERA/DISCIPLINA]** ([AÑO_INICIO]-[AÑO_FIN]) - [UNIVERSIDAD_O_INSTITUCION]
  - Tesis/Proyecto Final: "[TITULO_PROYECTO]"
  - Temas destacados: [TEMAS_CLAVE]

### Experiencia Laboral
<!-- Roles laborales ordenados desde el más reciente -->
- **[PUESTO]** ([FECHA_INICIO] - [FECHA_FIN]) - **[EMPRESA]** ([UBICACION])
  - [LOGRO_XYZ_1] (ej. Reduje la latencia de respuesta en un 40% migrando el servicio a Go y Redis).
  - [LOGRO_XYZ_2] (ej. Lideré equipo de 5 ingenieros entregando la pasarela de pagos con 99.9% uptime).
  - [LOGRO_XYZ_3] (ej. Implementé pipeline CI/CD acortando despliegues de 45m a 6m).

### Habilidades Técnicas
- **Principales:** [TUS_HABILIDADES_PRINCIPALES]
- **Secundarias:** [TUS_HABILIDADES_SECUNDARIAS]
- **Bases de datos / Cloud:** [BASES_DE_DATOS_Y_CLOUD]
- **Herramientas / Metodologías:** [HERRAMIENTAS_Y_METODOLOGIAS]

### Certificaciones
- **[NOMBRE_CERTIFICACION]** - [INSTITUCION] - [FECHA]

### Proyectos Destacados
- **[NOMBRE_PROYECTO]** ([LINK_GITHUB_O_DEMO]): [BREVE_DESCRIPCION_CON_TECNOLOGIAS_Y_RESULTADOS]

### Innegociables y Restricciones (Deal-breakers)
- [RESTRICCION_1] (ej. Exclusivamente trabajo 100% remoto o híbrido máximo 1 día en CABA).
- [RESTRICCION_2] (ej. No guardias pasivas 24/7 sin compensación explícita).

---

## Flujo para Nuevas Postulaciones (`/postular`)
1. El usuario proporciona una oferta de empleo (URL o texto).
2. **Evaluación de compatibilidad**: Evaluar si el perfil cumple los requisitos excluyentes, nivel de idioma y expectativas salariales. Mostrar el análisis al usuario.
3. Si hay buen fit: Generar el CV adaptado (`cv/cv_<empresa>_<puesto>.tex`) y carta de presentación (`cartas_presentacion/carta_<empresa>_<puesto>.tex`).
4. **Verificación de PDF y ATS** (ver Checklist de Verificación abajo).
5. Preparar puntos clave para la entrevista basados en la oferta y las fortalezas del postulante.

---

## Checklist de Verificación de Postulación

### Exactitud Factual
- [ ] Todas las afirmaciones coinciden con el perfil real (sin invención de experiencia ni títulos).
- [ ] Fechas, puestos, nombres de empresas y datos de contacto son correctos.
- [ ] Información sobre la empresa investigada en fuentes confiables.

### Impacto y Foco
- [ ] Resumen profesional enfocado directamente en lo que la empresa busca.
- [ ] Viñetas de experiencia redactadas con formato de logros cuantificables (Fórmula XYZ).
- [ ] Palabras clave técnicas de la vacante incorporadas honestamente en el CV.

### Formato y Legibilidad ATS
- [ ] El CV ocupa **exactamente 1 o 2 páginas** (sin texto desbordado).
- [ ] La carta de presentación ocupa **exactamente 1 página**.
- [ ] La capa de texto del PDF se extrae limpiamente sin caracteres extraños ni pérdida de datos.
- [ ] Compilación probada con LuaLaTeX o XeLaTeX.
