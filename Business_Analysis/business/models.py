from django.db import models
from django.contrib.auth.models import User


class Contract(models.Model):
    """
    合同信息表
    包含字段：合同编码、合同金额、合同签订时间、合同到期时间、交叉补贴金额
    """
    contract_id = models.CharField(max_length=32, primary_key=True, verbose_name='合同编码')
    contract_amount = models.FloatField(verbose_name='合同金额')
    contract_date = models.DateField(verbose_name='合同签订时间')
    contract_expire = models.DateField(verbose_name='合同到期时间')
    allowance = models.FloatField(verbose_name='交叉补贴')

    def __str__(self):
        return self.contract_id

    class Meta:
        verbose_name = verbose_name_plural = '合同信息'


class Product(models.Model):
    """
    专线信息表
    包含字段：专线号、状态、揽收组织、产品名称、主套餐、加装包、产品类型、客户名称、安装地址、揽收人、合同编码
    其中揽收人为外键，关联User类
    """
    # 状态0，1，2，3，4分别对应状态正常、拆机、单停、双停、停机保号
    STATUS_NORMAL = 0
    STATUS_DELETE = 1
    STATUS_ONE_WAY_STOP = 2
    STATUS_STOP = 3
    STATUS_STORE_NUMBER = 4
    STATUS_OTHER = 5
    # 状态选项
    ITEM = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '拆机'),
        (STATUS_ONE_WAY_STOP, '单停'),
        (STATUS_STOP, '双停'),
        (STATUS_STORE_NUMBER, '停机保号'),
        (STATUS_OTHER, '其他'),
    )
    sid = models.CharField(max_length=32, primary_key=True, verbose_name='专线号')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=ITEM,
                                         blank=True, verbose_name='状态')
    # MKT_CHNL_NAME = models.CharField(max_length=128)
    # MKT_GRID_NAME = models.CharField(max_length=128)
    price = models.DecimalField(verbose_name='计费金额', max_digits=8, decimal_places=2)
    receive_org = models.CharField(max_length=128, verbose_name='揽收组织')
    PRODUCT_NAME = models.CharField(max_length=128, verbose_name='产品名称')
    main_set = models.CharField(max_length=256, verbose_name='主套餐')
    add_set = models.CharField(max_length=256, verbose_name='加装包')
    # CRM = models.CharField(max_length=32)
    product_quality = models.CharField(max_length=64, verbose_name='产品性质')
    custom = models.CharField(max_length=128, verbose_name='客户名称')
    address = models.CharField(max_length=256, verbose_name='安装地址')

    staff = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='揽收人')
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='合同编码')

    def __str__(self):
        return self.sid

    class Meta:
        verbose_name = verbose_name_plural = '专线信息'


class Resource(models.Model):
    """
    资源信息表
    包含字段：专线号、套餐带宽、实际带宽、集团网管监控？
    """
    bandwidth = models.IntegerField(verbose_name='套餐带宽')
    true_bandwidth = models.IntegerField(verbose_name='实际带宽')
    net_management = models.CharField(max_length=16, verbose_name='集团网管监控')

    sid = models.OneToOneField(to=Product, on_delete=models.CASCADE, verbose_name='专线号')

    def __str__(self):
        return self.sid

    class Meta:
        verbose_name = verbose_name_plural = '资源信息'
