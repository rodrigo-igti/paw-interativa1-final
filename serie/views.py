from django.http import HttpResponseNotAllowed
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms
from . import models


def cadastro(request):
    form = forms.SerieForm()
    if request.method == 'POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            print("Saving")
            form.save(commit=True)
        else:
            print("ERROR")
    series_list = models.Serie.objects.order_by('nome')
    form = forms.SerieForm()
    data_dict = {"serie_records": series_list, 'form': form}

    return render(request, 'serie/serie.html', data_dict)


def delete(request, id):
    try:
        models.Serie.objects.filter(id=id).delete()
        form = forms.SerieForm()
        series_list = models.Serie.objects.order_by('nome')
        data_dict = {"serie_records": series_list, 'form': form}
        return render(request, 'serie/serie.html', data_dict)
    except:
        return HttpResponseNotAllowed();


def update(request, id):
    item = models.Serie.objects.get(id=id);
    if request.method == "GET":
        form = forms.SerieForm(initial={'nome': item.nome, 'idGenero': item.idGenero})
        data_dict = {'form': form}
        return render(request, 'serie/serie_upd.html', data_dict)
    else:
        form = forms.SerieForm(request.POST)
        item.nome = form.data['nome']
        item.idGenero_id = form.data['idGenero']
        item.save()
        form = forms.SerieForm()
        series_list = models.Serie.objects.order_by('nome')
        data_dict = {"serie_records": series_list, 'form': form}
        return render(request, 'serie/serie.html', data_dict)

