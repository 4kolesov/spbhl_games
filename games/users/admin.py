from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username',
                    'first_name', 'last_name', 'email',)
    search_fields = ('username', 'email')
    list_filter = ('email', 'username')
    empty_value_display = '-пусто-'
    save_on_top = True

    # def get_subscribers(self, obj):
    #     return obj.subscribers.count()
    # get_subscribers.short_description = 'Кол-во подписчиков'
