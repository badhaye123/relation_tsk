from django.urls import path
from . import views

urlpatterns = [
    path('stuadd/', views.stu_add, name='studadd'),
    path('deptadd/', views.dept_add, name='deptadd'),
    path('lectadd/', views.lect_add, name='lectadd'),
    path('updatestud/<int:id>/',views.stu_update,name='updatestud'),
    path('updatelect/<int:id>/',views.lect_update,name='updatelect'),
    path('updatedept/<int:id>/',views.dept_update,name='updatedept'),
    path('showstud/',views.show_stud,name='showstud'),
    path('showlect/', views.show_lect, name='showlect'),
    path('showdept/', views.show_dept, name='showdept'),
    path('deletestud/<int:id>/',views.stu_delete,name='deletestud'),
    path('deletelect/<int:id>/',views.lect_delete,name='deletelect'),
    path('deletedept/<int:id>/',views.dept_delete,name='deletedept'),
    path('home/',views.home,name='home'),
    path('showdeptstud/<int:id>/',views.search_dept_stu,name='showdeptstud'),
    path('showdeptlect/<int:id>/',views.search_dept_lect,name='showdeptlect'),
    path('search/',views.search,name='search'),


]