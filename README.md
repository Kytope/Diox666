# DIOXX 666 - Sistema de Gestión para Hogar de Reposo 🏥

![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.0-purple.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Sistema de gestión integral diseñado específicamente para hogares de reposo y residencias de adultos mayores. Permite administrar residentes, medicamentos, habitaciones y registro de visitas de manera eficiente y segura.

## 🌟 Características

- **Gestión de Residentes**
  - Registro completo de información personal
  - Asignación de habitaciones
  - Control de medicamentos
  - Historial médico

- **Control de Medicamentos**
  - Registro de medicamentos
  - Asignación a residentes
  - Control de dosis y frecuencias
  - Instrucciones específicas por residente

- **Administración de Habitaciones**
  - Control de habitaciones individuales y dobles
  - Estado de ocupación
  - Asignación a residentes

- **Registro de Visitas**
  - Control de entrada y salida
  - Registro de visitantes
  - Duración de visitas
  - Historial de visitas por residente

## 🛠️ Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/dioxx666.git
cd dioxx666
```
2. Instalar las dependencias:
```bash
pip install django
pip install django-bootstrap4
```
3. Realizar las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```
4. Crear un superusuario:
```bash
python manage.py createsuperuser
```
5. Iniciar el servidor:
```bash
python manage.py runserver
```

