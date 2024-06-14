# Urls
import re
from django.apps import apps
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.serializers import CatalogoBaseSerializer
from .views import *

from api import views

router = DefaultRouter()
router.register(r'caso', CasoViewSet, basename="caso")

router.register(r'dependencia', DependenciaViewSet, basename="dependencia")
router.register(r'departamento', DepartamentoViewSet, basename="departamento")
router.register(r'agentemp', AgenteMPViewSet, basename="AgenteMP")
router.register(r'perito', PeritoViewSet, basename="Perito")
router.register(r'carpetainvestigacion', CarpetaInvestigacionViewSet, basename="CarpetaInvestigacion")
router.register(r'cronotanatodiagnostico', CronotanatoDiagnosticoViewSet, basename="CronotanatoDiagnostico")
router.register(r'digitalizador', DigitalizadorViewSet, basename="Digitalizador")
router.register(r'datoscaptura', DatosCapturaViewSet, basename="DatosCaptura")
router.register(r'datosnecropsia', DatosNecropsiaViewSet, basename="DatosNecropsia")
router.register(r'datosmedicinalegal', DatosMedicinaLegalViewSet, basename="DatosMedicinaLegal")
router.register(r'solicitudmuestra', SolicitudMuestraViewSet, basename="SolicitudMuestra")
router.register(r'datosgeneralesacnid', DatosGeneralesACNIDViewSet, basename="DatosGeneralesACNID")
router.register(r'datoscriminalisticacampo', DatosCriminalisticaCampoViewSet, basename="DatosCriminalisticaCampo")
router.register(r'evento', EventoViewSet, basename="Evento")
router.register(r'elementosasociados', ElementosAsociadosViewSet, basename="ElementosAsociados")
router.register(r'elementosasociadosevento', ElementosAsociadosEventoViewSet, basename="ElementosAsociadosEvento")
router.register(r'datosgeneralesgenetica', DatosGeneralesGeneticaViewSet, basename="DatosGeneralesGenetica")
router.register(r'datosgeneticarelativo', DatosGeneticaRelativoViewSet, basename="DatosGeneticaRelativo")
router.register(r'datosgeneticacpm', DatosGeneticaCPMViewSet, basename="DatosGeneticaCPM")
router.register(r'datosgeneralesantropologia', DatosGeneralesAntropologiaViewSet, basename="DatosGeneralesAntropologia")
router.register(r'datosgeneralesarqueologia', DatosGeneralesArqueologiaViewSet, basename="DatosGeneralesArqueologia")
router.register(r'unidadinvestigacion', UnidadInvestigacionViewSet, basename="UnidadInvestigacion")
router.register(r'datosgeneralesodontologia', DatosGeneralesOdontologiaViewSet, basename="DatosGeneralesOdontologia")
router.register(r'datosgeneralesdactiloscopia', DatosGeneralesDactiloscopiaViewSet, basename="DatosGeneralesDactiloscopia")
router.register(r'datoidentificador', DatoIdentificadorViewSet, basename="DatoIdentificador")
router.register(r'datoidentificadorcaso', DatoIdentificadorCasoViewSet, basename="DatoIdentificadorCaso")
router.register(r'hipotesisinvestigacion', HipotesisInvestigacionViewSet, basename="HipotesisInvestigacion")
router.register(r'datosreconocimiento', DatosReconocimientoViewSet, basename="DatosReconocimiento")
router.register(r'datosoficioautorizacionentrega', DatosOficioAutorizacionEntregaViewSet, basename="DatosOficioAutorizacionEntrega")
router.register(r'mediafiliacion', MediaFiliacionViewSet, basename="MediaFiliacion")

# Add afterwards: 
# List your catalogue model names here
lista_catalogos = [  "IntegridadCadaverica", "EstadoPreservacion", "EstadoMuestra",
"TipoResguardo", "Municipios", "SedeAcnid", "Sexo", "TipoInhumacion", "EstadoActual",
"IndividuosInhumacion", "RelacionAnatomicaInhumacion", "CircunstanciasExtraordinarias", "AMP_UEI_INV", "DistritoJudicial", "TemporalidadDia",
"ClasificacionEvento","TipoEvento", "EstadoRepublica", "Paises", "MunicipioZacatecas", "ClimaSitio", "EspacioEspecifico", "AmbienteSitio",
"ColocacionCPM", "VestimentaCPM", "CircunstanciasCPMHallazgo", "UbicacionCPM", "PosicionCadavericaCPM", "FlexionDelCuerpoCPM",
"MunicipioSemefo", "CriminalistaCampo", "ElementoBiologico", "ElementosBiologicosReferenciales", "MedioReconocimiento",
"AreaReconocimientoPositivo", "Parentesco", "VinculoBiologico", "AlturaFrente", "AnchuraFrente", "FormaContornoSuperiorFrente",
"CaracteristicasExtraordinariasFrente", "CantidadCabello", "CabelloCalvicie", "ColorCabello", "Calvicie", "NivelCalvicie", "TexturaCabello",
"LongitudCabello", "TamanioBoca", "LabiosBoca", "InsercionProfundidadOjos", "FormaOjos", "TamanioOjos", "ColorOjos",
"FormaOrejas", "SeparacionOrejas", "TamanioLobuloOrejas", "TamanioOrejas", "InsercionLobuloOrejas", "TamanioNariz",
"PerfilNariz","AletasNariz", "FormaNariz", "TerminacionNariz", "Complexion", "AparienciaRacial", "ColorTez",
"FormaRostro", "TipoPerfil", "FormaCejas", "GrosorCejas", "Bigote", "FormaMenton", "Barba", "CausaMuerte"]


def pascal_to_snake_case(name):
    # Insert an underscore before each capital letter except the first one
    name = re.sub('([A-Z])', r'_\1', name)
    # Convert the entire string to lowercase
    return name.lower().lstrip('_')

for model_name in lista_catalogos:
    model = apps.get_model('api', model_name)
    serializer_meta = type(f'{model_name}Meta', (CatalogoBaseSerializer.Meta,), {'model': model})
    serializer_class = type(f'{model_name}Serializer', (CatalogoBaseSerializer,), {'Meta': serializer_meta})
    
    viewset_class = type(f'{model_name}ViewSet', (CatalogobaseViewSet,), {'model': model, 'serializer_class': serializer_class})

    router.register(f'catalogo/{model_name.lower()}', viewset_class, basename=pascal_to_snake_case(model_name))

urlpatterns = [
        path("auth/", views.auth),
        path('', include(router.urls)),
        path('serve-image/<str:filename>/', views.serve_image, name='serve_image'),
        path("casos_sin_x/", views.casos_sin_dato_x)
        ]
