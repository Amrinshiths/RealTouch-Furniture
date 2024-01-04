from django.db import models
from autoslug import AutoSlugField
from django.forms import TextInput, Textarea
from django.forms import ModelForm

# Create your models here.
class BodyAbout(models.Model):
    image1         =   models.ImageField(upload_to='about-image/', null=True, blank=True,)
    image2         =   models.ImageField(upload_to='about-image/', null=True, blank=True,)
    OurVision    =   models.CharField(max_length=300)
    OurMission =   models.CharField(max_length=255)
    WhoWeAre    =   models.CharField(max_length=255)
    slug            =   AutoSlugField(populate_from='OurVision',max_length=255,unique=True,null=True )
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.OurVision

class Clients(models.Model):
    HappyCustomer         =   models.IntegerField()
    YearsinBusiness         =   models.IntegerField()
    ReturnClients    =  models.IntegerField()
    AwardsWon =   models.IntegerField()
    slug            =   AutoSlugField(populate_from='HappyCustomer',max_length=255,unique=True,null=True )
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.HappyCustomer

class CustomerSay(models.Model):
    name    =   models.CharField(max_length=200)
    image         =   models.ImageField(upload_to='customer-image/', null=True, blank=True,)
    message   =   models.CharField(max_length=300)
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


class ClientBrand(models.Model):
    name    =   models.CharField(max_length=200)
    image         =   models.ImageField(upload_to='Brand-image/', null=True, blank=True,)
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    STATUS =(
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed')
    )
    name      = models.CharField(blank=True, max_length=250)
    phone_no  = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True,max_length=50 )
    subject = models.CharField(blank=True, max_length=255)
    message = models.TextField(blank=True, max_length=550 )
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    is_active       =   models.BooleanField(default=True)
    ip = models.CharField(max_length=20,blank=True)
    note =    models.CharField(blank=True, max_length=255)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)    


    def __str__(self):
        return self.name
    
class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','phone_no','email','subject','message']
        widgets={
            'name':TextInput(attrs={'class':"form-control", 'id':"cname", 'placeholder':"Name *", }),
            'email':TextInput(attrs={'class':"form-control" ,'id':"cemail" ,'placeholder':"Email *" }),
            'phone_no':TextInput(attrs={'name':"phone_no", 'class':"form-control" ,'id':"cphone", 'placeholder':"Phone"}),
            'subject':TextInput(attrs={ 'name':"subject", 'class':"form-control", 'id':"csubject" ,'placeholder':"Subject"}),
            'message':Textarea(attrs={'class':"form-control", 'name':"message" ,'cols':"30" ,'rows':"4", 'id':"cmessage"  ,'placeholder':"Message *"}),
        }


class customize(models.Model):
    name    =   models.CharField(max_length=200)
    image         =   models.ImageField(upload_to='custom-image/', null=True, blank=True,)
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)  
    discription      =   models.CharField(blank=True,null=True,max_length=300 )

    def __str__(self):
        return self.name
