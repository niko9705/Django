
from django.http import HttpResponse

def home(request):
       return HttpResponse("<h1>Bienvenidos a mi sitio de prueba</h1>")
# Create your views here.
