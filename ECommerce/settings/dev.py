DEBUG = True
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

REST_FRAMEWORK = {
    # 使用 Django 的标准 `django.contrib.auth` 权限，
    # 或允许未经身份验证的用户进行只读访问。
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}