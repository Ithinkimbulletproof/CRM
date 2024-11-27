from django.shortcuts import render


def documents_view(request):
    return render(request, "documents/documents.html")
