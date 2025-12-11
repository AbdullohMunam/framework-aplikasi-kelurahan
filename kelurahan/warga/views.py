from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets # Impor viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

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
    
class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows warga to be viewed or edited.
    """
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']


class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pengaduan to be viewed or edited.
    """
    queryset = Pengaduan.objects.all().order_by('-id')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]

    # Add filtering, searching and ordering for Pengaduan
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi', 'status']
    ordering_fields = ['status', 'tanggal_lapor']
