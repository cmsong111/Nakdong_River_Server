from django.contrib import admin
from .models import Nakdong, Comment


# Register your models here.


class NakdongAdmin(admin.ModelAdmin):
    fields = ['wtqltObsrvtCd', 'obsrvtNm', 'msmtTm', 'altdDpwt', 'mesureDpwt', 'wtep', 'saln']
    list_display = ('id', 'obsrvtNm', 'msmtTm','mesureDpwt', 'wtep', 'saln')
    ordering = ['-msmtTm']


class CommentsAdmin(admin.ModelAdmin):
    fields = ['ipAdress', 'text', 'date', 'reportCount']
    list_display = ('id', 'ipAdress', 'text', 'date', 'reportCount')


admin.site.register(Nakdong, NakdongAdmin)
admin.site.register(Comment, CommentsAdmin)
