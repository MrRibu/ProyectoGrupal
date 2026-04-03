from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, Count
from .models import Pais, ValorRepresentativo
from .forms import PaisForm, ValorRepresentativoForm


# ── Lista / Home ──────────────────────────────────────────────────────────────
def lista_paises(request):
    q          = request.GET.get('q', '').strip()
    continente = request.GET.get('continente', '')

    paises = Pais.objects.annotate(num_valores=Count('valores'))

    if q:
        paises = paises.filter(
            Q(nombre__icontains=q) |
            Q(capital__icontains=q) |
            Q(idioma__icontains=q)
        )
    if continente:
        paises = paises.filter(continente=continente)

    continentes = Pais.CONTINENTES
    total       = Pais.objects.count()

    return render(request, 'paises/lista.html', {
        'paises':     paises,
        'continentes': continentes,
        'q':          q,
        'continente_sel': continente,
        'total':      total,
    })


# ── Detalle ───────────────────────────────────────────────────────────────────
def detalle_pais(request, pk):
    pais   = get_object_or_404(Pais, pk=pk)
    valores = pais.valores.all().order_by('categoria')

    if request.method == 'POST':
        form = ValorRepresentativoForm(request.POST)
        if form.is_valid():
            v = form.save(commit=False)
            v.pais = pais
            v.save()
            messages.success(request, f'Valor "{v.titulo}" agregado correctamente.')
            return redirect('detalle_pais', pk=pk)
    else:
        form = ValorRepresentativoForm()

    return render(request, 'paises/detalle.html', {
        'pais':   pais,
        'valores': valores,
        'form':   form,
    })


# ── Crear país ────────────────────────────────────────────────────────────────
def crear_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            pais = form.save()
            messages.success(request, f'País "{pais.nombre}" registrado exitosamente.')
            return redirect('detalle_pais', pk=pais.pk)
    else:
        form = PaisForm()

    return render(request, 'paises/form_pais.html', {'form': form, 'accion': 'Registrar'})


# ── Editar país ───────────────────────────────────────────────────────────────
def editar_pais(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        if form.is_valid():
            form.save()
            messages.success(request, f'País "{pais.nombre}" actualizado.')
            return redirect('detalle_pais', pk=pk)
    else:
        form = PaisForm(instance=pais)

    return render(request, 'paises/form_pais.html', {'form': form, 'accion': 'Editar', 'pais': pais})


# ── Eliminar país ─────────────────────────────────────────────────────────────
def eliminar_pais(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        nombre = pais.nombre
        pais.delete()
        messages.success(request, f'País "{nombre}" eliminado.')
        return redirect('lista_paises')
    return render(request, 'paises/confirmar_eliminar.html', {'pais': pais})


# ── Eliminar valor ────────────────────────────────────────────────────────────
def eliminar_valor(request, pk):
    valor = get_object_or_404(ValorRepresentativo, pk=pk)
    pais_pk = valor.pais.pk
    if request.method == 'POST':
        valor.delete()
        messages.success(request, 'Valor eliminado.')
    return redirect('detalle_pais', pk=pais_pk)
