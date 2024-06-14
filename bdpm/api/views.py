import os

from django.apps import apps
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.conf import settings
from rest_framework.views import Response

from .models import *
from .serializers import *

from rest_framework import viewsets

# Create your views here.
def auth(request):
    return JsonResponse({ "site": "/api/v1/auth", "msg": "API Auth!" })

def casos_sin_dato_x(request):
    model_name = request.GET.get('model', None)  # Get the model name from the GET parameters
    
    if model_name:
        try:
            # ModelClass = apps.get_model('api', model_name)
            casos_sin_x = Caso.objects.filter(**{ f'{model_name.lower()}__isnull': True })
        except LookupError:
            casos_sin_x = Caso.objects.none()
        
    else:
        casos_sin_x = Caso.objects.all()
    
    casos_sin_x = CasoSerializer(casos_sin_x, many=True)
    return JsonResponse(casos_sin_x.data, safe=False)

class CatalogobaseViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogoBaseSerializer

    def get_queryset(self):
        return self.model.objects.all()


class CasoViewSet(viewsets.ModelViewSet):
    queryset = Caso.objects.all()
    serializer_class = CasoSerializer


class TipoMuestraViewSet(viewsets.ModelViewSet):
    queryset = TipoMuestra.objects.all()
    serializer_class = TipoMuestraSerializer



class PeritoViewSet(viewsets.ModelViewSet):
    queryset = Perito.objects.all()
    serializer_class = PeritoSerializer

class DatosCapturaViewSet(viewsets.ModelViewSet):
    queryset = DatosCaptura.objects.all()
    serializer_class = DatosCapturaSerializer

class DependenciaViewSet(viewsets.ModelViewSet):
    queryset = Dependencia.objects.all()
    serializer_class = DependenciaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class AgenteMPViewSet(viewsets.ModelViewSet):
    queryset = AgenteMP.objects.all()
    serializer_class = AgenteMPSerializer

class CarpetaInvestigacionViewSet(viewsets.ModelViewSet):
    queryset = CarpetaInvestigacion.objects.all()
    serializer_class = CarpetaInvestigacionSerializer

class CronotanatoDiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = CronotanatoDiagnostico.objects.all()
    serializer_class = CronotanatoDiagnosticoSerializer


class DigitalizadorViewSet(viewsets.ModelViewSet):
    queryset = Digitalizador.objects.all()
    serializer_class = DigitalizadorSerializer


class DatosNecropsiaViewSet(viewsets.ModelViewSet):
    queryset = DatosNecropsia.objects.all()
    serializer_class = DatosNecropsiaSerializer


class DatosMedicinaLegalViewSet(viewsets.ModelViewSet):
    queryset = DatosMedicinaLegal.objects.all()
    serializer_class = DatosMedicinaLegalSerializer

class SolicitudMuestraViewSet(viewsets.ModelViewSet):
    queryset = SolicitudMuestra.objects.all()
    serializer_class = SolicitudMuestraSerializer




class DatosGeneralesACNIDViewSet(viewsets.ModelViewSet):
    queryset = DatosGeneralesACNID.objects.all()
    serializer_class = DatosGeneralesACNIDSerializer



def serve_image(request, filename):
    image_path = os.path.join(settings.MEDIA_ROOT, filename)
    with open(image_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")  # Adjust content type as needed


class DatosCriminalisticaCampoViewSet(viewsets.ModelViewSet):
    queryset = DatosCriminalisticaCampo.objects.all()
    serializer_class = DatosCriminalisticaCampoSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class ElementosAsociadosViewSet(viewsets.ModelViewSet):
    queryset = ElementosAsociados.objects.all()
    serializer_class = ElementosAsociadosSerializer


class ElementosAsociadosEventoViewSet(viewsets.ModelViewSet):
    queryset = ElementosAsociadosEvento.objects.all()
    serializer_class = ElementosAsociadosEventoSerializer


class DatosGeneralesGeneticaViewSet(viewsets.ModelViewSet):
    queryset = DatosGeneralesGenetica.objects.all()
    serializer_class = DatosGeneralesGeneticaSerializer


class DatosGeneticaRelativoViewSet(viewsets.ModelViewSet):
    queryset = DatosGeneticaRelativo.objects.all()
    serializer_class = DatosGeneticaRelativoSerializer


class DatosGeneticaCPMViewSet(viewsets.ModelViewSet):
    queryset = DatosGeneticaCPM.objects.all()
    serializer_class = DatosGeneticaCPMSerializer


class DatosGeneralesAntropologiaViewSet(viewsets.ModelViewSet):
    queryset = DatosGeneralesAntropologia.objects.all()
    serializer_class = DatosGeneralesAntropologiaSerializer


class DatosGeneralesArqueologiaViewSet(viewsets.ModelViewSet):
    queryset = DatosGeneralesArqueologia.objects.all()
    serializer_class = DatosGeneralesArqueologiaSerializer


class UnidadInvestigacionViewSet(viewsets.ModelViewSet):
    queryset = UnidadInvestigacion.objects.all()
    serializer_class = UnidadInvestigacionSerializer


class DatosGeneralesOdontologiaViewSet(viewsets.ModelViewSet):
    queryset = DatosGeneralesOdontologia.objects.all()
    serializer_class = DatosGeneralesOdontologiaSerializer


class DatosGeneralesDactiloscopiaViewSet(viewsets.ModelViewSet):
    queryset = DatosGeneralesDactiloscopia.objects.all()
    serializer_class = DatosGeneralesDactiloscopiaSerializer


class DatoIdentificadorViewSet(viewsets.ModelViewSet):
    queryset = DatoIdentificador.objects.all()
    serializer_class = DatoIdentificadorSerializer


class DatoIdentificadorCasoViewSet(viewsets.ModelViewSet):
    queryset = DatoIdentificadorCaso.objects.all()
    serializer_class = DatoIdentificadorCasoSerializer


class HipotesisInvestigacionViewSet(viewsets.ModelViewSet):
    queryset = HipotesisInvestigacion.objects.all()
    serializer_class = HipotesisInvestigacionSerializer


class DatosReconocimientoViewSet(viewsets.ModelViewSet):
    queryset = DatosReconocimiento.objects.all()
    serializer_class = DatosReconocimientoSerializer


class DatosOficioAutorizacionEntregaViewSet(viewsets.ModelViewSet):
    queryset = DatosOficioAutorizacionEntrega.objects.all()
    serializer_class = DatosOficioAutorizacionEntregaSerializer


