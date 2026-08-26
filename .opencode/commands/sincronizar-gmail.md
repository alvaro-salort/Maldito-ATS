# /sincronizar-gmail - Detección Automática de Respuestas de Selección

Permite sincronizar y detectar correos entrantes de postulaciones laborales (invitaciones a entrevistas, desafíos técnicos o rechazos) para actualizar automáticamente tu planilla de seguimiento (`registro_postulaciones.csv`).

---

## Modos de Operación

1. **Búsqueda por Remitente / Empresa**:
   - Escanea correos recibidos de dominios o remitentes vinculados a empresas a las que te hayas postulado.
2. **Clasificación Automática de Estado**:
   - `Invitación a Entrevista`: Actualiza el estado a `en_proceso` o `entrevista_tecnica` y notifica al usuario.
   - `Desafío Técnico / Take-Home`: Sugiere preparar el roadmap con la habilidad `capacitacion`.
   - `Rechazo`: Actualiza el estado a `rechazado` e invita a registrar aprendizajes.
   - `Oferta`: Actualiza a `oferta` y sugiere usar `/comparar-ofertas`.
