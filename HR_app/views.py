from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import razorpay

# Create your views here.
def paymentpage(request):
    if 'aid' in request.session or 'id' in request.session:
        if request.session['role'] == 'Admin':
            return render(request,"HR_app/payment.html")
        elif request.session['role'] == 'Hr':
            return render(request,"HR_app/payment.html")
    else:
        return redirect('login')    

def loginpage(request):
    return render(request, "HR_app/pages-login.html")

def locks(request):
    if 'aid' in request.session or 'id' in request.session:
        return render(request,"HR_app/Lock.html")
    else:
        return redirect('login')

def newhr(request):
    if 'aid' in request.session:
        return render(request,"HR_app/hr-ragister.html")
    else:
        return redirect('login')

def empl(request):
    if 'id' in request.session:
        return render(request, "HR_app/employee.html")
    else:
        return redirect('login')

def forgot(request):
    return render(request, "HR_app/pages-forgot.html")

def newpaswd(request):
    return render(request, "HR_app/newpassword.html")

def hr_leave(request):
    if 'id' in request.session:
        return render(request, "HR_app/leave.html")
    else:
        return redirect('login')

def hr_shifte(request):
    if 'id' in request.session:
        return render(request,"HR_app/shifte.html")
    else:
        return redirect('login')

def hr_attendance(request):
    if 'id' in request.session:
        return render(request,"HR_app/attendance.html")
    else:
        return redirect('login')

def hr_expense(request):
    if 'id' in request.session:
        return render(request,"HR_app/expense.html")
    else:
        return redirect('login')

def emp_shift(request):
    if 'id' in request.session:
        return render(request,"HR_app/emp-shifte.html")
    else:
        return redirect('login')

def emp_leave(request):
    if 'id' in request.session:
        return render(request, "HR_app/emp-leave.html")
    else:
        return redirect('login')

def emp_attendance(request):
    if 'id' in request.session:
        return render(request,"HR_app/emp-attendance.html")
    else:
        return redirect('login')

def emp_expense(request):
    if 'id' in request.session:
        return render(request,"HR_app/emp-expense.html")
    else:
        return redirect('login')
    

        
def logout(request):
    try:
        if request.session['role'] == "Admin":
            del request.session['aid']
            del request.session['aemail']
        elif request.session['role'] == "Hr":
            del request.session['id']
            del request.session['email']
            del request.session['fname']
        elif request.session['role'] == "EMPLOYEE":
            del request.session['id']
            del request.session['email']
            del request.session['fname']
        return render(request, "HR_app/pages-login.html")
    except:
        return render(request, "HR_app/pages-login.html")

def indexpage(request):
    if 'email' in request.session or 'aemail'in request.session:
        if request.session['role'] == "Admin":
            admin = Admin.objects.get(id=request.session['aid'])
            si = shifte_request.objects.all()
            s = si.count()
            la = leave_request.objects.all()
            l = la.count()
            ate = Attendance_request.objects.all()
            at = ate.count()
            ep = expense_req.objects.all()
            e = ep.count()
            hrm = Hr.objects.all()
            hr = hrm.count()
            fb = bank_detail_hr.objects.all()
            f = fb.count()
            return render(request,"HR_app/index.html",{'user':admin,'s':s,'l':l,'at':at,'e':e,'hr':hr,'f':f})
        elif request.session['role'] == "Hr":
            admin = Admin.objects.get(id=request.session['id'])
            hr = Hr.objects.get(admin=admin)
            ak = emp_shift_req.objects.all()
            a = ak.count()
            bk = emp_leave_req.objects.all()
            b = bk.count()
            ck = emp_attendance_req.objects.all()
            c = ck.count()
            dk = emp_expense_req.objects.all()
            d = dk.count()
            ek = emp.objects.all()
            e = ek.count()
            fk = bank_detail.objects.all()
            f = fk.count()
            return render(request,"HR_app/index.html",{'user':hr,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f})
        elif request.session['role'] == "EMPLOYEE":
            admin = Admin.objects.get(id=request.session['id'])
            Emp = emp.objects.get(admin=admin)
            ak = emp_shift_req.objects.all()
            a = ak.count()
            bk = emp_leave_req.objects.all()
            b = bk.count()
            ck = emp_attendance_req.objects.all()
            c = ck.count()
            dk = emp_expense_req.objects.all()
            d = dk.count()
            return render(request,"HR_app/index.html",{'user':emp,'a':a,'b':b,'c':c,'d':d})
    else:
        return redirect('/')

from random import randint
def Send_OTP(request):
    if request.method == 'POST':
        em = request.POST['email']

        user = Admin.objects.filter(email=em)
        if len(user) > 0:
            did = Admin.objects.get(email=em)
            subject = 'Adminto Forgot Password'
            otp = ''
            for i in range (6):
                otp+=str(randint(1,9))
            did.fotp = otp
            did.save()
            message = f'Hi, {em}.\nThank you for Contact to Adminto. \nYour OTP is {otp}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [em, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request, "HR_app/newpassword.html",{'em':em})
        else:
            msg = "Email is Incorrect..!"
            return render(request, "HR_app/pages-forgot.html",{'err':msg})
    else:
        msg = "GET METHOD CALLED!"
        return render(request, "HR_app/pages-forgot.html",{'err':msg})   

def verifyotp_pws(request):
    if request.method == 'POST':
        em = request.POST['email']
        otp = int(request.POST['f_otp'])
        new = request.POST['newpws']
        did = Admin.objects.get(email=em)
        
        if did.fotp == otp:
            did.password = new
            did.save()
            return render(request, "HR_app/newpassword.html")
        else:
            msg="Incorrect OTP! Please Enter Again."
            return render(request, "HR_app/newpassword.html",{'err': msg})    

def lockscreen(request):
    if request.method == 'POST':
        ps = request.POST['psw']
        if request.session['role'] == 'Hr':
            lo = Admin.objects.get(id=request.session['id'])
            if lo.password == ps:
                return redirect('index')
            else: 
                del request.session['id']
                del request.session['email']
                del request.session['role']   
                del request.session['fname']
                return redirect('login')
        elif request.session['role'] == 'EMPLOYEE':
            empl = Admin.objects.get(id=request.session['id'])
            if empl.password == ps:
                return redirect('index')
            else: 
                del request.session['id']
                del request.session['email']
                del request.session['role']   
                del request.session['fname']
                return redirect('login')
        elif request.session['role'] == 'Admin':
            ad = Admin.objects.get(id=request.session['aid'])
            if ad.password == ps:
                return redirect('index')
            else: 
                del request.session['aid']
                del request.session['aemail']
                del request.session['role']   
                return redirect('login')
        return redirect('login')
    return redirect('lock-screen')

def login(request):
    try:
        if request.method == "POST":
            role = request.POST['role']
            em = request.POST['email']
            psswd = request.POST['pws']
            admin = Admin.objects.filter(email=em)
            if len(admin) > 0:
                if admin[0].password == psswd:
                    if admin[0].role == "Admin":
                        print("IN ADMIN")
                        request.session['aid'] = admin[0].id
                        request.session['aemail'] = admin[0].email
                        request.session['role'] = admin[0].role
                        return redirect("index")
                    elif admin[0].role == "Hr":
                        hr = Hr.objects.get(admin=admin[0])
                        request.session['id'] = admin[0].id
                        request.session['email'] = admin[0].email
                        request.session['role'] = admin[0].role
                        request.session['fname'] = hr.fname
                        return redirect("index")
                    elif admin[0].role == "EMPLOYEE":
                        # if active == "Active":
                        Emp = emp.objects.get(admin=admin[0])
                        request.session['id'] = admin[0].id
                        request.session['email'] = admin[0].email
                        request.session['role'] = admin[0].role
                        request.session['fname'] = Emp.fname
                        return redirect("index")
                        # else:
                        #     msg="Empolyee's ID Not Active"
                        #     return render(request, "HR_app/pages-login.html",{'err': msg})
                else:
                    msg="Password was incorrect!!"
                    return render(request, "HR_app/pages-login.html",{'err': msg})
            else:
                msg = "User not found"
                return render(request,"HR_app/pages-login.html",{'err': msg}) 
        else:
            return render(request,"HR_app/pages-login.html")
    except:
        return render(request,"HR_app/pages-login.html")

def registerhr_emp(request):
    if 'aid' in request.session or 'id' in request.session:
        role = request.POST['role']
        fn = request.POST['Fname']
        ln = request.POST['Lname']
        ph = request.POST['Phone']
        bir = request.POST['Bday']
        gn = request.POST['Gender']
        em = request.POST['Email']
        pwr = request.POST['Pwss']
        adrs = request.POST['addr']
        ac = request.POST['yes']
        

        user = Admin.objects.filter(email=em)
        if len(user) > 0:
            if role == 'Hr':
                msg = "User already Exitst"
                return render(request, "HR_app/hr-ragister.html",{'err':msg})
            elif role == 'EMPLOYEE':
                msg = "User already Exitst"
                return render(request, "HR_app/employee.html",{'err':msg})
            else:
                pass
        else:
            admin = Admin(email=em,password=pwr,role=role)
            admin.save()
            if admin.role == "Hr":
                hr= Hr.objects.create(admin=admin,fname=fn,lname=ln,phone=ph,bdate=bir,gender=gn,address=adrs,active=ac)
                msg = "HR Add successfully"
                return render(request, "HR_app/hr-ragister.html",{'err':msg})    
            elif admin.role == "EMPLOYEE":
                Emp = emp.objects.create(admin=admin,fname=fn,lname=ln,phone=ph,bdate=bir,gender=gn,address=adrs,active=ac)
                msg = "Employee Add Successfully"
                return render(request, "HR_app/employee.html",{'err':msg})
    else:
        return redirect('login')

def profile(request):
    if 'id' in request.session or 'id'in request.session:                            
        admin=Admin.objects.get(email=request.session['email'])
        if admin.role == 'Hr':
            hr=Hr.objects.get(admin=admin.id)
            return render(request, "HR_app/profile.html",{'hr':hr,'admin':admin})
        elif admin.role == 'EMPLOYEE':
            emps=emp.objects.get(admin=admin.id)
            return render(request, "HR_app/profile.html",{'emps':emps,'admin':admin})
    else:
        pass

def emp_profile(request):
    try:
        if request.method == 'POST':
            if 'id' in request.session:
                eadmin = Admin.objects.get(id=request.session['id'])
                eupd = emp.objects.get(admin=eadmin)

                eupd.fname = request.POST['Fname'] if request.POST['Fname'] else eupd.fname
                eupd.lname = request.POST['Lname'] if request.POST['Lname'] else eupd.lname
                eupd.address = request.POST['addr'] if request.POST['addr'] else eupd.address
                eupd.phone = request.POST['Phone'] if request.POST['Phone'] else eupd.phone
                eupd.gender = request.POST['gender'] if request.POST['gender'] else eupd.gender
                eupd.save()
                return redirect('Profile')
        else:
            pass
    except:
        return render(request, "HR_app/profile.html")

def hr_profile(request):
    try:
        if request.method == 'POST':
            if 'id' in request.session:
                hradmin = Admin.objects.get(id=request.session['id'])
                hrupd = Hr.objects.get(admin=hradmin)

                hrupd.fname = request.POST['Fname'] if request.POST['Fname'] else hrupd.fname
                hrupd.lname = request.POST['Lname'] if request.POST['Lname'] else hrupd.lname
                hrupd.address = request.POST['addr'] if request.POST['addr'] else hrupd.address
                hrupd.phone = request.POST['Phone'] if request.POST['Phone'] else hrupd.phone
                hrupd.gender = request.POST['gender'] if request.POST['gender'] else hrupd.gender
                hrupd.save()
                return redirect('Profile')
        else:
            pass  
    except:
        return render(request, "HR_app/profile.html")

def shiftreq(request):
    if 'id' in request.session:
        fromda = request.POST['fromd']
        toda = request.POST['tod']
        rsn = request.POST['res']

        getadmin = Admin.objects.get(id=request.session['id'])
        gethr = Hr.objects.get(admin=getadmin)
        req_shift = shifte_request.objects.create(
            hr = gethr,
            fromdate = fromda,
            todate = toda,
            reason = rsn,
        )
        return redirect('hr-shifte-request')
    else:
        return redirect('index')

def leavereq(request):
    if 'id' in request.session:
        fromd = request.POST['fdate']
        tod = request.POST['tdate']
        rsn = request.POST['reslev']

        getadmin = Admin.objects.get(id=request.session['id'])
        gethr = Hr.objects.get(admin=getadmin)
        req_leave = leave_request.objects.create(
            hr = gethr,
            fromdate = fromd,
            todate = tod,
            reason = rsn,
        )
        return redirect('hr-leave-request')
    else:
        return redirect('index')

def attendancereq(request):
    if 'id' in request.session:
        dateing = request.POST['adate']
        time = request.POST['atime']
        rsn = request.POST['areason']

        getadmin = Admin.objects.get(id=request.session['id'])
        gethr = Hr.objects.get(admin=getadmin)
        req_attendance = Attendance_request.objects.create(
            hr = gethr,
            Date = dateing,
            time= time,
            reason = rsn,
        )
        return redirect('hr_attendance-request')
    else:
        return redirect('index')

def expensereq(request):
    if 'id' in request.session:
        exdate = request.POST['edate']
        extime = request.POST['etime']
        exprove = request.FILES['prv']
        expay = request.POST['pay']

        getadmin = Admin.objects.get(id=request.session['id'])
        gethr = Hr.objects.get(admin=getadmin)
        req_expens = expense_req.objects.create(
            hr = gethr,
            Date = exdate,
            time = extime,
            Prove = exprove,
            Payment = expay,
        )
        return redirect('hr-expense-request')
    else:
        return redirect('index')

def empshifte(request):
    if 'id' in request.session:
        emfromd = request.POST['fromd']
        emtod = request.POST['tod']
        emrsn = request.POST['res']

        getadmin = Admin.objects.get(id=request.session['id'])
        getemp = emp.objects.get(admin=getadmin)
        emp_shifte = emp_shift_req.objects.create(
            employee = getemp,
            fromdate = emfromd,
            todate = emtod,
            reason = emrsn,
        )
        return redirect('emp-shifte-request')
    else:
        return redirect('index')

def empleave(request):
    if 'id' in request.session:
        emfromd = request.POST['fdate']
        emtod = request.POST['tdate']
        emrsn = request.POST['reslev'] 

        getadmin = Admin.objects.get(id=request.session['id'])
        getemp = emp.objects.get(admin=getadmin)
        emp_leave = emp_leave_req.objects.create(
            employee = getemp,
            fromdate = emfromd,
            todate = emtod,
            reason = emrsn,
        )
        return redirect('emp-leave-request')
    else:
        return redirect('index')

def empattendance(request):
    if 'id' in request.session:
        emdate = request.POST['adate']
        emtime = request.POST['atime']
        emrsn = request.POST['areason']

        getadmin = Admin.objects.get(id=request.session['id'])
        getemp = emp.objects.get(admin=getadmin)
        emp_attendance = emp_attendance_req.objects.create(
            employee= getemp,
            fromdate = emdate,
            time= emtime,
            reason = emrsn,
        )
        return redirect('emp-attendance-request')
    else:
        return redirect('index')

def empexpense(request):
    if 'id' in request.session:
        exdate = request.POST['edate']
        extime = request.POST['etime']
        exprove = request.FILES['prv']
        expay = request.POST['pay']

        getadmin = Admin.objects.get(id=request.session['id'])
        getemp = emp.objects.get(admin=getadmin)
        emp_expens = emp_expense_req.objects.create(
            employee = getemp,
            Date = exdate,
            time = extime,
            Prove = exprove,
            Payment = expay,
        )
        return redirect('emp-expense-request')
    else:
        return redirect('index')

# employee table
def table_shifte(request):
    if 'id' in request.session:
        em = emp_shift_req.objects.all()
        return render(request, "HR_app/table-shifte.html",{'em':em})
    else:
        return redirect('login')

def table_leave(request):
    if 'id' in request.session:
        le = emp_leave_req.objects.all()
        return render(request,"HR_app/table-leave.html",{'le':le})
    else:
        return redirect('login')

def table_attendance(request):
    if 'id' in request.session:
        at = emp_attendance_req.objects.all()
        return render(request,"HR_app/table-attendance.html",{'at':at})
    else:
        return redirect('login')

def table_expense(request):
    if 'id' in request.session:
        ex = emp_expense_req.objects.all()
        return render(request,"HR_app/table-expense.html",{'ex':ex})
    else:
        return redirect('login')

def emp_bank(request):
    if 'id' in request.session:
        admin = Admin.objects.get(email=request.session['email'])
        return render(request,"HR_app/banklog.html",{'admin':admin})
    else:
        return redirect('login')
        
def emp_bank_detail(request):
    if 'id' in request.session:
        if request.method == 'POST':
            ahn = request.POST['an']
            bn = request.POST['bankname']
            cod = request.POST['ifsc']
            an = request.POST['ac']
            pn = request.POST['Phone']
            
            admin = Admin.objects.get(email=request.session['email'])
            empl = emp.objects.get(admin=admin)
            bd = bank_detail.objects.create(
                employee = empl,
                ac_holder = ahn,
                bank_name = bn,
                ac_number = an,
                ifsc = cod,
                phone = pn,
            )
            msg = "Employee Bank Details Succesfull..."
            return render(request,"HR_app/banklog.html",{'msg':msg})
        else:
            msg = "Not Found..."
            return render(request,"HR_app/index.html",{'msg':msg})
    else:
        return redirect('login')


# hr tables
def emp_table_shifte(request):
    if 'id' in request.session:
        getem = emp_shift_req.objects.all()
        return render(request, "HR_app/emp-tables-shifte.html",{'getem':getem})
    else:
        return redirect('login')

def emp_table_leave(request):
    if 'id' in request.session:    
        getle = emp_leave_req.objects.all()
        return render(request, "HR_app/emp-table-leave.html",{'getle':getle})
    else:
        return redirect('login')

def emp_table_attendance(request):
    if 'id' in request.session:
        getat = emp_attendance_req.objects.all()
        return render(request, "HR_app/emp-table-attendance.html",{'getat':getat})
    else:
        return redirect('login')

def emp_table_expense(request):
    if 'id' in request.session:
        getex = emp_expense_req.objects.all()
        return render(request, "HR_app/emp-table-expense.html",{'getex':getex})
    else:
        return redirect('login')

def emp_detail(request):
    if 'id' in request.session:
        getemp = emp.objects.all()
        return render(request,"HR_app/emp-register-table.html",{'getemp':getemp})
    else:
        return redirect('login')

def hr_shiftereq(request):
    if 'id' in request.session:
        em = shifte_request.objects.all()
        return render(request, "HR_app/hr-shifterequeste.html",{'em':em})
    else:
        return redirect('login')

def hr_leavereq(request):
    if 'id' in request.session:
        le = leave_request.objects.all()
        return render(request, "HR_app/hr-leaverequest.html",{'le':le})
    else:
        return redirect('login')

def hr_attendancereq(request):
    if 'id' in request.session:
        at = Attendance_request.objects.all()
        return render(request, "HR_app/hr-attendancerequest.html",{'at':at})
    else:
        return redirect('login')

def hr_expensereq(request):
    if 'id' in request.session:
        ex = expense_req.objects.all()
        return render(request, "HR_app/hr-expenserequest.html",{'ex':ex})
    else:
        return redirect('login')

def hr_bank_detail(request):
    if 'id' in request.session:
        if request.method == 'POST':
            ahn = request.POST['an']
            bn = request.POST['bankname']
            cod = request.POST['ifsc']
            an = request.POST['ac']
            pn = request.POST['Phone']
            
            admin = Admin.objects.get(email=request.session['email'])
            hr = Hr.objects.get(admin=admin)
            ab = bank_detail_hr.objects.create(
                hr = hr,
                ac_holder = ahn,
                bank_name = bn,
                ac_number = an,
                ifsc = cod,
                phone = pn,
            )
            msg = "HR Bank Details Succesfull..."
            return render(request,"HR_app/banklog.html",{'msg':msg})
        else:
            msg = "Not Found..."
            return render(request,"HR_app/index.html",{'msg':msg})
    else:
        return redirect('login')


def emp_bank_table(request):
    if 'id' in request.session:
        getbank = bank_detail.objects.all()
        return render(request,"HR_app/bank-table.html",{'getbank':getbank})
    else:
        return redirect('login')

# Admin table
def hr_table_shifte(request):
    if 'aid' in request.session:
        sf = shifte_request.objects.all()
        return render(request, "HR_app/hr-table-shifte.html",{'sf':sf})
    else:
        return redirect('login')

def hr_table_leave(request):
    if 'aid' in request.session:
        le = leave_request.objects.all()
        return render(request, "HR_app/hr-table-leave.html",{'le':le})
    else:
        return redirect('login')
        
def hr_table_attendance(request):
    if 'aid' in request.session:
        at = Attendance_request.objects.all()
        return render(request, "HR_app/hr-table-attendance.html",{'at':at})
    else:
        return redirect('login')

def hr_table_expense(request):
    if 'aid' in request.session:
        ex = expense_req.objects.all()
        return render(request, "HR_app/hr-table-expense.html",{'ex':ex})
    else:
        return redirect('login')
        
def hr_detail(request):
    if 'aid' in request.session:
        gethr = Hr.objects.all()
        return render(request,"HR_app/hr-register-table.html",{'gethr':gethr})
    else:
        return redirect('login')

def hr_bank(request):
    if 'aid' in request.session:
        getb = bank_detail_hr.objects.all()
        return render(request,"HR_app/hr-bank-table.html",{'getb':getb})
    else:
        return redirect('login')

def pay(request):
    if request.method == "POST":
        name = int(request.POST['amt'])
        amount = name*100
        request.session['amt'] = amount

        client = razorpay.Client(
            auth=("rzp_test_c9INlCRgs3if3b", "8r6iq01czeOKi57nlfPKmLND"))

        payme = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
        
        return render(request, 'HR_app/payment.html')
    else:
        mag : "Error"
        return render(request, 'HR_app/hr-table-expense.html',{'err':mag})

# ADMIN conform HR Detail.

def ChngHrAttenReqStatus(request,st):
    sepidstatus = st.split(",")
    print(sepidstatus)
    reqid = int(sepidstatus[1])
    reqstatus = sepidstatus[0]
    req = Attendance_request.objects.get(id=reqid)
    req.status = reqstatus
    req.save()
    return redirect("hr-table-attendance")

def ChngHrLeaveReqStatus(request,st):
    sepidstatus = st.split(",")
    reqid = int(sepidstatus[1])
    reqstatus = sepidstatus[0]
    req = leave_request.objects.get(id=reqid)
    req.status = reqstatus
    req.save()
    return redirect("hr-table-leave")