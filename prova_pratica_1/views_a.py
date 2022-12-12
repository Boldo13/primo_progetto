from django.shortcuts import render

def materie(request):
    context={
      materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    }
    return render (request,context)
    
