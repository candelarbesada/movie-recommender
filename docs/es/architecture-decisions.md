# Decisiones de arquitectura

Este documento registra las decisiones técnicas aprobadas para Movie Recommender y su justificación.

## ADR-001: Selección del stack de frontend y backend

**Estado:** Aprobado

### Contexto

El proyecto necesita una aplicación web responsive con un backend capaz de gestionar usuarios, catálogo cinematográfico, preferencias, valoraciones y recomendaciones personalizadas.

El desarrollo será individual, con una dedicación estimada de 5–10 horas semanales y un presupuesto limitado.

Además, el recomendador es una funcionalidad central del producto y deberá estar operativo desde el lanzamiento del MVP.

### Decisión

- Utilizar React + TypeScript para el frontend.
- Utilizar Python + FastAPI para el backend.
- Mantener una API REST para la comunicación entre frontend y backend.

### Justificación

- Aprovechar los conocimientos actuales de TypeScript, JavaScript y Python.
- Utilizar el ecosistema Python para facilitar el desarrollo y la evolución del recomendador.
- Mantener una separación clara entre interfaz y lógica de negocio.
- Evitar introducir un servicio independiente para recomendaciones mientras no sea necesario.
- Mantener una arquitectura que pueda evolucionar sin complejidad prematura.

### Consecuencias

**Positivas:**

- Acceso al ecosistema de análisis de datos y machine learning de Python.
- Separación clara de responsabilidades.
- Posibilidad de evolucionar progresivamente el recomendador.

**Negativas:**

- Será necesario mantener dos entornos tecnológicos: TypeScript y Python.
- Habrá que coordinar los contratos de datos entre frontend y backend.
- El proyecto tendrá dos aplicaciones que configurar, probar y desplegar.

### Alternativas consideradas

- TypeScript + Node.js para frontend y backend.
- Se descarta inicialmente esta alternativa porque Python ofrece un ecosistema más adecuado para la evolución prevista del recomendador.

### Alcance

Esta decisión no aprueba todavía PostgreSQL, proveedores externos, servicios de alojamiento ni herramientas de infraestructura. Se evaluarán por separado.
