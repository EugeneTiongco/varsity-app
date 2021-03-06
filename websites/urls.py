from django.urls import path

from . import views



'''app_name = 'polls'
urlpatterns = [
	# ex: /polls/
	path('', views.index, name='index'),
	# ex: /polls/5/
	path('<int:question_id>/', views.detail, name='detail'),
	# ex: /polls/5/results/
	path('<int:question_id>/results/', views.results, name='results'),
	# ex: /polls/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
]'''


app_name = 'websites'
urlpatterns = [
	path('',views.Homepage, name='Homepage'),
	path('login/',views.loginattempt, name='loginattempt'),
	path('login/#',views.login, name='login'),
	path('directory/',views.directory, name='directory'),
	path('calendar/',views.events, name='events'),
	path('editpage/',views.editpage, name='editpage'),
	path('edit/',views.edit, name='edit'),
	path('schedule/',views.adddate, name='adddate'),
	path('schedule/#',views.insertdate, name='insertdate'),
	path('newmember/',views.newmember, name='newmember'),
	path('newmember/#',views.insertmember, name='insertmember'),
	path('customize/#',views.customize, name='customize')
]