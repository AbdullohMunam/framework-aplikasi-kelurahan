from django.urls import path
from .views import WargaListView, WargaDetailView, PengaduanListView

urlpatterns = [
    path("", WargaListView.as_view(), name='warga.list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan.list'),
]