from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('codigo_iso', models.CharField(max_length=3, unique=True, verbose_name='Código ISO')),
                ('continente', models.CharField(choices=[('AF', 'África'), ('AN', 'Antártida'), ('AS', 'Asia'), ('EU', 'Europa'), ('NA', 'América del Norte'), ('OC', 'Oceanía'), ('SA', 'América del Sur')], max_length=2, verbose_name='Continente')),
                ('capital', models.CharField(max_length=100, verbose_name='Capital')),
                ('poblacion', models.PositiveBigIntegerField(verbose_name='Población')),
                ('idioma', models.CharField(max_length=100, verbose_name='Idioma oficial')),
                ('moneda', models.CharField(max_length=100, verbose_name='Moneda')),
                ('bandera_emoji', models.CharField(blank=True, max_length=10, verbose_name='Emoji bandera')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={'verbose_name': 'País', 'verbose_name_plural': 'Países', 'ordering': ['nombre']},
        ),
        migrations.CreateModel(
            name='ValorRepresentativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('gastronomia', 'Gastronomía'), ('monumento', 'Monumento'), ('tradicion', 'Tradición'), ('personaje', 'Personaje histórico'), ('naturaleza', 'Naturaleza'), ('deporte', 'Deporte'), ('musica', 'Música'), ('otro', 'Otro')], max_length=20, verbose_name='Categoría')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('icono', models.CharField(blank=True, max_length=10, verbose_name='Emoji icono')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valores', to='paises_app.pais')),
            ],
            options={'verbose_name': 'Valor representativo', 'verbose_name_plural': 'Valores representativos'},
        ),
    ]
