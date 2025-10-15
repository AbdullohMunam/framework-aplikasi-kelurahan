# warga/forms.py
from django import forms
from .models import Warga

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        # Tentukan field mana saja dari model yang ingin ditampilkan di form
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
