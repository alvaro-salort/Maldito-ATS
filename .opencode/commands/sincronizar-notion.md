# /sincronizar-notion - Sincronización con Base de Datos de Notion

Permite exportar y sincronizar tus postulaciones locales de `registro_postulaciones.csv` con una base de datos o tablero Kanban en Notion.

---

## Parámetros Opcionales
- `--database-id`: ID de la base de datos de Notion de destino.
- `--token`: Token de integración de Notion (o configurado en variables de entorno `NOTION_API_KEY`).

---

## Mapeo de Propiedades
- `Empresa` -> Título
- `Puesto` -> Texto
- `Estado` -> Select / Estado (`Postulado`, `En Proceso`, `Entrevista Técnica`, `Oferta`, `Rechazado`)
- `Modalidad` -> Select (`Remoto`, `Híbrido`, `Presencial`, `Contractor USD`)
- `Sueldo Estimado` -> Texto / Número
- `Fecha` -> Fecha de postulación
