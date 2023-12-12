from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

import logging

from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from compraAhorra.models.modelo import Login

def loginUsuario(request):
        nombreUsuario = request.POST.get("nombreUsuario")
        password = request.POST.get("password")

        # Buscar el usuario en la base de datos
        try:
            usuario = Login.objects.get(nombreUsuario=nombreUsuario)
            # Verificar la contraseña
            if check_password(password, usuario.password):
                # Contraseña válida, iniciar sesión o redirigir a la página deseada
                # Por ejemplo:
                return render(request, 'index.html')
            else:
                # Contraseña inválida
                logging.error('Contraseña incorrecta para el usuario: %s', nombreUsuario)
                return render(request, 'login.html', {'error': 'Contraseña incorrecta'})
        except Login.DoesNotExist:
            # Usuario no encontrado
            logging.error('Usuario no encontrado: %s', nombreUsuario)
            return render(request, 'login.html', {'error': 'Usuario no encontrado'})



