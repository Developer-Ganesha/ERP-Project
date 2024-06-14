from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User

class UserModelAdmin(BaseUserAdmin):
    list_display = [
        'email', 'company_name', 'short_name', 'contact_no', 
        'is_active', 'is_admin'
    ]
    list_filter = ['is_admin']
    fieldsets = [
        ('User credentials', {'fields': ['email', 'password']}),
        ('Personal info', {
            'fields': [
                'company_name', 'short_name', 'address', 'website', 
                'contact_no', 'footer_message', 'director_name', 'msme_no', 
                'pin_code', 'city', 'state', 'district_code', 
                'state_no_numeric', 'state_code_alpha', 'VAT_TIN', 'CST_TIN', 
                'C_Excise_Range', 'Commissionerate', 'C_Excise_Reg_No', 
                'PLA_No', 'Service_Tax_No', 'Import_Export_Code', 'ARN_No', 
                'Export_House_No', 'Udyog_Aadhar_No', 'Vat_Tin_Date', 
                'Cst_Tin_Date', 'Subject_To', 'Division', 'GST_No', 
                'ECC_No', 'PAN_No', 'CIN_NO', 'Import_Export_Date', 
                'ARN_Date', 'LUT_NO', 'LUT_Date'
            ]
        }),
        ('Permissions', {'fields': ['is_admin']}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['email', 'password1', 'password2', 'company_name', 
                       'short_name', 'contact_no', 'is_active', 'is_admin'],
        }),
    ]
    search_fields = ['email']
    ordering = ['email', 'id']
    filter_horizontal = []

# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
