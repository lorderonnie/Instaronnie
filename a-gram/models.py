from django.db import models

class gram(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    def save_gram(self):
        self.save()


        
class Accounts(models.Model):
    image= models.ImageField(upload_to ='home/')
    name = models.CharField(max_length =60)
    description = models.TextField()
   
    @classmethod
    def search_by_name(cls,search_term):
        accounts = cls.objects.filter(name__icontains=search_term)
        return accounts
    
    @classmethod
    def all_accounts(cls):
       accounts= cls.objects.all()
       return accounts
    
    def save_account(self):
        self.save()