# 🌍 paises_app — Prueba individual Django

Mini aplicación Django para registrar países y sus valores culturales más representativos.

## Características

- **CRUD completo** de países (crear, ver, editar, eliminar)
- **Valores representativos** por país con categorías (gastronomía, monumentos, tradiciones, etc.)
- **Búsqueda y filtro** por nombre/capital/idioma y continente
- **Diseño estilo atlas** — elegante, con tipografía serif e interfaz responsiva
- Admin de Django preconfigurado

---

## Instalación rápida

### 1. Copiar la app al proyecto

```
ProyectoGrupal/
├── core/
├── paises_app/      ← pegar aquí esta carpeta
└── manage.py
```

### 2. Registrar la app en `core/settings.py`

```python
INSTALLED_APPS = [
    ...
    'paises_app',   # ← agregar esta línea
]
```

### 3. Registrar las URLs en `core/urls.py`

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paises/', include('paises_app.urls')),  # ← agregar
]
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. (Opcional) Cargar datos de ejemplo

```bash
python manage.py shell < paises_app/datos_ejemplo.py
```

### 6. Correr el servidor

```bash
python manage.py runserver
```

Abrir → http://127.0.0.1:8000/paises/

---

## Modelos

### `Pais`
| Campo          | Tipo              | Descripción                      |
|----------------|-------------------|----------------------------------|
| nombre         | CharField(100)    | Nombre del país (único)          |
| codigo_iso     | CharField(3)      | Código ISO 3 letras (único)      |
| continente     | CharField choices | 7 continentes disponibles        |
| capital        | CharField(100)    | Ciudad capital                   |
| poblacion      | PositiveBigInt    | Número de habitantes             |
| idioma         | CharField(100)    | Idioma oficial                   |
| moneda         | CharField(100)    | Nombre y código de moneda        |
| bandera_emoji  | CharField(10)     | Emoji de la bandera 🇧🇴          |
| descripcion    | TextField         | Descripción libre (opcional)     |
| fecha_registro | DateTimeField     | Auto al crear                    |

### `ValorRepresentativo`
| Campo       | Tipo              | Descripción                        |
|-------------|-------------------|------------------------------------|
| pais        | FK → Pais         | País al que pertenece              |
| categoria   | CharField choices | gastronomia / monumento / tradicion / personaje / naturaleza / deporte / musica / otro |
| titulo      | CharField(150)    | Nombre del valor                   |
| descripcion | TextField         | Descripción detallada              |
| icono       | CharField(10)     | Emoji representativo (opcional)    |

---

## Vistas disponibles

| URL                          | Vista            | Descripción                  |
|------------------------------|------------------|------------------------------|
| `/paises/`                   | lista_paises     | Home con todos los países    |
| `/paises/nuevo/`             | crear_pais       | Formulario nuevo país        |
| `/paises/<id>/`              | detalle_pais     | Detalle + agregar valores    |
| `/paises/<id>/editar/`       | editar_pais      | Editar país                  |
| `/paises/<id>/eliminar/`     | eliminar_pais    | Confirmar y eliminar         |
| `/paises/valor/<id>/eliminar/` | eliminar_valor | Eliminar un valor            |
