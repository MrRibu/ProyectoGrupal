from django.db import models


class Pais(models.Model):
    CONTINENTES = [
        ('AF', 'África'),
        ('AN', 'Antártida'),
        ('AS', 'Asia'),
        ('EU', 'Europa'),
        ('NA', 'América del Norte'),
        ('OC', 'Oceanía'),
        ('SA', 'América del Sur'),
    ]

    nombre        = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    codigo_iso    = models.CharField(max_length=3, unique=True, verbose_name='Código ISO')
    continente    = models.CharField(max_length=2, choices=CONTINENTES, verbose_name='Continente')
    capital       = models.CharField(max_length=100, verbose_name='Capital')
    poblacion     = models.PositiveBigIntegerField(verbose_name='Población')
    idioma        = models.CharField(max_length=100, verbose_name='Idioma oficial')
    moneda        = models.CharField(max_length=100, verbose_name='Moneda')
    bandera_emoji = models.CharField(max_length=10, blank=True, verbose_name='Emoji bandera')
    descripcion   = models.TextField(blank=True, verbose_name='Descripción')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.bandera_emoji} {self.nombre}"

    def get_continente_display_custom(self):
        return dict(self.CONTINENTES).get(self.continente, '')

    @property
    def poblacion_formato(self):
        p = self.poblacion
        if p >= 1_000_000_000:
            return f"{p / 1_000_000_000:.1f}B"
        if p >= 1_000_000:
            return f"{p / 1_000_000:.1f}M"
        if p >= 1_000:
            return f"{p / 1_000:.1f}K"
        return str(p)


class ValorRepresentativo(models.Model):
    CATEGORIAS = [
        ('gastronomia',  'Gastronomía'),
        ('monumento',    'Monumento'),
        ('tradicion',    'Tradición'),
        ('personaje',    'Personaje histórico'),
        ('naturaleza',   'Naturaleza'),
        ('deporte',      'Deporte'),
        ('musica',       'Música'),
        ('otro',         'Otro'),
    ]

    pais       = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='valores')
    categoria  = models.CharField(max_length=20, choices=CATEGORIAS, verbose_name='Categoría')
    titulo     = models.CharField(max_length=150, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    icono      = models.CharField(max_length=10, blank=True, verbose_name='Emoji icono')

    class Meta:
        verbose_name = 'Valor representativo'
        verbose_name_plural = 'Valores representativos'

    def __str__(self):
        return f"{self.pais.nombre} — {self.titulo}"
