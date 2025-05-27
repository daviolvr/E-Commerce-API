from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permite leitura para qualquer usuário autenticado.
    Edição/Criação/Exclusão apenas para admins.
    """

    def has_permission(self, request, view):
        # Permite qualquer metodo de leitura
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Para métodos de escrita, exige que seja admin
        return request.user and request.user.is_authenticated and request.user.is_staff
    

# class IsAdminOrOwner(permissions.BasePermission):
#     """
#     Admin pode fazer tudo. Usuário comum só pode ler aquilo que for seu.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Admin tem acesso geral
#         if request.user.is_staff:
#             return True
        
#         # Usuário comum pode acessar apenas aquilo que ele for owner
#         return obj.user == request.user
    
#     def has_permission(self, request, view):
#         # Usuários autenticados tem permissão inicial 
#         return request.user and request.user.is_authenticated

