from django.contrib import admin

from .models import *


admin.site.register(CategoriesModel)
admin.site.register(CodesModel)
admin.site.register(GenerateModel)



admin.site.register(Categories)
admin.site.register(Codes)