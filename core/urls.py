from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResidenteListView.as_view(), name='residente_list'),
    path('residente/<int:pk>/', views.ResidenteDetailView.as_view(), name='residente_detail'),
    path('residente/new/', views.ResidenteCreateView.as_view(), name='residente_new'),
    path('residente/<int:pk>/edit/', views.ResidenteUpdateView.as_view(), name='residente_edit'),
    path('residente/<int:pk>/delete/', views.ResidenteDeleteView.as_view(), name='residente_delete'),
    path('habitaciones/', views.HabitacionListView.as_view(), name='habitacion_list'),
    path('habitacion/new/', views.HabitacionCreateView.as_view(), name='habitacion_new'),
    path('medicamentos/', views.MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamento/new/', views.MedicamentoCreateView.as_view(), name='medicamento_new'),
    path('residente/<int:pk>/asignar-medicamento/', views.asignar_medicamento, name='asignar_medicamento'),
    path('residente/medicamento/<int:pk>/edit/', views.MedicamentoResidenteUpdateView.as_view(), name='medicamento_residente_edit'),
    path('residente/medicamento/<int:pk>/delete/', views.MedicamentoResidenteDeleteView.as_view(), name='medicamento_residente_delete'),
    path('visitas/', views.VisitaListView.as_view(), name='visita_list'),
    path('visitas/nueva/', views.VisitaCreateView.as_view(), name='visita_create'),
    path('visitas/<int:pk>/salida/', views.VisitaUpdateView.as_view(), name='visita_update'),
    path('visitas/<int:pk>/eliminar/', views.VisitaDeleteView.as_view(), name='visita_delete'),
    path('visitas/<int:pk>/registrar-salida/', views.registrar_salida, name='registrar_salida'),
]