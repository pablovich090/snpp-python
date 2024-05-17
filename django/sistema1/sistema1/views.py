from django.http import HttpResponse
import os

def saludo(request):#primera vista
    return HttpResponse("hola mundo")
def getGoogle(request):
    return os.system("start brave")



