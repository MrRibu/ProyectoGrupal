"""
Comando para cargar datos de ejemplo.
Uso: python manage.py cargar_datos
"""
import sys
import io
from django.core.management.base import BaseCommand
from paises_app.models import Pais, ValorRepresentativo


# Forzar UTF-8 en stdout (necesario en Windows)
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


DATOS = [
    {
        "nombre": "Bolivia",
        "codigo_iso": "BOL",
        "continente": "SA",
        "capital": "Sucre",
        "poblacion": 12_000_000,
        "idioma": "Español",
        "moneda": "Boliviano (BOB)",
        "bandera_emoji": "\U0001f1e7\U0001f1f4",
        "descripcion": "Pais plurinacional en el corazon de Sudamerica, conocido por su diversidad cultural y natural.",
        "valores": [
            ("naturaleza",  "Salar de Uyuni",    "El salar mas grande del mundo, con mas de 10.000 km2."),
            ("tradicion",   "Carnaval de Oruro",  "Patrimonio cultural inmaterial de la Humanidad por la UNESCO."),
            ("gastronomia", "Saltenas",           "Empanadas jugosas tipicas de Bolivia, consumidas como desayuno."),
            ("monumento",   "Tiwanaku",           "Ciudad precolombina y centro espiritual de la cultura Tiwanaku."),
        ],
    },
    {
        "nombre": "Japon",
        "codigo_iso": "JPN",
        "continente": "AS",
        "capital": "Tokio",
        "poblacion": 125_000_000,
        "idioma": "Japones",
        "moneda": "Yen (JPY)",
        "bandera_emoji": "\U0001f1ef\U0001f1f5",
        "descripcion": "Nacion insular de Asia Oriental famosa por su mezcla unica de tradicion y modernidad.",
        "valores": [
            ("tradicion",   "Ceremonia del te",   "El Chanoyu es una practica espiritual y estetica milenaria."),
            ("naturaleza",  "Monte Fuji",         "Volcan sagrado simbolo de Japon con 3.776 metros de altitud."),
            ("gastronomia", "Sushi",              "Preparacion de arroz avinagrado con pescado crudo o cocido."),
            ("deporte",     "Sumo",               "Arte marcial y deporte nacional con mas de 2.000 anos de historia."),
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
        "bandera_emoji": "\U0001f1ee\U0001f1f9",
        "descripcion": "Cuna del Renacimiento, hogar de una gastronomia y arte incomparables.",
        "valores": [
            ("monumento",   "Coliseo Romano",     "Anfiteatro del siglo I d.C., simbolo del Imperio Romano."),
            ("gastronomia", "Pizza Napolitana",   "Patrimonio cultural inmaterial de la UNESCO desde 2017."),
            ("musica",      "Opera",              "Forma musical nacida en Italia en el siglo XVI, de influencia mundial."),
            ("personaje",   "Leonardo da Vinci",  "Polimata del Renacimiento: pintor, escultor, cientifico e inventor."),
        ],
    },
]


class Command(BaseCommand):
    help = 'Carga datos de ejemplo: Bolivia, Japon e Italia con sus valores representativos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limpiar',
            action='store_true',
            help='Elimina todos los paises antes de cargar los datos',
        )

    def handle(self, *args, **options):
        if options['limpiar']:
            count = Pais.objects.count()
            Pais.objects.all().delete()
            self.stdout.write(self.style.WARNING(f'Se eliminaron {count} paises existentes.'))

        creados = 0
        omitidos = 0

        for d in DATOS:
            valores = d.pop("valores")
            pais, nuevo = Pais.objects.get_or_create(
                codigo_iso=d["codigo_iso"],
                defaults=d,
            )
            if nuevo:
                for cat, titulo, desc in valores:
                    ValorRepresentativo.objects.create(
                        pais=pais,
                        categoria=cat,
                        titulo=titulo,
                        descripcion=desc,
                        icono="",
                    )
                self.stdout.write(self.style.SUCCESS(
                    f'[OK] {pais.nombre} creado con {len(valores)} valores'
                ))
                creados += 1
            else:
                self.stdout.write(self.style.WARNING(
                    f'[--] {pais.nombre} ya existe, se omitio'
                ))
                omitidos += 1

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'Listo: {creados} paises creados, {omitidos} omitidos.'
        ))
        if omitidos:
            self.stdout.write('      Usa --limpiar para reiniciar los datos.')
