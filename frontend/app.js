// app.js
document.addEventListener('DOMContentLoaded', () => {
    const wargaListContainer = document.getElementById('warga-list-container');
    const apiUrl = 'http://127.0.0.1:8000/api/warga/';

    function renderWarga(warga) {
        // Membuat elemen untuk setiap warga
        const wargaDiv = document.createElement('div');
        wargaDiv.style.border = '1px solid #ccc';
        wargaDiv.style.padding = '10px';
        wargaDiv.style.marginBottom = '10px';

        const nama = document.createElement('h3');
        nama.textContent = warga.nama_lengkap;

        const nik = document.createElement('p');
        nik.textContent = `NIK: ${warga.nik}`;

        const alamat = document.createElement('p');
        alamat.textContent = `Alamat: ${warga.alamat}`;

        wargaDiv.appendChild(nama);
        wargaDiv.appendChild(nik);
        wargaDiv.appendChild(alamat);

        return wargaDiv;
    }

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            wargaListContainer.innerHTML = ''; // Hapus pesan "Memuat data..."
            data.results.forEach(warga => {
                const wargaElement = renderWarga(warga);
                wargaListContainer.appendChild(wargaElement);
            });
        })
        .catch(error => {
            wargaListContainer.innerHTML = '<p>Gagal memuat data. Pastikan server backend berjalan.</p>';
            console.error('There has been a problem with your fetch operation:', error);
        });
});
