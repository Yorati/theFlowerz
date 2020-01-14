from django.contrib import admin
from .models import  Flower, KindOfFlower, Color, ForSale

#admin.site.register(Flower)
#admin.site.register(KindOfFlower)
admin.site.register(Color)
#admin.site.register(ForSale)

# Define the admin class
class KindOfFlowerAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(KindOfFlower, KindOfFlowerAdmin)

# Register the Admin classes for Flower using the decorator
class ForSaleInline(admin.TabularInline):
    model = ForSale
@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_color', 'kind_of_flower')
    inlines = [ForSaleInline]
# Register the Admin classes for ForSale using the decorator

@admin.register(ForSale)
class ForSaleAdmin(admin.ModelAdmin):
    list_filter = ('flower','borrower', 'status')
    fieldsets =(
    (None, {'fields': ('imprint', 'id',)}),
    ('Availability', {'fields': ('flower', 'status','borrower',)}),
    )
