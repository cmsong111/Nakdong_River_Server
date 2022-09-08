from django.contrib import admin
from .models import Nakdong, Comment


# Register your models here.


class NakdongAdmin(admin.ModelAdmin):
    fields = ['wtqltObsrvtCd', 'obsrvtNm', 'msmtTm', 'altdDpwt', 'mesureDpwt', 'wtep', 'saln']


class CommentsAdmin(admin.ModelAdmin):
    fields = ['ipAdress', 'text', 'date', 'reportCount']


admin.site.register(Nakdong, NakdongAdmin)
admin.site.register(Comment, CommentsAdmin)
