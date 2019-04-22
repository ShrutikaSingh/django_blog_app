#************to add any field in user section of admin section just create a model in users-> models.py  and import trh model and register in admin.py*********

'''
            ********write below code in models.py*******
class Check(models.Model):
    print("hi")
'''

'''
        ****and these below codes for importing nd registering the models in admin.py(here)*******
from .models import Check
admin.site.register(Check)
'''

from django.contrib import admin
from .models import Profile


admin.site.register(Profile)


# Register your models here.
