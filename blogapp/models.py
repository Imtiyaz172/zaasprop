from django.db import models
from imagekit.models import ImageSpecField # < import this
from imagekit.processors import ResizeToFill # < import this
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe 
import os

# Create your models here.
class Logo(models.Model):
    Title       = models.CharField(max_length=50)
    Image       = models.ImageField(upload_to="logo/",blank= True)
    icon        = models.ImageField(upload_to="logo/",blank= True)
    Status      = models.BooleanField(default = True)
    header_image = models.ImageField(upload_to="logo/",blank= True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos' 

class company_footer_link(models.Model):
    Title       = models.CharField(max_length=50)
    facebook    = models.TextField(max_length=254)
    tweeter     = models.TextField(max_length=254,blank= True)
    google_plas = models.TextField(max_length=254,blank= True)
    youtube     = models.TextField(max_length=254,blank= True)
    Status        = models.BooleanField(default = True)
    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'company_footer_link'
        verbose_name_plural = 'company_footer_link'    

class Contact(models.Model):
    Name          = models.TextField(max_length=254)
    Designation   = models.TextField(max_length=254,blank= True)
    Phone_number  = models.CharField(max_length=50)
    Mail          = models.EmailField(max_length=254)
    Address       = models.TextField(max_length=254)
    Website       = models.TextField(max_length=254,blank= True)
    Facebook      = models.TextField(max_length=254,blank= True)
    Speach        = RichTextField(blank= True)
    google_map    = models.TextField(blank= True)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'    

class About_us(models.Model):
    Title         = models.CharField(max_length=50)
    Image         = models.ImageField(upload_to="Aboutus/")
    Speach        = RichTextField()
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Title 
    class Meta:
        verbose_name = 'About_us'
        verbose_name_plural = 'About_us'  


class Service(models.Model):
    Title         = models.CharField(max_length=100)
    Icon          = models.CharField(max_length=50)
    Details       = RichTextField()
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'  

class Slider(models.Model):
    Title         = models.CharField(max_length=100)
    image         = models.ImageField(upload_to="slider/")
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'  

class speach(models.Model):
    Title         = models.CharField(max_length=300)
    Details       = RichTextField()
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = 'speach'
        verbose_name_plural = 'speach'  


class Agent(models.Model):
    Name          = models.CharField(max_length=100)
    Designation   = models.CharField(max_length=50)
    mail          = models.CharField(max_length=50,blank= True)
    phone         = models.CharField(max_length=50,blank= True)
    Image         = models.ImageField(upload_to="Agents/")
    Facebook      = models.CharField(max_length=100,blank= True)
    Twitter       = models.CharField(max_length=100,blank= True)
    linkdin       = models.CharField(max_length=100,blank= True)
    google_plas   = models.CharField(max_length=100,blank= True)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Name 

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

class Category(models.Model):
    Name          = models.CharField(max_length=100)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Name     
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categores'  

class subcategory(models.Model):
    Name          = models.CharField(max_length=100)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Name 
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategores' 

class user_reg(models.Model):
    Name          = models.CharField(max_length=100)
    email         = models.EmailField(max_length=250)
    password      = models.CharField(max_length=100)
    phone         = models.CharField(max_length=100)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Name 
    class Meta:
        verbose_name = 'user_reg'
        verbose_name_plural = 'user_reg' 


class Properte(models.Model):
    user          = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory   = models.ForeignKey(subcategory, on_delete=models.CASCADE)
    image1        = models.ImageField(upload_to="property/")
    image1_resize = ImageSpecField(source='image1',processors=[ResizeToFill(700,500)],format='JPEG',options={'quality': 100})
    image2        = models.ImageField(upload_to="property/", blank=True, null=True)
    image2_resize = ImageSpecField(source='image2',processors=[ResizeToFill(700,500)],format='JPEG',options={'quality': 100})
    image3        = models.ImageField(upload_to="property/", blank=True, null=True)
    image3_resize = ImageSpecField(source='image3',processors=[ResizeToFill(700,500)],format='JPEG',options={'quality': 100})
    image4        = models.ImageField(upload_to="property/", blank=True, null=True)
    image4_resize = ImageSpecField(source='image4',processors=[ResizeToFill(700,500)],format='JPEG',options={'quality': 100})
    image5        = models.ImageField(upload_to="property/", blank=True, null=True)
    image5_resize = ImageSpecField(source='image5',processors=[ResizeToFill(700,500)],format='JPEG',options={'quality': 100})
    title         = models.CharField(max_length=200)
    area          = models.CharField(max_length=200,blank=True)
    price         = models.CharField(max_length=20,default=0,blank=True)
    discription   = RichTextField()
    feature1      = models.CharField(max_length=50)
    feature2      = models.CharField(max_length=50,blank=True)
    feature3      = models.CharField(max_length=50,blank=True)
    feature4      = models.CharField(max_length=50,blank=True)
    feature5      = models.CharField(max_length=50,blank=True)
    feature6      = models.CharField(max_length=50,blank=True)
    feature7      = models.CharField(max_length=50,blank=True)
    feature8      = models.CharField(max_length=50,blank=True)
    feature9      = models.CharField(max_length=50,blank=True)
    feature10      = models.CharField(max_length=50,blank=True)
    feature11      = models.CharField(max_length=50,blank=True)
    feature12     = models.CharField(max_length=50,blank=True)       
    feature13      = models.CharField(max_length=50,blank=True)       
    feature14      = models.CharField(max_length=50,blank=True)       
    feature15      = models.CharField(max_length=50,blank=True)         
    location      = models.CharField( max_length=250)
    gmap          = models.TextField(blank=True)
    contact_name  = models.CharField(max_length=100,blank=True)
    Phone_number  = models.CharField(max_length=100)
    mail          = models.EmailField(max_length=250,blank=True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    seo_title     = models.TextField(blank=True)
    propertyID    = models.AutoField(primary_key= True)
    Status        = models.BooleanField(default = False)
    feature_property      = models.BooleanField(default = False)
    view          = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Propertes' 
    
    def url(self):
        return os.path.join('/static/blogapp/media/property/', os.path.basename(str(self.image1)))

    def photo(self):
        return mark_safe('<img src = "{}" width="100" height="50"/>'.format(self.url()))


class user_massage(models.Model):
    Name          = models.CharField(max_length=100)
    email         = models.EmailField(max_length=250)
    subject       = models.TextField(blank=True)
    massage       = RichTextField()
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.Name 
    class Meta:
        verbose_name = 'user_massage'
        verbose_name_plural = 'user_massages'
        

class blog(models.Model):
    image1        = models.FileField(upload_to="blog/")
    image2        = models.FileField(upload_to="blog/", blank=True, null=True)
    image3        = models.FileField(upload_to="blog/", blank=True, null=True)
    image4        = models.FileField(upload_to="blog/",blank=True, null=True)
    image5        = models.FileField(upload_to="blog/",blank=True, null=True)
    title         = models.CharField(max_length=200)
    discription   = RichTextField()
    author        = models.CharField(max_length=100,blank=True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    upload_date   = models.DateField(auto_now_add = True)
    Status        = models.BooleanField(default = True)
    view          = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs' 
    def url(self):
        return os.path.join('/static/blogapp/media/blog/', os.path.basename(str(self.image1)))

    def photo(self):
        return mark_safe('<img src = "{}" width="100" height="50"/>'.format(self.url()))

class SeoContent(models.Model):
    index_meta_title            = models.TextField(blank=True)
    index_meta_description      = models.TextField(blank=True)
    index_meta_keywords         = models.TextField(blank=True)
    blog_title                  = models.TextField(blank=True)
    blog_description            = models.TextField(blank=True)
    blog_keywords               = models.TextField(blank=True)
    contact_title               = models.TextField(blank=True)
    contact_description         = models.TextField(blank=True)
    contact_keywords            = models.TextField(blank=True)
    properties_title            = models.TextField(blank=True)
    properties_description      = models.TextField(blank=True)
    properties_keywords         = models.TextField(blank=True)
    about_us_title              = models.TextField(blank=True)
    about_us_description        = models.TextField(blank=True)
    about_us_keywords           = models.TextField(blank=True)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.index_meta_title 
    class Meta:
        verbose_name = 'SeoContent'
        verbose_name_plural = 'SeoContents'