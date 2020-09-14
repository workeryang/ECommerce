from django.db import models


class Right(models.Model):
    """权限"""

    auth_name = models.CharField(max_length=24)
    level = models.IntegerField(default=0, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)

    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.auth_name

    def to_dict(self):
        return {
            'id': self.id,
            'auth_name': self.auth_name,
            'level': self.level,
            'path': self.path,
            'parent': self.parent.auth_name if self.parent else '',
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')
        }

    class Meta:
        db_table = 'right'
