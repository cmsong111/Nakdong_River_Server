# exec(open("./nakdong/script.py",encoding='UTF-8').read())

from nakdong.models import Nakdong
import datetime

item = [
    {
        "altdDpwt": 1,
        "ec": "220.00",
        "mesureDpwt": 6.82,
        "msmtTm": 202209100010,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 24.99,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 2,
        "ec": "229.00",
        "mesureDpwt": 5.82,
        "msmtTm": 202209100010,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 24.96,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 3,
        "ec": "225.00",
        "mesureDpwt": 4.82,
        "msmtTm": 202209100010,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": "25.00",
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 4,
        "ec": "223.00",
        "mesureDpwt": 3.82,
        "msmtTm": 202209100010,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 25.06,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 5,
        "ec": "173.00",
        "mesureDpwt": 2.82,
        "msmtTm": 202209100010,
        "obsrvtNm": "하구둑10번교각",
        "saln": "0.10",
        "wtep": 39.74,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 6,
        "ec": "230.00",
        "mesureDpwt": 1.82,
        "msmtTm": 202209100010,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 25.22,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 4,
        "ec": "223.00",
        "mesureDpwt": 3.82,
        "msmtTm": 202209100020,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 25.06,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 1,
        "ec": "220.00",
        "mesureDpwt": 6.82,
        "msmtTm": 202209100020,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 24.99,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 2,
        "ec": "229.00",
        "mesureDpwt": 5.82,
        "msmtTm": 202209100020,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 24.96,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 3,
        "ec": "225.00",
        "mesureDpwt": 4.82,
        "msmtTm": 202209100020,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": "25.00",
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 5,
        "ec": "173.00",
        "mesureDpwt": 2.82,
        "msmtTm": 202209100020,
        "obsrvtNm": "하구둑10번교각",
        "saln": "0.10",
        "wtep": 39.74,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 6,
        "ec": "230.00",
        "mesureDpwt": 1.82,
        "msmtTm": 202209100020,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 25.22,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 4,
        "ec": "223.00",
        "mesureDpwt": 3.82,
        "msmtTm": 202209100030,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 25.06,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 1,
        "ec": "220.00",
        "mesureDpwt": 6.82,
        "msmtTm": 202209100030,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 24.99,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 2,
        "ec": "229.00",
        "mesureDpwt": 5.82,
        "msmtTm": 202209100030,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 24.96,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 3,
        "ec": "225.00",
        "mesureDpwt": 4.82,
        "msmtTm": 202209100030,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": "25.00",
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 5,
        "ec": "173.00",
        "mesureDpwt": 2.82,
        "msmtTm": 202209100030,
        "obsrvtNm": "하구둑10번교각",
        "saln": "0.10",
        "wtep": 39.74,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 6,
        "ec": "230.00",
        "mesureDpwt": 1.82,
        "msmtTm": 202209100030,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 25.22,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 2,
        "ec": "229.00",
        "mesureDpwt": 5.82,
        "msmtTm": 202209100040,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 24.96,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 1,
        "ec": "220.00",
        "mesureDpwt": 6.82,
        "msmtTm": 202209100040,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 24.99,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 3,
        "ec": "225.00",
        "mesureDpwt": 4.82,
        "msmtTm": 202209100040,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": "25.00",
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 4,
        "ec": "223.00",
        "mesureDpwt": 3.82,
        "msmtTm": 202209100040,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 25.06,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 5,
        "ec": "173.00",
        "mesureDpwt": 2.82,
        "msmtTm": 202209100040,
        "obsrvtNm": "하구둑10번교각",
        "saln": "0.10",
        "wtep": 39.74,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 6,
        "ec": "230.00",
        "mesureDpwt": 1.82,
        "msmtTm": 202209100040,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 25.22,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 6,
        "ec": "230.00",
        "mesureDpwt": 1.82,
        "msmtTm": 202209100050,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 25.22,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 1,
        "ec": "220.00",
        "mesureDpwt": 6.82,
        "msmtTm": 202209100050,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 24.99,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 3,
        "ec": "225.00",
        "mesureDpwt": 4.82,
        "msmtTm": 202209100050,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": "25.00",
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 5,
        "ec": "173.00",
        "mesureDpwt": 2.82,
        "msmtTm": 202209100050,
        "obsrvtNm": "하구둑10번교각",
        "saln": "0.10",
        "wtep": 39.74,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 2,
        "ec": "229.00",
        "mesureDpwt": 5.82,
        "msmtTm": 202209100050,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 24.96,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 4,
        "ec": "223.00",
        "mesureDpwt": 3.82,
        "msmtTm": 202209100050,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 25.06,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 6,
        "ec": "230.00",
        "mesureDpwt": 1.82,
        "msmtTm": 202209100100,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 25.22,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 1,
        "ec": "220.00",
        "mesureDpwt": 6.82,
        "msmtTm": 202209100100,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 24.99,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 5,
        "ec": "173.00",
        "mesureDpwt": 2.82,
        "msmtTm": 202209100100,
        "obsrvtNm": "하구둑10번교각",
        "saln": "0.10",
        "wtep": 39.74,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 2,
        "ec": "229.00",
        "mesureDpwt": 5.82,
        "msmtTm": 202209100100,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.13,
        "wtep": 24.96,
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 3,
        "ec": "225.00",
        "mesureDpwt": 4.82,
        "msmtTm": 202209100100,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": "25.00",
        "wtqltObsrvtCd": "2022B4b"
    },
    {
        "altdDpwt": 4,
        "ec": "223.00",
        "mesureDpwt": 3.82,
        "msmtTm": 202209100100,
        "obsrvtNm": "하구둑10번교각",
        "saln": 0.12,
        "wtep": 25.06,
        "wtqltObsrvtCd": "2022B4b"
    }
]

for i in item:
    year = int(str(i['msmtTm'])[:4])
    month = int(str(i['msmtTm'])[4:6])
    day = int(str(i['msmtTm'])[6:8])
    hours = int(str(i['msmtTm'])[8:10])
    min = int(str(i['msmtTm'])[10:12])
    p = datetime.datetime(year, month, day, hour=hours, minute=min)
    temp = Nakdong.objects.create(altdDpwt=i['altdDpwt'], mesureDpwt=str(i['mesureDpwt']),wtqltObsrvtCd=i['wtqltObsrvtCd'], wtep=i['wtep'], saln=i['saln'],obsrvtNm=i['obsrvtNm'], msmtTm=p)
