from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    # /application
    path('', views.home, name='home'),

    # /application/tutorial
    path('tutorial', views.fmTutorial, name='tutorial'),

    # /application/simulator
    path('simulator', views.fmSimulator, name='simulator'),

    # /application/simulator_material
    path('simulator_material', views.fmSimulatorMaterial, name='simulator_material'),

    # /application/simulator_source
    path('simulator_source', views.fmSimulatorSource, name='simulator_source'),

    # /application/visualization
    path('visualization', views.fmVisualization, name='visualization'),

    # /application/visualization
    path('download', views.fmDownload, name='download'),

    # /application/about
    path('about', views.about, name='about'),

    # /application/tcl_viewer
    path('tcl_viewer', views.tclViewer, name='tcl_viewer'),

    # /application/kernel_info
    path('kernel_info', views.kernelInfo, name='kernel_info'),

    # /application/download_preset
    path('download_preset', views.downloadPreset, name='download_preset'),
               
    # /application/create_preset_material
    path('create_preset_material', views.createPresetMaterial, name='create_preset_material'),

    path('signup', views.signup, name='signup'),

    path('login', views.LoginView.as_view(), name='login'),

    path('logout', views.LogoutView.as_view(), name='logout'),
               
    url(r'^ajax_requests/', views.ajaxrequests_view, name='ajax_requests'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
