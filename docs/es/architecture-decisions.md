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

## ADR-002: Selección de PostgreSQL como base de datos principal

**Estado:** Aprobado

### Contexto

Movie Recommender necesita almacenar y relacionar usuarios, películas, valoraciones, listas, watchlists, visualizaciones y preferencias. También necesitará consultas para búsqueda, estadísticas y generación de recomendaciones.

### Decisión

Utilizar PostgreSQL como sistema gestor de bases de datos relacional principal.

### Justificación

- Su modelo relacional encaja con las relaciones entre las entidades del producto.
- Ofrece integridad referencial y restricciones para proteger la consistencia de los datos.
- Proporciona capacidades SQL avanzadas para consultas y analítica.
- Se integra bien con Python y FastAPI.
- Permite evolucionar sin introducir prematuramente otra base de datos.

### Alternativas consideradas

- **MySQL:** alternativa válida, pero sin ventajas decisivas para nuestras necesidades.
- **SQLite:** útil para desarrollo local y pruebas, pero no seleccionada como base de datos principal para el despliegue multiusuario.

### Consecuencias

**Positivas:**

- Persistencia adecuada para los datos relacionales.
- Buen soporte para consultas complejas.
- Integración madura con Python.

**Negativas:**

- Requiere operar un servidor de base de datos.
- Necesita copias de seguridad, actualizaciones y monitorización.
- Añade mantenimiento frente a SQLite.

### Alcance

La decisión selecciona el motor, no el proveedor de alojamiento. ORM, migraciones y operación se evaluarán por separado.

## ADR-003: Selección de SQLAlchemy como ORM

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

El backend necesita una herramienta para interactuar con PostgreSQL desde Python. La aplicación tendrá entidades relacionadas entre sí, como usuarios, películas, valoraciones, listas, watchlists e historial.

### Decisión

Se utilizará SQLAlchemy 2.x como ORM para gestionar la interacción entre el backend y PostgreSQL.

### Justificación

- Es una herramienta madura y ampliamente utilizada en el ecosistema Python.
- Permite gestionar relaciones complejas entre entidades.
- Ofrece flexibilidad para combinar operaciones ORM con consultas SQL.
- Se integra correctamente con FastAPI.
- Facilita el mantenimiento y la evolución del modelo de datos.

### Alternativas consideradas

- **SQLModel:** ofrece una sintaxis más sencilla y una integración muy cómoda con FastAPI, pero se prioriza la flexibilidad de SQLAlchemy.
- **Psycopg:** es un controlador de PostgreSQL, no un ORM. Requeriría gestionar manualmente más operaciones de persistencia.

### Consecuencias

- Se utilizará SQLAlchemy 2.x para las operaciones de persistencia.
- El proyecto deberá definir cómo gestionar las sesiones y transacciones de base de datos.
- Se evaluará Alembic como herramienta de migraciones en una decisión independiente.

## ADR-004: Selección de Alembic para las migraciones

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La estructura de la base de datos PostgreSQL evolucionará durante el desarrollo. Necesitamos una herramienta que permita registrar, controlar y aplicar los cambios de esquema de forma ordenada y reproducible.

### Decisión

Se utilizará Alembic para gestionar las migraciones de la base de datos.

### Justificación

- Está diseñado para trabajar con SQLAlchemy.
- Permite mantener un historial de cambios en la estructura de la base de datos.
- Facilita aplicar y revertir migraciones.
- Puede generar migraciones automáticamente a partir de diferencias entre los modelos y el esquema de la base de datos.
- Es una solución consolidada en el ecosistema Python.

### Alternativas consideradas

- **Scripts SQL manuales:** ofrecen control directo, pero requieren gestionar manualmente el historial y la aplicación de los cambios.
- **Otras herramientas de migración:** no aportan una ventaja clara frente a Alembic para nuestro stack.

### Consecuencias

- Las modificaciones del esquema de PostgreSQL se gestionarán mediante migraciones de Alembic.
- Las migraciones se almacenarán junto al código del proyecto y estarán versionadas en Git.
- Será necesario revisar las migraciones generadas automáticamente antes de aplicarlas.

## ADR-005: Selección de Clerk como proveedor de autenticación

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La aplicación necesita un sistema de autenticación que permita a los usuarios registrarse, iniciar sesión y gestionar sus sesiones de forma segura.

Queremos reducir la complejidad de implementar y mantener un sistema de autenticación propio, manteniendo el control sobre los datos y la lógica de negocio de la aplicación.

### Decisión

Se utilizará Clerk como proveedor externo de autenticación.

La integración se realizará de la siguiente manera:

- **Frontend:** integración de Clerk con React.
- **Backend:** FastAPI verificará los tokens de autenticación emitidos por Clerk.
- **Base de datos:** PostgreSQL almacenará los datos propios de los usuarios y de la aplicación.
- **Persistencia:** SQLAlchemy gestionará las entidades y relaciones propias del sistema.

### Justificación

- Proporciona funcionalidades de registro e inicio de sesión sin tener que implementarlas desde cero.
- Ofrece componentes e integración para React.
- Permite verificar la identidad de los usuarios desde nuestro backend.
- Reduce el trabajo de mantenimiento relacionado con credenciales y sesiones.
- Dispone de un plan gratuito adecuado para comenzar el desarrollo y validar el MVP.

### Alternativas consideradas

- **Autenticación propia con FastAPI:** ofrece control total, pero aumenta el trabajo de implementación, seguridad y mantenimiento.
- **Auth0:** alternativa consolidada y completa, pero no presenta una ventaja decisiva para las necesidades iniciales del proyecto.
- **Supabase Auth:** alternativa interesante, aunque se prioriza Clerk para separar claramente la autenticación de nuestra infraestructura

## ADR-006: Selección de Render como plataforma de despliegue

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La aplicación necesita una plataforma donde alojar el frontend, el backend y la base de datos PostgreSQL.

Buscamos una solución sencilla de mantener, compatible con nuestro stack tecnológico y que permita mantener los costes dentro del presupuesto estimado de 0–20 € mensuales.

### Decisión

Se utilizará Render como plataforma principal de despliegue.

La distribución de los componentes será:

- **Frontend:** Render Static Site para React + TypeScript.
- **Backend:** Render Web Service para Python + FastAPI.
- **Base de datos:** Render PostgreSQL.

Inicialmente se contemplarán dos entornos: desarrollo local y producción.

### Justificación

- Permite alojar los tres componentes dentro de una misma plataforma.
- Ofrece integración con GitHub y despliegues automáticos.
- Simplifica la configuración y el mantenimiento de la infraestructura.
- Es compatible con las tecnologías seleccionadas.
- Los servicios básicos de pago permiten mantener una estimación inicial de costes dentro del presupuesto del proyecto.

### Alternativas consideradas

- **Vercel:** excelente alternativa para el frontend, pero necesitaríamos otro proveedor para el backend y PostgreSQL. Su plan Hobby tiene restricciones de uso.
- **Railway:** permite desplegar todos los componentes y ofrece una experiencia integrada, pero su facturación depende del consumo.
- **Combinación de proveedores:** podría ofrecer ventajas específicas, pero introduciría más complejidad operativa sin una necesidad actual.

### Consecuencias

- Los tres componentes dependerán inicialmente de Render.
- El coste mensual deberá revisarse según el uso y los planes contratados.
- Se deberán configurar correctamente las variables de entorno y los secretos.
- La base de datos de producción deberá utilizar un plan con persistencia y copias de seguridad adecuadas.
- Se deberá definir una estrategia de copias de seguridad y recuperación.
- Los despliegues deberán poder realizarse de forma reproducible desde GitHub.

## ADR-007: Organización de los entornos de la aplicación

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

El proyecto necesita separar el desarrollo de funcionalidades, la ejecución de pruebas y la aplicación utilizada por los usuarios.

Esta separación permite reducir el riesgo de introducir errores en producción y evita que las pruebas afecten a los datos reales.

### Decisión

Se utilizarán tres entornos diferenciados:

1. **Desarrollo (Development):**
   - Se ejecutará localmente en el equipo de desarrollo.
   - Utilizará una base de datos PostgreSQL local.
   - Se utilizará para implementar y probar funcionalidades durante el desarrollo.

2. **Pruebas (Testing):**
   - Se utilizará para ejecutar pruebas automatizadas.
   - Dispondrá de una base de datos independiente de desarrollo y producción.
   - Las pruebas se ejecutarán localmente y mediante GitHub Actions.

3. **Producción (Production):**
   - Se alojará en Render.
   - Utilizará una base de datos PostgreSQL independiente.
   - Contendrá los datos reales de los usuarios.

El entorno staging no se incorporará inicialmente. Se evaluará cuando el proyecto necesite una fase adicional de validación antes de publicar cambios.

### Justificación

- Evita que las pruebas y los cambios de desarrollo afecten a los datos reales.
- Permite validar las modificaciones antes de desplegarlas.
- Reduce el riesgo de errores en producción.
- Mantiene una infraestructura sencilla y económica para un proyecto individual.

### Alternativas consideradas

- **Un único entorno:** simplifica inicialmente la configuración, pero aumenta el riesgo de afectar a los datos reales.
- **Cuatro entornos incluyendo staging:** ofrece una separación adicional, pero añade complejidad operativa que no resulta necesaria en esta fase.

### Consecuencias

- Cada entorno tendrá su propia configuración y variables de entorno.
- Desarrollo, pruebas y producción utilizarán bases de datos independientes.
- Los secretos y credenciales nunca se compartirán entre entornos.
- Las pruebas automatizadas no utilizarán datos reales de producción.
- Los despliegues en producción deberán realizarse después de validar los cambios.

## ADR-008: Selección del proveedor de datos cinematográficos

- **Estado:** Propuesto, pendiente de validación de licencia
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender necesita obtener información cinematográfica de una fuente externa, incluyendo títulos, sinopsis, pósteres, géneros, reparto, equipo técnico, fechas de estreno y valoraciones.

La aplicación se publicará para que cualquier usuario pueda utilizarla. Además, existe la intención de que pueda convertirse en un producto comercial en el futuro.

Por tanto, el proveedor debe ofrecer una cobertura amplia de información cinematográfica y unas condiciones de uso compatibles con los objetivos actuales y futuros del proyecto.

### Decisión

Se selecciona TMDB (The Movie Database) como proveedor preferido de datos cinematográficos, pero su aprobación definitiva queda pendiente de validar las condiciones de licencia.

Antes de adoptar TMDB como proveedor definitivo, será necesario confirmar:

- Que las condiciones permiten publicar y ofrecer gratuitamente la aplicación a usuarios externos.
- Que permiten utilizar sus metadatos para generar recomendaciones cinematográficas personalizadas.
- Qué restricciones se aplican al almacenamiento y reutilización de los datos.
- Qué licencia y condiciones económicas serían necesarias para una futura explotación comercial.
- Qué requisitos de atribución y reconocimiento deben incorporarse a la aplicación.

### Alternativas consideradas

- **OMDb:** alternativa sencilla para consultar información cinematográfica, pero con limitaciones de funcionalidades y restricciones de licencia.
- **IMDb:** dispone de conjuntos de datos con condiciones de uso que no encajan bien con los objetivos de publicación y posible comercialización del proyecto.

### Justificación

TMDB ofrece una API completa, documentación adecuada y funcionalidades de búsqueda y consulta que encajan con las necesidades de Movie Recommender.

Sin embargo, la elección técnica no implica que se hayan aprobado sus condiciones legales de uso.

### Consecuencias

- El backend utilizará una capa de integración independiente para comunicarse con el proveedor cinematográfico.
- Los identificadores externos se mantendrán separados de los identificadores internos de la aplicación.
- Se evitará acoplar la lógica de negocio directamente a la estructura de respuestas de TMDB.
- No se utilizarán datos de TMDB en producción hasta confirmar que el uso previsto está autorizado.
- Si las condiciones de licencia no son compatibles con los objetivos del proyecto, se evaluará otro proveedor.
- La integración deberá permitir sustituir el proveedor sin modificar significativamente el resto de la aplicación.

## ADR-009: Almacenamiento y reutilización de datos cinematográficos

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender necesita consultar y almacenar información cinematográfica procedente de un proveedor externo.

Consultar repetidamente la API para recuperar información que ya hemos obtenido puede aumentar los tiempos de respuesta, el número de solicitudes externas y la dependencia del proveedor.

Necesitamos una estrategia que permita reutilizar los datos cinematográficos sin introducir infraestructura innecesaria.

### Decisión

Se utilizará PostgreSQL como mecanismo inicial de almacenamiento y reutilización de datos cinematográficos.

El backend seguirá esta estrategia:

1. Buscará primero la información solicitada en PostgreSQL.
2. Si la información no existe, consultará al proveedor cinematográfico.
3. Si está desactualizada, podrá solicitar una actualización al proveedor.
4. Guardará o actualizará la información en PostgreSQL cuando las condiciones de licencia lo permitan.
5. Devolverá los datos disponibles al frontend.

No se incorporará Redis durante el desarrollo del MVP.

### Justificación

- Aprovecha la base de datos PostgreSQL ya seleccionada.
- Evita incorporar servicios adicionales.
- Reduce las consultas repetidas al proveedor externo.
- Permite conservar un catálogo cinematográfico propio, siempre que la licencia lo autorice.
- Mantiene una arquitectura sencilla y adecuada para un proyecto individual.

### Alternativas consideradas

- **Sin almacenamiento intermedio:** consultar siempre al proveedor externo. Es sencillo, pero aumenta la dependencia y el número de solicitudes.
- **Redis:** ofrece una caché especializada y rápida, pero introduce infraestructura y mantenimiento adicionales que no se justifican inicialmente.

### Consecuencias

- Se deberá definir una política de actualización de los datos cinematográficos.
- Los datos almacenados deberán respetar las condiciones de licencia del proveedor.
- Se distinguirá entre los datos persistentes del catálogo y la información temporalmente reutilizable.
- Se evaluará Redis si el volumen de consultas o las necesidades de rendimiento lo justifican.

## ADR-010: Gestión y almacenamiento de imágenes cinematográficas

- **Estado:** Aprobado, condicionado a la validación de la licencia del proveedor
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender necesita mostrar imágenes cinematográficas, principalmente pósteres y fondos, para enriquecer la experiencia de navegación y descubrimiento de películas.

Estas imágenes procederán del proveedor de datos cinematográficos seleccionado, inicialmente TMDB. Es necesario decidir cómo gestionarlas sin introducir infraestructura innecesaria y respetando los derechos y condiciones de uso correspondientes.

Esta decisión está relacionada con la selección del proveedor y la validación de su licencia (ADR-008), así como con la estrategia de almacenamiento y reutilización de datos cinematográficos (ADR-009).

### Decisión

Durante el MVP no se descargarán ni almacenarán archivos de imagen en infraestructura propia.

Se utilizará el siguiente enfoque:

1. PostgreSQL almacenará las referencias o rutas de imagen proporcionadas por el proveedor, como `poster_path` y `backdrop_path`, cuando la licencia permita conservarlas.
2. El backend o el frontend utilizará esas referencias para construir o resolver las direcciones necesarias para mostrar las imágenes desde la CDN del proveedor, de acuerdo con la documentación y las condiciones de uso aplicables.
3. El frontend cargará las imágenes directamente desde la CDN del proveedor.
4. Se utilizarán tamaños adecuados al contexto de visualización, siempre dentro de las opciones permitidas por el proveedor.
5. Si una imagen no está disponible o no puede cargarse, la interfaz mostrará una imagen alternativa o placeholder.

La decisión queda condicionada a confirmar que la licencia del proveedor permite el uso previsto. Antes de utilizar imágenes en producción se deberán comprobar, entre otros aspectos, los requisitos de atribución, las restricciones de uso comercial, la conservación de referencias, la visualización directa desde la CDN, las reglas de caché y las transformaciones o tamaños permitidos.

No se establecerán políticas específicas de caché, expiración ni transformación de imágenes hasta verificar las condiciones aplicables.

### Justificación

- Evita duplicar archivos que ya están disponibles en la infraestructura del proveedor.
- Reduce los costes de almacenamiento y transferencia.
- Evita incorporar servicios adicionales como Cloudinary o Amazon S3 durante el MVP.
- Simplifica la arquitectura y el mantenimiento.
- Mantiene las referencias de imágenes asociadas a los datos cinematográficos almacenados en PostgreSQL.
- Reduce el acoplamiento al conservar referencias del proveedor en lugar de gestionar archivos binarios propios.

### Alternativas consideradas

- **Almacenamiento propio:** descargar las imágenes y guardarlas en un servicio de almacenamiento de objetos. Ofrece mayor control sobre disponibilidad y optimización, pero introduce costes, mantenimiento y la necesidad de confirmar los derechos de almacenamiento y distribución.
- **Servicio externo de gestión de imágenes:** utilizar plataformas como Cloudinary. Aporta herramientas de transformación y optimización, pero añade otra dependencia, configuración y posibles costes; tampoco elimina la necesidad de disponer de derechos para utilizar las imágenes.
- **Uso directo de la CDN del proveedor:** permite mostrar las imágenes sin gestionar archivos propios y reduce la infraestructura necesaria. Es la opción elegida para el MVP, condicionada a la licencia.

### Consecuencias

**Positivas:**

- Menor complejidad técnica y operativa.
- No será necesario gestionar almacenamiento de archivos de imagen.
- Se aprovecha la infraestructura de distribución del proveedor.
- Se reducen los costes iniciales de infraestructura.

**Negativas:**

- La aplicación dependerá de la disponibilidad y el rendimiento de la CDN externa.
- Los cambios en las rutas o referencias del proveedor pueden afectar a la visualización.
- No se tendrá control completo sobre la optimización, transformación o disponibilidad de las imágenes.
- Si el proveedor deja de ofrecer una imagen, la aplicación deberá mostrar una alternativa.

**Consideraciones:**

- La decisión depende de las condiciones de licencia del proveedor seleccionado en el ADR-008.
- Si la licencia no permite este modelo de uso, será necesario revisar la decisión antes de utilizar imágenes en producción.
- Cualquier política de caché, expiración o transformación deberá ajustarse a las condiciones confirmadas del proveedor.

## ADR-011: Organización del código y arquitectura de la aplicación

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender necesita una estructura de código que permita desarrollar y mantener el frontend y el backend de forma organizada.

El proyecto será desarrollado inicialmente por una sola persona, por lo que interesa mantener una arquitectura sencilla, evitando complejidad e infraestructura innecesarias.

Al mismo tiempo, es importante separar las responsabilidades de las distintas funcionalidades para facilitar su evolución.

### Decisión

Se utilizará una arquitectura de monolito modular, con frontend y backend separados dentro de un mismo repositorio.

La estructura inicial será:

```text
movie-recommender/
├── frontend/
├── backend/
├── docs/
└── README.md
```

**Frontend**

- Aplicación independiente desarrollada con React y TypeScript.
- Consumirá el backend mediante una API REST.

**Backend**

- Una única aplicación desarrollada con Python y FastAPI.
- Organizada en módulos que separen las distintas responsabilidades del dominio.
- Compartirá una única base de datos PostgreSQL.

Los módulos iniciales previstos serán:

- `auth`: autenticación e integración con Clerk.
- `users`: información y preferencias de los usuarios.
- `movies`: catálogo e información cinematográfica.
- `ratings`: valoraciones de películas.
- `lists`: listas personales y watchlist.
- `recommendations`: generación de recomendaciones personalizadas.

La organización concreta de estos módulos podrá evolucionar durante la implementación.

### Justificación

- Mantiene una arquitectura sencilla y adecuada para un desarrollo individual.
- Separa claramente frontend y backend.
- Facilita mantener las responsabilidades del backend organizadas.
- Evita los costes operativos y la complejidad de los microservicios.
- Permite ampliar o reorganizar los módulos según evolucionen las necesidades del producto.

### Alternativas consideradas

- **Aplicación monolítica sin modularización:** más sencilla inicialmente, pero puede dificultar la organización cuando crezcan las funcionalidades.
- **Arquitectura de microservicios:** ofrece despliegues y escalabilidad independientes, pero introduce complejidad operativa y de comunicación innecesaria para el MVP.

### Consecuencias

- El frontend y el backend podrán desarrollarse y probarse de forma independiente.
- El backend se desplegará como un único servicio.
- Los módulos compartirán el mismo proceso de ejecución y la misma base de datos PostgreSQL.
- Los módulos no podrán desplegarse ni escalarse de forma independiente dentro de esta arquitectura inicial.
- La separación modular facilitará mantener las responsabilidades organizadas y permitirá extraer servicios independientes en el futuro si las necesidades del proyecto lo justifican.
- La estructura podrá evolucionar durante la implementación sin necesidad de introducir complejidad arquitectónica prematura.

## ADR-012: Diseño inicial del modelo de datos

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender necesita almacenar información sobre los usuarios, las películas y las interacciones de los usuarios con el catálogo.

Es necesario definir un modelo de datos inicial que cubra las funcionalidades principales del MVP sin introducir entidades o relaciones que todavía no sean necesarias.

### Decisión

El modelo de datos inicial de PostgreSQL se organizará alrededor de las siguientes seis entidades principales:

1. **User:** representa a los usuarios de Movie Recommender. Su identidad estará vinculada al identificador proporcionado por Clerk.
2. **Movie:** almacena la información de las películas del catálogo, incluyendo identificadores internos y referencias al proveedor cinematográfico externo.
3. **Rating:** registra las valoraciones que los usuarios realizan sobre las películas.
4. **Watchlist:** representa las películas que un usuario quiere ver.
5. **List:** representa las listas personalizadas creadas por los usuarios.
6. **DiaryEntry:** registra las películas que los usuarios han visto y las entradas asociadas a su diario cinematográfico.

### Relaciones principales

- Un usuario puede tener muchas valoraciones.
- Un usuario puede guardar muchas películas en su watchlist.
- Un usuario puede crear muchas listas.
- Una lista puede contener muchas películas y una película puede aparecer en muchas listas.
- Un usuario puede registrar muchas entradas en su diario.
- Las valoraciones, las entradas del diario y las listas estarán vinculadas a sus respectivos usuarios y películas.

### Identificadores

Las entidades principales utilizarán identificadores internos UUID.

Los identificadores externos del proveedor cinematográfico se almacenarán por separado, evitando utilizar identificadores de TMDB como claves primarias internas.

### Justificación

- Cubre las funcionalidades principales previstas para el MVP.
- Mantiene una estructura comprensible y ampliable.
- Evita acoplar el modelo de datos a un proveedor cinematográfico concreto.
- Facilita establecer relaciones y restricciones de integridad en PostgreSQL.
- Permite incorporar nuevas funcionalidades sin rediseñar toda la base de datos.

### Alternativas consideradas

- **Modelo de datos más amplio desde el inicio:** incorporar géneros, actores, directores, estadísticas y otras entidades desde la primera versión. Se descarta para evitar complejidad prematura.
- **Utilizar identificadores externos como claves primarias:** simplificaría inicialmente la integración con TMDB, pero aumentaría el acoplamiento al proveedor.

### Consecuencias

- Se deberán definir las restricciones de integridad y las relaciones entre las entidades durante la implementación.
- Las tablas de relación necesarias, como la que conecta listas y películas, se crearán según las relaciones del dominio.
- Las entidades de géneros, actores, directores y estadísticas se incorporarán cuando las funcionalidades del producto lo requieran.
- El modelo podrá evolucionar mediante migraciones gestionadas con Alembic.

Los campos concretos de cada entidad y las reglas detalladas de borrado y actualización se definirán durante el diseño e implementación de la base de datos.

## ADR-013: Integridad y restricciones de datos

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender necesita garantizar que los datos almacenados en PostgreSQL sean coherentes y que las relaciones entre usuarios, películas, valoraciones, listas y entradas del diario respeten las reglas del producto.

Para ello, se definirán restricciones de integridad y unicidad en la propia base de datos, evitando depender exclusivamente de las validaciones del backend.

### Decisión

Se establecerán las siguientes reglas:

1. **Usuarios**
   - Cada usuario tendrá un UUID interno único.
   - El identificador de usuario proporcionado por Clerk será único.

2. **Películas**
   - Cada película tendrá un UUID interno.
   - La combinación del proveedor cinematográfico y su identificador externo será única.

3. **Valoraciones**
   - Cada usuario podrá tener una única valoración por película.
   - La combinación de usuario y película tendrá una restricción de unicidad.
   - Si el usuario vuelve a valorar una película, se actualizará la valoración existente.

4. **Watchlist**
   - Un usuario no podrá guardar dos veces la misma película en su watchlist.
   - La combinación de usuario y película será única.

5. **Listas**
   - Cada lista pertenecerá a un usuario.
   - Solo el propietario podrá modificar o eliminar sus listas.
   - El backend comprobará la propiedad de la lista antes de permitir operaciones protegidas.

6. **Películas en listas**
   - Una película no podrá aparecer más de una vez dentro de la misma lista.
   - La combinación de lista y película será única.

7. **Diario cinematográfico**
   - Cada entrada estará asociada a un usuario y una película.
   - Un usuario podrá registrar varias entradas para una misma película, permitiendo guardar distintos visionados.

8. **Relaciones y eliminaciones**
   - Se utilizarán claves foráneas para garantizar la integridad de las relaciones.
   - Las reglas de eliminación se definirán explícitamente para cada relación durante la implementación, evitando registros huérfanos o borrados accidentales.

### Justificación

- Evita duplicados y relaciones inconsistentes.
- Mantiene la integridad de los datos incluso cuando existen operaciones simultáneas.
- Permite actualizar valoraciones sin perder la coherencia del modelo.
- Separa las valoraciones del historial de visionados.
- Aprovecha las restricciones nativas de PostgreSQL.
- Refuerza la protección de los datos personales mediante comprobaciones de propiedad en el backend.

### Alternativas consideradas

- **Validaciones exclusivamente en el backend:** se descartan porque no garantizan por sí solas la integridad ante operaciones simultáneas o accesos desde otros procesos.
- **Historial de múltiples valoraciones:** se descarta para el MVP porque el producto tendrá una única valoración actual por usuario y película.

### Consecuencias

- Las restricciones de unicidad y las claves foráneas se implementarán mediante SQLAlchemy y Alembic.
- El backend deberá gestionar los intentos de insertar registros duplicados y devolver errores adecuados al cliente.
- Las operaciones protegidas sobre listas deberán verificar que el usuario autenticado es su propietario.
- Las reglas de borrado se definirán según las necesidades de cada entidad y relación.
- El diario permitirá múltiples registros de una misma película por usuario.

## ADR-014: Organización interna del backend

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender utilizará FastAPI para implementar su backend.

A medida que se incorporen funcionalidades, será necesario separar las responsabilidades relacionadas con las peticiones HTTP, la lógica de negocio y el acceso a la base de datos.

Se busca una estructura que facilite el mantenimiento, las pruebas y la evolución del proyecto sin introducir complejidad arquitectónica innecesaria.

### Decisión

El backend utilizará una arquitectura de tres capas:

1. **API / Routes**
   - Gestiona los endpoints de FastAPI.
   - Recibe y valida las peticiones HTTP.
   - Delega las operaciones en la capa de servicios.
   - Construye y devuelve las respuestas HTTP.

2. **Services**
   - Contiene la lógica de negocio de la aplicación.
   - Coordina las operaciones necesarias para cada funcionalidad.
   - Aplica las reglas de negocio.
   - Utiliza los repositorios para acceder a los datos.

3. **Repositories / Data Access**
   - Gestiona las consultas y operaciones sobre PostgreSQL.
   - Utiliza SQLAlchemy para interactuar con la base de datos.
   - Encapsula las operaciones de persistencia y recuperación de información.

Estas capas se organizarán dentro de los módulos funcionales definidos en el ADR-011.

### Flujo de una petición

Por ejemplo, al registrar una valoración:

1. Una ruta de FastAPI recibe la petición `POST /api/v1/ratings`.
2. El servicio correspondiente aplica las reglas de negocio y determina si debe crear o actualizar la valoración.
3. El repositorio realiza las operaciones necesarias sobre PostgreSQL.
4. El resultado vuelve a través de las capas hasta generar la respuesta HTTP.

### Justificación

- Separa las responsabilidades de cada parte del backend.
- Evita mezclar consultas SQL con lógica de negocio y gestión HTTP.
- Facilita las pruebas unitarias de los servicios.
- Permite reutilizar la lógica de negocio desde diferentes endpoints.
- Mantiene una arquitectura comprensible y adecuada para el MVP.

### Alternativas consideradas

- **Lógica concentrada en las rutas:** más sencilla inicialmente, pero dificulta el mantenimiento y las pruebas a medida que crece la aplicación.
- **Arquitecturas más complejas, como Clean Architecture completa:** ofrecen una separación adicional de responsabilidades, pero introducirían abstracciones y complejidad que no se consideran necesarias inicialmente.

### Consecuencias

- Cada módulo funcional tendrá sus rutas, servicios y repositorios cuando corresponda.
- Las rutas no contendrán directamente la lógica de negocio ni las consultas SQL.
- Los servicios no dependerán de los detalles de las peticiones HTTP.
- Los repositorios serán responsables del acceso a los datos mediante SQLAlchemy.
- La implementación podrá evolucionar si aparecen necesidades arquitectónicas nuevas.

## ADR-015: Gestión de sesiones y transacciones de base de datos

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender utilizará PostgreSQL como base de datos principal y SQLAlchemy 2.x como ORM.

Es necesario establecer cómo se gestionarán las sesiones de base de datos y las transacciones para garantizar la integridad de los datos y evitar problemas derivados de compartir sesiones entre peticiones concurrentes.

También debemos decidir si utilizaremos SQLAlchemy en modo síncrono o asíncrono.

### Decisión

Se utilizará SQLAlchemy 2.x en modo síncrono durante el desarrollo del MVP.

La gestión de sesiones y transacciones seguirá estas reglas:

1. Cada petición HTTP que necesite acceder a PostgreSQL tendrá su propia sesión de SQLAlchemy.
2. FastAPI gestionará la creación y el cierre de las sesiones mediante dependencias (`Depends`).
3. Las sesiones no se compartirán entre peticiones concurrentes.
4. Las operaciones que modifiquen datos utilizarán transacciones.
5. Los servicios coordinarán las operaciones que formen parte de una misma transacción.
6. Se realizará `commit` cuando todas las operaciones correspondientes terminen correctamente.
7. Si ocurre un error, se realizará `rollback` para deshacer los cambios pendientes.
8. Las sesiones se cerrarán al finalizar su uso, independientemente del resultado de la operación.

### Justificación

- El modo síncrono ofrece una implementación sencilla y suficiente para las necesidades iniciales del MVP.
- Evita introducir complejidad adicional en la gestión de operaciones asíncronas.
- El uso de una sesión por petición facilita aislar las operaciones concurrentes.
- Las transacciones permiten mantener la integridad de los datos cuando una operación requiere varios cambios relacionados.
- La gestión mediante dependencias de FastAPI facilita centralizar el ciclo de vida de las sesiones.

### Alternativas consideradas

- **SQLAlchemy asíncrono:** permite realizar operaciones de base de datos de forma asíncrona, pero añade complejidad en la configuración y gestión de sesiones. Se podrá reconsiderar si las necesidades de concurrencia lo justifican.
- **Compartir una sesión entre peticiones:** se descarta porque las sesiones de SQLAlchemy no están diseñadas para compartirse simultáneamente entre distintos hilos o tareas.

### Consecuencias

- Se configurará un motor de SQLAlchemy síncrono.
- Se utilizará `sessionmaker` para crear sesiones.
- FastAPI proporcionará las sesiones mediante una dependencia reutilizable.
- Los servicios deberán gestionar correctamente los límites de las transacciones.
- Se evitarán sesiones globales compartidas entre peticiones.
- Si en el futuro se necesita procesamiento asíncrono, se evaluará una migración específica.

## ADR-016: Diseño y convenciones de la API REST

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender utilizará una API REST desarrollada con FastAPI para comunicar el frontend React con el backend.

Es necesario establecer convenciones comunes para las rutas, los métodos HTTP, los formatos de intercambio de datos, los códigos de respuesta y la documentación.

### Decisión

La API REST seguirá las siguientes convenciones:

#### 1. Versionado

Todas las rutas utilizarán el prefijo `/api/v1`.

Ejemplos:

- `GET /api/v1/movies`
- `GET /api/v1/movies/{movie_id}`
- `POST /api/v1/ratings`

El versionado permitirá introducir cambios incompatibles en futuras versiones sin afectar necesariamente a los clientes existentes.

#### 2. Métodos HTTP

Se utilizarán los métodos HTTP según su propósito:

- `GET`: consultar recursos.
- `POST`: crear recursos.
- `PUT`: sustituir un recurso.
- `PATCH`: modificar parcialmente un recurso.
- `DELETE`: eliminar recursos.

#### 3. Formato de intercambio de datos

- Las peticiones y respuestas utilizarán JSON cuando corresponda.
- Los nombres de los campos utilizarán `snake_case`.
- Las fechas y horas se representarán mediante formatos compatibles con ISO 8601.

#### 4. Códigos de respuesta HTTP

Se utilizarán códigos HTTP adecuados para representar el resultado de las operaciones.

Entre los principales:

- `200 OK`: operación correcta.
- `201 Created`: recurso creado.
- `204 No Content`: operación correcta sin contenido de respuesta.
- `400 Bad Request`: petición incorrecta.
- `401 Unauthorized`: usuario no autenticado.
- `403 Forbidden`: usuario sin permisos.
- `404 Not Found`: recurso inexistente.
- `409 Conflict`: conflicto con el estado actual del recurso.
- `422 Unprocessable Content`: datos de entrada no válidos.
- `500 Internal Server Error`: error interno del servidor.

Los errores deberán seguir el formato común definido en el ADR-017, independientemente de que se originen en la lógica de negocio o en la validación de peticiones de FastAPI.

#### 5. Documentación de la API

Se utilizará OpenAPI como especificación para describir los endpoints, parámetros, esquemas de datos, respuestas y requisitos de autenticación.

FastAPI generará automáticamente la especificación OpenAPI y proporcionará dos interfaces de documentación:

- **Swagger UI:** disponible en `/docs`, permitirá consultar y probar los endpoints desde el navegador.
- **ReDoc:** disponible en `/redoc`, ofrecerá una presentación alternativa orientada a la consulta de la documentación.

### Justificación

- Utiliza convenciones ampliamente conocidas en el desarrollo de APIs REST.
- Facilita la comunicación entre frontend y backend.
- Permite mantener una API coherente y predecible.
- Aprovecha las funcionalidades integradas de FastAPI.
- Facilita las pruebas y la documentación durante el desarrollo.

### Alternativas consideradas

- **API sin versionado:** simplifica inicialmente las rutas, pero dificulta introducir cambios incompatibles en el futuro.
- **Documentación manual:** ofrece control sobre el contenido, pero obliga a mantenerla separada de la implementación.
- **Herramientas de documentación adicionales:** no se consideran necesarias porque FastAPI ya proporciona integración con OpenAPI, Swagger UI y ReDoc.

### Consecuencias

- Las rutas estarán organizadas bajo `/api/v1`.
- Los endpoints seguirán convenciones HTTP coherentes.
- Los esquemas de petición y respuesta se definirán mediante modelos de Pydantic.
- Los errores de validación generados automáticamente por FastAPI se adaptarán al formato común definido en el ADR-017.
- La documentación se generará automáticamente a partir de la implementación.
- Se podrán probar los endpoints mediante Swagger UI durante el desarrollo.

## ADR-017: Gestión y formato de errores de la API

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender utilizará una API REST desarrollada con FastAPI.

Es necesario establecer un formato consistente para comunicar los errores del backend al frontend, de manera que React pueda identificarlos y gestionarlos correctamente.

También debemos evitar que las respuestas de error expongan información interna o sensible de la aplicación.

### Decisión

Todos los errores controlados de la API utilizarán una estructura JSON común:

```json
{
	"error": {
		"code": "VALIDATION_ERROR",
		"message": "The submitted data is invalid.",
		"details": [
			{
				"field": "rating",
				"message": "Rating must be between 1 and 10."
			}
		]
	}
}
```

La estructura incluirá:

- `code`: identificador estable del tipo de error.
- `message`: descripción general del problema.
- `details`: información adicional opcional, especialmente útil para errores de validación.

Se definirán inicialmente los siguientes códigos:

| Código                    | Descripción                                                       |
| ------------------------- | ----------------------------------------------------------------- |
| `VALIDATION_ERROR`        | Los datos enviados no son válidos.                                |
| `AUTHENTICATION_REQUIRED` | El usuario no está autenticado.                                   |
| `PERMISSION_DENIED`       | El usuario no tiene permisos para realizar la operación.          |
| `RESOURCE_NOT_FOUND`      | El recurso solicitado no existe.                                  |
| `RESOURCE_CONFLICT`       | La operación entra en conflicto con el estado actual del recurso. |
| `INTERNAL_SERVER_ERROR`   | Se ha producido un error inesperado.                              |

### Responsabilidades

- **FastAPI:** gestionará las excepciones HTTP, los errores de validación y las excepciones no controladas.
- **Services:** generará los errores relacionados con las reglas de negocio.
- **Backend:** transformará los errores en el formato JSON común.
- **Frontend:** interpretará los códigos y mostrará mensajes adecuados al usuario.

Para mantener un formato uniforme, se implementarán manejadores globales de excepciones en FastAPI:

- Los errores de validación generados por FastAPI (`RequestValidationError`) se transformarán en respuestas con código `VALIDATION_ERROR`. Se extraerá la información relevante de los campos y se adaptará a la estructura común.
- Las excepciones HTTP controladas se convertirán al código de error correspondiente, respetando su código de estado HTTP.
- Las excepciones relacionadas con las reglas de negocio se traducirán a los códigos de error definidos.
- Las excepciones inesperadas devolverán `INTERNAL_SERVER_ERROR` y un estado HTTP `500`.

Los errores internos se registrarán mediante logs, pero las respuestas públicas no incluirán trazas internas, consultas SQL, credenciales ni información sensible.

### Justificación

- Proporciona una estructura consistente para todos los endpoints.
- Facilita el tratamiento de errores en React.
- Permite identificar los errores mediante códigos estables.
- Separa los mensajes técnicos de los mensajes que verá el usuario.
- Reduce el riesgo de exposición accidental de información sensible.

### Alternativas consideradas

- **Formato de error diferente por endpoint:** se descarta porque complicaría el tratamiento de errores en el frontend.
- **Devolver únicamente mensajes de texto:** se descarta porque dificulta identificar y clasificar los errores de forma programática.

### Consecuencias

- Se implementarán manejadores globales de excepciones en FastAPI.
- Se definirá un manejador específico para los errores de validación de peticiones.
- Se definirán estructuras de respuesta reutilizables para los errores.
- Los servicios utilizarán excepciones específicas para representar errores de negocio.
- El frontend tendrá un mecanismo común para interpretar los errores.
- Se deberá mantener actualizada la documentación de los códigos de error.

## ADR-018: CORS y comunicación entre frontend y backend

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

Movie Recommender tendrá un frontend desarrollado con React y un backend desarrollado con FastAPI.

Ambas aplicaciones se ejecutarán como servicios independientes y se comunicarán mediante una API REST.

Durante el desarrollo local y en producción, el frontend y el backend utilizarán orígenes diferentes. Por ello, es necesario configurar CORS para permitir las peticiones legítimas sin exponer el backend a orígenes no autorizados.

También debemos establecer medidas básicas para proteger la comunicación y las credenciales de autenticación.

### Decisión

Se utilizará el middleware `CORSMiddleware` de FastAPI para gestionar CORS.

La configuración seguirá estas reglas:

#### 1. Orígenes permitidos

**Desarrollo local:**

- Frontend: `http://localhost:5173`.
- Backend: `http://localhost:8000`.

**Producción:**

- Se permitirá exclusivamente el dominio público del frontend desplegado en Render.
- No se utilizarán comodines para permitir cualquier origen.

Los orígenes permitidos se configurarán mediante variables de entorno o configuración específica de cada entorno.

#### 2. Métodos HTTP

Se permitirán únicamente los métodos necesarios para la API:

- `GET`
- `POST`
- `PUT`
- `PATCH`
- `DELETE`

#### 3. Encabezados HTTP

Se permitirán los encabezados necesarios para las peticiones, incluyendo:

- `Content-Type`
- `Authorization`

#### 4. Autenticación y autorización

El frontend utilizará tokens de Clerk mediante el encabezado:

`Authorization: Bearer <token>`

El backend verificará los tokens recibidos antes de permitir el acceso a los recursos protegidos.

La autenticación confirmará la identidad del usuario, pero no sustituirá la autorización. El backend comprobará en cada operación protegida que el usuario autenticado tiene permisos para acceder o modificar el recurso solicitado.

No se habilitará inicialmente la autenticación mediante cookies cross-origin.

#### 5. Comunicación segura

- La comunicación en producción utilizará HTTPS.
- Las claves privadas y los secretos se almacenarán en variables de entorno del backend.
- No se incluirán credenciales privadas en el código del frontend.
- La configuración de CORS no sustituirá los mecanismos de autenticación y autorización.

### Justificación

- Permite la comunicación entre aplicaciones desplegadas en distintos orígenes.
- Limita el acceso del navegador a los orígenes autorizados.
- Evita configuraciones excesivamente permisivas.
- Aprovecha el middleware integrado de FastAPI.
- Mantiene una configuración sencilla y diferenciada por entorno.
- Refuerza la protección de los recursos privados de cada usuario.

### Alternativas consideradas

- **Permitir cualquier origen (`*`):** se descarta porque ampliaría innecesariamente los orígenes autorizados.
- **Utilizar un único origen para todos los entornos:** se descarta porque desarrollo y producción tienen configuraciones diferentes.
- **Autenticación mediante cookies cross-origin:** no se considera necesaria inicialmente porque utilizaremos tokens Bearer de Clerk.

### Consecuencias

- Se configurará `CORSMiddleware` durante la inicialización de FastAPI.
- Cada entorno tendrá una lista explícita de orígenes permitidos.
- Se deberán actualizar las variables de entorno cuando cambie el dominio del frontend.
- El backend verificará los tokens de Clerk independientemente de CORS.
- Los servicios y endpoints protegidos deberán aplicar las comprobaciones de autorización correspondientes.
- La configuración de producción utilizará exclusivamente HTTPS.

## ADR-019: Configuración y gestión de variables de entorno

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La aplicación necesita gestionar configuraciones diferentes para los entornos de desarrollo, testing y producción. Algunas de estas configuraciones contienen información sensible, como credenciales de bases de datos o claves privadas de servicios externos.

Es necesario establecer un mecanismo uniforme para gestionar esta configuración sin exponer secretos en el repositorio ni en el código fuente.

### Decisión

Se utilizarán variables de entorno para gestionar la configuración de la aplicación.

Las reglas serán:

1. **Desarrollo local:** se utilizarán archivos `.env` para almacenar la configuración local. Estos archivos estarán excluidos del control de versiones mediante `.gitignore`.
2. **Plantillas de configuración:** se mantendrán archivos `.env.example` versionados, con los nombres de las variables necesarias y valores ficticios o de ejemplo, nunca secretos reales. Cada entorno deberá proporcionar sus propios valores.
3. **Testing:** las variables necesarias para las pruebas se configurarán en el entorno de ejecución y en GitHub Actions mediante sus mecanismos de configuración y secretos.
4. **Producción:** las variables de entorno y los secretos se configurarán mediante el sistema de variables y secretos de Render.
5. **Backend:** se utilizará `pydantic-settings` para centralizar, validar y cargar la configuración desde variables de entorno.
6. **Frontend:** únicamente se expondrán al cliente las variables que necesite conocer. Nunca se incluirán claves privadas ni credenciales sensibles en el código frontend. Las variables que Vite exponga al cliente mediante el prefijo `VITE_` se considerarán públicas.

### Reglas de seguridad

- Nunca se subirán archivos `.env` con credenciales reales al repositorio.
- Los secretos serán diferentes entre entornos cuando corresponda.
- Las credenciales privadas solo estarán disponibles en los componentes que necesiten utilizarlas.
- La aplicación validará la presencia y el formato de las variables obligatorias al iniciarse.
- No se escribirán secretos ni credenciales en los logs.
- Si una credencial se expone accidentalmente, deberá revocarse y sustituirse.

### Consecuencias

**Ventajas:**

- Separación clara de la configuración y el código.
- Mayor seguridad al gestionar credenciales.
- Configuración reproducible entre entornos.
- Integración sencilla con GitHub Actions y Render.
- Validación centralizada de la configuración del backend.

## ADR-020: Estrategia de testing

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La aplicación necesita una estrategia de testing que permita detectar errores durante el desarrollo y comprobar que los distintos componentes funcionan correctamente, tanto de forma individual como en conjunto.

También es necesario automatizar la ejecución de las pruebas para evitar que cambios nuevos introduzcan regresiones.

### Decisión

Se utilizarán herramientas específicas para probar el frontend, el backend y la integración entre ambos.

**1. Backend**

- `pytest` será el framework principal de testing.
- `httpx` se utilizará para realizar pruebas de los endpoints de FastAPI mediante su cliente de testing.
- Se implementarán pruebas unitarias para servicios y lógica de negocio.
- Se implementarán pruebas de integración para endpoints, repositorios y acceso a la base de datos.

**2. Frontend**

- `Vitest` será el framework de testing.
- `React Testing Library` se utilizará para probar componentes e interacciones desde la perspectiva del usuario.
- Se comprobará el comportamiento de los componentes y las principales funcionalidades de la interfaz.

**3. Base de datos**

- Las pruebas de integración utilizarán una base de datos PostgreSQL independiente de desarrollo y producción.
- La configuración de conexión de testing será propia de este entorno, tanto en local como en GitHub Actions.
- Los datos de prueba se prepararán y limpiarán de forma controlada para evitar interferencias entre pruebas.
- Las pruebas deberán poder ejecutarse de forma repetible e independiente del orden de ejecución.

**4. Integración continua**

- Se utilizará GitHub Actions para automatizar la ejecución de las pruebas.
- Las pruebas se ejecutarán en cada Pull Request y en los cambios que se incorporen a la rama `main`.
- Una ejecución fallida deberá identificarse antes de considerar validado el cambio.

### Consecuencias

**Ventajas:**

- Detección temprana de errores.
- Mayor confianza al modificar funcionalidades existentes.
- Separación de las pruebas de frontend, backend e integración.
- Ejecución automática de pruebas mediante GitHub Actions.
- Menor riesgo de introducir regresiones.

**Inconvenientes:**

- Las pruebas requieren mantenimiento a medida que evoluciona la aplicación.
- La configuración inicial de testing e integración continua añade trabajo.
- Será necesario mantener una base de datos específica para las pruebas de integración.

### Fuera de alcance inicial

No se establece todavía un porcentaje mínimo obligatorio de cobertura de código ni se incorpora testing end-to-end con herramientas como Playwright. Estas decisiones podrán revisarse cuando el MVP tenga sus funcionalidades principales implementadas.

## ADR-021: Estrategia de logging y monitorización

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La aplicación necesita mecanismos para registrar eventos relevantes, detectar errores y facilitar el diagnóstico de problemas durante el desarrollo y en producción.

Es importante disponer de información suficiente para identificar incidencias sin comprometer la privacidad ni la seguridad de los usuarios.

### Decisión

Se implementará una estrategia básica de logging y monitorización, utilizando inicialmente las herramientas disponibles en la plataforma de despliegue.

**1. Backend**

- Se utilizará el módulo estándar `logging` de Python.
- En desarrollo, los logs se mostrarán en consola con un formato legible.
- En producción, los logs utilizarán un formato estructurado JSON para facilitar su consulta y análisis.
- Se registrarán errores, excepciones y eventos relevantes de la aplicación.
- Se utilizarán niveles de logging apropiados: DEBUG, INFO, WARNING, ERROR y CRITICAL.
- Se utilizará un identificador de petición (_request ID_) para relacionar los logs correspondientes a una misma petición HTTP.

**2. Frontend**

- Se gestionarán los errores de ejecución y los errores relevantes de las peticiones a la API.
- Se mostrará información comprensible al usuario cuando ocurra un error.
- No se registrarán datos sensibles ni información personal innecesaria.
- Los errores registrados en el frontend no incluirán tokens de autenticación, credenciales ni contenido sensible de las respuestas de la API.

**3. Producción**

- Se utilizarán inicialmente los logs y las métricas disponibles en Render.
- No se contratarán herramientas externas de monitorización durante el MVP.
- Se revisarán periódicamente los errores y el estado general de los servicios.

### Reglas de seguridad y privacidad

- Nunca se registrarán contraseñas, tokens de autenticación, claves API ni credenciales.
- Se evitará registrar datos personales que no sean necesarios para diagnosticar incidencias.
- Los mensajes de error destinados al usuario no expondrán detalles internos de la aplicación.
- Los logs deberán permitir identificar el contexto técnico de una incidencia sin revelar información sensible.
- Se establecerá una política de retención de logs teniendo en cuenta las necesidades de privacidad y las capacidades de la plataforma.

### Consecuencias

**Ventajas:**

- Facilita la detección y resolución de errores.
- Permite analizar el comportamiento general de la aplicación.
- Evita incorporar costes adicionales durante el MVP.
- Establece una base para incorporar herramientas de observabilidad más avanzadas en el futuro.
- Facilita relacionar los eventos de una misma petición mediante su identificador.

**Inconvenientes:**

- Las herramientas básicas pueden ofrecer capacidades limitadas de análisis y alertas.
- La revisión de incidencias dependerá inicialmente de la consulta manual de logs y métricas.
- Será necesario definir y revisar la política de retención de logs conforme a las necesidades de privacidad y a las capacidades de la plataforma.

## ADR-022: Estrategia de despliegue y CI/CD

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La aplicación necesita un proceso de integración y despliegue que permita incorporar cambios de forma controlada, ejecutar las pruebas automáticamente y publicar nuevas versiones sin comprometer la estabilidad de producción.

Se utilizarán GitHub como plataforma de control de versiones, GitHub Actions para integración continua y Render como plataforma de despliegue.

### Decisión

Se establecerá el siguiente flujo de trabajo:

**1. Control de versiones**

- GitHub será el repositorio central del código fuente.
- Se utilizará `main` como rama principal y estable.
- Cada funcionalidad o corrección se desarrollará preferentemente en una rama independiente.
- Los cambios se integrarán en `main` mediante Pull Requests.

**2. Integración continua (CI)**

- GitHub Actions ejecutará automáticamente las pruebas del backend y frontend.
- Las comprobaciones se realizarán en cada Pull Request y en los cambios incorporados a `main`.
- Los cambios deberán superar las comprobaciones automatizadas antes de considerarse validados.

**3. Despliegue continuo (CD)**

- Render alojará el frontend y el backend como servicios de aplicación independientes.
- PostgreSQL se utilizará como servicio gestionado de base de datos en Render.
- Se configurará el despliegue automático de los servicios de aplicación cuando se incorporen cambios a `main`.
- Los secretos y variables de configuración se gestionarán desde Render.
- No se introducirán procesos de despliegue adicionales durante el MVP.

**4. Migraciones de base de datos**

- Alembic gestionará las modificaciones del esquema de PostgreSQL.
- Las migraciones deberán revisarse y probarse antes de aplicarse en producción.
- Las migraciones se ejecutarán como parte del proceso de despliegue, antes de iniciar la nueva versión del backend.
- Si una migración falla, el despliegue del backend no deberá continuar.
- Se tendrá en cuenta la posibilidad de recuperación ante migraciones fallidas. No se asumirá que todas las migraciones pueden revertirse automáticamente; las medidas de recuperación dependerán del tipo de cambio y de su impacto sobre los datos.

**5. Verificación posterior al despliegue**

- Se comprobará que los servicios se encuentran operativos después de cada despliegue.
- Se revisarán los logs y las métricas disponibles en Render.
- Se verificarán los endpoints de salud del backend y el funcionamiento básico del frontend.

### Herramientas

- Git y GitHub: control de versiones y colaboración.
- GitHub Actions: integración continua.
- Render: alojamiento del frontend, backend y base de datos gestionada.
- Alembic: migraciones de base de datos.

No se incorporará Docker ni infraestructura adicional durante esta fase.

### Consecuencias

**Ventajas:**

- Proceso de integración y despliegue sencillo.
- Ejecución automática de pruebas.
- Reducción del riesgo de publicar cambios defectuosos.
- Menor carga operativa durante el MVP.
- Posibilidad de evolucionar hacia procesos más avanzados cuando sea necesario.

**Inconvenientes:**

- Dependencia de GitHub Actions y Render.
- Los despliegues automáticos requieren una configuración correcta de las comprobaciones y dependencias.
- Las migraciones de base de datos necesitan especial atención para evitar incompatibilidades entre versiones.
- Una migración fallida puede requerir intervención manual y un procedimiento de recuperación específico.

## ADR-023: Estrategia de versionado y compatibilidad de la API

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La API REST necesita una estrategia de versionado que permita introducir cambios y nuevas funcionalidades sin provocar incompatibilidades inesperadas en el frontend o en otros posibles consumidores.

También es necesario establecer una forma de identificar las versiones de la aplicación y documentar los cambios relevantes.

### Decisión

**1. Versionado de la API**

- Se mantendrá el versionado mediante rutas, utilizando el prefijo `/api/v1`.
- Los cambios compatibles con la versión actual se incorporarán a `v1`.
- Los cambios que rompan la compatibilidad requerirán una nueva versión de API, por ejemplo, `/api/v2`.
- Se considerarán potencialmente incompatibles los cambios que modifiquen o eliminen endpoints, campos de respuesta, parámetros, formatos de datos o comportamientos existentes de forma que puedan afectar a sus consumidores.
- No se mantendrán varias versiones de la API simultáneamente durante el MVP, salvo que exista una necesidad justificada.

**2. Versionado de la aplicación**

- Se utilizará versionado semántico (Semantic Versioning o SemVer), siguiendo el formato `MAJOR.MINOR.PATCH`.
- `MAJOR`: cambios incompatibles con versiones anteriores.
- `MINOR`: incorporación de funcionalidades compatibles.
- `PATCH`: correcciones compatibles y mejoras menores.

El versionado de la aplicación será independiente del versionado de la API. Por tanto, una nueva versión de la aplicación no implicará necesariamente una nueva versión de la API.

**3. Compatibilidad**

- Se evitarán cambios incompatibles en los endpoints existentes.
- Los cambios en estructuras JSON, parámetros, códigos de respuesta y comportamiento de los endpoints deberán evaluarse teniendo en cuenta su impacto sobre los consumidores.
- Siempre que sea posible, se priorizarán cambios compatibles, como añadir funcionalidades sin alterar los contratos existentes.
- Cuando sea necesario introducir cambios incompatibles, se valorará crear una nueva versión de API.

**4. Documentación de cambios**

- Los cambios relevantes de cada versión deberán quedar documentados.
- Se mantendrá un registro de cambios (`CHANGELOG`) cuando el proyecto comience a publicar versiones.
- La documentación OpenAPI deberá mantenerse actualizada con los cambios de la API.

### Consecuencias

**Ventajas:**

- Mayor previsibilidad al evolucionar la API.
- Menor riesgo de romper la comunicación entre frontend y backend.
- Identificación clara de los cambios entre versiones.
- Estrategia sencilla y adecuada para el MVP.
- Separación entre la evolución de la aplicación y la evolución del contrato de la API.

**Inconvenientes:**

- Será necesario evaluar la compatibilidad de los cambios antes de incorporarlos.
- La creación de nuevas versiones de API puede aumentar el trabajo de mantenimiento si el proyecto crece.
- Mantener la documentación y el registro de cambios actualizados requiere disciplina.

## ADR-024: Estrategia de accesibilidad y diseño responsive

- **Estado:** Aprobado
- **Fecha:** 2026-11-18

### Contexto

La aplicación debe ofrecer una experiencia de uso accesible y consistente en diferentes dispositivos y tamaños de pantalla.

Es necesario establecer criterios técnicos que orienten la implementación del frontend y permitan reducir las barreras de acceso para personas con distintas capacidades y formas de interacción.

### Decisión

**1. Accesibilidad**

- Se utilizarán las pautas WCAG 2.2 nivel AA como objetivo de conformidad.
- La interfaz deberá permitir la navegación mediante teclado, sin depender exclusivamente del ratón o de gestos táctiles.
- Se utilizará HTML semántico siempre que sea posible.
- Los componentes interactivos deberán disponer de nombres, etiquetas y roles accesibles.
- Los campos de formulario deberán tener etiquetas asociadas y los errores deberán identificarse de forma comprensible.
- Se respetarán los requisitos de contraste de texto y elementos visuales establecidos por WCAG 2.2 AA.
- Los elementos que reciban el foco deberán mostrarlo de forma visible y no quedar ocultos por otros elementos de la interfaz.
- Los estados de interacción, como foco, selección, carga y errores, deberán comunicarse de forma perceptible.
- Se evitará transmitir información únicamente mediante colores.

**2. Diseño responsive**

- Se seguirá una estrategia _mobile-first_.
- La interfaz se adaptará a móviles, tablets y pantallas de escritorio.
- Los diseños deberán mantener su funcionalidad y legibilidad en diferentes resoluciones.
- Se evitarán desplazamientos horizontales innecesarios y elementos interactivos difíciles de utilizar en pantallas pequeñas.
- Los controles deberán disponer de un tamaño y separación adecuados para facilitar su interacción táctil.

**3. Consistencia de interfaz**

- Se utilizarán patrones visuales y de interacción consistentes.
- Los componentes reutilizables deberán mantener criterios comunes de accesibilidad.
- Se priorizará una experiencia predecible en toda la aplicación.
- Los cambios de estado y las acciones principales deberán comunicarse de manera coherente entre pantallas.

**4. Testing y validación**

- Se incorporarán herramientas de comprobación automática de accesibilidad durante el desarrollo.
- Se realizarán revisiones manuales de navegación por teclado, visibilidad del foco, etiquetas, mensajes de error y comportamiento de los componentes.
- Se comprobará el funcionamiento responsive en distintos tamaños de pantalla.
- Las comprobaciones automáticas se considerarán complementarias y no sustituirán las revisiones manuales.
- Se revisarán los componentes interactivos reutilizables para evitar que los problemas de accesibilidad se propaguen por distintas pantallas.

### Consecuencias

**Ventajas:**

- Mejora de la experiencia para personas con distintas capacidades.
- Mayor facilidad de uso en diferentes dispositivos.
- Reducción de problemas de accesibilidad durante el desarrollo.
- Mayor consistencia entre componentes y pantallas.
- Una base técnica más sólida para el crecimiento del frontend.

**Inconvenientes:**

- La validación de accesibilidad requiere tiempo adicional.
- Algunos componentes visuales pueden necesitar implementaciones específicas para cumplir los criterios de accesibilidad.
- Alcanzar la conformidad WCAG 2.2 AA requiere revisiones continuas durante el desarrollo.

## ADR-025: Estrategia de seguridad, autorización y aislamiento de datos entre usuarios

- **Estado:** Aceptado
- **Fecha:** 2026-11-18

## Contexto

Movie Recommender permite que los usuarios gestionen información personal, como valoraciones, listas, watchlist y entradas de su diario cinematográfico. Además, la aplicación incorpora perfiles públicos y privados, por lo que es necesario definir cómo se controla el acceso a estos recursos.

La autenticación identifica al usuario, pero no garantiza por sí sola que tenga permiso para acceder a un recurso concreto. El backend debe aplicar las reglas de autorización y garantizar que cada usuario solo pueda acceder a los datos que le corresponden.

También es necesario establecer reglas de visibilidad coherentes para los perfiles y los distintos recursos de la aplicación.

## Decisión

### 1. Autenticación

- Clerk será el proveedor de autenticación.
- El frontend utilizará Clerk para gestionar el inicio y cierre de sesión.
- El backend verificará los tokens de autenticación recibidos en las peticiones protegidas.
- La identidad externa de Clerk se relacionará con un usuario interno mediante un identificador externo almacenado en la entidad `User`.
- El backend no confiará en la identidad o los permisos declarados por el frontend sin verificar.

### 2. Autorización en el backend

- Toda operación protegida deberá comprobar los permisos del usuario autenticado.
- El backend determinará la identidad del usuario a partir del token verificado.
- No se confiará en un `user_id` enviado por el frontend para determinar a qué usuario pertenecen los datos de una operación.
- Cada consulta o modificación deberá comprobar que el usuario tiene permiso para acceder al recurso correspondiente.
- Las comprobaciones de autorización se implementarán en el backend, principalmente en la capa de servicios.

### 3. Privacidad de los perfiles

La aplicación permitirá configurar los perfiles como públicos o privados.

- Los perfiles serán públicos por defecto.
- Un perfil público podrá consultarse sin iniciar sesión.
- Un perfil privado solo podrá consultarlo su propietario.
- La privacidad del perfil prevalecerá sobre la configuración individual de visibilidad de sus listas.

### 4. Privacidad de las listas y la watchlist

Las listas y la watchlist seguirán las mismas reglas de visibilidad:

- Con un perfil público, las listas serán públicas por defecto.
- El usuario podrá configurar individualmente una lista como privada.
- Con un perfil privado, todas sus listas serán privadas, independientemente de su configuración individual.
- Si un usuario cambia su perfil de público a privado, todas sus listas pasarán a ser privadas.
- Si posteriormente vuelve a hacer público su perfil, las listas permanecerán privadas hasta que decida hacerlas públicas explícitamente.
- Las listas públicas podrán consultarse sin iniciar sesión.
- Las listas privadas solo podrán consultarse por su propietario.

### 5. Privacidad de las valoraciones y el diario

Las valoraciones y las entradas del diario seguirán la configuración de privacidad del perfil:

- En perfiles públicos, podrán consultarse por cualquier usuario que haya iniciado sesión.
- En perfiles privados, solo podrán consultarse por su propietario.
- Las valoraciones y el diario no estarán disponibles para visitantes sin iniciar sesión, incluso cuando pertenezcan a un perfil público.

### 6. Aislamiento de datos

El backend garantizará que los usuarios no puedan acceder ni modificar información privada de otros usuarios.

Esta protección se aplicará, como mínimo, a:

- Valoraciones.
- Watchlist.
- Listas.
- Entradas del diario.
- Datos privados del perfil.

Las operaciones de lectura, creación, modificación y eliminación deberán aplicar las comprobaciones de autorización correspondientes.

### 7. Protección de información

- Las respuestas de la API incluirán únicamente la información necesaria para cada operación.
- Los errores no expondrán detalles internos del sistema ni información sensible.
- Los logs no almacenarán tokens de autenticación, contraseñas ni información personal innecesaria.
- Las comunicaciones de producción utilizarán HTTPS.

### 8. Bloqueo de usuarios

La funcionalidad para bloquear a otros usuarios queda fuera del alcance del MVP. Podrá evaluarse en el futuro si se incorporan funcionalidades sociales que hagan necesaria esta protección adicional.

## Consecuencias

### Positivas

- Se establece una separación clara entre autenticación y autorización.
- Se centralizan las comprobaciones de permisos en el backend.
- Se reduce el riesgo de acceso no autorizado a datos de otros usuarios.
- Las reglas de privacidad son coherentes entre perfiles, listas, watchlist, valoraciones y diario.
- Se permite descubrir perfiles y listas públicas sin necesidad de registrarse.
- Se evita añadir complejidad social innecesaria durante el MVP.

### Negativas

- Será necesario implementar comprobaciones de autorización en las operaciones protegidas.
- Las reglas de privacidad de perfiles y listas añaden cierta complejidad a las consultas y servicios.
- Habrá que prestar especial atención a los cambios de privacidad para garantizar que no se expongan datos accidentalmente.

## Consideraciones para la implementación

- Las comprobaciones de autorización deberán probarse mediante tests que contemplen tanto al propietario como a otros usuarios autenticados y visitantes sin autenticar.
- Los cambios de privacidad de un perfil deberán actualizar la visibilidad efectiva de todas sus listas.
- La privacidad del perfil deberá comprobarse también al consultar listas, valoraciones y entradas del diario.
- La verificación de tokens de Clerk deberá realizarse en el backend mediante mecanismos oficiales y actualizados del proveedor.
- La implementación deberá evitar depender exclusivamente de controles de visibilidad en el frontend.

## ADR-026: Sistema de recomendaciones

- **Estado:** Aceptado
- **Fecha:** 2026-11-18

## Contexto

Movie Recommender necesita ofrecer recomendaciones cinematográficas personalizadas desde el MVP. El objetivo es ayudar a los usuarios a descubrir películas que encajen con sus gustos y preferencias, utilizando la información disponible sobre su actividad dentro de la aplicación y los metadatos de las películas.

Como el proyecto será desarrollado individualmente y dispone de recursos limitados, el sistema inicial debe ser sencillo de implementar, mantener y ampliar. No se introducirán modelos de machine learning ni infraestructuras adicionales durante el MVP.

## Decisión

### 1. Enfoque del recomendador

Se implementará un sistema híbrido que combine:

- Recomendaciones basadas en las preferencias y actividad del usuario.
- Recomendaciones basadas en la similitud entre películas.

La primera versión utilizará reglas y algoritmos sencillos basados en metadatos. No se utilizará machine learning durante el MVP.

### 2. Datos utilizados para personalizar las recomendaciones

El sistema podrá utilizar las siguientes fuentes de información:

- **Valoraciones:** películas valoradas por el usuario y puntuaciones asignadas.
- **Géneros:** géneros de las películas que el usuario valora positivamente.
- **Películas favoritas:** películas que el usuario haya marcado como favoritas.
- **Similitud cinematográfica:** géneros, palabras clave, directores, reparto y otros metadatos disponibles.
- **Diario:** películas que el usuario haya registrado como vistas.

Estos datos permitirán identificar preferencias y encontrar películas que puedan resultar interesantes para cada usuario.

### 3. Usuarios nuevos

Para usuarios que todavía no tengan suficiente actividad, se utilizará un enfoque combinado:

- Durante el registro, podrán seleccionar géneros y películas de su interés.
- Estas preferencias servirán para generar las primeras recomendaciones personalizadas.
- Mientras no haya suficientes datos de actividad, el sistema complementará las recomendaciones con películas populares y bien valoradas.
- A medida que el usuario interactúe con la aplicación, las recomendaciones se adaptarán progresivamente a sus gustos.

### 4. Actualización de las recomendaciones

Las recomendaciones se actualizarán mediante una combinación de actualización por eventos y actualización periódica.

**Actualización por eventos:**

Se actualizarán cuando el usuario realice acciones relevantes, como:

- Valorar una película.
- Marcar una película como favorita.
- Registrar una película en el diario.

**Actualización periódica:**

Se realizará una actualización periódica como complemento, para refrescar las recomendaciones aunque el usuario no haya realizado nuevas acciones.

No se recalcularán todas las recomendaciones en tiempo real con cada interacción.

### 5. Organización de las recomendaciones

La interfaz organizará las recomendaciones en cuatro secciones:

- **Recomendadas para ti:** selección personalizada según las preferencias y actividad del usuario.
- **Porque te gustó…:** películas similares a otras que el usuario haya valorado positivamente.
- **Descubre algo nuevo:** películas populares o bien valoradas que encajen con las preferencias del usuario.
- **Tendencias:** películas populares en general, independientemente de las preferencias individuales.

### 6. Feedback sobre las recomendaciones

Los usuarios podrán indicar si una recomendación les interesa mediante dos acciones:

- **Me interesa:** registra una señal positiva.
- **No me interesa:** registra una señal negativa.

El sistema utilizará estas señales para mejorar futuras recomendaciones y evitar mostrar repetidamente películas que el usuario haya descartado o películas demasiado similares a ellas.

Este mecanismo tendrá una implementación sencilla durante el MVP y complementará el resto de los datos utilizados por el recomendador.

### 7. Arquitectura e integración

El sistema de recomendaciones se implementará dentro del backend existente, como parte del módulo `recommendations`.

- La lógica de recomendación estará separada de las rutas de la API.
- Se reutilizarán los datos cinematográficos y las entidades existentes.
- No se introducirán microservicios ni infraestructura adicional para el recomendador.
- Las recomendaciones se expondrán mediante endpoints de la API REST.
- El sistema podrá evolucionar posteriormente sin necesidad de modificar la arquitectura general de la aplicación.

## Consecuencias

### Positivas

- Se ofrece personalización desde el MVP.
- Se combinan diferentes fuentes de información para mejorar la relevancia de las recomendaciones.
- Los usuarios nuevos pueden recibir recomendaciones útiles desde el principio.
- La solución inicial es asumible para un desarrollo individual.
- El feedback permite incorporar información adicional sobre los intereses del usuario.
- La arquitectura permite evolucionar hacia algoritmos más sofisticados en el futuro.

### Negativas

- Las recomendaciones iniciales serán menos precisas que las de sistemas basados en modelos de machine learning.
- La calidad dependerá de la cantidad y calidad de los metadatos cinematográficos disponibles.
- Será necesario definir reglas de puntuación y criterios de similitud.
- La actualización periódica requerirá algún mecanismo de ejecución programada.
- El sistema deberá gestionar usuarios con poca actividad y evitar recomendaciones repetitivas.

## Consideraciones para la implementación

- Definir una puntuación interna para ordenar las recomendaciones.
- Establecer criterios iniciales para determinar cuándo dos películas son similares.
- Evitar recomendar películas que el usuario ya haya registrado como vistas, salvo que exista una razón funcional para mostrarlas.
- Evitar mostrar repetidamente las mismas películas en distintas secciones.
- Definir cómo se almacenan y utilizan las señales positivas y negativas del feedback.
- Respetar las reglas de privacidad y autorización establecidas en el ADR-025.
- Mantener la lógica de recomendación desacoplada para facilitar futuras mejoras.
- Evaluar la calidad de las recomendaciones mediante pruebas funcionales y feedback de los usuarios.

## ADR-027: Estrategia de backups y recuperación de datos

- **Estado:** Aceptado
- **Fecha:** 2026-11-18

## Contexto

Movie Recommender utilizará PostgreSQL para almacenar información importante de la aplicación, incluyendo usuarios, películas, valoraciones, listas, watchlist, entradas del diario y preferencias.

La pérdida o corrupción de estos datos podría afectar directamente a la disponibilidad de la aplicación y a la experiencia de sus usuarios.

Por tanto, es necesario establecer una estrategia de copias de seguridad y recuperación que permita restaurar la base de datos ante incidentes, fallos técnicos o pérdida de información.

Como el proyecto será desarrollado individualmente y dispone de recursos limitados, la solución deberá ser sencilla de mantener y tener un coste asumible.

## Decisión

### 1. Estrategia de backups

Se utilizará una estrategia combinada:

- Se aprovecharán los backups automáticos ofrecidos por Render para PostgreSQL, según las características del plan contratado.
- Además, se generarán copias de seguridad propias de forma independiente.
- Las copias propias permitirán reducir la dependencia de Render y disponer de una alternativa de recuperación.

### 2. Frecuencia de las copias propias

Se generará una copia de seguridad propia cada día.

Esta frecuencia establece un equilibrio entre protección de los datos, coste de almacenamiento y complejidad de implementación.

### 3. Retención de las copias

Las copias propias se conservarán durante 30 días.

- Se mantendrán las copias correspondientes a los últimos 30 días.
- Las copias que superen ese periodo podrán eliminarse automáticamente.
- El proceso de limpieza deberá evitar eliminar copias recientes o necesarias para la recuperación.

### 4. Almacenamiento externo

Las copias propias se almacenarán en un servicio externo independiente de Render.

Se valorarán proveedores como Amazon S3 o Cloudflare R2.

La elección definitiva del proveedor se realizará durante la implementación, teniendo en cuenta:

- Coste de almacenamiento.
- Coste de transferencia y recuperación.
- Seguridad y cifrado.
- Facilidad de automatización.
- Fiabilidad y disponibilidad del servicio.

Las copias no se almacenarán exclusivamente en el mismo proveedor que aloja la base de datos de producción.

### 5. Cifrado y protección

Todos los backups deberán estar cifrados:

- **En tránsito:** durante la transferencia desde el entorno de producción hasta el almacenamiento externo, utilizando conexiones seguras.
- **En reposo:** mientras las copias permanezcan almacenadas en el proveedor externo.

Las claves y credenciales necesarias para el cifrado y el acceso al almacenamiento deberán protegerse mediante variables de entorno o un sistema seguro de gestión de secretos.

Las claves de cifrado no se almacenarán junto a las copias de seguridad.

### 6. Pruebas de restauración

Se realizará una prueba de restauración al menos una vez al mes.

Estas pruebas se ejecutarán en un entorno separado de producción para evitar afectar a los datos reales de los usuarios.

Se comprobará que:

- La copia puede descargarse y descifrarse correctamente.
- PostgreSQL puede restaurar la base de datos.
- Las tablas y los datos esperados están presentes.
- La aplicación puede acceder correctamente a la base de datos restaurada.

Se registrará el resultado de cada prueba y se corregirán los problemas detectados.

### 7. Objetivos de recuperación

Se establecen los siguientes objetivos iniciales para el MVP:

**RPO (Recovery Point Objective): 24 horas**

Representa la pérdida máxima de datos que se considera aceptable ante un incidente.

El objetivo inicial será no perder más de 24 horas de información.

**RTO (Recovery Time Objective): 24 horas**

Representa el tiempo objetivo máximo para recuperar el servicio después de un incidente.

El objetivo inicial será restablecer el funcionamiento de la aplicación en un máximo de 24 horas.

Estos objetivos son orientativos y no constituyen garantías de disponibilidad.

## Consecuencias

### Positivas

- Se reduce el riesgo de pérdida permanente de información.
- Se dispone de una alternativa independiente de recuperación.
- Se reduce la dependencia de un único proveedor.
- El cifrado protege la confidencialidad de los datos almacenados.
- Las pruebas periódicas permiten detectar problemas antes de que ocurra un incidente real.
- La política de retención facilita controlar el coste de almacenamiento.

### Negativas

- Será necesario implementar y mantener un proceso automatizado de backups.
- El almacenamiento externo puede generar costes adicionales.
- La gestión de claves y credenciales requiere medidas de seguridad.
- Las pruebas de restauración requieren tiempo y un entorno separado.
- Los objetivos de recuperación pueden resultar exigentes si el proceso de restauración no está suficientemente automatizado.

## Consideraciones para la implementación

- Automatizar la generación diaria de copias de seguridad.
- Automatizar su transferencia al almacenamiento externo.
- Implementar la eliminación de copias con más de 30 días.
- Proteger las credenciales y claves de cifrado.
- Registrar el resultado de cada ejecución de backup.
- Implementar alertas o mecanismos para detectar fallos en la generación o transferencia de copias.
- Documentar el procedimiento de recuperación de PostgreSQL.
- Documentar los pasos necesarios para recuperar el backend y restablecer la aplicación.
- Comprobar periódicamente que los backups automáticos de Render están disponibles según el plan contratado.
- Realizar pruebas mensuales de restauración en un entorno separado de producción.
- Revisar los objetivos RPO y RTO cuando la aplicación tenga usuarios reales y mayores requisitos de disponibilidad.
