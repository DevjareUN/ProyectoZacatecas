from rest_framework import serializers
from .models import *

from rest_framework import serializers

# ===============================================================================
# ================================= CATALOGOS ===================================
# ===============================================================================
class CatalogoBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoBase
        fields = "__all__"  # Include all fields from the model

class CausaMuerteSerializer(CatalogoBaseSerializer): pass
class IntegridadCadavericaSerializer(CatalogoBaseSerializer): pass
class TiposMuestrasSerializer(CatalogoBaseSerializer): pass
class EstadoPreservacionSerializer(CatalogoBaseSerializer): pass
class TipoResguardoSerializer(CatalogoBaseSerializer): pass
class MunicipiosSerializer(CatalogoBaseSerializer): pass
class SedeAcnidSerializer(CatalogoBaseSerializer): pass
class EstadoActualSerializer(CatalogoBaseSerializer): pass
class SexoSerializer(CatalogoBaseSerializer): pass
class TipoInhumacionSerializer(CatalogoBaseSerializer): pass
class IndividuosInhumacionSerializer(CatalogoBaseSerializer): pass
class RelacionAnatomicaInhumacionSerializer(CatalogoBaseSerializer): pass
class CircunstanciasExtraordinariasSerializer(CatalogoBaseSerializer): pass
class AMP_UEI_INVSerializer(CatalogoBaseSerializer): pass
class DistritoJudicialSerializer(CatalogoBaseSerializer): pass
class TemporalidadDiaSerializer(CatalogoBaseSerializer): pass
class ClasificacionEventoSerializer(CatalogoBaseSerializer): pass
class TipoEventoSerializer(CatalogoBaseSerializer): pass
class EstadoRepublicaSerializer(CatalogoBaseSerializer): pass
class PaisesSerializer(CatalogoBaseSerializer): pass
class MunicipioZacatecasSerializer(CatalogoBaseSerializer): pass
class ClimaSitioSerializer(CatalogoBaseSerializer): pass
class EspacioEspecificoSerializer(CatalogoBaseSerializer): pass
class AmbienteSitioSerializer(CatalogoBaseSerializer): pass
class ColocacionCPMSerializer(CatalogoBaseSerializer): pass
class VestimentaCPMSerializer(CatalogoBaseSerializer): pass
class CircunstanciasCPMHallazgoSerializer(CatalogoBaseSerializer): pass
class UbicacionCPMSerializer(CatalogoBaseSerializer): pass
class PosicionCadavericaCPMSerializer(CatalogoBaseSerializer): pass
class FlexionDelCuerpoCPMSerializer(CatalogoBaseSerializer): pass
class MunicipioSemefoSerializer(CatalogoBaseSerializer): pass
class CriminalistaCampoSerializer(CatalogoBaseSerializer): pass
class ElementoBiologicoSerializer(CatalogoBaseSerializer): pass
class ElementosBiologicosReferencialesSerializer(CatalogoBaseSerializer): pass
class MedioReconocimientoSerializer(CatalogoBaseSerializer): pass
class AreaReconocimientoPositivoSerializer(CatalogoBaseSerializer): pass
class ParentescoSerializer(CatalogoBaseSerializer): pass
class VinculoBiologicoSerializer(CatalogoBaseSerializer): pass
# ======================== MEDIA FILIACION ======================
# Frente
class AlturaFrenteSerializer(CatalogoBaseSerializer): pass
class AnchuraFrenteSerializer(CatalogoBaseSerializer): pass
class FormaContornoSuperiorFrenteSerializer(CatalogoBaseSerializer): pass
class CaracteristicasExtraordinariasFrenteSerializer(CatalogoBaseSerializer): pass
# Cabello
class CantidadCabelloSerializer(CatalogoBaseSerializer): pass
class CabelloCalvicieSerializer(CatalogoBaseSerializer): pass
class ColorCabelloSerializer(CatalogoBaseSerializer): pass
class CalvicieSerializer(CatalogoBaseSerializer): pass
class NivelCalvicieSerializer(CatalogoBaseSerializer): pass
class TexturaCabelloSerializer(CatalogoBaseSerializer): pass
class LongitudCabelloSerializer(CatalogoBaseSerializer): pass
# Boca
class TamanioBocaSerializer(CatalogoBaseSerializer): pass
class LabiosBocaSerializer(CatalogoBaseSerializer): pass
# Ojos
class InsercionProfundidadOjosSerializer(CatalogoBaseSerializer): pass
class FormaOjosSerializer(CatalogoBaseSerializer): pass
class TamanioOjosSerializer(CatalogoBaseSerializer): pass
class ColorOjosSerializer(CatalogoBaseSerializer): pass
# Orejas
class FormaOrejasSerializer(CatalogoBaseSerializer): pass
class SeparacionOrejasSerializer(CatalogoBaseSerializer): pass
class TamanioLobuloOrejasSerializer(CatalogoBaseSerializer): pass
class TanaioOrejasSerializer(CatalogoBaseSerializer): pass
class InsercionLobuloOrejasSerializer(CatalogoBaseSerializer): pass
# Nariz
class TamanioNarizSerializer(CatalogoBaseSerializer): pass
class PerfilNarizSerializer(CatalogoBaseSerializer): pass
class AletasNarizSerializer(CatalogoBaseSerializer): pass
class FormaNarizSerializer(CatalogoBaseSerializer): pass
class TerminacionNarizSerializer(CatalogoBaseSerializer): pass
# Varios
class ComplexionSerializer(CatalogoBaseSerializer): pass
class AparienciaRacialSerializer(CatalogoBaseSerializer): pass
class ColorTezSerializer(CatalogoBaseSerializer): pass
class FormaRostroSerializer(CatalogoBaseSerializer): pass
class TipoPerfilSerializer(CatalogoBaseSerializer): pass
class FormaCejasSerializer(CatalogoBaseSerializer): pass
class GrosorCejasSerializer(CatalogoBaseSerializer): pass
class BigoteSerializer(CatalogoBaseSerializer): pass
class FormaMentonSerializer(CatalogoBaseSerializer): pass
class BarbaSerializer(CatalogoBaseSerializer): pass


# ===============================================================================
# ================================== Normales ===================================
# ===============================================================================

class PeritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perito
        fields = "__all__"
        read_only_fields = ['unique_key']


class CasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caso
        fields = ['carpeta_investigacion', 'year', 'consecutivo', 'region', 'cni', 'identificador']
        read_only_fields = ['identificador', 'consecutivo' ]


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"

class TipoMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMuestra
        fields = "__all__"

class AgenteMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenteMP
        fields = "__all__"

class CarpetaInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarpetaInvestigacion
        fields = "__all__"


class CronotanatoDiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronotanatoDiagnostico
        fields = "__all__"

class DigitalizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digitalizador
        fields = "__all__"

class DatosCapturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCaptura
        fields = "__all__"

class DatosNecropsiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosNecropsia
        fields = "__all__"

class DatosMedicinaLegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosMedicinaLegal
        fields = "__all__"

class SolicitudMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudMuestra
        fields = "__all__"

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = "__all__"

class MediaFiliacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFiliacion
        fields = "__all__"

class DatosGeneralesACNIDSerializer(serializers.ModelSerializer):

    estatus = serializers.SerializerMethodField()
    sexo = serializers.SerializerMethodField()
    caso = serializers.SerializerMethodField()

    class Meta:
        model = DatosGeneralesACNID
        fields = "__all__"
   
    def get_estatus(self, obj):
        return str(obj.estatus)

    def get_sexo(self, obj):
        return str(obj.sexo)

    def get_caso(self, obj):
        return str(obj.caso)

class DatosCriminalisticaCampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCriminalisticaCampo
        fields = "__all__"


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"


class ElementosAsociadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementosAsociados
        fields = "__all__"


class ElementosAsociadosEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementosAsociadosEvento
        fields = "__all__"


class DatosGeneralesGeneticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGeneralesGenetica
        fields = "__all__"


class DatosGeneticaRelativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGeneticaRelativo
        fields = "__all__"


class DatosGeneticaCPMSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGeneticaCPM
        fields = "__all__"


class DatosGeneralesAntropologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGeneralesAntropologia
        fields = "__all__"


class DatosGeneralesArqueologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGeneralesArqueologia
        fields = "__all__"


class UnidadInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadInvestigacion
        fields = "__all__"


class DatosGeneralesOdontologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGeneralesOdontologia
        fields = "__all__"


class DatosGeneralesDactiloscopiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGeneralesDactiloscopia
        fields = "__all__"


class DatoIdentificadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatoIdentificador
        fields = "__all__"


class DatoIdentificadorCasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatoIdentificadorCaso
        fields = "__all__"


class HipotesisInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HipotesisInvestigacion
        fields = "__all__"


class DatosReconocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosReconocimiento
        fields = "__all__"


class DatosOficioAutorizacionEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosOficioAutorizacionEntrega
        fields = "__all__"




# ===============================================================================
# ================================= Relaciones ==================================
# ===============================================================================

