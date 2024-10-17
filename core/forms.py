from django import forms
from .models import Residente, Habitacion, Medicamento, MedicamentoResidente, Visita

class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ['nombre', 'fecha_nacimiento', 'numero_identificacion', 'contacto_emergencia', 'telefono_emergencia', 'habitacion']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero', 'tipo']

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'dosis', 'frecuencia']

class MedicamentoResidenteForm(forms.ModelForm):
    class Meta:
        model = MedicamentoResidente
        fields = ['medicamento', 'instrucciones']

class VisitaEntradaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['visitante_nombre', 'visitante_identificacion', 'residente']

class VisitaSalidaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['fecha_salida']
        widgets = {
            'fecha_salida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }