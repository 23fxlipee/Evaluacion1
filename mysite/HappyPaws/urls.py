from django.urls import path

from . import views

urlpatterns = [
    path("inicio", views.index, name="inicio"),
    path("productos/perro", views.get_perros, name="perros"),
    path("productos/gato", views.get_gatos, name="gatos"),
    path("registro", views.get_registro, name="registro"),
    path("pago", views.get_pago, name="pago"),
    path("cuenta/<int:registro_id>", views.get_cuenta, name="cuenta"),
    path("cuenta/eliminar/<int:registro_id>/", views.delete_registro, name="borrar_registro"),
    path("cuenta/admin", views.get_lista_cuentas,name="cuentas"),
    path("cuenta/editar/<int:registro_id>", views.update_cuenta , name="editar_cuenta")
    ]