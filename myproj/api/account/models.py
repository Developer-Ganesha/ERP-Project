from django.db import models

from django.db import models
from django.contrib.auth.models import  AbstractBaseUser ,BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email,company_name, short_name, address, website, 
                contact_no, footer_message, director_name, msme_no, 
                pin_code, city, state, district_code, 
                state_no_numeric, state_code_alpha, VAT_TIN, CST_TIN, 
                C_Excise_Range, Commissionerate, C_Excise_Reg_No, 
                PLA_No, Service_Tax_No, Import_Export_Code, ARN_No, 
                Export_House_No, Udyog_Aadhar_No, Vat_Tin_Date, 
                Cst_Tin_Date, Subject_To, Division, GST_No, 
                ECC_No, PAN_No, CIN_NO, Import_Export_Date, 
                ARN_Date, LUT_NO, LUT_Date, password=None,password2=None,**extra_fields):
        print("djhdsjksdkj")
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            company_name=company_name, short_name=short_name, address=address, website=website, 
                contact_no=contact_no, footer_message=footer_message, director_name=director_name, msme_no=msme_no, 
                pin_code=pin_code, city=city, state=state, district_code=district_code, 
                state_no_numeric=state_no_numeric, state_code_alpha=state_code_alpha, VAT_TIN=VAT_TIN, CST_TIN=CST_TIN, 
                C_Excise_Range=C_Excise_Range, Commissionerate=Commissionerate, C_Excise_Reg_No=C_Excise_Reg_No, 
                PLA_No=PLA_No, Service_Tax_No=Service_Tax_No, Import_Export_Code=Import_Export_Code, ARN_No=ARN_No, 
                Export_House_No=Export_House_No, Udyog_Aadhar_No=Udyog_Aadhar_No, Vat_Tin_Date=Vat_Tin_Date, 
                Cst_Tin_Date=Cst_Tin_Date, Subject_To=Subject_To, Division=Division, GST_No=GST_No, 
                ECC_No=ECC_No, PAN_No=PAN_No, CIN_NO=CIN_NO, Import_Export_Date=Import_Export_Date, 
                ARN_Date=ARN_Date, LUT_N=LUT_NO, LUT_Date=LUT_Date, 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name,tc, password=None):
        user = self.create_user(email,password=password, name= name,tc=tc)
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=255,unique=True,)
    company_name = models.CharField(max_length=255,blank=True, null=True)
    short_name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField(max_length=255)
    contact_no = models.CharField(max_length=15)
    footer_message = models.TextField()
    director_name = models.CharField(max_length=255)
    msme_no = models.CharField(max_length=255, blank=True, null=True)
    pin_code = models.CharField(max_length=6)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district_code = models.CharField(max_length=10)   
    state_no_numeric = models.CharField(max_length=10)
    state_code_alpha = models.CharField(max_length=10)
    VAT_TIN = models.CharField(max_length=100)
    CST_TIN = models.CharField(max_length=100)
    C_Excise_Range = models.CharField(max_length=100)
    Commissionerate = models.CharField(max_length=100)
    C_Excise_Reg_No = models.CharField(max_length=100)
    PLA_No = models.CharField(max_length=100)
    Service_Tax_No = models.CharField(max_length=100)
    Import_Export_Code = models.CharField(max_length=100)
    ARN_No = models.CharField(max_length=100)
    Export_House_No = models.CharField(max_length=100)
    Udyog_Aadhar_No = models.CharField(max_length=100)
    Vat_Tin_Date = models.DateField()
    Cst_Tin_Date = models.DateField()
    Subject_To = models.CharField(max_length=100)
    Division = models.CharField(max_length=100)
    GST_No = models.CharField(max_length=100)
    ECC_No = models.CharField(max_length=100)
    PAN_No = models.CharField(max_length=100)
    CIN_NO = models.CharField(max_length=100)
    Import_Export_Date = models.DateField()
    ARN_Date = models.DateField()
    LUT_NO = models.CharField(max_length=100)
    LUT_Date = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    creates_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","tc"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

