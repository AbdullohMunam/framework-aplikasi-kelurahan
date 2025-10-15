from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import WargaForm, PengaduanForm
from .models import Warga, Pengaduan

@login_required
def warga_detail(request, warga_id):
    warga = get_object_or_404(Warga, id=warga_id)
    return render(request, 'warga/detail.html', {'warga': warga})

@login_required
def warga_update(request, warga_id):
    warga = get_object_or_404(Warga, id=warga_id)
    form = WargaForm(request.POST, instance=warga)
    if form.is_valid():
        form.save()
        messages.success(request, 'Warga berhasil diperbarui.')
    return redirect('warga-detail', warga_id=warga_id)

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

@login_required
def pengaduan_list(request):
    pengaduan = Pengaduan.objects.all()
    return render(request, 'warga/pengaduan_list.html', {'pengaduan': pengaduan})

@login_required
def pengaduan_detail(request, pengaduan_id):
    pengaduan = get_object_or_404(Pengaduan, id=pengaduan_id)
    return render(request, 'warga/pengaduan_detail.html', {'pengaduan': pengaduan})

@login_required
def pengaduan_update(request, pengaduan_id):
    pengaduan = get_object_or_404(Pengaduan, id=pengaduan_id)
    form = PengaduanForm(request.POST, instance=pengaduan)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pengaduan berhasil diperbarui.')
    return redirect('pengaduan-detail', pengaduan_id=pengaduan_id)

@login_required
def pengaduan_delete(request, pengaduan_id):
    pengaduan = get_object_or_404(Pengaduan, id=pengaduan_id)
    if request.method == 'POST':
        pengaduan.delete()
        messages.success(request, 'Pengaduan berhasil dihapus.')
    return redirect('pengaduan-list')