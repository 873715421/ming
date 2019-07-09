from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^logout/$',views.logout,name='logout'),
    # url(r'^cart/$',views.cart,name='cart'),
    url(r'^info/$',views.info,name='info'),
    url(r'^order/$',views.order,name='order'),
    url(r'^placeorder/$',views.placeorder,name='placeorder'),
    url(r'^site/$',views.site,name='site'),
    url(r'^detail/(?P<goodid>\w+)/$',views.detail,name='detail'),
    url(r'^cart/(?P<goodsid>\w+)/$',views.cart,name='detail'),
    url(r'^check/$', views.check, name='check'),
    url(r'^change/$', views.change, name='change'),
    url(r'^xiugai/$', views.xiugai, name='xiugai'),

]

