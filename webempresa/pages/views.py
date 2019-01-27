from django.shortcuts import render, get_object_or_404
from .models import Pages

def page(request, page_id):
    page=get_object_or_404(Pages, pk=page_id)
    return render(request, 'pages/sample.html', {'page':page})
# Create your views here.
