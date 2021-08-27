from django.db import models

# Create your models here.
global langht
langht = 255
class Admin(models.Model):
    role = models.CharField(max_length=langht,default="role")
    fotp = models.IntegerField(default=123456)
    email = models.EmailField(unique=True,default="email")
    password = models.CharField(max_length=langht,default="password")
    address = models.CharField(max_length=langht,default="addres")
    Is_created = models.DateField(auto_now_add=True)
    Is_activated = models.BooleanField(default=False)

    def __str__(self):
        return self.role

class Hr(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    fname = models.CharField(max_length=langht,default="firsname")
    lname = models.CharField(max_length=langht,default="lastname")
    address = models.CharField(max_length=langht,default="addres")
    bdate = models.DateField(null=True)
    phone = models.BigIntegerField(default=1234567890)
    gender = models.CharField(max_length=langht,default="gender")
    active = models.CharField(max_length=20,default="Active")


    def __str__(self):
        return self.fname

class emp(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    fname = models.CharField(max_length=langht,default="firsname")
    lname = models.CharField(max_length=langht,default="lastname")
    address = models.CharField(max_length=langht,default="addres")
    bdate = models.DateField(null=True)
    phone = models.BigIntegerField(default=123456)
    gender = models.CharField(max_length=langht,default="gender")
    active = models.CharField(max_length=20,default="Active")

    def __str__(self):
        return self.fname

class shifte_request(models.Model):
    hr = models.ForeignKey(Hr, on_delete= models.CASCADE, null=True)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    reason = models.CharField(max_length=255,default='reason')
    status = models.CharField(max_length=255,default="pending")


class leave_request(models.Model):
    hr = models.ForeignKey(Hr, on_delete= models.CASCADE, null=True)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    reason = models.CharField(max_length=255,default="reason")
    status = models.CharField(max_length=255,default="pending")

    # def __str__(self):
    #     return self.hr

class Attendance_request(models.Model):
    hr = models.ForeignKey(Hr, on_delete= models.CASCADE, null=True)
    Date = models.DateField()
    time = models.TimeField(auto_now=True)
    reason = models.CharField(max_length=255,default="reason")
    status = models.CharField(max_length=255,default="pending")

    # def __str__(self):
    #     return self.hr

class expense_req(models.Model):
    hr = models.ForeignKey(Hr, on_delete= models.CASCADE, null=True)
    Date = models.DateField()
    time = models.TimeField(auto_now=True)
    Prove = models.FileField(upload_to='img/',default='.jpg')
    Payment = models.IntegerField(default=22)
    status = models.CharField(max_length=255,default="pending")

class emp_shift_req(models.Model):
    employee = models.ForeignKey(emp, on_delete= models.CASCADE, null=True)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    reason = models.CharField(max_length=255,default='reason')
    status = models.CharField(max_length=255,default="pending")

class emp_leave_req(models.Model):
    employee = models.ForeignKey(emp, on_delete= models.CASCADE, null=True)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    reason = models.CharField(max_length=255,default="reason")
    status = models.CharField(max_length=255,default="pending")

class emp_attendance_req(models.Model):
    employee = models.ForeignKey(emp, on_delete= models.CASCADE, null=True)
    fromdate = models.DateField()
    time = models.TimeField(auto_now=True)
    reason = models.CharField(max_length=255,default="reason")
    status = models.CharField(max_length=255,default="pending")

class emp_expense_req(models.Model):
    employee = models.ForeignKey(emp, on_delete= models.CASCADE, null=True)
    Date = models.DateField()
    time = models.TimeField(auto_now=True)
    Prove = models.FileField(upload_to='img/',default='.jpg')
    Payment = models.IntegerField(default=22)
    status = models.CharField(max_length=255,default="pending")

class bank_detail(models.Model):
    employee = models.ForeignKey(emp, on_delete=models.CASCADE)
    ac_holder = models.CharField(max_length=255,default="accountholder")
    bank_name = models.CharField(max_length=255,default="bank_name")
    ac_number = models.BigIntegerField(default=133422525)
    ifsc = models.CharField(max_length=255,default="sbin0124025")
    phone = models.BigIntegerField(default=123456)

class bank_detail_hr(models.Model):
    hr = models.ForeignKey(Hr, on_delete=models.CASCADE)
    ac_holder = models.CharField(max_length=255,default="accountholder")
    bank_name = models.CharField(max_length=255,default="bank_name")
    ac_number = models.BigIntegerField(default=1334)
    ifsc = models.CharField(max_length=255,default="sbin0124025")
    phone = models.BigIntegerField(default=123456)