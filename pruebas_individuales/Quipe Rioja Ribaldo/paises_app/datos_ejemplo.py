"""
Script de datos de ejemplo — ejecutar con:
    python manage.py shell < paises_app/datos_ejemplo.py
"""
from paises_app.models import Pais, ValorRepresentativo

# Limpiar datos previos (opcional)
# Pais.objects.all().delete()

datos = [
    {
        "nombre": "Bolivia",
        "codigo_iso": "BOL",
        "continente": "SA",
        "capital": "Sucre",
        "poblacion": 12_000_000,
        "idioma": "Español",
        "moneda": "Boliviano (BOB)",
        "bandera_emoji": "🇧🇴",
        "descripcion": "País plurinacional en el corazón de Sudamérica, conocido por su diversidad cultural y natural.",
        "valores": [
            ("naturaleza",  "Salar de Uyuni",    "El salar más grande del mundo, con más de 10.000 km².", ""),
            ("tradicion",   "Carnaval de Oruro",  "Patrimonio cultural inmaterial de la Humanidad por la UNESCO.", ""),
            ("gastronomia", "Salteñas",           "Empanadas jugosas típicas de Bolivia, consumidas como desayuno.", ""),
            ("monumento",   "Tiwanaku",           "Ciudad precolombina y centro espiritual de la cultura Tiwanaku.", ""),
        ],
    },
    {
        "nombre": "Japón",
        "codigo_iso": "JPN",
        "continente": "AS",
        "capital": "Tokio",
        "poblacion": 125_000_000,
        "idioma": "Japonés",
        "moneda": "Yen (JPY)",
        "bandera_emoji": "🇯🇵",
        "descripcion": "Nación insular de Asia Oriental famosa por su mezcla única de tradición y modernidad.",
        "valores": [
            ("tradicion",   "Ceremonia del té",   "El Chanoyu es una práctica espiritual y estética milenaria.", ""),
            ("naturaleza",  "Monte Fuji",         "Volcán sagrado símbolo de Japón con 3.776 metros de altitud.", ""),
            ("gastronomia", "Sushi",              "Preparación de arroz avinagrado con pescado crudo o cocido.", ""),
            ("deporte",     "Sumo",               "Arte marcial y deporte nacional con más de 2.000 años de historia.", ""),
        ],
    },
    {
        "nombre": "Italia",
        "codigo_iso": "ITA",
        "continente": "EU",
        "capital": "Roma",
        "poblacion": 60_000_000,
        "idioma": "Italiano",
        "moneda": "Euro (EUR)",
        "bandera_emoji": "🇮🇹",
        "descripcion": "Cuna del Renacimiento, hogar de una gastronomía y arte incomparables.",
        "valores": [
            ("monumento",   "Coliseo Romano",     "Anfiteatro del siglo I d.C., símbolo del Imperio Romano.", ""),
            ("gastronomia", "Pizza Napolitana",   "Patrimonio cultural inmaterial de la UNESCO desde 2017.", ""),
            ("musica",      "Ópera",              "Forma musical nacida en Italia en el siglo XVI, de influencia mundial.", ""),
            ("personaje",   "Leonardo da Vinci",  "Polímata del Renacimiento: pintor, escultor, científico e inventor.", ""),
        ],
    },
]

for d in datos:
    pais, creado = Pais.objects.get_or_create(
        codigo_iso=d["codigo_iso"],
        defaults={k: v for k, v in d.items() if k != "valores"}
    )
    if creado:
        print(f"Creado: {pais}")
        for cat, titulo, desc, icono in d["valores"]:
            ValorRepresentativo.objects.create(
                pais=pais, categoria=cat, titulo=titulo, descripcion=desc, icono=icono
            )
    else:
        print(f"Ya existe: {pais.nombre}")

print("\nDatos de ejemplo cargados.")
