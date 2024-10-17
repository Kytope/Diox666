from django.db import models
from django.utils import timezone

class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=20, choices=[('individual', 'Individual'), ('doble', 'Doble')])

    def __str__(self):
        return f"Habitación {self.numero} ({self.get_tipo_display()})"

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    dosis = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.dosis}"

class Residente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero_identificacion = models.CharField(max_length=20, unique=True)
    contacto_emergencia = models.CharField(max_length=100)
    telefono_emergencia = models.CharField(max_length=20)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.SET_NULL, null=True, blank=True)
    medicamentos = models.ManyToManyField(Medicamento, through='MedicamentoResidente')

    def __str__(self):
        return self.nombre

class MedicamentoResidente(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    instrucciones = models.TextField()

    def __str__(self):
        return f"{self.residente.nombre} - {self.medicamento.nombre}"
    
class Visita(models.Model):
    visitante_nombre = models.CharField(max_length=100)
    visitante_identificacion = models.CharField(max_length=20)
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE, related_name='visitas')
    fecha_entrada = models.DateTimeField(default=timezone.now)
    fecha_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.visitante_nombre} visitando a {self.residente.nombre}"

    def duracion(self):
        if self.fecha_salida:
            return self.fecha_salida - self.fecha_entrada
        return None