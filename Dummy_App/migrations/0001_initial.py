# Generated by Django 3.0 on 2020-02-14 16:31

import Dummy_App.manager
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('registration_no', models.CharField(blank=True, max_length=100)),
                ('gstin', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('trade_licence', models.CharField(blank=True, max_length=100)),
                ('vat_no', models.CharField(blank=True, max_length=100)),
                ('tan_no', models.CharField(blank=True, max_length=100)),
                ('fax', models.CharField(blank=True, max_length=100)),
                ('address_st1', models.CharField(blank=True, max_length=100)),
                ('address_st2', models.CharField(blank=True, max_length=100)),
                ('pincode', models.IntegerField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('note', models.TextField(blank=True, help_text='brief note about the company')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='brief description about the education')),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_id', models.CharField(max_length=100)),
                ('template_name', models.CharField(max_length=100)),
                ('mail_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('employee_id', models.CharField(blank=True, max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('profile_image', models.ImageField(blank=True, max_length=700, upload_to='hrms/employee/profile/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobTitles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('job_description', models.TextField(blank=True, help_text='brief description about the job')),
                ('job_specification', models.FileField(blank=True, max_length=700, upload_to='hrms/jobtitle/documents/')),
                ('note', models.TextField(blank=True, help_text='brief note about the job title')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='brief description about the language')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('menu_group', models.CharField(blank=True, max_length=100)),
                ('menu_heading', models.CharField(blank=True, max_length=100)),
                ('menu_link', models.CharField(blank=True, max_length=100)),
                ('icon_class', models.CharField(blank=True, max_length=100)),
                ('display_order', models.IntegerField(blank=True)),
                ('parent_flag', models.IntegerField(default=0, help_text='0 for outer, 1 for inner, 2 for nested inner')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='menu_parent', to='Dummy_App.Menu')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(max_length=100)),
                ('department_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='brief description about the department')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('role_name', models.CharField(blank=True, max_length=100)),
                ('depth', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='role_parent', to='Dummy_App.Role')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='brief description about the skill')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_name', models.CharField(blank=True, max_length=100)),
                ('work_hours_from', models.CharField(blank=True, max_length=100)),
                ('work_hours_to', models.CharField(blank=True, max_length=100)),
                ('duration_hours', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('emp_ref', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employee_user', to='Dummy_App.Employee')),
                ('status', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Dummy_App.Status')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', Dummy_App.manager.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Dummy_App.Role')),
                ('user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(blank=True, max_length=100)),
                ('link', models.CharField(blank=True, max_length=100)),
                ('menu_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Dummy_App.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('dl_no', models.CharField(blank=True, max_length=100)),
                ('dl_expiry', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('marital_status', models.CharField(blank=True, max_length=20)),
                ('spouse_name', models.CharField(blank=True, max_length=100)),
                ('nationality', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('emp_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to='Dummy_App.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeJobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('designation', models.CharField(max_length=20)),
                ('specification', models.TextField(blank=True, help_text='brief description about your job role')),
                ('employement_status', models.CharField(blank=True, max_length=100)),
                ('job_category', models.CharField(blank=True, max_length=100)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('contract_detail', models.TextField(blank=True, help_text='brief description about your job contract')),
                ('termination_reason', models.CharField(blank=True, max_length=100)),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('termination_note', models.TextField(blank=True, help_text='brief description about your job resignation')),
                ('emp_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_job_detail', to='Dummy_App.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeEmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('home_phone', models.CharField(max_length=10)),
                ('work_phone', models.CharField(max_length=10)),
                ('emp_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_emergency_contact', to='Dummy_App.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(blank=True, max_length=50)),
                ('doc_type', models.CharField(blank=True, max_length=50)),
                ('doc_image', models.FileField(blank=True, max_length=700, upload_to='hrms/employee/documents/')),
                ('description', models.TextField(blank=True, help_text='any description about uploaded doc')),
                ('emp_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_docs', to='Dummy_App.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDependent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=50)),
                ('specification', models.CharField(max_length=200)),
                ('dob', models.DateField(blank=True, null=True)),
                ('emp_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_dependent', to='Dummy_App.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('loc_address_1', models.CharField(blank=True, max_length=150)),
                ('loc_pincode', models.CharField(blank=True, default='', max_length=10)),
                ('loc_country', models.CharField(blank=True, max_length=50)),
                ('loc_state', models.CharField(blank=True, max_length=50)),
                ('loc_city', models.CharField(blank=True, max_length=50)),
                ('perm_address_1', models.CharField(blank=True, max_length=150)),
                ('perm_pincode', models.CharField(blank=True, default='', max_length=10)),
                ('perm_country', models.CharField(blank=True, max_length=50)),
                ('perm_state', models.CharField(blank=True, max_length=50)),
                ('perm_city', models.CharField(blank=True, max_length=50)),
                ('home_phone', models.CharField(blank=True, max_length=20)),
                ('work_phone', models.CharField(blank=True, max_length=20)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('work_email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('personal_email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('skype_id', models.CharField(blank=True, max_length=100)),
                ('emp_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_contact', to='Dummy_App.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeBankDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('account_no', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=100)),
                ('branch_address', models.CharField(max_length=150)),
                ('branch_code', models.CharField(max_length=50)),
                ('micr_code', models.CharField(max_length=50)),
                ('upi_id', models.CharField(max_length=50)),
                ('emp_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_bank_detail', to='Dummy_App.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanySubsidiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_code', models.CharField(max_length=100)),
                ('hr_email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('company_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Dummy_App.Company')),
                ('company_parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_parent', to='Dummy_App.Company')),
            ],
        ),
        migrations.CreateModel(
            name='MenuRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_actions', models.CharField(blank=True, max_length=100)),
                ('menu', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Dummy_App.Menu')),
                ('role', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Dummy_App.Role')),
            ],
            options={
                'unique_together': {('menu', 'role')},
            },
        ),
    ]
