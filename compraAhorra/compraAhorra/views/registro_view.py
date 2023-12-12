from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from compraAhorra.models.modelo import Usuario
from compraAhorra.models.modelo import Login


def registro(request):
    if request.method == "POST":
        nombreUsuario = request.POST.get("nombreUsuario")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        password = request.POST.get("password")

        # Encriptar la contraseña
        hashed_password = make_password(password)

        nuevoUsuario = Usuario(nombreUsuario=nombreUsuario, nombre=nombre, apellido=apellido, password=hashed_password)
        nuevoUsuario.save()

                # Guardar el usuario en el modelo Login
        nuevoLogin = Login(nombreUsuario=nombreUsuario, password=hashed_password)
        nuevoLogin.save()
        
        return render(request, 'index.html') 
    else:
        return render(request, 'registro.html')
