DEBUG = True

ALLOWED_HOSTS = ['*']

CUSTOM_EXPRESSION = []

CUSTOM_APPS = [

]
SECRET_KEY = '7%ik!z11=#kzp$sz1)d@mbl+tvh%xvw_7c%ibp1jy6x_p=l0m2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
           'charset': 'utf8mb4',
           'read_default_file': './deeru/my.cnf',
        },
    }
}

DEBUG = False

