"""
Django settings for djnago_project project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))






# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0%b7i4-d0@rh2xyn9z7)3lvpj=7kx4o8)vaw1=e(c@lvwg9%3@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'crispy_forms',
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'django.contrib.admindocs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djnago_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  #directory are defined here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djnago_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'



#if multiple users are all saving different kinds of images then they clutter up our project directory with different image directory
#so lets change the setting so that we can change the location  of where the images are saved
#we also ned to change some additional settings so that or website can find these images when we try to view the images from browser
#in the seeting (djangoproject->another djangoproject->setting.py)we need to define something called media route and media url
#we are creating media folder to store the images
#MEDIA_ROOT=os.path.join(BASE_DIR,'media')#full path where we like django to store uploaded files these files are stored in file system and not in the database
#we are using the os.path.join method we will make sure that the full path of directory is created correctly no matter which operating system we r on
# BASE_DIR is the variable that the django created at top of our setting file that specifies the location of project base directory
#so basically it says that MEDIA_ROOT will be in the project base directory and then have a directory in there called media
#MEDIA_ROOT IS the place where uploaded file will be located in the file system,
#so now when we upload a pic it it will create a profile_pics directory(that we mentioned in user->models.py) inside of this Media directory and that media directory will be located at the base directory of our project
#MEDIA_URL='/media/'#is the public url of media directory that we can access through browser also
#media url is basicall /media/profile_pics/nameofimage

#look in the folder media folder will be created inside our base directory
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



'''
below code is to write in django_project->urls.py and is taken from django docs for making the profile pic o get uploaded
https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
Serving files uploaded by a user during development¶
During development, you can serve user-uploaded media files from MEDIA_ROOT using the django.views.static.serve() view.

This is not suitable for production use! For some common deployment strategies, see Deploying static files.

For example, if your MEDIA_URL is defined as /media/, you can do this by adding the following snippet to your urls.py:

This helper function works only in debug mode and only if the given prefix is local (e.g. /media/) and not a URL (e.g. http://media.example.com/).


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
CRISPY_TEMPLATE_PACK = 'bootstrap4' #for using css/styling for crispy form use bootstrap 4
#and if we want to chnage anything else  then we can go to crispy form  documentation online and see the seetings
#so now we our bootstrap is set and we can load it into our template and use it
#so go to the users/register.html where our form lives and at the top   load crispy form template

LOGIN_REDIRECT_URL = 'blog-home' #blog-home is the name of the path that we gave to home page

LOGIN_URL ='login'#login is the name that we gave to the login url pattern add this line bcz if it isnt here django goes to default at accounts/login
