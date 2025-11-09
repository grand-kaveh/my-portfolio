from django.db import models
from extentions.utils import user_image_path, portfolio_image_path, degree_image_path


class InfoModel(models.Model):
    profile = models.ImageField(upload_to=user_image_path, verbose_name='Profile')
    age = models.PositiveIntegerField(verbose_name='Age')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    ln = models.CharField(max_length=255, verbose_name='LinkedIn')
    insta = models.CharField(max_length=255, verbose_name='Instagram')
    github = models.CharField(max_length=255, verbose_name='GitHub')
    telegram = models.CharField(max_length=255, verbose_name='Telegram')
    phone = models.PositiveBigIntegerField(verbose_name='Phone Number')
    address = models.CharField(max_length=255, verbose_name='Address')

    def __str__(self):
        return 'This is your Information :)'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Information'
        verbose_name_plural = 'Informations'


class SkillModel(models.Model):
    TITLE_SKILL = (('beginner', 'BEGINNER'), ('expert', 'EXPERT'), ('master', 'MASTER'), ('advance', 'ADVANCE'))
    skill = models.CharField(max_length=255, verbose_name='Skill')
    percent = models.PositiveIntegerField(verbose_name='Percent')
    title = models.CharField(max_length=255, choices=TITLE_SKILL, verbose_name='Title')

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class DegreeModel(models.Model):
    image = models.ImageField(upload_to=degree_image_path, verbose_name='Image')
    title = models.CharField(max_length=255, verbose_name='Title')
    created = models.DateField(verbose_name='Created')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Degree'
        verbose_name_plural = 'Degrees'


class PortfolioModel(models.Model):
    image = models.ImageField(upload_to=portfolio_image_path, verbose_name='Image')
    title = models.CharField(max_length=255, verbose_name='Title')
    techs = models.CharField(max_length=255, verbose_name='Technologies')
    description = models.TextField(verbose_name='Description')
    created = models.DateField(verbose_name='Created')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'


class ContactModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    email_address = models.EmailField(max_length=255, verbose_name='E-mail')
    message = models.TextField(verbose_name='Message')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    is_read = models.BooleanField(default=False, verbose_name='Is Read?')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'