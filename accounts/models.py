from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class department(models.Model):
    departmentname = models.CharField("Department Name",max_length=25,null=True)
    description = models.CharField(max_length=200, default='None')
    max_users = models.IntegerField(default=1)
    max_projects = models.IntegerField(default=1)
    max_projects_social = models.IntegerField(default=1)
    max_online_feeds = models.IntegerField(default=1)
    max_social_feeds = models.IntegerField(default=1)
    max_twitter_data = models.IntegerField(default=1)
    logo = models.ImageField(upload_to='static/department_logo', null=True, blank=True)
    current_number_of_projects = models.IntegerField(default=0)
    current_number_of_social_projects = models.IntegerField(default=0)
    current_number_of_users = models.IntegerField(default=0)

    def __str__(self):
        return str(self.departmentname)

class Profile(models.Model):
    COMPANY = 'company'
    REGULAR_USER = 'regular_user'
    PICKER = 'picker'
    WRITER = 'writer'
    PUBLISHER = 'publisher'

    ROLE_CHOICES = (
        (COMPANY, 'Company'),
        (REGULAR_USER, 'Regular User'),
        (PICKER, 'Picker'),
        (WRITER, 'Writer'),
        (PUBLISHER, 'Publisher'),
    )
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    phone = models.CharField("Phon No",max_length=100,null=True)
    jobtitle = models.CharField("Job Title",max_length=100,null=True)
    department = models.ForeignKey(department,blank=True,null=True,on_delete=models.CASCADE,related_name='department_users',verbose_name ='Department')
    photo = models.ImageField(upload_to='static/user_image', blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, blank=True, null=True, default=ROLE_CHOICES[1][1])

    def save(self, *args, **kwargs):
        if self.department:
            if self.department.department_users.all().count() < self.department.max_users:
                self.department.current_number_of_users += 1
                self.department.save()
                return super(Profile, self).save(*args, **kwargs)
            self.user.delete()
            raise ValidationError('Users creation limit reached')            
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

@receiver(pre_delete, sender=Profile)
def decrease_cur_number_of_users(sender, instance, using, **kwargs):
    instance.department.current_number_of_users -= 1
    instance.department.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
