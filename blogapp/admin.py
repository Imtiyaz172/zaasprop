from django.contrib import admin
from . import models
admin.site.site_header='Zaas Property'


# Register your models here.

class LogoModel(admin.ModelAdmin):
    list_display    = ["__str__","Title", "Status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["Title", "Status"]

admin.site.register(models.Logo, LogoModel)

class ContactModel(admin.ModelAdmin):
    list_display    = ["__str__","Name","Address","Status"]
    search_fields   = ["Name","Address","Status"]
    list_per_page   = 20
    list_filter     = ["Name","Address","Status"]


admin.site.register(models.Contact, ContactModel)


class About_usModel(admin.ModelAdmin):
    list_display    = ["__str__","Status"]
    search_fields   = ["Title"]
    list_per_page   = 20
    list_filter     = ["Title"]

admin.site.register(models.About_us, About_usModel)


class ServiceModel(admin.ModelAdmin):
    list_display    = ["__str__","Title","Status"]
    search_fields   = ["Title"]
    list_per_page   = 20
    list_filter     = ["Title"]

admin.site.register(models.Service, ServiceModel)


class speachModel(admin.ModelAdmin):
    list_display    = ["__str__","Title","Status"]
    search_fields   = ["Title"]
    list_per_page   = 20
    list_filter     = ["Title"]

admin.site.register(models.speach, speachModel)


class AgentModel(admin.ModelAdmin):
    list_display    = ["__str__","Name","Designation"]
    search_fields   = ["Name","Designation"]
    list_per_page   = 20
    list_filter     = ["Name","Designation"]
    
admin.site.register(models.Agent, AgentModel)

class CategoryModel(admin.ModelAdmin):
    list_display    = ["__str__","Name","Status"]
    search_fields   = ["Name"]
    list_per_page   = 20
    list_filter     = ["Name"]

admin.site.register(models.Category, CategoryModel)

class subcategoryModel(admin.ModelAdmin):
    list_display    = ["__str__","Name","Status"]
    search_fields   = ["Name"]
    list_per_page   = 20
    list_filter     = ["Name"]

admin.site.register(models.subcategory, subcategoryModel)

class ProperteModel(admin.ModelAdmin):
    list_display    = ["__str__","title","photo","propertyID","category","subcategory","Status","feature_property","location","view"]
    search_fields   = ["title","propertyID","location"]
    list_per_page   = 20
    list_filter     = ["category","subcategory","Status"]


admin.site.register(models.Properte, ProperteModel)

class user_massageModel(admin.ModelAdmin):
    list_display    = ["__str__","Name","email","subject"]
    search_fields   = ["Name","email","subject","massage"]
    list_per_page   = 20
    list_filter     = ["Status"]


admin.site.register(models.user_massage, user_massageModel)

class user_regModel(admin.ModelAdmin):
    list_display    = ["__str__","Name","email","phone"]
    search_fields   = ["Name","email","phone"]
    list_per_page   = 20
    list_filter     = ["Status"]


admin.site.register(models.user_reg, user_regModel)

class blogModel(admin.ModelAdmin):
    list_display    = ["__str__","title","author","photo",'upload_date',"view","Status"]
    search_fields   = ["title","author"]
    list_per_page   = 20
    list_filter     = ["author","Status"]


admin.site.register(models.blog, blogModel)

class SliderModel(admin.ModelAdmin):
    list_display    = ["__str__","Title","image"]
    search_fields   = ["title"]
    list_per_page   = 20
    list_filter     = ["Status"]

admin.site.register(models.Slider, SliderModel)


class company_footer_linkModel(admin.ModelAdmin):
    list_display    = ["__str__","Title"]
    search_fields   = ["title"]
    list_per_page   = 20
    list_filter     = ["Status"]

admin.site.register(models.company_footer_link, company_footer_linkModel)


class SeoContentModel(admin.ModelAdmin):
    list_display    = ["__str__","index_meta_title"]
    search_fields   = ["index_meta_title"]
    list_per_page   = 30
    list_filter     = ["Status"]

admin.site.register(models.SeoContent, SeoContentModel)

