from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Default UserAdmin'i kaldır, özelleştirilmişini ekle
admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Filtreleri tamamen kaldır
    list_filter = []

    # Action bar'ı gizle (actions = None yapınca GO butonu ve dropdown kalkar)
    actions = ['delete_selected_users']

    def delete_selected_users(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} kullanıcı başarıyla silindi.")
    delete_selected_users.short_description = "Seçili kullanıcıları sil"

    class Media:
        css = {'all': ('css/admin_custom.css',)}
        js = ('js/admin_custom.js',)
