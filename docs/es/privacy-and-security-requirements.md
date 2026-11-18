# Requisitos de privacidad y seguridad

**Estado:** requisitos de producto aprobados; solución técnica y revisión legal detallada pendientes.

## 1. Principios

- Privacy by Design y minimización de datos.
- Transparencia sobre el tratamiento de información.
- Control del usuario sobre su perfil y contenido.
- Protección de datos personales y preferencias.
- Seguridad transversal desde el inicio.
- Consideración del RGPD y normativa aplicable en España y la Unión Europea.

Este documento recoge requisitos de producto y no sustituye asesoramiento jurídico ni una evaluación legal formal.

## 2. Autenticación y cuenta

### MVP
- Registro e inicio de sesión con email y contraseña.
- Verificación de email.
- Recuperación de contraseña.
- Cierre de sesión.
- Cierre de sesión en todos los dispositivos si el proveedor lo permite.

### Futuro
- Inicio de sesión con Google.

## 3. Privacidad de perfil y contenido

El usuario podrá configurar el perfil como público o privado.

El perfil público podrá mostrar username, nombre visible, biografía, fotografía, películas favoritas y listas que el usuario haya compartido públicamente.

Se contemplan controles individuales para:
- Reseñas.
- Historial de visualizaciones.
- Listas.
- Watchlist.

**Regla de precedencia:** un perfil privado oculta el contenido del perfil a otros usuarios, independientemente de los ajustes individuales de visibilidad.

## 4. Control y gestión de datos

El usuario podrá:
- Editar perfil y datos de cuenta.
- Cambiar email y contraseña.
- Modificar país y preferencias de streaming.
- Modificar preferencias cinematográficas.
- Cambiar opciones de privacidad.
- Gestionar películas vistas, visualizaciones, ratings y reseñas.
- Crear y eliminar listas y sus contenidos.

### Exportación

La exportación de datos personales está incluida como requisito del MVP. El formato y alcance técnico exactos se definirán durante la fase técnica.

### Eliminación de cuenta

La eliminación será definitiva y requerirá confirmación explícita. Antes de confirmar, se explicarán sus consecuencias.

Los datos personales deberán eliminarse o anonimizarse conforme a las obligaciones legales aplicables. No se conservará un perfil de gustos vinculado a una cuenta eliminada. Cualquier excepción de conservación legal deberá estar justificada y documentada.

## 5. Seguridad

Requisitos:
- Protección adecuada de contraseñas y credenciales.
- Autorización por usuario y recurso.
- Prevención de acceso cruzado a datos de otros usuarios.
- Validación de entradas.
- Protección frente a vulnerabilidades web.
- Gestión segura de secretos.
- Minimización de datos personales.
- No incluir secretos ni configuración operativa sensible en el repositorio público.

Los mecanismos concretos se decidirán en arquitectura y diseño técnico.

## 6. Datos cinematográficos y personales

Distinguir claramente:
- Metadatos procedentes de proveedores.
- Puntuaciones externas.
- Valoraciones y reseñas del usuario.
- Preferencias explícitas.
- Preferencias inferidas.
- Registros de visualización.

No deben mostrarse inferencias como hechos declarados por el usuario. El usuario debe poder consultar y corregir las preferencias inferidas.

## 7. Ubicación y streaming

El país configurado en el perfil representa el mercado de referencia para disponibilidad de contenido; no debe tratarse como ubicación física actual. Debe poder modificarse por el usuario.

No inferir residencia ni viaje a partir de señales no confirmadas.

## 8. Cumplimiento y cuestiones pendientes

Pendiente de concretar en fases posteriores:
- Política de privacidad y términos.
- Base jurídica y finalidades de tratamiento.
- Plazos de conservación.
- Gestión de solicitudes de derechos.
- Cookies y tecnologías similares, si aplican.
- Proveedores y encargados de tratamiento.
- Transferencias internacionales, si las hubiera.
- Procedimiento de incidentes y brechas.
- Revisión jurídica de licencias y uso de datos cinematográficos.

## 9. Alcance

Estos requisitos aplican transversalmente a todas las funcionalidades, no solo a las que se prioricen inicialmente para el MVP.
