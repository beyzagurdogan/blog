# blog/admin.py
from django.contrib import admin
from .models import Blog  # BlogPost yerine Blog içe aktarılmalı

admin.site.register(Blog)  # Blog modelini kaydedin
