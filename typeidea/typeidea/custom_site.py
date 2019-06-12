from django.contrib.admin import AdminSite

class CustomStite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea 管理后台'
    index_title = '首页'

custom_site = CustomStite(name='cus_admin')
