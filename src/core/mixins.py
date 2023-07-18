from django.contrib.auth.mixins import UserPassesTestMixin

class SuperusuarioAutorMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        obj = self.get_object()


        # Aca entra si se trata de una publicacion
        if hasattr(obj, 'creador'):
            return usuario == obj.creador or usuario.is_superuser 
    
        # Aca entra si se trata de un comentario
        if hasattr(obj,'autor'):
            return usuario == obj.autor or usuario.is_superuser or usuario == obj.post.creador
        

class ColaboradorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.es_colaborador or self.request.user.is_superuser