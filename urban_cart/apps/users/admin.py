from django.contrib import admin
from .models import Register,State,District

# Register your models here.
admin.site.register(Register),
# admin.site.register(Login),
# admin.site.register(Logout),
admin.site.register(State),
admin.site.register(District),


