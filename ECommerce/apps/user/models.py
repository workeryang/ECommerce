from django.db import models


class UserInfo(models.Model):

    username = models.CharField(max_length=24)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11, null=True)
    is_super = models.IntegerField(default=0)  # 0 or 1
    email = models.CharField(max_length=50, null=True, blank=True)
    state = models.SmallIntegerField(default=1)  # 0 ro 1
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {'id': self.id, 'username': self.username, 
        'password': self.password, 'mobile': self.mobile, 'is_super': self.is_super,
        'email': self.email, 'state': self.state, 'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
        'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_info'

    def get_role_Name(self):

        print(self.users)


class Role(models.Model):

    role_name = models.CharField(max_length=24)
    level = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    user_info = models.ManyToManyField(to='UserInfo', related_name='users')

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'role'

