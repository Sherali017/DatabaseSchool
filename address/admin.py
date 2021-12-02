from django.contrib import admin

from address.models import VilAddressModel, TShAddressModel, \
    SchoolAddressModel, SchoolModel

admin.site.register(VilAddressModel)
admin.site.register(TShAddressModel)
admin.site.register(SchoolAddressModel)
admin.site.register(SchoolModel)