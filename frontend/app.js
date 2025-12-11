// Konfigurasi URL API (Sesuaikan dengan port Django Anda, biasanya 8000)
// Jika frontend dan backend di domain yg sama, cukup '/api'
const API_BASE = 'http://127.0.0.1:8000/api'; 

// --- NAVIGASI ---
function hideAllViews() {
    document.querySelectorAll('.view-section').forEach(el => el.classList.add('hidden'));
}

function showView(viewId) {
    hideAllViews();
    document.getElementById(viewId).classList.remove('hidden');
}

// --- WARGA LOGIC ---

// 1. Get List Warga
async function showWargaList() {
    showView('view-warga-list');
    const container = document.getElementById('warga-container');
    container.innerHTML = '<p>Loading...</p>';

    try {
        const response = await fetch(`${API_BASE}/warga/`);
        const data = await response.json();
        
        container.innerHTML = '';
        if(data.length === 0) container.innerHTML = '<li>Belum ada data warga.</li>';

        data.forEach(warga => {
            container.innerHTML += `
                <li class="list-item">
                    <div>
                        <div class="item-title" onclick="showWargaDetail(${warga.id})">${warga.nama_lengkap}</div>
                        <small>NIK: ${warga.nik}</small>
                    </div>
                    <div>
                        <button class="btn btn-primary" onclick="editWarga(${warga.id})">Edit</button>
                        <button class="btn btn-danger" onclick="deleteWarga(${warga.id})">Hapus</button>
                    </div>
                </li>
            `;
        });
    } catch (error) {
        container.innerHTML = '<p style="color:red">Gagal mengambil data. Pastikan server Django berjalan.</p>';
        console.error(error);
    }
}

// 2. Get Detail Warga
async function showWargaDetail(id) {
    try {
        const response = await fetch(`${API_BASE}/warga/${id}/`);
        const warga = await response.json();

        // Render Data Diri
        const detailHtml = `
            <div class="detail-row"><div class="detail-label">Nama:</div> <div>${warga.nama_lengkap}</div></div>
            <div class="detail-row"><div class="detail-label">NIK:</div> <div>${warga.nik}</div></div>
            <div class="detail-row"><div class="detail-label">Telp:</div> <div>${warga.no_telepon || '-'}</div></div>
            <div class="detail-row"><div class="detail-label">Alamat:</div> <div>${warga.alamat}</div></div>
        `;
        document.getElementById('detail-content').innerHTML = detailHtml;

        // Render Pengaduan Terkait (Diasumsikan Serializer Warga menyertakan field pengaduan_set)
        const aduanList = document.getElementById('warga-pengaduan-list');
        aduanList.innerHTML = '';
        
        // Cek apakah ada data pengaduan di response JSON
        const pengaduans = warga.pengaduan_set || []; // Sesuaikan dengan nama field di Serializer
        
        if (pengaduans.length === 0) {
            aduanList.innerHTML = '<li>Tidak ada riwayat pengaduan.</li>';
        } else {
            pengaduans.forEach(aduan => {
                aduanList.innerHTML += `
                    <li class="list-item" style="background:white; border:1px solid #eee;">
                        <strong>${aduan.judul}</strong><br>${aduan.deskripsi}
                    </li>
                `;
            });
        }

        showView('view-warga-detail');
    } catch (error) {
        alert('Gagal memuat detail warga');
    }
}

// 3. Form Warga (Tambah & Edit)
async function showWargaForm() {
    document.getElementById('warga-form').reset();
    document.getElementById('warga-id').value = ''; // Kosong berarti mode Tambah
    document.getElementById('form-warga-title').innerText = 'Tambah Warga Baru';
    showView('view-warga-form');
}

async function editWarga(id) {
    // Ambil data dulu untuk diisi ke form
    const response = await fetch(`${API_BASE}/warga/${id}/`);
    const warga = await response.json();

    document.getElementById('warga-id').value = warga.id;
    document.getElementById('warga-nama').value = warga.nama_lengkap;
    document.getElementById('warga-nik').value = warga.nik;
    document.getElementById('warga-telp').value = warga.no_telepon;
    document.getElementById('warga-alamat').value = warga.alamat;
    
    document.getElementById('form-warga-title').innerText = 'Edit Data Warga';
    showView('view-warga-form');
}

// Handle Submit Form Warga
document.getElementById('warga-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const id = document.getElementById('warga-id').value;
    const data = {
        nama_lengkap: document.getElementById('warga-nama').value,
        nik: document.getElementById('warga-nik').value,
        no_telepon: document.getElementById('warga-telp').value,
        alamat: document.getElementById('warga-alamat').value,
    };

    const method = id ? 'PUT' : 'POST';
    const url = id ? `${API_BASE}/warga/${id}/` : `${API_BASE}/warga/`;

    await fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    showWargaList();
});

// 4. Delete Warga
async function deleteWarga(id) {
    if(confirm('Yakin ingin menghapus warga ini?')) {
        await fetch(`${API_BASE}/warga/${id}/`, { method: 'DELETE' });
        showWargaList();
    }
}


// --- PENGADUAN LOGIC ---

async function showPengaduanList() {
    showView('view-pengaduan-list');
    const container = document.getElementById('pengaduan-container');
    container.innerHTML = 'Loading...';

    const response = await fetch(`${API_BASE}/pengaduan/`);
    const data = await response.json();

    container.innerHTML = '';
    data.forEach(aduan => {
        container.innerHTML += `
            <li class="list-item">
                <div>
                    <div class="item-title">${aduan.judul}</div>
                    <small>Oleh: ${aduan.nama_warga || 'Warga ID: ' + aduan.warga}</small>
                    <p>${aduan.deskripsi}</p>
                </div>
                <div>
                    <button class="btn btn-danger" onclick="deletePengaduan(${aduan.id})">Hapus</button>
                </div>
            </li>
        `;
    });
}

async function showPengaduanForm() {
    // Load dropdown warga dulu
    const res = await fetch(`${API_BASE}/warga/`);
    const wargaList = await res.json();
    
    const select = document.getElementById('pengaduan-warga');
    select.innerHTML = '<option value="">-- Pilih Warga --</option>';
    wargaList.forEach(w => {
        select.innerHTML += `<option value="${w.id}">${w.nama_lengkap}</option>`;
    });

    document.getElementById('pengaduan-form').reset();
    showView('view-pengaduan-form');
}

// Handle Submit Pengaduan
document.getElementById('pengaduan-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const data = {
        warga: document.getElementById('pengaduan-warga').value,
        judul: document.getElementById('pengaduan-judul').value,
        deskripsi: document.getElementById('pengaduan-deskripsi').value,
    };

    await fetch(`${API_BASE}/pengaduan/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    showPengaduanList();
});

async function deletePengaduan(id) {
    if(confirm('Hapus pengaduan ini?')) {
        await fetch(`${API_BASE}/pengaduan/${id}/`, { method: 'DELETE' });
        showPengaduanList();
    }
}

// Inisialisasi awal
showWargaList();