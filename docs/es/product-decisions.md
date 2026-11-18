# Registro de decisiones de producto

Este documento registra decisiones confirmadas y separa explícitamente las cuestiones pendientes. Las decisiones técnicas se documentarán en los artefactos de arquitectura correspondientes.

## Convenciones

- **Aprobado:** confirmado por el usuario.
- **Pendiente:** requiere definición posterior.
- **Por priorizar:** capacidad contemplada sin compromiso de entrega.
- **Riesgo / por investigar:** depende de validación externa.

## Decisiones aprobadas

| ID | Área | Decisión |
|---|---|---|
| PD-001 | Visión | Plataforma centrada en descubrimiento cinematográfico personalizado, con diario y analítica como pilares complementarios. |
| PD-002 | Público | Espectador habitual como público principal; ocasional y cinéfilo como segmentos adicionales. |
| PD-003 | UX | Simplicidad progresiva, sin aplicaciones separadas ni restricciones arbitrarias por perfil. |
| PD-004 | Watchlist | Una watchlist principal por usuario, sin duplicados; al registrar como vista se retira automáticamente. |
| PD-005 | Listas | Listas personalizadas independientes de watchlist; una película puede pertenecer a varias. |
| PD-006 | Descubrimiento | Inicio combina decisión rápida, recomendaciones personalizadas y exploración editorial/contextual. |
| PD-007 | Preferencias | Combinación de preferencias explícitas e inferidas; el usuario podrá consultar y corregir inferencias. |
| PD-008 | Semántica | Vista no significa gustada; no vista no significa desinterés. |
| PD-009 | Rating | Escala 0–10 en pasos de 0,5; una única valoración vigente por usuario/película en MVP. |
| PD-010 | Reseñas | Una reseña opcional por película y usuario en MVP, siempre vinculada a película vista. |
| PD-011 | Rewatch | Cada rewatch crea una visualización nueva; no crea rating ni reseña duplicados en MVP. |
| PD-012 | Fechas | Fecha local actual sugerida y editable a fechas pasadas; nunca futura. Vistas pre-registro sin fecha inventada. |
| PD-013 | Onboarding | Clasificación de películas con dos opciones: «La he visto» y «No la he visto»; abandonable, sin mínimo ni límite fijo. |
| PD-014 | Onboarding | Las películas marcadas como vistas durante onboarding se registran como históricas sin fecha. |
| PD-015 | Analítica | Dashboard visual, narrativo e interactivo; conclusiones solo cuando los datos las respalden. |
| PD-016 | Gamificación | Economía de puntos, no niveles; individual, no competitiva y sin valor monetario. |
| PD-017 | Social | MVP individual, sin red social completa; perfiles públicos y listas compartibles contemplados. |
| PD-018 | Búsqueda | Búsqueda por título, título original, año, director y reparto; lenguaje natural sobre filtros estructurados. |
| PD-019 | Ficha | Seis áreas: información principal, adicional, datos cinematográficos, acciones, contenido personal y descubrimiento relacionado. |
| PD-020 | Datos | No inventar metadatos; identificar fuentes, diferenciar puntuaciones externas y personales y ocultar datos poco fiables. |
| PD-021 | Recomendaciones | Feedback explícito y explicación basada en evidencias. |
| PD-022 | Streaming | País de perfil como mercado de referencia; disponibilidad solo si hay datos fiables. |
| PD-023 | Privacidad | Perfil público/privado y controles individuales; perfil privado prevalece. |
| PD-024 | Cuenta | Email/contraseña, verificación y recuperación en MVP; Google Login futuro. |
| PD-025 | Datos personales | Exportación de datos incluida en MVP. |
| PD-026 | Datos personales | Eliminación definitiva de cuenta con confirmación y tratamiento conforme a obligaciones legales. |
| PD-027 | Seguridad | Privacy by Design, autorización por recurso, protección de credenciales, validación y gestión segura de secretos. |
| PD-028 | Notificaciones | Opcionales y configurables; posibilidad de desactivarlas por completo; sin spam ni urgencia artificial. |
| PD-029 | Accesibilidad | WCAG 2.2 AA como objetivo de referencia, sin certificación formal exigida en esta fase. |
| PD-030 | Feedback | Tres vías: reportar problema, reportar datos incorrectos y enviar sugerencias. |
| PD-031 | Éxito | El valor de descubrimiento y recomendaciones es el criterio principal; no maximizar tiempo de pantalla. |
| PD-032 | MVP | El recomendador personalizado debe estar funcional desde el lanzamiento, aunque su primera versión sea sencilla. |
| PD-033 | Proyecto | Web responsive inicial, interfaz en castellano e internacionalización prevista desde el principio. |
| PD-034 | Proyecto | Producto inicialmente gratuito, desarrollo individual, presupuesto y dedicación limitados. |
| PD-035 | Documentación | La documentación del repositorio será la referencia vigente del producto; las conversaciones no sustituyen los documentos. |

## Cuestiones pendientes

| ID | Área | Pendiente |
|---|---|---|
| OPEN-001 | Marca | Nombre e identidad definitivos. |
| OPEN-002 | MVP | Priorización P0/P1/P2 y corte exacto del MVP. |
| OPEN-003 | Datos | Selección de proveedor(es), cobertura, atribución, licencias, almacenamiento y condiciones de uso. |
| OPEN-004 | Streaming | Viabilidad, cobertura, fiabilidad, coste y proveedor. |
| OPEN-005 | Recomendador | Evaluación objetiva de calidad y evolución del enfoque inicial. |
| OPEN-006 | Analítica | Métricas y gráficos exactos del dashboard inicial. |
| OPEN-007 | Gamificación | Reglas de concesión de puntos y alcance que, si procede, entraría en MVP. |
| OPEN-008 | Notificaciones | Canales y frecuencias concretas. |
| OPEN-009 | Exportación | Formato y alcance técnico de exportación; se decide en fase técnica. |
| OPEN-010 | Métricas | Métrica norte cuantitativa, fórmulas y objetivos iniciales. |
| OPEN-011 | Catálogo | Cobertura mínima, estrategia de actualización y calidad de datos. |
| OPEN-012 | Búsqueda | Límites de interpretación y tratamiento de ambigüedades. |
| OPEN-013 | Legal | Políticas, bases jurídicas, conservación, derechos, cookies y revisión de proveedores. |
| OPEN-014 | Roadmap | Dependencias, estimaciones y secuencia definitiva. |

## Registro de cambios

Este registro se ampliará conforme se tomen nuevas decisiones. Cada cambio relevante debe incluir fecha, contexto, decisión y documentos afectados.
