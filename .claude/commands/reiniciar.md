# /reiniciar - Reinicio de Perfil y Limpieza de Estado

Permite restablecer los archivos de configuración y estado para volver a ejecutar el onboarding desde cero o limpiar vacantes vistas.

---

## Opciones
- `/reiniciar perfil`: Restablece `CLAUDE.md`, `01-perfil-candidato.md` y `cv/cv_maestro.md` a sus plantillas vacías.
- `/reiniciar buscador`: Limpia `buscador_empleos/empleos_vistos.json` para volver a analizar vacantes previas.
- `/reiniciar todo`: Limpia el perfil y el historial de búsquedas (conserva los documentos en `documentos/`).
