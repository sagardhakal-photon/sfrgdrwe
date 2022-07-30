from django.db import models  



class Full_Address(models.Model):
    City = models.CharField("City Name",max_length = 20)
    Area = models.CharField("Area",max_length=20)
    Street = models.CharField("Street",max_length=20)
    House_Num = models.CharField("House Number",max_length=20)
    Phone_Num = models.IntegerField(unique=True,primary_key=True)

    class Meta:
        db_table ="full_address"
    def __str__(self):
        return "Phone Number: " + str(self.Phone_Num) 

class Musician(models.Model):  
    M_Sn = models.IntegerField(primary_key=True) 
    First_Name = models.CharField(max_length=100)
    Mid_Name = models.CharField(max_length=100,null=True)
    Last_Name = models.CharField(max_length=100)
    Phone_Num = models.ForeignKey(Full_Address,to_field="Phone_Num",on_delete=models.CASCADE,db_column='Phone_Num')


    class Meta:  
        db_table = "musician" 
    def __str__(self):
            return "SSN: " + str(self.M_Sn) + " \n  " + "Name: " + str(self.First_Name) 

class Album(models.Model):
    Title = models.CharField("Title",max_length=20)
    Alubm_ID = models.IntegerField(primary_key=True)
    Copyright_Data = models.CharField(max_length=100)
    Format = models.CharField(max_length=100)
    class Meta:
        db_table = "album"
    def __str__(self):
            return f"Album ID:{self.Alubm_ID}"
            return f"Name :{self.Title}"
            return f"Format:{self.Format}"
            return f"Copyright Data :{self.Copyright_Data}"
    


class Song(models.Model):
    Title = models.CharField(max_length=100,primary_key=True)
    Song_ID = models.IntegerField()
    Author = models.CharField(max_length=100)
    Album_ID = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        db_table = "song"
    def __str__(self):
            return "SONG ID: " + str(self.Song_ID)  
           





class Performance(models.Model):
    Song_ID = models.ForeignKey(Song, on_delete=models.CASCADE)
    M_Sn = models.ForeignKey(Musician, on_delete=models.CASCADE)
    class Meta:
        db_table = "performance" 
    def __str__(self):
            return f"SSN :{self.M_Sn}" 
            return f"title name :{self.Song_ID}" 
            

class Instrument(models.Model):
    Instrument_ID = models.IntegerField(primary_key=True)
    Music_Key=models.CharField(max_length=10)
    Name=models.CharField(max_length=30)
    class Meta:
        db_table = "instrument" 
    def __str__(self):
            return f"Instrument ID:{self.Instrument_ID}"

            return f"Instruments Name :{self.Name}" 
            return f"Music Key :{self.Music_Key}" 
            

class Instrument_Player(models.Model):
    M_Sn = models.ForeignKey(Musician, on_delete=models.CASCADE)
    Instrument_ID = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    class Meta:
        db_table = "instrument_player"
    def __str__(self):
            return f"Social Security Number :{self.M_Sn}" 
            return f"Instrument ID :{self.Insturment_ID}" 

