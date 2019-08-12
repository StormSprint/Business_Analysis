from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from Business_Analysis.base_admin import BaseOwnerAdmin


@admin.register(Product)
class ProductAdmin(BaseOwnerAdmin):
    list_display = ('sid', 'status', 'price', 'receive_org', 'PRODUCT_NAME',
                    'main_set', 'add_set', 'custom', 'staff', 'contract_id')
    # 按"专线号sid"和"合同编码contract_id"进行搜索
    search_fields = ('sid', 'contract_id')
    # 每页最多显示15条数据
    list_per_page = 15
    actions_on_top = True


@admin.register(Contract)
class ContractAdmin(BaseOwnerAdmin):
    list_display = ('contract_id', 'contract_amount', 'contract_date', 'contract_expire',
                    'allowance')
    # 按字段"合同编码"进行搜索
    search_fields = ('contract_id', )
    # 每页最多显示15条数据
    list_per_page = 15
    actions_on_top = True


@admin.register(Resource)
class ResourceAdmin(BaseOwnerAdmin):
    list_display = ('sid', 'bandwidth', 'true_bandwidth', 'net_management')
    # 按字段"专线号sid"进行搜索
    search_fields = ('sid', )
    # 每页最多显示15条数据
    list_per_page = 15
    actions_on_top = True
