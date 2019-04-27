from django.contrib import admin

from pril.models import Template,Moment,Golos,Collect,RequiredPeople

admin.site.register(Template)

admin.site.register(Moment)

admin.site.register(Golos)

admin.site.register(Collect)

admin.site.register(RequiredPeople)