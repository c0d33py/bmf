from django_summernote.admin import SummernoteModelAdmin
from metatags.admin import MetaTagAbleMixin
from .models import Services, Contact
from django.contrib import admin

# Register your models here.
admin.site.site_header = "BMS Admin"
admin.site.site_title = "BMS Admin Portal"
admin.site.index_title = "Welcome to BMS Admin Portal"

admin.site.register(Contact)


@admin.register(Services)
class ServicesModelAdmin(MetaTagAbleMixin, SummernoteModelAdmin, admin.ModelAdmin):

    list_display = ('title', 'status', 'author', 'created_at')
    search_fields = ['title', 'timeline', 'content']
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['author', ]
    summernote_fields = ('content',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
