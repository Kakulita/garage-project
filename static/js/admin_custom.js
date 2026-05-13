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
    var userDropdowns = document.querySelectorAll('.navbar-nav .nav-item.dropdown .nav-link');
    userDropdowns.forEach(function (link) {
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

    // ── Add butonlarının yazısını sadece "Add" yap ──
    var addBtns = document.querySelectorAll('a[href*="add/"].btn');
    addBtns.forEach(function (btn) {
        btn.innerHTML = '<i class="fas fa-plus mr-1"></i> Add';
    });

    // ── Delete butonu — Add butonunun yanına ekle ──
    var addBtn = document.querySelector('a[href*="add/"].btn, .btn.btn-success');
    if (addBtn) {
        var deleteBtn = document.createElement('button');
        deleteBtn.type = 'button';
        deleteBtn.className = 'btn btn-danger ml-2';
        deleteBtn.innerHTML = '<i class="fas fa-trash mr-1"></i> Delete';
        deleteBtn.style.marginLeft = '8px';
        deleteBtn.addEventListener('click', function () {
            var checked = document.querySelectorAll('input.action-select:checked');
            if (checked.length === 0) {
                alert('Lütfen silmek istediğiniz öğeleri seçin.');
                return;
            }
            if (!confirm(checked.length + ' öğe silinecek. Emin misiniz?')) return;

            var actionSelect = document.querySelector('select[name="action"]');
            if (actionSelect) {
                for (var i = 0; i < actionSelect.options.length; i++) {
                    if (actionSelect.options[i].value.indexOf('delete') !== -1) {
                        actionSelect.value = actionSelect.options[i].value;
                        break;
                    }
                }
                var form = actionSelect.closest('form');
                if (form) form.submit();
            }
        });
        addBtn.parentNode.insertBefore(deleteBtn, addBtn.nextSibling);
    }

    // ── Action bar'ı gizle (dropdown + GO + "0 of X selected") ──
    var actionBar = document.querySelector('.changelist-form-container .actions, .action-counter');
    if (actionBar) {
        var actionsRow = actionBar.closest('.row') || actionBar.closest('.actions');
        if (actionsRow) actionsRow.style.display = 'none';
    }

});
