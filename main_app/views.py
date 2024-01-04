from django.shortcuts import render

from .models import DataModels


def data_list(request):
    data = DataModels.objects.all()
    return render(request, 'main_app/index.html', {'data': data})
