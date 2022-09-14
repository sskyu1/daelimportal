# from django.apps import AppConfig


# class PostsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'posts'


from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostsConfig(AppConfig):
    name = "djangogram.posts"
    verbose_name = _("Posts")

    def ready(self):
        try:
            import djangogram.posts.signals  # noqa F401
        except ImportError:
            pass
