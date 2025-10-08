from django.contrib import admin
from .models import Warga, Pengaduan


@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
	list_display = ('nik', 'nama_lengkap', 'no_telepon', 'tanggal_registrasi')
	search_fields = ('nik', 'nama_lengkap')


@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
	list_display = ('judul', 'pelapor', 'status', 'tanggal_lapor')
	list_filter = ('status', 'tanggal_lapor')
	search_fields = ('judul', 'deskripsi', 'pelapor__nama_lengkap')

