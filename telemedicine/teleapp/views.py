from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pymysql

db=pymysql.connect("localhost","root","","dbtelemedicine")
c=db.cursor()

######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"index.html")
######################################################################
#                           LOGIN
######################################################################
def login(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where username='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="doctor"):
                        return HttpResponseRedirect("/doctorhome")
                    elif(i[2]=="pharmacy"):
                        return HttpResponseRedirect("/pharmacyhome")
                    elif(i[2]=="courier"):
                        return HttpResponseRedirect("/courierhome")
                    elif(i[2]=="patient"):
                        return HttpResponseRedirect("/patienthome")
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"
    return render(request,"commonlogin.html",{"msg":msg})
######################################################################
#                           DOCTOR
######################################################################
def doctor(request):
    """ 
        The function to manage department
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        dept=request.POST["dept"]
        qual=request.POST["txtQual"]
        exp=request.POST["txtExp"]
        dist=request.POST["dist"]
        docid=request.POST["docid"]
        pwd=request.POST["txtPassword"]
        
        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)

        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tbldoctor (dName,dAddress,dContact,dEmail,depId,dImg,dQualification,dExperience,dDistrict,dlic) values('"+name+"','"+address+"','"+contact+"','"+email+"','"+dept+"','"+uploaded_file_url+"','"+qual+"','"+exp+"','"+dist+"','"+docid+"')"
            try:
                c.execute(s)
                db. commit()
            except:
                msg="Sorry some error occured"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+email+"','"+pwd+"','doctor','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    msg="Registration successfull"
    s="select * from tbldepartment where status='1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"doctor.html",{"dept":data,"msg":msg})
######################################################################
#                           PHARMACY
######################################################################
def pharmacy(request):
    """ 
        The function to register pharmacy
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        
        licens=request.POST["txtLicense"]
        
        dist=request.POST["dist"]
        pwd=request.POST["txtPassword"]
        
        
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblpharmacy (phName,phAddress,phContact,phEmail,phDistrict,phLicense) values('"+name+"','"+address+"','"+contact+"','"+email+"','"+dist+"','"+licens+"')"
            try:
                c.execute(s)
                db. commit()
            except:
                msg="Sorry some error occured"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+email+"','"+pwd+"','pharmacy','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    msg="Registration successfull"
    
    return render(request,"pharmacy.html",{"msg":msg})
######################################################################
#                           COURIER
######################################################################
def courier(request):
    """ 
        The function to register courier
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        
        
        
        licence=request.POST["licence"]
        dist=request.POST["dist"]
        pwd=request.POST["txtPassword"]
        
        
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblcourier (cName,cAddress,cContact,cEmail,cDistrict,cLicence) values('"+name+"','"+address+"','"+contact+"','"+email+"','"+dist+"','"+licence+"')"
            try:
                c.execute(s)
                db. commit()
            except:
                msg="Sorry some error occured"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+email+"','"+pwd+"','courier','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    msg="Registration successfull"
    
    return render(request,"courier.html",{"msg":msg})
######################################################################
#                           PATIENT
######################################################################
def patient(request):
    """ 
        The function to register patient
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        dob=request.POST["dob"]
        idp=request.POST["idp"]
        gender=request.POST["gender"]
        pin=request.POST["txtPin"]
        pwd=request.POST["txtPassword"]
        allergy=request.POST["txtAllergy"]
        heriditary=request.POST["txtHeriditary"]
        surgery=request.POST["txtSurgery"]
        admit=request.POST["txtAdmit"]
        history=request.POST["txtHistory"]
        pay=request.POST["pay"]
        cardno=request.POST["cardno"]
        month=request.POST["month"]
        year=request.POST["year"]
        cvv=request.POST["cvv"]
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblpatient (pName,pAddress,pContact,pEmail,pPincode,allergy,heriditary,surgery,admit,history,dob,validid,gender) values('"+name+"','"+address+"','"+contact+"','"+email+"','"+pin+"','"+allergy+"','"+heriditary+"','"+surgery+"','"+admit+"','"+history+"','"+dob+"','"+idp+"','"+gender+"')"
            try:
                c.execute(s)
                db. commit()
            except:
                msg="Sorry some error occured"
            else:
                s="insert into tbllogin (username,password,utype,status) values('"+email+"','"+pwd+"','patient','1')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry login error"
                else:
                    s="insert into tblpayment(username,amount,cardno,month,year,cvv)values('"+email+"','"+pay+"','"+cardno+"','"+month+"','"+year+"','"+cvv+"')"
                    try:
                        c.execute(s)
                        db. commit()
                    except:
                        msg="Sorry some error occured"
                    else:
                        msg="Registration successfull"

    
    return render(request,"patient.html",{"msg":msg})
######################################################################
#                           ADMIN HOME
######################################################################
def adminhome(request):
    """ 
        The function to load admin home page
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"adminhome.html")
######################################################################
#                           ADMIN DEPARTMENT
######################################################################
def admindepartment(request):
    """ 
        The function to manage department
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        dep=request.POST["txtDepartment"]
        s="insert into tbldepartment(deptName,status) values('"+dep+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Data added successfully"
    s="select * from tbldepartment where status='1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"admindepartment.html",{"data":data,"msg":msg})
######################################################################
#                           ADMIN DOCTOR
######################################################################
def admindoctor(request):
    """ 
        The function to load doctor page for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select tbldoctor.*,tbldepartment.deptName from tbldoctor,tbldepartment where tbldoctor.dEmail in(select username from tbllogin where status='0') and tbldepartment.deptId=tbldoctor.depId"
    c.execute(s)
    data=c.fetchall()
    s="select tbldoctor.*,tbldepartment.deptName from tbldoctor,tbldepartment where tbldoctor.dEmail in(select username from tbllogin where status='1') and tbldepartment.deptId=tbldoctor.depId"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"admindoctor.html",{"data":data,"data1":data1})
######################################################################
#                           ADMIN DOCTOR
######################################################################
def adminpharmacy(request):
    """ 
        The function to load doctor page for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblpharmacy where phEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data=c.fetchall()
    s="select * from tblpharmacy where phEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"adminpharmacy.html",{"data":data,"data1":data1})
######################################################################
#                           ADMIN COURIER
######################################################################
def admincourier(request):
    """ 
        The function to load courier page for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblcourier where cEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data=c.fetchall()
    s="select * from tblcourier where cEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"admincourier.html",{"data":data,"data1":data1})
######################################################################
#                           ADMIN APPROVE USER
######################################################################
def adminapproveuser(request):
    """ 
        The function to approve user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.GET.get("id")
    status=request.GET.get("status")
    url=request.GET.get("url")
    s="update tbllogin set status='1' where username='"+str(email)+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect(url)

######################################################################
                    #       Admin Reject doctor
######################################################################

def adminrejectuser(request):
    email=request.GET.get("id")
    status=request.GET.get("status")
    url=request.GET.get("url")
    s="delete from tbllogin where username='"+str(email)+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect(url)

######################################################################
#                           ADMIN PATIENT
######################################################################
def adminpatient(request):
    """ 
        The function to load patients page for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblpatient where pEmail in(select username from tblLogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminpatient.html",{"data":data})
######################################################################
#                           ADMIN MEDICINE
######################################################################
def adminmedicine(request):
    """ 
        The function to manage medicine
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        desc=request.POST["txtDesc"]
        content=request.POST["txtContent"]
        company=request.POST["txtCompany"]
        rate=request.POST["txtRate"]
        s="insert into tblmedicine(medName,medDesc,medContent,medCompany,medRate,medStatus) values('"+name+"','"+desc+"','"+content+"','"+company+"','"+rate+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Data added successfully"
    s="select * from tblmedicine where medStatus='1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminmedicine.html",{"data":data,"msg":msg})
######################################################################
#                           ADMIN REQUEST
######################################################################
def adminrequest(request):
    """ 
        The function to load request for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select tblrequest.*,tblpatient.pName,tbldepartment.deptName from tblrequest,tblpatient,tbldepartment where tblrequest.pEmail=tblpatient.pEmail and tblrequest.depId=tbldepartment.deptId and tblrequest.reqStatus='requested'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminrequest.html",{"data":data})
######################################################################
#                           ADMIN SEARCH DOCTOR
######################################################################
def adminsearchdoctor(request):
    """ 
        The function to search doctor for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    rid=request.GET.get("id")
    request.session["rid"]=rid
    s="select * from tblrequest where reqId='"+rid+"'"
    c.execute(s)
    i=c.fetchone()
    dist=i[5]
    dep=i[2]
    s="select tbldoctor.*,tbldepartment.deptName from tbldoctor,tbldepartment where tbldoctor.dDistrict='"+str(dist)+"' and tbldoctor.depId='"+str(dep)+"' and tbldepartment.deptId=tbldoctor.depId"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminsearchdoctor.html",{"data":data})
######################################################################
#                           ADMIN REQUEST ALLOCATE
######################################################################
def adminrequestallocate(request):
    """ 
        The function to allocate request to doctor
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.GET.get("id")
    rid=request.session["rid"]
    s="insert into tblallocation (reqId,dEmail) values('"+rid+"','"+email+"')"
    c.execute(s)
    db.commit()
    s="update tblrequest set reqStatus='doctor allocated' where reqId='"+rid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminrequest")
######################################################################
#                           PHARMACY HOME
######################################################################
def pharmacyhome(request):
    """ 
        The function to load pharmacy home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        district=request.POST["txtDistrict"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        licens=request.POST["txtLicense"]
        s="update tblpharmacy set phName='"+name+"',phAddress='"+address+"',phContact='"+contact+"',phEmail='"+email+"',phLicense='"+licens+"',phDistrict='"+district+"' where phEmail='"+email+"'"
        try:
            c.execute(s)
            db. commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Registration successfull"
    s="select * from tblpharmacy where phEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    s="select phDistrict from tblpharmacy where phEmail='"+email+"'"
    c.execute(s)
    i=c.fetchone()
    request.session["district"]=i[0]
    return render(request,"pharmacyhome.html",{"data":data})
######################################################################
#                           PHARMACY HOME
######################################################################
def pharmacymedicine(request):
    """ 
        The function to load pharmacy home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        medid=request.POST["medid"]
        stock=request.POST["txtStock"]
        s="select count(*) from tblmedicinestock where medId='"+medid+"' and phEmail='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="update tblmedicinestock set stock='"+stock+"' where medId='"+medid+"' and phEmail='"+email+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Stock updated"
        else:
            s="insert into tblmedicinestock (medId,phEmail,stock) values('"+medid+"','"+email+"','"+stock+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Stock updated"
    s="select tblmedicine.medName,tblmedicinestock.stock from tblmedicine,tblmedicinestock where tblmedicine.medId=tblmedicinestock.medId and tblmedicinestock.phEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    s="select * from tblmedicine where medStatus='1'"
    c.execute(s)
    med=c.fetchall()
    return render(request,"pharmacymedicine.html",{"data":data,"med":med,"msg":msg})
######################################################################
#                         PHARMACY ORDER
######################################################################
def pharmacyorder(request):
    """ 
        The function to load pharmacy orders
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblprescription.presId,tbldoctor.dName from tbldoctor,tblprescription,tblallocation where tblprescription.presId in(select prescId from tblmedicineorder where phEmail='"+email+"' and tblmedicineorder.status='ordered') and  tblprescription.allocId=tblallocation.allocId and tblallocation.dEmail=tbldoctor.dEmail "
    print(s)
    c.execute(s)
    data=c.fetchall()
    return render(request,"pharmacyorder.html",{"data":data})
######################################################################
#                         PHARMACY ALL ORDER
######################################################################
def pharmacyallorder(request):
    """ 
        The function to load  pharmacy order status
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="SELECT `tblpatient`.`pName`,`tblpatient`.`pAddress`,`tblpatient`.`pContact`,`tblmedicineorder`.`status` FROM `tblpatient`,`tblmedicineorder`,`tblprescription`,`tblallocation`,`tblrequest`,`tblpharmacy` WHERE `tblmedicineorder`.`prescId`=`tblprescription`.`presId` AND `tblprescription`.`allocId`=`tblallocation`.`allocId` AND `tblallocation`.`reqId`=`tblrequest`.`reqId` AND `tblrequest`.`pEmail`=`tblpatient`.`pEmail` AND `tblmedicineorder`.`phEmail`=`tblpharmacy`.`phEmail` AND `tblmedicineorder`.`phEmail`='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"pharmacyallorder.html",{"data":data})
######################################################################
#                         PHARMACY ORDER DETAILS
######################################################################
def pharmacyorderdetails(request):
    """ 
        The function to load pharmacy order details
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    presid=request.GET.get("id")
    request.session["presid"]=presid
    s="SELECT tblmedicine.medName,tblprescmedicine.course,tblprescmedicine.days,tblpatient.`pName`,tblpatient.`pAddress`,tblpatient.`pContact`,tblpatient.`pEmail` FROM tblmedicine,tblprescmedicine,`tblprescription`,`tblallocation`,`tblrequest`,`tblpatient` WHERE tblprescmedicine.presId='"+presid+"' AND tblmedicine.medId=tblprescmedicine.medId AND `tblprescription`.`presId`=tblprescmedicine.`presId` AND `tblprescription`.`allocId`=`tblallocation`.`allocId` AND `tblallocation`.`reqId`=`tblrequest`.`reqId` AND `tblrequest`.`pEmail`=`tblpatient`.`pEmail`"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        return HttpResponseRedirect("/pharmacyinvoice")        
    return render(request,"pharmacyorderdetails.html",{"data":data})
######################################################################
#                          PHARMACY INVOICE
######################################################################
def pharmacyinvoice(request):
    """ 
        The function to add invoice
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    presid=request.session["presid"]
    s="SELECT tblpatient.`pName` FROM tblmedicine,tblprescmedicine,`tblprescription`,`tblallocation`,`tblrequest`,`tblpatient` WHERE tblprescmedicine.presId='"+presid+"' AND tblmedicine.medId=tblprescmedicine.medId AND `tblprescription`.`presId`=tblprescmedicine.`presId` AND `tblprescription`.`allocId`=`tblallocation`.`allocId` AND `tblallocation`.`reqId`=`tblrequest`.`reqId` AND `tblrequest`.`pEmail`=`tblpatient`.`pEmail`"
    c.execute(s)
    i=c.fetchone()
    request.session["reqid"]=i[0]
    pname=i[0]
    s="select sysdate()"
    c.execute(s)
    i=c.fetchone()
    date=i[0]
    s="select tblmedicine.medName,tblmedicine.medRate,tblprescmedicine.days,tblprescmedicine.total from tblmedicine,tblprescmedicine where tblmedicine.medId=tblprescmedicine.medId and tblprescmedicine.presId='"+presid+"'"
    c.execute(s)
    data=c.fetchall()
    s="select sum(total) from tblprescmedicine where presId='"+presid+"'"
    c.execute(s)
    i=c.fetchone()
    total=i[0]
    s="select fees from tblconsultationfee where prescId='"+presid+"'"
    c.execute(s)
    i=c.fetchone()
    fees=i[0]
    if(request.POST):
        return HttpResponseRedirect("/pharmacycourier")
    return render(request,"pharmacyinvoice.html",{"data":data,"pname":pname,"date":date,"total":total,"fees":fees})
######################################################################
#                          PHARMACY COURIER
######################################################################
def pharmacycourier(request):
    """ 
        The function to load all couriers for pharmacy
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    dist=request.session["district"]
    s="select * from tblcourier where cDistrict='"+dist+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"pharmacycourier.html",{"data":data})
######################################################################
#                          PHARMACY COURIER ORDER
######################################################################
def pharmacyordercourier(request):
    """ 
        The function to order courier
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    cid=request.GET.get("id")
    presid=request.session["presid"]
    s="insert into tblcourierorder (cEmail,prescId,status) values('"+cid+"','"+presid+"','ordered')"
    try:
        c.execute(s)
        db.commit()
    except:
        pass
    else:
        s="update tblmedicineorder set status='passed to courier' where prescId='"+presid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            return HttpResponseRedirect("/pharmacyallorder")
    return render(request,"pharmacycourier.html")
######################################################################
#                           DOCTOR HOME
######################################################################
def doctorhome(request):
    """ 
        The function to load doctor home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        district=request.POST["txtDistrict"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        exp=request.POST["txtExp"]
        qual=request.POST["txtQual"]
        s="update tbldoctor set dName='"+name+"',dAddress='"+address+"',dContact='"+contact+"',dEmail='"+email+"',dQualification='"+qual+"',dExperience='"+exp+"',dDistrict='"+district+"' where dEmail='"+email+"'"
        try:
            c.execute(s)
            db. commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Registration successfull"
    email=request.session["email"]
    s="select * from tbldoctor where dEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"doctorhome.html",{"data":data})
######################################################################
#                           DOCTOR REQUEST
######################################################################
def doctorrequest(request):
    """ 
        The function to load doctor request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblrequest.*,tblpatient.pName from tblrequest,tblpatient where tblrequest.reqId in(select reqId from tblallocation where dEmail='"+email+"' and allocId not in(select allocId from tblPrescription)) and tblrequest.pEmail=tblpatient.pEmail"
    c.execute(s)
    data=c.fetchall()
    return render(request,"doctorviewrequest.html",{"data":data})
######################################################################
#                           DOCTOR VIEW PATIENT
######################################################################
def doctorviewpatient(request):
    """ 
        The function to load doctor request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    reqid=request.GET.get("id")
    s="select allocId from tblallocation where reqId='"+str(reqid)+"'"
    c.execute(s)
    i=c.fetchone()
    request.session["reqid"]=i[0]
    s="select * from tblpatient where pEmail in(select pEmail from tblrequest where reqId='"+reqid+"')"
    c.execute(s)
    data=c.fetchall()
    if(request.POST):
        return HttpResponseRedirect("/doctoraddprescription")
    return render(request,"doctorviewpatient.html",{"data":data})
######################################################################
#                           DOCTOR ADD PRESCRIPTION
######################################################################
def doctoraddprescription(request):
    """ 
        The function to add prescription
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    reqid=request.session["reqid"]
    if(request.POST):
        diagnosis=request.POST["txtDiagnosis"]
        presc=request.POST["txtPrescription"]
        s="insert into tblprescription (allocId,diagnosis,prescription) values('"+str(reqid)+"','"+str(diagnosis)+"','"+str(presc)+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            return HttpResponseRedirect("/doctormedicine")
    return render(request,"doctoraddprescription.html",{"msg":msg})
######################################################################
#                           DOCTOR ADD MEDICINE
######################################################################
def doctormedicine(request):
    """ 
        The function to select pharmacy for prescription
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="Select * from tblmedicine order by medName"
    c.execute(s)
    med=c.fetchall()
    s="select max(presId) from tblprescription"
    c.execute(s)
    i=c.fetchone()
    request.session["prescid"]=i[0]
    prescid=i[0]
    if 'btnNext' in request.POST:
        mid=request.POST["medicine"]
        course=request.POST["txtCourse"]
        days=request.POST["txtQty"]
        s="select medRate from tblmedicine where medId='"+mid+"'"
        c.execute(s)
        i=c.fetchone()
        rate=i[0]
        total=int(rate)*int(days)
        s="insert into tblprescmedicine (presId,medId,course,days,total) values('"+str(prescid)+"','"+str(mid)+"','"+str(course)+"','"+str(days)+"','"+str(total)+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            return HttpResponseRedirect("/doctorrequest")
        else:
            return HttpResponseRedirect("/doctormedicine")
    if 'btnSubmit' in request.POST:
        s="select count(*) from tblprescmedicine where presId='"+str(prescid)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            return HttpResponseRedirect("/doctorfees")
    return render(request,"doctormedicine.html",{"med":med})
######################################################################
#                           DOCTOR CONSULTATION FEE
######################################################################
def doctorfees(request):
    """ 
        The function to add consultation fee
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    prescid=request.session["prescid"]
    if(request.POST):
        fee=request.POST["txtFees"]
        s="insert into tblconsultationfee(prescId,fees) values('"+str(prescid)+"','"+str(fee)+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            return HttpResponseRedirect("/doctorpharmacy")
    return render(request,"doctorfees.html",{"msg":msg})
######################################################################
#                           DOCTOR SELECT PHARMACY
######################################################################
def doctorpharmacy(request):
    """ 
        The function to select pharmacy for doctor
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblpharmacy where phEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    return render(request,"doctorpharmacy.html",{"data":data})
######################################################################
#                           DOCTOR ORDER MEDICINE
######################################################################
def doctorordermedicine(request):
    """ 
        The function to place order to a medicine
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    prescid=request.session["prescid"]
    email=request.GET.get("id")
    s="insert into tblmedicineorder(phEmail,prescId,status) values('"+str(email)+"','"+str(prescid)+"','ordered')"
    try:
        c.execute(s)
        db.commit()
    except:
        msg="Sorry some error occured"
    else:
        msg="Order placed"
    return render(request,"doctorpharmacy.html",{"msg":msg})
######################################################################
#                           COURIER HOME
######################################################################
def courierhome(request):
    msg=""
    email=request.session["email"]
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        district=request.POST["txtDistrict"]
        lic=request.POST["txtLicense"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        s="update tblcourier set cName='"+name+"',cAddress='"+address+"',cContact='"+contact+"',cEmail='"+email+"',cDistrict='"+district+"',cLicence='"+lic+"' where cEmail='"+email+"'"
        try:
            c.execute(s)
            db. commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Registration successfull"
    email=request.session["email"]
    s="select * from tblcourier where cEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"courierhome.html",{"data":data})
######################################################################
#                         COURIER ORDER
######################################################################
def courierorder(request):
    """ 
        The function to load courier orders
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """

    email=request.session["email"]
    s="SELECT `tblcourierorder`.`prescId`,`tblpatient`.`pName`,`tblpatient`.`pAddress`,`tblpatient`.`pContact`,tblpharmacy.phName,tblpharmacy.phAddress,tblpharmacy.phContact FROM tblpharmacy,`tblcourierorder`,`tblallocation`,`tblrequest`,`tblpatient`,`tblprescription`,tblmedicineorder WHERE tblcourierorder.cEmail='"+email+"' AND tblcourierorder.`prescId`=`tblprescription`.`presId` AND `tblprescription`.`allocId`=`tblallocation`.`allocId` AND `tblrequest`.`pEmail`=`tblpatient`.`pEmail` AND tblcourierorder.status='ordered' AND `tblallocation`.`reqId`=`tblrequest`.`reqId`AND tblcourierorder.prescId=tblmedicineorder.prescId AND tblmedicineorder.phEmail=tblpharmacy.phEmail"
    c.execute(s)
    data=c.fetchall()
    return render(request,"courierorder.html",{"data":data})
######################################################################
#                       COURIER ORDER DELIVERY
######################################################################
def courierdelivery(request):
    """ 
        The function to deliver courier orders
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    oid=request.GET.get("id")
    s="update tblcourierorder set status='delivered' where prescId='"+oid+"'"
    c.execute(s)
    s="update tblmedicineorder set status='delivered' where prescId='"+oid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/courierallorder")
######################################################################
#                         COURIER ALL ORDER
######################################################################
def courierallorder(request):
    """ 
        The function to load  pharmacy order status
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="SELECT `tblcourierorder`.`prescId`,`tblpatient`.`pName`,`tblpatient`.`pAddress`,`tblpatient`.`pContact`,tblpharmacy.phName,tblpharmacy.phAddress,tblpharmacy.phContact,tblcourierorder.`status` FROM tblpharmacy,`tblcourierorder`,`tblallocation`,`tblrequest`,`tblpatient`,`tblprescription`,tblmedicineorder WHERE tblcourierorder.cEmail='"+email+"' AND tblcourierorder.`prescId`=`tblprescription`.`presId` AND `tblprescription`.`allocId`=`tblallocation`.`allocId` AND `tblrequest`.`pEmail`=`tblpatient`.`pEmail` AND tblcourierorder.status='delivered' AND `tblallocation`.`reqId`=`tblrequest`.`reqId`AND tblcourierorder.prescId=tblmedicineorder.prescId AND tblmedicineorder.phEmail=tblpharmacy.phEmail"
    c.execute(s)
    data=c.fetchall()
    return render(request,"courierallorder.html",{"data":data})
######################################################################
#                           PATIENT HOME
######################################################################
def patienthome(request):
    """ 
        The function to load patient home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        pin=request.POST["txtPin"]
        allergy=request.POST["txtAllergy"]
        heriditary=request.POST["txtHeriditary"]
        surgery=request.POST["txtSurgery"]
        admit=request.POST["txtAdmit"]
        history=request.POST["txtHistory"]
        s="update tblpatient set pName='"+name+"',pAddress='"+address+"',pContact='"+contact+"',pPincode='"+pin+"',allergy='"+allergy+"',heriditary='"+heriditary+"',surgery='"+surgery+"',admit='"+admit+"',history='"+history+"' where pEmail='"+email+"'"
        try:
            c.execute(s)
            db. commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Registration successfull"
    s="select * from tblpatient where pEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"patienthome.html",{"data":data,"msg":msg})
######################################################################
#                           PATIENT REQUEST
######################################################################
def patientrequest(request):
    """ 
        The function to load patient home
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        dept=request.POST["dept"]
        disease=request.POST["txtDisease"]
        desc=request.POST["txtDesc"]
        dist=request.POST["dist"]
        s="insert into tblrequest (pEmail,depId,disease,description,district,reqDate,reqStatus) values('"+email+"','"+dept+"','"+disease+"','"+desc+"','"+dist+"',(select sysdate()),'requested')"
        try:
            c.execute(s)
            db. commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Request added"
    s="select tblrequest.*,tbldepartment.deptName from tblrequest,tbldepartment where tblrequest.pEmail='"+email+"' and tblrequest.depId=tbldepartment.deptId"
    c.execute(s)
    data=c.fetchall()
    s="select * from tbldepartment where status='1'"
    c.execute(s)
    dept=c.fetchall()
    return render(request,"patientrequest.html",{"data":data,"msg":msg,"dept":dept})
######################################################################
#                           PATIENT PRESCRIPTION
######################################################################
def patientprescription(request):
    """ 
        The function to load prescription for patient
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblrequest.reqId,tblrequest.disease,tbldoctor.dName,tblprescription.diagnosis,tblprescription.prescription,tblprescription.presId from tblrequest,tbldoctor,tblprescription,tblallocation where tblrequest.pEmail='"+email+"' and tblrequest.reqId=tblallocation.reqId and tblallocation.dEmail=tbldoctor.dEmail and tblprescription.allocId=tblallocation.allocId"
    c.execute(s)
    data=c.fetchall()
    return render(request,"patientprescription.html",{"data":data})
######################################################################
#                           PATIENT MEDICINE
######################################################################
def patientmedicine(request):
    """ 
        The function to load medicine for patient
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    pid=request.GET.get("id")
    request.session["presid"]=pid
    s="select count(*) from tblmedicine,tblprescmedicine where tblprescmedicine.medId=tblmedicine.medId and tblprescmedicine.presId='"+pid+"'"
    c.execute(s)
    i=c.fetchone()
    if(i[0]==0):
        return HttpResponseRedirect("/patientprescription")
    s="select tblmedicine.medName,tblprescmedicine.course,tblprescmedicine.days,tblprescmedicine.total from tblmedicine,tblprescmedicine where tblprescmedicine.medId=tblmedicine.medId and tblprescmedicine.presId='"+pid+"'"
    c.execute(s)
    data=c.fetchall()
    s="select status from tblmedicineorder where prescId='"+pid+"'"
    c.execute(s)
    i=c.fetchone()
    status=i[0]
    return render(request,"patientmedicine.html",{"data":data,"status":status})
######################################################################
#                          PATIENT INVOICE
######################################################################
def patientinvoice(request):
    """ 
        The function to view invoice
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    presid=request.session["presid"]
    email=request.session["email"]
    s="select pName from tblpatient where pEmail='"+email+"'"
    c.execute(s)
    i=c.fetchone()
    pname=i[0]
    s="select sysdate()"
    c.execute(s)
    i=c.fetchone()
    date=i[0]
    s="select tblmedicine.medName,tblmedicine.medRate,tblprescmedicine.days,tblprescmedicine.total from tblmedicine,tblprescmedicine where tblmedicine.medId=tblprescmedicine.medId and tblprescmedicine.presId='"+presid+"'"
    c.execute(s)
    data=c.fetchall()
    s="select sum(total) from tblprescmedicine where presId='"+presid+"'"
    c.execute(s)
    i=c.fetchone()
    total=i[0]
    s="select fees from tblconsultationfee where prescId='"+presid+"'"
    c.execute(s)
    i=c.fetchone()
    fees=i[0]
    if(request.POST):
        return HttpResponseRedirect("/pharmacycourier")
    return render(request,"patientinvoice.html",{"data":data,"pname":pname,"date":date,"total":total,"fees":fees})
######################################################################
#                          ADMIN DELETE MEDICINE
######################################################################
def adminmedicinedelete(request):
    """ 
        The function to delete medicine
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    mid=request.GET.get("id")
    s="update tblmedicine set medStatus='0' where medId='"+mid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminmedicine")
######################################################################
#                          PATIENT FEEDBACK
######################################################################
def patientfeedback(request):
    """ 
        The function to patient feedback
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.session["email"]
        feedback=request.POST["txtFeedback"]
        s="insert into tblfeedback(pEmail,feeback,fDate) values('"+email+"','"+feedback+"',(select sysdate()))"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Feedback added"
    return render(request,"patientfeedback.html",{"msg":msg})
######################################################################
#                          ADMIN FEEDBACK
######################################################################
def adminfeedback(request):
    """ 
        The function to view patient feedback
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select tblpatient.pName,tblfeedback.feeback,tblfeedback.fDate from tblpatient,tblfeedback where tblfeedback.pEmail=tblpatient.pEmail order by tblfeedback.fDate desc"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminfeedback.html",{"data":data})