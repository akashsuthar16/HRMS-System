from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Admin)
admin.site.register(Hr)
admin.site.register(emp)
admin.site.register(leave_request)
admin.site.register(Attendance_request)
admin.site.register(shifte_request)
admin.site.register(expense_req)
admin.site.register(emp_shift_req)
admin.site.register(emp_leave_req)
admin.site.register(emp_attendance_req)
admin.site.register(emp_expense_req)
admin.site.register(bank_detail)
admin.site.register(bank_detail_hr)