
from django.urls import path

from main_app.EditResultView import EditResultView

from . import hod_views, staff_views, student_views, views

urlpatterns = [
    path("", views.index, name='index'),
    path("doLogin/", views.doLogin, name='doLogin'),
    path("logout_user/", views.logout_user, name='user_logout'),

    # HOD
    path("hod_template/hod_home", hod_views.hod_home, name='hod_home'),

    path("hod_template/add_staff", hod_views.add_staff, name='add_staff'),
    path("hod_template/add_course", hod_views.add_course, name='add_course'),
    path("hod_template/add_student", hod_views.add_student, name='add_student'),
    path("hod_template/add_subject", hod_views.add_subject, name='add_subject'),

    path("hod_template/hod_view_attendance", hod_views.hod_view_attendance,name="hod_view_attendance"),
    path("hod_template/hod_view_profile", hod_views.hod_view_profile,name='hod_view_profile'),
    
    path("hod_template/edit_staff/<int:staff_id>", hod_views.edit_staff, name='edit_staff'),
    path("hod_template/edit_student/<int:student_id>",hod_views.edit_student, name='edit_student'),
    path("hod_template/edit_course/<int:course_id>",hod_views.edit_course, name='edit_course'),
    path("hod_template/edit_subject/<int:subject_id>",hod_views.edit_subject, name='edit_subject'),

    path("hod_template/send_student_notification/", hod_views.send_student_notification,name='send_student_notification'),

    # path("staff/delete/<int:staff_id>",hod_views.delete_staff, name='delete_staff'),
    # path("course/delete/<int:course_id>",hod_views.delete_course, name='delete_course'),
    # path("student/delete/<int:student_id>",hod_views.delete_student, name='delete_student'),
    # path("subject/delete/<int:subject_id>",hod_views.delete_subject, name='delete_subject'),
    
#     path("admin_notify_student", hod_views.admin_notify_student,name='admin_notify_student'),
#     path("check_email_availability", hod_views.check_email_availability,name="check_email_availability"),
 


    # Staff
    path("staff/result/edit/", EditResultView.as_view(),name='edit_student_result'),
        
    path("staff_template/staff_home", staff_views.staff_home, name='staff_home'),
    path("staff_template/staff_view_profile", staff_views.staff_view_profile,name='staff_view_profile'),
    path("staff_template/staff_update_attendance", staff_views.staff_update_attendance,name='staff_update_attendance'),
    path("staff/fcmtoken/", staff_views.staff_fcmtoken, name='staff_fcmtoken'),
    path("staff_template/staff_add_result", staff_views.staff_add_result, name='staff_add_result'),



    # Student 
    path("student_template/studeny_home", student_views.student_home, name='student_home'),
    path("student_template/student_view_attendance", student_views.student_view_attendance,name='student_view_attendance'),
    path("student_template/student_view_profile", student_views.student_view_profile,name='student_view_profile'),
    path("student_template/fcmtoken", student_views.student_fcmtoken,name='student_fcmtoken'),
    path("student_template/student_view_notification", student_views.student_view_notification,name="student_view_notification"),
    path('student_template/student_view_result/', student_views.student_view_result,name='student_view_result'),

]