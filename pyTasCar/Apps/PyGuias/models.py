from django.db import models

# Create your models here.

class Usuario(models.Model):
    Usuario =models.CharField(max_length=30)
    Password =models.CharField(max_length=30)
    PERMISOS=(('T', 'Control Total'), ('L', 'Solo Lectura'))
    Permiso=models.CharField(max_length=1, choices=PERMISOS, default='L' )

    def UsuarioComppleto(self):
        cadena= "{0} ({1})"
        return cadena.format(self.Usuario,self.Permiso)

    def __str__(self):
        cadena= "{0} ({1})"
        return cadena.format(self.Usuario,self.Permiso)

