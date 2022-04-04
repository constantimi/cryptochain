from django.contrib import admin

from .models import Block, Transaction, Input, Output

admin.site.register(Block)
admin.site.register(Transaction)
admin.site.register(Input)
admin.site.register(Output)
