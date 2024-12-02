from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def documents_view(request):
    return render(request, "documents/documents.html")
