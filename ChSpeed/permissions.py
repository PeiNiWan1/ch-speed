from rest_framework.permissions import BasePermission
# 判断是否拥有特殊权限
class HasPerm(BasePermission):
    """
    检查单独权限，或分组中权限
    """
    def __init__(self,perm) -> None:
        self.perm=perm
        super().__init__()

    def has_permission(self, request, view):
        # 检查用户权限中是否拥有perm权限
        user = request.user
        allPerm= user.get_all_permissions()
        print("用户权限",self.perm)
        # if user.is_superuser:
        #     return True
        if self.perm in allPerm:
            return True
        return False
