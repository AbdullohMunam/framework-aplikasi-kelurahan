# File ini tidak diperlukan. Silakan gunakan warga/forms.py sesuai konvensi Django.

from django.urls import path
from .views import (
    PengaduanCreateView,
    PengaduanDetailView,
    PengaduanUpdateView,
    PengaduanDeleteView,
)

app_name = 'warga'

urlpatterns = [
    path('pengaduan/<int:pk>/', PengaduanDetailView.as_view(), name='pengaduan-detail'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
]