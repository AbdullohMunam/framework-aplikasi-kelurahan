# warga/serializers.py
from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        # Tentukan field dari model Warga yang ingin kita ekspos di API
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        # Gunakan semua field agar sesuai model; ganti dengan daftar field jika perlu
        fields = '__all__'
