import os
import django
import random
from datetime import datetime, timedelta

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dioxx_666.settings')
django.setup()

from core.models import Habitacion, Medicamento, Residente, MedicamentoResidente

def create_habitaciones(n=10):
    for i in range(1, n+1):
        Habitacion.objects.create(
            numero=f"{i:03d}",
            tipo=random.choice(['individual', 'doble'])
        )
    print(f"{n} habitaciones creadas.")

def create_medicamentos(n=20):
    nombres = ["Paracetamol", "Ibuprofeno", "Omeprazol", "Amoxicilina", "Lorazepam", "Metformina", "Atorvastatina"]
    for _ in range(n):
        Medicamento.objects.create(
            nombre=random.choice(nombres),
            dosis=f"{random.choice([100, 200, 250, 500, 1000])}mg",
            frecuencia=random.choice(["Cada 4 horas", "Cada 6 horas", "Cada 8 horas", "Cada 12 horas", "Una vez al día"])
        )
    print(f"{n} medicamentos creados.")

def create_residentes(n=50):
    habitaciones = list(Habitacion.objects.all())
    for i in range(n):
        fecha_nacimiento = datetime.now() - timedelta(days=random.randint(20000, 36500))
        Residente.objects.create(
            nombre=f"Residente {i+1}",
            fecha_nacimiento=fecha_nacimiento,
            numero_identificacion=f"{random.randint(10000000, 99999999)}",
            contacto_emergencia=f"Contacto {i+1}",
            telefono_emergencia=f"{random.randint(600000000, 699999999)}",
            habitacion=random.choice(habitaciones)
        )
    print(f"{n} residentes creados.")

def asignar_medicamentos():
    residentes = Residente.objects.all()
    medicamentos = list(Medicamento.objects.all())
    for residente in residentes:
        for _ in range(random.randint(1, 5)):
            MedicamentoResidente.objects.create(
                residente=residente,
                medicamento=random.choice(medicamentos),
                instrucciones="Tomar según las indicaciones del médico."
            )
    print("Medicamentos asignados a residentes.")

if __name__ == '__main__':
    create_habitaciones()
    create_medicamentos()
    create_residentes()
    asignar_medicamentos()
    print("Población de la base de datos completada.")