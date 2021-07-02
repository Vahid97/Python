from django.db import models


class Category(models.Model):
    
    title = models.CharField('Title', max_length=127)
    image = models.CharField('Image', max_length=127)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    


class Contact(models.Model):
    """ Contact information """
    full_name = models.CharField('Title', max_length=127)
    email = models.EmailField('E-mail', max_length=127)
    subject = models.CharField('Subject', max_length=127)
    message = models.TextField('Message', help_text='Send your messages')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.subject} named feedback'
    



class Case_study(models.Model):
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, related_name='case_studies', db_index=True)

    title = models.CharField('Title', max_length=127)
    image = models.ImageField('Image', upload_to='case_study_images')
    slug = models.SlugField('Slug', max_length=150)
    description = models.TextField('Description',)
    order = models.PositiveIntegerField('Order', default=1)

    class Meta:
        verbose_name = 'Case_study'
        verbose_name_plural = 'Case_studies'

    def __str__(self):
        return self.title


class Practice_areas(models.Model):
    
    title = models.CharField('Title', max_length=127)
    image = models.ImageField('Image', max_length=127, upload_to='practice_area_images')
    slug = models.SlugField('Slug', max_length=150)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Practice_area'
        verbose_name_plural = 'Practice_areas'

    def __str__(self):
        return self.title


class Attorneys(models.Model):
    
    name = models.CharField('Name', max_length=127)
    title = models.CharField('Title', max_length=127)
    image = models.ImageField('Image', max_length=127, upload_to='attorneys')
    slug = models.SlugField('Slug', max_length=150)

    
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Attorney'
        verbose_name_plural = 'Attorneys'

    def __str__(self):
        return self.name