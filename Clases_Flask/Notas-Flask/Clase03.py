"""
    Templates avazandos, formularios y APIs
    Parte A - Herencia de templates
    Repetir el <head>, el menú y el <footer> en cada HTML es insistenible. Jinja2 resulve esto con herencia 'templates/base.html'

┌─────────────────────┐          extends           ┌─────────────────────┐
│      base.html      │ ─────────────────────────► │      home.html      │
├─────────────────────┤                            ├─────────────────────┤
│                     │                            │                     │
│  Estructura común   │                            │  Contenido propio   │
│                     │                            │                     │
│  {% block content %}│                            │  {% block content %}│
│  {% endblock %}     │                            │    <h1>Home</h1>    │
│                     │                            │  {% endblock %}     │
└─────────────────────┘                            └─────────────────────┘

    El hijo solo define lo que cambia. Si no defines un bloque, se usa el contenido por defecto del padre

    -- Includes
    Para fragmentos reutilizables que no son una página completa
    'templates/partials/menu.html'

    Para insertar particiones 
    {% include "partials/menu.html" %}

    -- Filtros
    Jinja2 tiene filtros para transformar valores dentro del template:
    <p>{{ nombre|upper }}</p> = ARTURO
    <p>{{ nombre|lower }}</p> = arturo
    <p>{{ nombre|title }}</p> = Arturo
    <p>{{ lista|lenght }}</p> = cantidad de elementos 
    <p>{{ texto|truncate(20) }}</p> = corta a 20 caracteres
    <p>{{ valor|default("Sin dato") }}</p> = si es undefined
    <p>{{ precio|round(2) }}</p> = no más de 2 decimales

    NOTA: Puedes crear tus propios filtros:
    @app.template_filter("moneda")
    def moneda(valor):
        return f"${valor:,.2f} MXN"

    <p>{{ 20|moneda(valor) }}</p> = $20.00 MXN
    
    Formularios!!!
    El error más común en Flask es procesar un POST y devolver el HTML directamente. Si el Usuario recarga la página, se reenvía el formulario. La solución es el patrón "POST/Redirect/GET"
    * Flash messages: Flask tiene un sistema de mensajes de un solo uso, guardados en sesión:

    NOTA!!: app.secret_key: sin ella, flash() y session fallan, porque Flask firma criptográficamente la cookie de sesión. En producción esa clave va en una variable de entornro '.env.local', NUNCA EN CODIGO!!!
    Escape automatico: Jinja2 escapa HTML por defecto. Si el usuario escribe <script>alerta(1)</script> en un campo y lo imprimes con {{ }}. se muestra como texto plano, no se ejecuta. Solo se vuelve peligros si usas el filtro |safe, asi que usalo unicamente con contenido que controlas.
"""

"""
    TAREA FINAL PARA FLASK
    Práctica

    Construye una app de "catálogo de productos" con:

    1. GET /productos → template que lista productos desde una lista en memoria, usando extends de un base.html
    2. GET /productos/<int:id> → detalle de un producto; si no existe, un 404 con template propio
    3. GET /productos/nuevo y POST /productos/nuevo → formulario con validación (nombre obligatorio, precio numérico y mayor a 0), flash messages y patrón PRG
    4. GET /api/productos → la misma lista pero en JSON
    Un filtro personalizado |moneda para mostrar los precios en el template
"""