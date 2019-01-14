from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^dologin/$',views.dologin,name='dologin'),
    url(r'^about/$',views.about,name='about'),
    url(r'^new/$',views.new,name='new'),
    url(r'^newlist/$',views.newlist,name='newlist'),
    url(r'^share/$',views.share,name='share'),
    url(r'^login/$',views.login,name='login'),
    # url(r'^send/$',views.send,name='send'),
    url(r'^register/$',views.register,name='register'),

    #后台登录
    url(r'^adminindex/$',views.adminindex,name='adminindex'),
    url(r'^adminmain/$',views.adminmain,name='adminmain'),

    # 后台跳转界面
    url(r'^add_article/$',views.add_article,name='add_article'),
    url(r'^add_category/$',views.add_category,name='add_category'),
    url(r'^add_flink/$',views.add_flink,name='add_flink'),
    url(r'^add_notice/$',views.add_notice,name='add_notice'),
    url(r'^article/$',views.article,name='article'),
    url(r'^category/$',views.category,name='category'),
    url(r'^comment/$',views.comment,name='comment'),
    url(r'^flink/$',views.flink,name='flink'),
    url(r'^loginlog/$',views.loginlog,name='loginlog'),
    url(r'^manage_user/$',views.manage_user,name='manage_user'),
    url(r'^notice/$',views.notice,name='notice'),
    url(r'^readset/$',views.readset,name='readset'),
    url(r'^setting/$',views.setting,name='setting'),
    url(r'^update_flink/$',views.update_flink,name='update_flink'),
    url(r'^update_category/$',views.update_category,name='update_category'),
    url(r'^update_article/$',views.update_article,name='update_article'),
]