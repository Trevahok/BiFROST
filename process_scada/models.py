from django.db import models
from django.urls import reverse_lazy
from django.utils.timezone import now

# Create your models here.
class File(models.Model):
    file =  models.FileField( upload_to='reports/', max_length=100)

class Product(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    def __str__(self):
        return f'{self.name}'
    
class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_no = models.CharField(primary_key=True,max_length=20)

    def __str__(self):
        return f'{self.product}  {self.batch_no}'

class Parameter(models.Model):
    sno = models.PositiveSmallIntegerField(primary_key=True, verbose_name='Serial No.',help_text='Enter the Serial No.')
    name = models.CharField(max_length=200,verbose_name='Parameter Name', help_text='Enter the Parameter Name')
    value = models.CharField(max_length=200,verbose_name='Parameter Value', help_text='Enter the Parameter Value')
    description = models.TextField(blank=True,null=True,max_length=1000, verbose_name='Parameter Description', help_text='Enter the Parameter Description')

    class Meta:
        ordering = ['sno'] 

    def __str__(self):
        return f'{self.sno}  {self.name}  {self.value}'
    
    def get_absolute_url(self):
        return reverse_lazy('view_parameter')

class Diagnosis(models.Model):

    DIAGNOSIS_FILTERS = (
        ('S', 'S'),
        ('W', 'W'),
        ('D', 'D'),
    )
    timestamp = models.DateTimeField(default=now,verbose_name='Event Time', primary_key=True)
    diagnosis_filter = models.CharField(max_length=5, choices=DIAGNOSIS_FILTERS,help_text='Choose the diagnosis filter')    
    error_code = models.IntegerField(help_text='Enter the Error Code',verbose_name='Error Code')
    details = models.TextField(blank=True, null=True, verbose_name="Details", help_text='Enter the Details of Diagnosis')
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.timestamp}  {self.diagnosis_filter}  {self.error_code}'

    def get_absolute_url(self):
        return reverse_lazy('view_diagnosis')

class Production(models.Model):

    TYPE_CHOICES = [
        ('P','P'),
        ('E','E'),
        
    ]

    time = models.DateTimeField(default=now,verbose_name='Date and Time', help_text='Enter the date and time for the event', primary_key=True)
    types = models.CharField(max_length=5, choices = TYPE_CHOICES,verbose_name='Type', help_text='Enter the type')
    quantity  = models.PositiveIntegerField(help_text='Enter the production quantity in x1000', verbose_name='Quantity')
    comp_mmv =  models.CharField(max_length=10,help_text='Enter the Compression force M,MV', verbose_name='Compression Force ( M MV)')
    comp_srel = models.CharField(max_length=10,help_text = 'Enter compression force Srel %', verbose_name='Compression force( SRel %)')
    comp_pmv = models.CharField(max_length=10,help_text='Enter the compression force P MV', verbose_name='Compression Force ( P MV) ')
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return f'{self.time}  {self.types}  {self.quantity}  {self.comp_mmv}   {self.comp_srel}  {self.comp_pmv}'
    def get_absolute_url(self):
        return reverse_lazy("view_production")
    
class Change(models.Model):
    time = models.DateTimeField(verbose_name= 'Date and Time', primary_key=True)
    operation = models.CharField(max_length=30, verbose_name='Operation Type', help_text='Enter the operation type')
    description = models.TextField(max_length=200, verbose_name='Description',help_text='Enter Operation Description')
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'{self.time}  {self.operation}  {self.description}'
    
    def get_absolute_url(self):
        return reverse_lazy('view_change')
    

