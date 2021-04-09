# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FarmerAppCategory(models.Model):
    status = models.BooleanField()
    category_image = models.CharField(max_length=100, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_app_category'


class FarmerAppOrder(models.Model):
    ref_code = models.CharField(max_length=15, blank=True, null=True)
    is_ordered = models.BooleanField()
    date_ordered = models.DateTimeField()
    status = models.IntegerField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_app_order'


class FarmerAppOrderItems(models.Model):
    order = models.ForeignKey(FarmerAppOrder, models.DO_NOTHING)
    orderitem = models.ForeignKey('FarmerAppOrderitem', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'farmer_app_order_items'
        unique_together = (('order', 'orderitem'),)


class FarmerAppOrderitem(models.Model):
    quantity = models.IntegerField()
    is_ordered = models.BooleanField()
    product = models.OneToOneField('FarmerAppProduct', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_app_orderitem'


class FarmerAppProduct(models.Model):
    name_tr = models.CharField(max_length=250, blank=True, null=True)
    name_en = models.CharField(max_length=250, blank=True, null=True)
    status = models.BooleanField()
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    photo = models.CharField(max_length=1000, blank=True, null=True)
    category = models.ForeignKey(FarmerAppCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_app_product'


class Pytab(models.Model):
    id = models.FloatField(blank=True, null=True)
    data = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pytab'


class Test(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
