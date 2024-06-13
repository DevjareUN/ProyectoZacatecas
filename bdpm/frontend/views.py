from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from api.serializers import *
from frontend.forms import FormACNID

from .forms import FormDatosGeneralesACNID, FormMediaFiliacion, FormMedicinaLegal

# Create your views here.
def index(request):
    return render(request, template_name="frontend/home.html", context={ "data": 123 })

class Login(LoginView):
    redirect_authenticated_user = True
    template_name = "registration/login.html"

    def get_success_url(self):
        messages.success(self.request, f"User {self.request.user} successfully logged in!, redirecting...")
        return reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, f"Failed to authenticate user {self.request.user}.")
        return self.render_to_response(self.get_context_data(form=form))

# class Home(LoginRequiredMixin, TemplateView):
#     template_name = "frontend/home.html"

class Home(APIView):
    # permission_classes = [IsAuthenticated]  # Ensure the user is authenticated
    
    def get(self, request, *args, **kwargs):
        print(f"User tryng to get /home: {request.user}")
        if request.user.groups.filter(name = 'medicina_legal').exists():
            return render(request, 'medicina_legal/home.html', {"message": "Hello, ML Admin!, Showing quick info..."})
        elif request.user.groups.filter(name = 'acnid').exists():
    # TODO: SETUP IMAGE SERVING ON VIEWS WITH THE PRIMARY KEY OF THE 'CASO'
            lista_estatus = list(EstadoActual.objects.all().values_list("nombre", flat=True))
            lista_sexo = list(Sexo.objects.all().values_list("nombre", flat=True))
            metadata = { 
                        "caso": { "display_name": "Caso CNI" }, 
                        "estatus": { 
                                    "display_name": "Estado actual",
                                    "catalogue": lista_estatus
                                    }, 
                        "no_control_acnid": { "display_name": "No. Control ACNID" }, 
                        "no_control_medleg": { "display_name": "No. Control MedLeg" },
                        "fecha_ingreso": { "display_name": "Fecha ingreso" },
                        "edad": { "display_name": "Edad" },
                        "sexo": { 
                                 "display_name": "Sexo" ,
                                 "catalogue": lista_sexo
                                 },
                        "foto_rostro": { "display_name": "Foto rostro" },
                        "foto_panoramica": { "display_name": "Foto panoramica" },
                        }

            return render(request, 'acnid/home.html', { "meta": metadata })
        else:
            return redirect("login")


class Capture(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'medicina_legal').exists():
            form = FormMedicinaLegal()
            return render(request, 'medicina_legal/capture.html', { 
                                                                   "form": form 
                                                                   })
        elif request.user.groups.filter(name = 'acnid').exists():
            form = FormACNID()
            return render(request, 'acnid/capture.html', { "data": list(Caso.objects.all()), "form": form })
        else:
            return redirect("/login")

    def post(self, request, *args, **kwargs):
        if request.user.groups.filter(name='medicina_legal').exists():
            form = FormMedicinaLegal(request.POST)
            if form.is_valid():
                # Process the form data for 'medicina_legal' group
                # form.cleaned_data['field_name']
                return redirect('home')  # Replace with your success URL
        
        elif request.user.groups.filter(name='acnid').exists():
            caso_id = request.POST.get('caso')
            form_datos_generales = FormDatosGeneralesACNID(request.POST, request.FILES)
            form_media_filiacion = FormMediaFiliacion(request.POST, request.FILES)
            
            if form_datos_generales.is_valid():
                # Process and save form_datos_generales data
                print(f"Datos generales desde formulario: {form_datos_generales.cleaned_data}")
                # Process and save form_media_filiacion data
                # Extract primary keys from related objects
                estatus_pk = form_datos_generales.cleaned_data['estatus'].pk
                sexo_pk = form_datos_generales.cleaned_data['sexo'].pk

                # Modify cleaned data to use primary keys
                form_datos_generales.cleaned_data['estatus'] = estatus_pk
                form_datos_generales.cleaned_data['sexo'] = sexo_pk
                cleaned_data = form_datos_generales.cleaned_data
                cleaned_data['caso'] = caso_id
                
                estatus_pk = form_datos_generales.cleaned_data['estatus'].pk

                serializer = DatosGeneralesACNIDSerializer(data=cleaned_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'success': True, 'message': 'Form submitted successfully'})
                else:
                    return JsonResponse({'success': False, 'errors': serializer.errors})
            elif form_media_filiacion.is_valid():
                print(f"Submitting Media filiacion")
                # Changing to PKs
                cleaned_data = {}
                for key, value in form_datos_generales.cleaned_data.items():
                    print(f"Replacing cleaned_data[{key}]={value}, with {value.pk}")
                    cleaned_data[key] = value.pk

                cleaned_data['caso'] = caso_id 
                print(f"Cleaned data: {cleaned_data}")

                serializer = MediaFiliacionSerializer(data=cleaned_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'success': True, 'message': 'Form submitted successfully'})
                else:
                    return JsonResponse({'success': False, 'errors': serializer.errors})
            else:
                errors = form_datos_generales.errors if not form_datos_generales.is_valid() else form_media_filiacion.errors
                return JsonResponse({'success': False, 'errors': errors})
        else:
            return redirect("/login")

        # If the form is invalid, re-render the page with the form
        if request.user.groups.filter(name='medicina_legal').exists():
            return render(request, 'medicina_legal/capture.html', {"form": form})
        elif request.user.groups.filter(name='acnid').exists():
            return render(request, 'acnid/capture.html', {"form": form})


class Lookup(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'medicina_legal').exists():
            return render(request, 'medicina_legal/lookup.html', {"message": "Hello, ML Admin!, Looking fields up..."})
        elif request.user.groups.filter(name = 'acnid').exists():
            return render(request, 'acnid/lookup.html', {"message": "Hello, ACNID Admin!, Looking fields up..."})
        else:
            return redirect("/login")


# Form views
# =====================================================================================
# ================================== Medicina legal ===================================
# =====================================================================================
# views.py
