document.addEventListener('DOMContentLoaded', function () {

    // ── İki satırlı brand (Virtual Garage / ADMIN PANEL) ──
    var brand = document.querySelector('.navbar-brand');
    if (brand) {
        brand.innerHTML =
            '<span style="font-size:1.5rem;line-height:1;margin-right:8px;">🏎️</span>' +
            '<span style="display:flex;flex-direction:column;line-height:1.15;">' +
            '<span style="font-size:1rem;font-weight:700;color:#fff;letter-spacing:.02em;">Virtual Garage</span>' +
            '<span style="font-size:.62rem;font-weight:600;color:#e74c3c;letter-spacing:.1em;text-transform:uppercase;">Admin Panel</span>' +
            '</span>';
        brand.style.display = 'flex';
        brand.style.alignItems = 'center';
    }

    // ── Sağ üst: kullanıcı avatarı + kullanıcı adı ──
    // Jazzmin'de sağ köşedeki kullanıcı dropdown'ı bul
    var userDropdowns = document.querySelectorAll('.navbar-nav .nav-item.dropdown .nav-link');
    userDropdowns.forEach(function (link) {
        // Top-nav menu linklerini atla, sadece kullanıcı dropdown'ını hedefle
        if (link.closest('.top-nav')) return;
        var username = link.textContent.trim();
        if (!username || link.querySelector('img')) return;
        var avatarUrl =
            'https://ui-avatars.com/api/?name=' +
            encodeURIComponent(username) +
            '&background=e74c3c&color=fff&size=32&bold=true';
        link.innerHTML =
            '<img src="' + avatarUrl + '" width="30" height="30" ' +
            'style="border-radius:50%;border:2px solid #e74c3c;margin-right:8px;vertical-align:middle;" alt=""> ' +
            '<span style="font-weight:600;">' + username + '</span>';
    });

});
