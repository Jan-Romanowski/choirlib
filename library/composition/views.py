from django.shortcuts import render

def index(request):
    return render(request, 'composition/compositionList.html')

def editComposition(request):
    return render(request, 'composition/compositionForm.html')

def  detailsComposition(request):
    return render(request, 'composition/compositionDetails.html')


