from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from models import *
from django.contrib.auth.form import UserCreatiom,AuthentificationForm
from django.contrib.auth import login,Authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import UserCreatiom
def inicio (request):
	return render_to_response('index.html',{},RecuestContex(request))
	def nuevoUsuario(request):
		if request.method=='POST':
			formulario=UserCreatiomForm(request.POST)
			if formulario.is_valid:
				formulario.save()
				return HttpResponseRedirect('/inicio')
		else:
		    formulario=UserCreatiomForm()
		    return render_to_response('regisusuario.html',{'formulario':formulario},context_instance=RecuestContex(request))
#pagina de ingreso al sistema
def ingresar(request):
    if request.method=='POST':
    	formulario=AuthentificationForm(request.POST)
    	if formulario.is_valid:
    		usuario=request.POST['username']
    		clave=recuest.POST['password']
    		acceso=Authenticate(username=usuario,password=clave)
    		if acceso is not None:
    			if acceso.is_active:
    			   login(request,acceso)
    			   return HttpResponseRedirect('/inicio')
    	        else:
    	    	   return render_to_response('noactivo.hatml', context_instance=RecuestContex(request))
    	    else:
    	        return render_to_response('noactivo.hatml', context_instance=RecuestContex(request))  
    else:
		formulario=AuthenticationForm()
	return render_to_response('ingresar.html',{'formulario':formulario},context_instance=RequestContext(request))

#pagina de inicio del sistema
def inicio1 (request):
	return render_to_response('index1.html',{},RequestContext(request))  	





# Create your views here.
