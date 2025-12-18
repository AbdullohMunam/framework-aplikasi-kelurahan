from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

# Imports untuk API
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets 
# PERBAIKAN 1: Tambahkan AllowAny di import sini
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

# --- VIEW UNTUK TEMPLATE DJANGO LAMA (Boleh dibiarkan) ---

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')
    
# --- VIEW UNTUK API (YANG DIGUNAKAN FRONTEND JS) ---

class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows warga to be viewed or edited.
    """
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    
    # PERBAIKAN 2: Gunakan AllowAny (Huruf Besar)
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']


class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pengaduan to be viewed or edited.
    """
    queryset = Pengaduan.objects.all().order_by('-id')
    serializer_class = PengaduanSerializer
    
    # PERBAIKAN 3: Ubah IsAdminUser menjadi AllowAny agar frontend bisa akses tanpa login
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi', 'status']
    ordering_fields = ['status', 'tanggal_lapor']