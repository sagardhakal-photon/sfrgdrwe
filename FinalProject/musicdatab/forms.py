from django import forms  
from musicdatab.models import Instrument_Player
from musicdatab.models import Performance
from musicdatab.models import Song
from musicdatab.models import Album
from musicdatab.models import Instrument
from musicdatab.models import Musician  
from musicdatab.models import Full_Address


class MusicianForm(forms.ModelForm):  
    class Meta:  
        model = Musician  
        fields = "__all__"  


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = "__all__"


class Instrument_PlayerForm(forms.ModelForm):
    class Meta:
        model = Instrument_Player
        fields = "__all__"

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = "__all__"

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

class Full_AddressForm(forms.ModelForm):
    class Meta:
        model = Full_Address
        fields ="__all__"