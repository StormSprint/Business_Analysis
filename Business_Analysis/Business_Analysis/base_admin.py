from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. 用来自动补充文章、分类、标签、侧边栏、友链这些Model的owner字段
    2. 用来针对queryset过滤当前用户的数据
    """
    exclude = ('staff', )

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        #  判断是否为超级用户，超级用户可查看所有用户的内容
        if request.user.is_superuser:
            return qs
        elif request.user.groups:
            return qs.filter(group=request.user.groups)
        else:
            return qs.filter(staff=request.user)

    def save_model(self, request, obj, form, change):
        obj.staff = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)