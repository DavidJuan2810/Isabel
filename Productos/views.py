from django.shortcuts import render,redirect
from .models import Vestido
from .forms import VestidoForm

# Create your views here.

def ListarVestido(request):
    vestidos= Vestido.objects.all()
    return render(request,'ListarVestido.html', {'vestidos':vestidos})

def registrarVestido(request):
    if request.method == 'POST':
        form=VestidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListarVestido')
    
    else:
        form= VestidoForm()
        return render(request,'registrarVestido.html',{'form':form})