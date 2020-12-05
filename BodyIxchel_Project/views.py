from django.shortcuts import render
from django.http import HttpResponseRedirect

def getInfoPage(request):
    return render(request, 'info_page.html')