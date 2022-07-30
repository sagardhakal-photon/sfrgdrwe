from django.contrib import admin
# Register your models here.
from . models import Album
from . models import Musician
from . models import Song
from . models import Instrument
from . models import Full_Address
from . models import Instrument_Player
from . models import Performance



admin.site.register(Album)
admin.site.register(Musician)
admin.site.register(Song)
admin.site.register(Performance)
admin.site.register(Instrument)
admin.site.register(Instrument_Player)
admin.site.register(Full_Address)


from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()