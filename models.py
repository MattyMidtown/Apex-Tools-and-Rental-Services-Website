# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    accountid = models.CharField(db_column='AccountID', primary_key=True, max_length=20)  # Field name made lowercase.
    businesstype = models.CharField(db_column='BusinessType', max_length=15)  # Field name made lowercase.
    emailaddressid = models.ForeignKey('Accountaddress', models.DO_NOTHING, db_column='EmailAddressID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'


class Accountaddress(models.Model):
    emailaddressid = models.CharField(db_column='EmailAddressID', primary_key=True, max_length=10)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=25)  # Field name made lowercase.
    passwordid = models.ForeignKey('Password', models.DO_NOTHING, db_column='PasswordID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accountaddress'


class Accountpaymentinforel(models.Model):
    accountpaymentinforelid = models.CharField(db_column='AccountPaymentInfoRelID', primary_key=True, max_length=20)  # Field name made lowercase.
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='AccountID')  # Field name made lowercase.
    cardid = models.ForeignKey('Paymentinfo', models.DO_NOTHING, db_column='CardID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accountpaymentinforel'


class Address(models.Model):
    addressid = models.CharField(db_column='AddressID', primary_key=True, max_length=10)  # Field name made lowercase.
    addressline1 = models.CharField(db_column='AddressLine1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='AddressLine2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=25, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    provid = models.ForeignKey('Province', models.DO_NOTHING, db_column='ProvID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Companyentity(models.Model):
    companyentityid = models.CharField(db_column='CompanyEntityID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'companyentity'


class Companyentityaddressrel(models.Model):
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    companyentityid = models.ForeignKey(Companyentity, models.DO_NOTHING, db_column='CompanyEntityID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'companyentityaddressrel'


class Defects(models.Model):
    defectid = models.IntegerField(db_column='DefectID', primary_key=True)  # Field name made lowercase.
    retrivalid = models.ForeignKey('Retrieval', models.DO_NOTHING, db_column='RetrivalID')  # Field name made lowercase.
    order_productrelid = models.ForeignKey('OrderProductrel', models.DO_NOTHING, db_column='Order_ProductRelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'defects'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', primary_key=True, max_length=10)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=30)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Store', models.DO_NOTHING, db_column='StoreID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Invoice(models.Model):
    invoiceid = models.CharField(db_column='InvoiceID', primary_key=True, max_length=10)  # Field name made lowercase.
    dategenerated = models.DateField(db_column='DateGenerated', blank=True, null=True)  # Field name made lowercase.
    paymentdue = models.DateField(db_column='PaymentDue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice'


class OrderProductrel(models.Model):
    order_productrelid = models.CharField(db_column='Order_ProductRelID', primary_key=True, max_length=10)  # Field name made lowercase.
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    productserialnumber = models.ForeignKey('Productinventory', models.DO_NOTHING, db_column='ProductSerialNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_productrel'

class Orderproduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user', on_delete=models.CASCADE)
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    ordered = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'orderproduct'

class Orders(models.Model):
    orderid = models.CharField(db_column='OrderID', primary_key=True, max_length=15)  # Field name made lowercase.
    invoiceid = models.ForeignKey('Invoice', models.DO_NOTHING, db_column='InvoiceID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    orderrecieveddate = models.DateField(db_column='OrderRecievedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    statusdatechanged = models.DateField(db_column='StatusDateChanged', blank=True, null=True)  # Field name made lowercase.
    accountid = models.ForeignKey('Account', models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    referenceorderid = models.CharField(db_column='ReferenceOrderID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('Userprofile', models.DO_NOTHING, db_column='user', blank=True, null=True)
    ordered = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'



class Password(models.Model):
    passwordid = models.CharField(db_column='PasswordID', primary_key=True, max_length=5)  # Field name made lowercase.
    currentpassword = models.CharField(db_column='CurrentPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datechanged = models.DateField(db_column='DateChanged', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'password'


class Payment(models.Model):
    paymentid = models.CharField(db_column='PaymentID', primary_key=True, max_length=10)  # Field name made lowercase.
    invoiceid = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='InvoiceID', blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='PaymentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Paymentinfo(models.Model):
    cardid = models.CharField(db_column='CardID', primary_key=True, max_length=20)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentinfo'


class Penalties(models.Model):
    penaltyid = models.CharField(db_column='PenaltyID', primary_key=True, max_length=10)  # Field name made lowercase.
    penaltytypename = models.CharField(db_column='PenaltyTypeName', max_length=20)  # Field name made lowercase.
    penaltyfee = models.CharField(db_column='PenaltyFee', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'penalties'


class Penaltyorderrel(models.Model):
    penaltyorderid = models.CharField(db_column='PenaltyOrderID', primary_key=True, max_length=50)  # Field name made lowercase.
    orderid = models.ForeignKey(Orders, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    penaltyid = models.ForeignKey(Penalties, models.DO_NOTHING, db_column='PenaltyID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'penaltyorderrel'


class Person(models.Model):
    personid = models.CharField(db_column='PersonID', primary_key=True, max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    companyentityid = models.ForeignKey(Companyentity, models.DO_NOTHING, db_column='CompanyEntityID', blank=True, null=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Roletype', models.DO_NOTHING, db_column='RoleID', blank=True, null=True)  # Field name made lowercase.
    projectmanagerid = models.CharField(db_column='ProjectManagerID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person'


class Phonenumber(models.Model):
    phonenumber = models.CharField(db_column='PhoneNumber', primary_key=True, max_length=20)  # Field name made lowercase.
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)  # Field name made lowercase.
    phonetype = models.CharField(db_column='PhoneType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phonenumber'


class Product(models.Model):
    productid = models.CharField(db_column='ProductID', primary_key=True, max_length=30)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcategoryid = models.ForeignKey('Subproductcategory', models.DO_NOTHING, db_column='SubCategoryID', blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weightmeasurecode = models.CharField(db_column='WeightMeasureCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rentalcost = models.CharField(db_column='RentalCost', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hexcolour = models.CharField(db_column='HexColour', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    dateremoved = models.DateField(db_column='DateRemoved', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    product_img = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'product'


class Productcategory(models.Model):
    productcategoryid = models.CharField(db_column='ProductCategoryID', primary_key=True, max_length=5)  # Field name made lowercase.
    productcategoryname = models.CharField(db_column='ProductCategoryName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datemodified = models.DateField(db_column='DateModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productcategory'


class Productinventory(models.Model):
    productserialnumber = models.CharField(db_column='ProductSerialNumber', primary_key=True, max_length=15)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    shelf = models.CharField(db_column='Shelf', max_length=10, blank=True, null=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Store', models.DO_NOTHING, db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    rentalstartdate = models.DateField(db_column='RentalStartDate', blank=True, null=True)  # Field name made lowercase.
    rentalenddate = models.DateField(db_column='RentalendDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productinventory'


class Province(models.Model):
    provid = models.CharField(db_column='ProvID', primary_key=True, max_length=10)  # Field name made lowercase.
    provname = models.CharField(db_column='ProvName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'province'


class Refunds(models.Model):
    refundid = models.CharField(db_column='RefundID', primary_key=True, max_length=5)  # Field name made lowercase.
    retrivalid = models.ForeignKey('Retrieval', models.DO_NOTHING, db_column='RetrivalID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'refunds'


class Retrieval(models.Model):
    retrivalid = models.CharField(db_column='RetrivalID', primary_key=True, max_length=15)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Orders, models.DO_NOTHING, db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    retrivaltype = models.CharField(db_column='RetrivalType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dateretrived = models.DateField(db_column='DateRetrived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'retrieval'


class Roletype(models.Model):
    roleid = models.CharField(db_column='RoleID', primary_key=True, max_length=5)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roletype'


class Sheet1(models.Model):
    number_4153114855 = models.FloatField(db_column='4153114855', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_6426851 = models.FloatField(db_column='6426851', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1249214106 = models.FloatField(db_column='1249214106', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    product_returned = models.CharField(db_column='Product Returned', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_42897 = models.DateTimeField(db_column='42897', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'sheet1$'


class Shipment(models.Model):
    shipmentid = models.CharField(db_column='ShipmentID', primary_key=True, max_length=50)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmployeeID')  # Field name made lowercase.
    orderid = models.ForeignKey(Orders, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    shippingdate = models.DateField(db_column='ShippingDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment'


class Store(models.Model):
    storeid = models.CharField(db_column='StoreID', primary_key=True, max_length=2)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'


class Subproductcategory(models.Model):
    subproductcategoryid = models.CharField(db_column='SubProductCategoryID', primary_key=True, max_length=50)  # Field name made lowercase.
    productcategoryid = models.ForeignKey(Productcategory, models.DO_NOTHING, db_column='ProductCategoryID')  # Field name made lowercase.
    subproductcategoryname = models.CharField(db_column='SubProductCategoryName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datemodified = models.DateField(db_column='DateModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subproductcategory'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=160)
    principal_id = models.IntegerField()
    diagram_id = models.IntegerField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Userprofile(models.Model):
    user = models.CharField(primary_key=True, max_length=20)
    accountid = models.ForeignKey('Account', models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    oneclickbuy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userprofile'