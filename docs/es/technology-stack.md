# Stack tecnológico

**Estado:** selección inicial aprobada; arquitectura e infraestructura pendientes de evaluación.

## Tecnologías seleccionadas

| Capa | Tecnología | Estado | Justificación |
|---|---|---|---|
| Frontend | React + TypeScript | Aprobado | Permite construir una interfaz web responsive y mantener tipado estático en el frontend. |
| Backend | Python + FastAPI | Aprobado | Aprovecha los conocimientos existentes de Python y facilita la evolución del sistema de recomendación. |
| Base de datos | PostgreSQL | Aprobado | Base de datos relacional adecuada para las relaciones entre usuarios, películas, valoraciones, listas e historial. |

## Criterios de selección

La elección tecnológica tiene en cuenta:

- Desarrollo y mantenimiento por una sola persona.
- Conocimientos técnicos actuales y curva de aprendizaje.
- Presupuesto limitado.
- Dedicación estimada de 5–10 horas semanales.
- Necesidad de disponer de un recomendador funcional desde el MVP.
- Posibilidad de evolucionar el recomendador sin introducir complejidad prematura.
- Mantenibilidad y disponibilidad de documentación y herramientas.

## Arquitectura de partida

La aplicación tendrá inicialmente dos partes principales:

- **Frontend:** aplicación React + TypeScript.
- **Backend:** API REST desarrollada con Python + FastAPI.
- **Persistencia:** PostgreSQL como sistema gestor de bases de datos principal.

El frontend se comunicará con el backend mediante peticiones HTTP. La configuración de alojamiento, despliegue y operación de la base de datos se definirá en decisiones posteriores.

## Decisiones pendientes

- Evaluar ORM y estrategia de migraciones.
- Definir autenticación y gestión de sesiones.
- Evaluar alojamiento y despliegue.
- Definir estrategia de almacenamiento de imágenes y otros recursos.
- Evaluar proveedores externos de datos cinematográficos.
- Definir herramientas de pruebas, calidad y automatización.
- Definir estrategia de copias de seguridad, monitorización y mantenimiento de PostgreSQL.

## Registro de cambios

| Decisión | Estado |
|---|---|
| React + TypeScript para frontend | Aprobado |
| Python + FastAPI para backend | Aprobado |
| PostgreSQL para persistencia principal | Aprobado |
