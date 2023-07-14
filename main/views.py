from django.shortcuts import render
from .models import Anonce


def index(request):
    anonces = Anonce.objects.all()
    content = {
        'anonces': anonces,
    }

    return render(request, 'main/index.html', content)
