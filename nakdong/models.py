from django.db import models


# Create your models here.
class Nakdong(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 수질관측소코드
    wtqltObsrvtCd = models.TextField()
    # 수질관측소명
    obsrvtNm = models.TextField()
    # 계측시각
    msmtTm = models.DateTimeField()
    # 표고수심(EL.m)
    altdDpwt = models.FloatField()
    # 측정수심(m)
    mesureDpwt = models.FloatField()
    # 수온(℃)
    wtep = models.FloatField()
    # 염분도(psu)
    saln = models.FloatField()


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    ipAdress = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    text = models.TextField()
    date = models.DateTimeField()
    reportCount = models.IntegerField()
