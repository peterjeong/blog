from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout

from blog.urlurls import urlpatterns as blog_urls

from blog.views import create_user

urlpatterns = [
    url(r'^blog/', include(blog_urls, namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', django_login,
        {'template_name': 'login.html'}, name="login_user"
    ),
    url(r'^logout/$', django_logout,
        {'next_page': '/blog/posts/'}, name="logout_user"
    ),
    url(r'^register/$', create_user, name="create_user"
    ),
]