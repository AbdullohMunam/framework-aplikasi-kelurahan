# Framework Aplikasi Kelurahan (Django)


## Cara Menjalankan (prioritas)

Prasyarat:
- Python 3.10+ (direkomendasikan)
- pip, venv
- requirements.txt ada di root proyek (mengandung: Django, djangorestframework, asgiref, sqlparse)

Langkah cepat (development):


Linux (bash/wsl)
1. Buat dan aktifkan virtual environment
- python3 -m venv .venv
- source .venv/bin/activate

2. Instal dependensi
- python -m pip install --upgrade pip
- pip install -r requirements.txt

3. Siapkan environment
- Jika tersedia: cp .env.example .env
- Jika tidak ada, buat minimal .env dengan:
  - SECRET_KEY="isi_dengan_secret_key"
  - DEBUG=1
  - ALLOWED_HOSTS=127.0.0.1,localhost

4. Migrasi database
- python manage.py migrate

5. (Opsional) Buat superuser
- python manage.py createsuperuser

6. Jalankan server pengembangan
- python manage.py runserver 0.0.0.0:8000
- Buka: http://localhost:8000 (atau http://<host-ip>:8000)

Windows (CMD / PowerShell / WSL)
- Rekomendasi: gunakan WSL2 (Ubuntu) jika tersedia. Jika menggunakan native Windows:

CMD
- python -m venv .venv
- .venv\Scripts\activate
- python -m pip install --upgrade pip
- pip install -r requirements.txt
- copy .env.example .env      (jika ada; atau buat .env manual)
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver 0.0.0.0:8000

PowerShell
- python -m venv .venv
- .\.venv\Scripts\Activate.ps1
  (Jika ExecutionPolicy mencegah, jalankan: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass)
- python -m pip install --upgrade pip
- pip install -r requirements.txt
- Copy-Item .env.example .env  (atau buat .env)
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver 0.0.0.0:8000

Catatan singkat untuk env vars di Windows:
- CMD: set SECRET_KEY=nilai
- PowerShell: $env:SECRET_KEY = "nilai"
- Gunakan file .env jika proyek membaca variabel dari .env (direkomendasikan)




## Keterangan singkat project

Aplikasi ini adalah backend Django untuk kebutuhan administrasi kelurahan (CRUD data, surat/layanan, autentikasi/role, API via DRF). Dependensi utama (lihat requirements.txt):
- Django 5.2.x
- djangorestframework
- asgiref, sqlparse

Komponen umum:
- API dibuat menggunakan Django REST Framework
- Default DB: SQLite (mudah untuk development). Untuk Postgres/MySQL, sesuaikan DATABASES di settings atau env vars.

## Struktur proyek (umum)
- manage.py
- kelurahan/settings.py, urls.py, wsgi/asgi.py
- apps/* — aplikasi Django (models, views, serializers, urls)
- templates/, static/
- requirements.txt
- .env.example (jika ada)

## Menjalankan test
- python manage.py test
- atau pytest jika terpasang dan dikonfigurasi


