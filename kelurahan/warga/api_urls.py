# # warga/api_urls.py
# from django.urls import path
# from .views import WargaListAPIView, WargaDetailAPIView

# urlpatterns = [
#     path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
#     path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

# Buat router dan daftarkan ViewSet
router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='api-warga')           # ubah basename supaya nama URL tidak bentrok
router.register(r'pengaduan', PengaduanViewSet, basename='api-pengaduan')  # ubah basename supaya nama URL tidak bentrok

# URL API ditentukan oleh router
urlpatterns = [
    path('', include(router.urls)),
]
