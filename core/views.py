from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .models import Residente, Habitacion, Medicamento, MedicamentoResidente, Visita
from .forms import ResidenteForm, HabitacionForm, MedicamentoForm, MedicamentoResidenteForm, VisitaEntradaForm, VisitaSalidaForm

class ResidenteListView(ListView):
    model = Residente
    template_name = 'core/residente_list.html'
    context_object_name = 'residentes'
    paginate_by = 10  # Añadimos paginación para manejar grandes cantidades de residentes

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(numero_identificacion__icontains=query) |
                Q(habitacion__numero__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class ResidenteDetailView(DetailView):
    model = Residente
    template_name = 'core/residente_detail.html'

class ResidenteCreateView(CreateView):
    model = Residente
    form_class = ResidenteForm
    template_name = 'core/residente_form.html'
    success_url = reverse_lazy('residente_list')
    def form_valid(self, form):
        messages.success(self.request, 'Residente creado con éxito.')
        return super().form_valid(form)    

class ResidenteUpdateView(UpdateView):
    model = Residente
    form_class = ResidenteForm
    template_name = 'core/residente_form.html'
    success_url = reverse_lazy('residente_list')
    def form_valid(self, form):
        messages.success(self.request, 'Residente actualizado con éxito.')
        return super().form_valid(form)    

class ResidenteDeleteView(DeleteView):
    model = Residente
    template_name = 'core/residente_confirm_delete.html'
    success_url = reverse_lazy('residente_list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Residente eliminado con éxito.')
        return super().delete(request, *args, **kwargs)

class HabitacionListView(ListView):
    model = Habitacion
    template_name = 'core/habitacion_list.html'
    context_object_name = 'habitaciones'

class HabitacionCreateView(CreateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'core/habitacion_form.html'
    success_url = reverse_lazy('habitacion_list')

    def form_valid(self, form):
        messages.success(self.request, 'Habitación creada con éxito.')
        return super().form_valid(form)

class MedicamentoListView(ListView):
    model = Medicamento
    template_name = 'core/medicamento_list.html'
    context_object_name = 'medicamentos'

class MedicamentoCreateView(CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core/medicamento_form.html'
    success_url = reverse_lazy('medicamento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Medicamento creado con éxito.')
        return super().form_valid(form)

def asignar_medicamento(request, pk):
    residente = get_object_or_404(Residente, pk=pk)
    if request.method == 'POST':
        form = MedicamentoResidenteForm(request.POST)
        if form.is_valid():
            medicamento_residente = form.save(commit=False)
            medicamento_residente.residente = residente
            medicamento_residente.save()
            messages.success(request, 'Medicamento asignado con éxito.')
            return redirect('residente_detail', pk=residente.pk)
    else:
        form = MedicamentoResidenteForm()
    return render(request, 'core/asignar_medicamento.html', {'form': form, 'residente': residente})

class MedicamentoResidenteUpdateView(UpdateView):
    model = MedicamentoResidente
    form_class = MedicamentoResidenteForm
    template_name = 'core/medicamento_residente_form.html'

    def get_success_url(self):
        return reverse('residente_detail', kwargs={'pk': self.object.residente.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Medicamento actualizado con éxito.')
        return super().form_valid(form)

class MedicamentoResidenteDeleteView(DeleteView):
    model = MedicamentoResidente
    template_name = 'core/medicamento_residente_confirm_delete.html'

    def get_success_url(self):
        return reverse('residente_detail', kwargs={'pk': self.object.residente.pk})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Medicamento eliminado con éxito.')
        return super().delete(request, *args, **kwargs)
    
class VisitaListView(ListView):
    model = Visita
    template_name = 'core/visita_list.html'
    context_object_name = 'visitas'
    ordering = ['-fecha_entrada']

class VisitaCreateView(CreateView):
    model = Visita
    form_class = VisitaEntradaForm
    template_name = 'core/visita_form.html'
    success_url = reverse_lazy('visita_list')

    def form_valid(self, form):
        messages.success(self.request, 'Visita registrada con éxito.')
        return super().form_valid(form)

class VisitaUpdateView(UpdateView):
    model = Visita
    form_class = VisitaSalidaForm
    template_name = 'core/visita_salida_form.html'
    success_url = reverse_lazy('visita_list')

    def form_valid(self, form):
        messages.success(self.request, 'Salida de visita registrada con éxito.')
        return super().form_valid(form)

class VisitaDeleteView(DeleteView):
    model = Visita
    template_name = 'core/visita_confirm_delete.html'
    success_url = reverse_lazy('visita_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Visita eliminada con éxito.')
        return super().delete(request, *args, **kwargs)

def registrar_salida(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    if not visita.fecha_salida:
        visita.fecha_salida = timezone.now()
        visita.save()
        messages.success(request, 'Salida registrada con éxito.')
    else:
        messages.warning(request, 'La salida ya había sido registrada.')
    return redirect('visita_list')