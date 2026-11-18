# Requisitos del producto

**Estado:** consolidado conceptualmente; la priorización de entrega sigue pendiente.

Este documento describe comportamientos y capacidades de producto. No prescribe arquitectura ni implementación.

## 1. Inicio y navegación

La página de inicio combinará una decisión rápida («¿Qué vemos hoy?») con exploración más amplia.

Secciones conceptuales:
1. ¿Qué vemos hoy?: selección reducida y personalizada.
2. Para ti: recomendaciones personalizadas.
3. Descubre algo diferente: propuestas fuera de los patrones habituales.
4. Populares y tendencias.
5. Estrenos recientes.
6. Explora intereses: géneros, directores y actores.
7. Colecciones y selecciones temáticas.

Las secciones podrán adaptarse dinámicamente al usuario.

Navegación candidata: Inicio, Explorar, Mi cine, Estadísticas y Perfil. La ficha de película será accesible desde distintas secciones.

## 2. Onboarding y personalización

El onboarding será progresivo, abandonable y podrá completarse más adelante.

Flujo conceptual:
- Crear cuenta.
- Configurar país o mercado de referencia.
- Seleccionar plataformas de streaming opcionalmente.
- Indicar gustos iniciales.
- Clasificar películas conocidas.
- Recibir primeras recomendaciones.

### Clasificación inicial de películas

- Deslizar a la derecha o pulsar «La he visto».
- Deslizar a la izquierda o pulsar «No la he visto».
- No existe una tercera opción «No la conozco».
- No hay mínimo obligatorio ni límite fijo de películas clasificadas.
- La selección de tarjetas se adapta a las respuestas.
- No repetir continuamente películas ya clasificadas.
- Las películas marcadas como vistas se registran como históricas, sin fecha asignada.
- No se exige valorar películas.

«No la he visto» no significa desinterés ni valoración negativa.

### Preferencias explícitas

Se contemplan géneros favoritos y a evitar, actores y directores favoritos o no deseados, décadas, idiomas originales, duración, estilos cinematográficos y países/regiones.

No todas estas preferencias deben solicitarse durante el onboarding.

### Preferencias inferidas

El sistema podrá aprender de películas vistas, valoraciones, feedback, géneros, reparto, directores y patrones.

Deben distinguirse las preferencias explícitas de las inferidas. El usuario podrá consultar y corregir las inferidas.

Reglas semánticas:
- Haber visto una película no implica que guste.
- No haberla visto no implica que no interese.
- Las valoraciones y el feedback explícito aportan señales diferenciadas.

## 3. Descubrimiento y recomendaciones

El descubrimiento es el núcleo funcional del producto.

Las recomendaciones podrán considerar:
- Preferencias explícitas e inferidas.
- Historial de visualizaciones.
- Valoraciones.
- Feedback sobre recomendaciones.
- Contexto temporal.
- Disponibilidad en servicios, cuando existan datos fiables.

También se contemplan contenidos populares, tendencias, estrenos, selecciones temáticas y recomendaciones diarias, semanales, mensuales y estacionales.

Debe distinguirse claramente entre recomendaciones personalizadas y selecciones editoriales o contextuales.

### Feedback de recomendaciones

- **Me interesa:** señal positiva de interés, no equivale a que guste la película.
- **No me interesa:** señal negativa de interés, no significa que la película sea mala.
- **Ya la he visto:** actualiza el estado de visualización.
- **Guardar para después:** añade a la watchlist.
- **¿Por qué esta recomendación?:** muestra motivos fundamentados en datos.

Las explicaciones no deben inventar razones ni presentar racionalizaciones sin evidencia.

**Requisito de MVP:** habrá un recomendador personalizado funcional desde el lanzamiento. Su primera versión puede ser sencilla; la sofisticación evolucionará progresivamente.

## 4. Catálogo y búsqueda

### Búsqueda general

Buscar por título, título original, año, director y actor/actriz. Debe tolerar mayúsculas, acentos y pequeñas variaciones.

### Filtros avanzados

Géneros, rango de años, duración, director, reparto e idioma original.

### Ordenación

Popularidad, valoración, fecha de estreno y título.

### Búsqueda en lenguaje natural

El usuario podrá formular consultas como «Películas de ciencia ficción de los 90 con viajes en el tiempo que no sean demasiado largas».

La consulta se interpretará como criterios estructurados sobre el catálogo. No se inventarán películas ni metadatos. Se pedirá aclaración cuando exista ambigüedad relevante.

## 5. Ficha de película

La ficha tendrá seis áreas:

1. **Información principal:** póster, título, título original, año, director, géneros, duración y sinopsis.
2. **Información adicional:** reparto, guionistas, productoras, países, idiomas y fechas de estreno.
3. **Datos cinematográficos:** puntuaciones externas, popularidad e indicadores disponibles, identificando fuentes.
4. **Acciones personales:** marcar como vista, registrar visualización, valorar, reseñar y gestionar watchlist/listas.
5. **Contenido personal:** valoración vigente, reseña e historial.
6. **Descubrimiento relacionado:** películas similares, mismo director o reparto compartido.

La información esencial se mostrará primero y los detalles se revelarán progresivamente.

### Calidad del catálogo

- No inventar metadatos.
- Identificar las fuentes.
- Utilizar fallback cuando falten imágenes.
- Ocultar puntuaciones externas poco fiables o no disponibles.
- Diferenciar puntuaciones externas de valoraciones personales.
- Contemplar correcciones y actualizaciones.
- Revisar licencias y condiciones de los proveedores.

## 6. Mi cine: watchlist y listas

### Watchlist

- Una watchlist principal por usuario.
- No admite películas duplicadas.
- Permite orden personalizado y por fecha de incorporación, además de filtros.
- Puede ser pública o privada.
- Al registrar una película como vista, se retira automáticamente de la watchlist.
- El usuario puede eliminar películas manualmente.
- No habrá prioridades alta/media/baja en el MVP.

### Listas personalizadas

- Crear, editar y eliminar listas.
- Añadir y quitar películas.
- Una película puede pertenecer a varias listas.
- Visibilidad pública o privada.
- Independientes de la watchlist.

## 7. Visualizaciones, valoraciones y reseñas

### Visualizaciones

- Registrar una visualización marca automáticamente la película como vista.
- Es válido registrar una película vista sin rating ni reseña.
- Se sugiere la fecha local actual del dispositivo.
- La fecha puede editarse a cualquier fecha pasada, nunca futura.
- Un rewatch crea una nueva visualización.
- Se permiten varias visualizaciones el mismo día.
- El historial se ordena de más reciente a más antiguo; el momento de registro desempata.
- Las películas vistas antes del registro en la plataforma no reciben una fecha inventada.

### Valoraciones

- Escala de 0 a 10 en incrementos de 0,5.
- Opcional.
- Una única valoración vigente por usuario y película en el MVP.
- En un rewatch se muestra la valoración vigente como valor inicial editable.
- Editar actualiza la valoración; no se mantienen ratings simultáneos por rewatch.
- Las estadísticas utilizan la valoración vigente, sin duplicar peso por rewatch.

### Reseñas

- Siempre vinculadas a una película vista.
- Una reseña por película y usuario en el MVP.
- Opcional y editable.
- Visibilidad pública o privada.
- Se conservan `created_at` y `updated_at`; cuando proceda, se mostrará la fecha de actualización sin perder la creación original.

### Eliminación e historial

- Se pueden eliminar visualizaciones individuales.
- Si se elimina la última visualización, se pregunta qué hacer con el estado de vista y el contenido asociado.
- Si se vuelve a marcar como vista, se crea una entrada nueva; no se recuperan fechas ni comentarios eliminados.
- Desmarcar una película como vista requiere advertir de las consecuencias sobre visualizaciones y reseña.

Las vistas históricas pre-registro cuentan para recomendaciones y estadísticas globales, pero no para métricas temporales, rachas, retos u objetivos.

## 8. Estadísticas y analítica

La experiencia será visual, narrativa e interactiva, no un panel plano.

Métricas contempladas:
- Distribución de valoraciones.
- Géneros más vistos y mejor valorados.
- Actividad temporal.
- Décadas.
- Actores y directores.
- Evolución de preferencias.

Interacciones:
- Selección de periodos.
- Filtros.
- Comparaciones.
- Exploración de los datos subyacentes.
- Actualización coherente de gráficos y narrativa.

La narrativa solo destacará patrones respaldados por datos suficientes. Se distinguirán conteos de visualizaciones, valoraciones y preferencias inferidas.

Dashboard básico: contemplado para el MVP, pendiente de priorización detallada. Wrapped anual y analítica avanzada: evolución futura.

## 9. Gamificación

Concepto aprobado, alcance y priorización pendientes:
- Economía de puntos, no niveles.
- Puntos por actividad auténtica: visualizaciones, valoraciones, reseñas, objetivos, retos e hitos.
- Prevenir spam y acciones artificiales.
- Tienda cosmética para fondos, marcos, badges, temas y decoraciones.
- Puntos sin valor monetario, no comprables inicialmente, no transferibles y sin ventajas funcionales.
- Historial y balance visibles.
- Sin rankings, leaderboard ni competición.
- Objetivos, retos e hitos individuales; rachas posiblemente futuras.

La tienda y la economía cosmética no son el centro del MVP y probablemente pertenezcan a una fase posterior.

## 10. Perfil y funcionalidades sociales

### Perfil

Puede incluir username, nombre visible, biografía, foto, películas favoritas, estadísticas y listas públicas.

El perfil podrá ser público o privado.

### Social

Futuro: follows, feed, comentarios, reacciones y descubrimiento basado en usuarios similares.

Fuera del MVP: red social completa. Se contemplan perfiles públicos y listas compartibles, sin feed ni interacciones sociales completas.

## 11. Streaming y disponibilidad

Se contempla mostrar disponibilidad en la ficha cuando exista una fuente fiable.

- La disponibilidad es regional.
- El país del perfil representa el mercado de referencia, no necesariamente la ubicación física actual.
- Las plataformas suscritas son opcionales y configurables.
- Se podrá priorizar contenido disponible en servicios suscritos sin excluir el resto, salvo preferencia expresa.
- Mostrar servicio, modalidad (suscripción/alquiler/compra), región y última actualización cuando los datos lo permitan.
- No afirmar disponibilidad actual si la fuente no es fiable.

La viabilidad depende de proveedores, cobertura, coste y licencias.

## 12. Notificaciones

Notificaciones opcionales y configurables por el usuario:
- Nuevas recomendaciones.
- Resumen semanal.
- Progreso de objetivos.
- Recordatorios de descubrimiento.

El usuario podrá desactivar categorías o todas las notificaciones sin perder funcionalidad. No habrá spam, urgencia artificial ni notificaciones indiscriminadas. Canales y frecuencias concretas quedan pendientes.

## 13. Feedback y reportes

Se contemplan tres vías:
1. Reportar problemas funcionales o visuales.
2. Reportar datos incorrectos de películas.
3. Enviar sugerencias.

El mecanismo será sencillo, con descripción y contexto. Cuando se reporte desde una ficha, el reporte podrá asociarse a esa película. No se plantea un sistema complejo de tickets ni votaciones.

## 14. Requisitos de cuenta relacionados

- Registro e inicio de sesión con email y contraseña en el MVP.
- Verificación de email y recuperación de contraseña.
- Google Login como evolución futura.
- Exportación de datos del usuario en el MVP; formato pendiente de definición técnica.
- Eliminación definitiva de cuenta, con confirmación explícita y tratamiento de datos conforme a obligaciones legales.

Véanse [privacy-and-security-requirements.md](privacy-and-security-requirements.md) y [mvp-scope.md](mvp-scope.md).
