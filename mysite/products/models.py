from django.db import models

# Create your models here.
from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Product(models.Model):
	SN = models.CharField(max_length=120,null=False,blank=True)
	OrderID  = models.CharField(max_length=120,null=False,blank=True)
	BatchNo = models.CharField(max_length=120,null=False,blank=True)
	ShipDate = models.DateTimeField()
	TimeWarranty = models.CharField(max_length=10,null=True,blank=True)
	Exprie = models.DateTimeField()
	Type = models.CharField(max_length=120,null=True,blank=True)
	IMEI = models.CharField(max_length=120,null=True,blank=True)
	SIMICC_id  = models.CharField(max_length=120,null=True,blank=True)
	Version = models.CharField(max_length=120,null=True,blank=True)
	SecretKey = models.CharField(max_length=120,null=True,blank=True)
	NCR_No = models.CharField(max_length=120,null=True,blank=True)
	NCR_Handling = models.CharField(max_length=120,null=True,blank=True)

	def __unicode__(self):
			#	return smart_unicode(self.email)
			return self.NCR_No

class SignUp(models.Model):
	first_name = models.CharField(max_length=120,null=True,blank=True)
	last_name = models.CharField(max_length=120,null=True,blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	def __unicode__(self):
				return smart_unicode(self.email)			