import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE
from django.db.models.query_utils import Q
from django.utils import timezone

from datetime import datetime
# api/models.py
from django.db import models

# Catalogos

class CatalogoBase(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta: # type: ignore
        abstract = True

    def __str__(self):
        return self.nombre

# Catalogos:
class CausaMuerte(CatalogoBase): pass
class IntegridadCadaverica(CatalogoBase): pass
class EstadoPreservacion(CatalogoBase): pass
class EstadoMuestra(CatalogoBase): pass
class TipoResguardo(CatalogoBase): pass
class Municipios(CatalogoBase): pass
class SedeAcnid(CatalogoBase): pass
class EstadoActual(CatalogoBase): pass
class Sexo(CatalogoBase): pass
class TipoInhumacion(CatalogoBase): pass
class IndividuosInhumacion(CatalogoBase): pass
class RelacionAnatomicaInhumacion(CatalogoBase): pass
class CircunstanciasExtraordinarias(CatalogoBase): pass
class AMP_UEI_INV(CatalogoBase): pass
class DistritoJudicial(CatalogoBase): pass
class TemporalidadDia(CatalogoBase): pass
class ClasificacionEvento(CatalogoBase): pass
class TipoEvento(CatalogoBase): pass
class EstadoRepublica(CatalogoBase): pass
class Paises(CatalogoBase): pass
class MunicipioZacatecas(CatalogoBase): pass
class ClimaSitio(CatalogoBase): pass
class EspacioEspecifico(CatalogoBase): pass
class AmbienteSitio(CatalogoBase): pass
class ColocacionCPM(CatalogoBase): pass
class VestimentaCPM(CatalogoBase): pass
class CircunstanciasCPMHallazgo(CatalogoBase): pass
class UbicacionCPM(CatalogoBase): pass
class PosicionCadavericaCPM(CatalogoBase): pass
class FlexionDelCuerpoCPM(CatalogoBase): pass
class MunicipioSemefo(CatalogoBase): pass
class CriminalistaCampo(CatalogoBase): pass
class ElementoBiologico(CatalogoBase): pass
class ElementosBiologicosReferenciales(CatalogoBase): pass
class MedioReconocimiento(CatalogoBase): pass
class AreaReconocimientoPositivo(CatalogoBase): pass
class Parentesco(CatalogoBase): pass
class VinculoBiologico(CatalogoBase): pass

# ======================== MEDIA FILIACION ======================
# Frente
class AlturaFrente(CatalogoBase): pass
class AnchuraFrente(CatalogoBase): pass
class FormaContornoSuperiorFrente(CatalogoBase): pass
class CaracteristicasExtraordinariasFrente(CatalogoBase): pass
# Cabello
class CantidadCabello(CatalogoBase): pass
class CabelloCalvicie(CatalogoBase): pass
class ColorCabello(CatalogoBase): pass
class Calvicie(CatalogoBase): pass
class NivelCalvicie(CatalogoBase): pass
class TexturaCabello(CatalogoBase): pass
class LongitudCabello(CatalogoBase): pass
# Boca
class TamanioBoca(CatalogoBase): pass
class LabiosBoca(CatalogoBase): pass
# Ojos
class InsercionProfundidadOjos(CatalogoBase): pass
class FormaOjos(CatalogoBase): pass
class TamanioOjos(CatalogoBase): pass
class ColorOjos(CatalogoBase): pass
# Orejas
class FormaOrejas(CatalogoBase): pass
class SeparacionOrejas(CatalogoBase): pass
class TamanioLobuloOrejas(CatalogoBase): pass
class TamanioOrejas(CatalogoBase): pass
class InsercionLobuloOrejas(CatalogoBase): pass
# Nariz
class TamanioNariz(CatalogoBase): pass
class PerfilNariz(CatalogoBase): pass
class AletasNariz(CatalogoBase): pass
class FormaNariz(CatalogoBase): pass
class TerminacionNariz(CatalogoBase): pass
# Varios
class Complexion(CatalogoBase): pass
class AparienciaRacial(CatalogoBase): pass
class ColorTez(CatalogoBase): pass
class FormaRostro(CatalogoBase): pass
class TipoPerfil(CatalogoBase): pass
class FormaCejas(CatalogoBase): pass
class GrosorCejas(CatalogoBase): pass
class Bigote(CatalogoBase): pass
class FormaMenton(CatalogoBase): pass
class Barba(CatalogoBase): pass


# Relaciones

# Normales

class Dependencia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    region = models.ForeignKey(SedeAcnid, on_delete=CASCADE)

    def __str__(self): 
        return f"{self.nombre} (self.region)"

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    dependencia = models.ForeignKey(Dependencia, related_name='departmentos', on_delete=CASCADE)

    def __str__(self):
        return f"Departamento de {self.nombre} ({self.dependencia})"

class TipoMuestra(CatalogoBase):
    departamento = models.ForeignKey(Departamento, on_delete=CASCADE)

class AgenteMP(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Agente del MP {self.nombres} ({self.posicion})"

class Perito(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_empleado = models.CharField(max_length=100, unique=True)
    
    dependencia = models.ForeignKey(Dependencia, related_name='peritos', on_delete=CASCADE)
    departmento = models.ForeignKey(Departamento, related_name='peritos', on_delete=CASCADE)

    def __str__(self):
        return f"Perito {self.numero_empleado}, {self.departmento} ({self.dependencia})"

class CarpetaInvestigacion(models.Model):
    cui = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.cui

class Caso(models.Model):
    carpeta_investigacion = models.ForeignKey(CarpetaInvestigacion, on_delete=CASCADE)
    
    year = models.IntegerField(default=timezone.now().year)
    consecutivo = models.PositiveIntegerField(editable=False)
    region = models.ForeignKey(SedeAcnid, on_delete=CASCADE)
    cni = models.BooleanField(default=False)
    identificador = models.CharField(max_length=50, blank=True, unique=True, editable=False)

    class Meta: # type: ignore
        constraints = [
            UniqueConstraint(fields=['year', 'region', 'consecutivo'], 
                             name='unique_year_region_consecutivo_for_cni', 
                             condition=Q(cni=True)),
            UniqueConstraint(fields=['year', 'region', 'consecutivo'], 
                             name='unique_year_region_consecutivo_for_not_cni', 
                             condition=Q(cni=False)),
                ]

    def save(self, *args, **kwargs):
        if not self.pk:
            last_record = Caso.objects.filter(year=self.year, cni=self.cni, region=self.region).order_by('-consecutivo').first()
            if last_record:
                self.consecutivo = last_record.consecutivo + 1
            else:
                self.consecutivo = 1
        if not self.identificador:
            self.identificador = f"{'CNI' if self.cni else 'CI'} {self.consecutivo}/{self.region}/{self.year}"
        super(Caso, self).save(*args, **kwargs)

    def __str__(self):
        return self.identificador
    
    def __repr__(self):
        return f"Caso(cni={self.cni}, identificador={self.identificador}"

class MediaFiliacion(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    alturafrente = models.ForeignKey(AlturaFrente, on_delete=CASCADE, default=1)
    anchurafrente = models.ForeignKey(AnchuraFrente, on_delete=CASCADE, default=1)
    formacontornosuperiorfrente = models.ForeignKey(FormaContornoSuperiorFrente, on_delete=CASCADE, default=1)
    caracteristicasextraordinariasfrente = models.ForeignKey(CaracteristicasExtraordinariasFrente, on_delete=CASCADE, default=1)
    cantidadcabello = models.ForeignKey(CantidadCabello, on_delete=CASCADE, default=1)
    cabellocalvicie = models.ForeignKey(CabelloCalvicie, on_delete=CASCADE, default=1)
    colorcabello = models.ForeignKey(ColorCabello, on_delete=CASCADE, default=1)
    calvicie = models.ForeignKey(Calvicie, on_delete=CASCADE, default=1)
    nivelcalvicie = models.ForeignKey(NivelCalvicie, on_delete=CASCADE, default=1)
    texturacabello = models.ForeignKey(TexturaCabello, on_delete=CASCADE, default=1)
    longitudcabello = models.ForeignKey(LongitudCabello, on_delete=CASCADE, default=1)
    tamanioboca = models.ForeignKey(TamanioBoca, on_delete=CASCADE, default=1)
    labiosboca = models.ForeignKey(LabiosBoca, on_delete=CASCADE, default=1)
    insercionprofundidadojos = models.ForeignKey(InsercionProfundidadOjos, on_delete=CASCADE, default=1)
    formaojos = models.ForeignKey(FormaOjos, on_delete=CASCADE, default=1)
    tamanioojos = models.ForeignKey(TamanioOjos, on_delete=CASCADE, default=1)
    colorojos = models.ForeignKey(ColorOjos, on_delete=CASCADE, default=1)
    formaorejas = models.ForeignKey(FormaOrejas, on_delete=CASCADE, default=1)
    separacionorejas = models.ForeignKey(SeparacionOrejas, on_delete=CASCADE, default=1)
    tamaniolobuloorejas = models.ForeignKey(TamanioLobuloOrejas, on_delete=CASCADE, default=1)
    tamanioorejas = models.ForeignKey(TamanioOrejas, on_delete=CASCADE, default=1)
    insercionlobuloorejas = models.ForeignKey(InsercionLobuloOrejas, on_delete=CASCADE, default=1)
    tamanionariz = models.ForeignKey(TamanioNariz, on_delete=CASCADE, default=1)
    perfilnariz = models.ForeignKey(PerfilNariz, on_delete=CASCADE, default=1)
    aletasnariz = models.ForeignKey(AletasNariz, on_delete=CASCADE, default=1)
    formanariz = models.ForeignKey(FormaNariz, on_delete=CASCADE, default=1)
    terminacionnariz = models.ForeignKey(TerminacionNariz, on_delete=CASCADE, default=1)
    complexion = models.ForeignKey(Complexion, on_delete=CASCADE, default=1)
    aparienciaracial = models.ForeignKey(AparienciaRacial, on_delete=CASCADE, default=1)
    colortez = models.ForeignKey(ColorTez, on_delete=CASCADE, default=1)
    formarostro = models.ForeignKey(FormaRostro, on_delete=CASCADE, default=1)
    tipoperfil = models.ForeignKey(TipoPerfil, on_delete=CASCADE, default=1)
    formacejas = models.ForeignKey(FormaCejas, on_delete=CASCADE, default=1)
    grosorcejas = models.ForeignKey(GrosorCejas, on_delete=CASCADE, default=1)
    bigote = models.ForeignKey(Bigote, on_delete=CASCADE, default=1)
    formamenton = models.ForeignKey(FormaMenton, on_delete=CASCADE, default=1)
    barba = models.ForeignKey(Barba, on_delete=CASCADE, default=1)
    
    def __str__(self):
        return f"MediaFiliacion({self.pk}"


class CronotanatoDiagnostico(models.Model):

    INTERVALOS = [
            ("EX", "Exacto"),
            ("MQ", "Mayor que"),
            ("mQ", "Menor que"),
            ("IN", "Intervalo")
            ]

    tipo_intervalo_pm = models.CharField(max_length=2, choices=INTERVALOS)
    limite_inferior_pm = models.IntegerField(default=-1)
    limite_superior_pm = models.IntegerField(default=-1)
    valor_exacto_pm = models.IntegerField(default=-1)
    
    def __str__(self):
        return f"Intervalo Post-Mortem ({self.pk}) {self.tipo_intervalo_pm}"


class Digitalizador(User):
    
    perito = models.ForeignKey(Perito, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.perito.numero_empleado}, {self.perito.departamento}, {self.groups}"

class DatosCaptura(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)
    capturista = models.ForeignKey(Digitalizador, on_delete=CASCADE)
    fecha_hora_captura = models.DateTimeField()


class DatosNecropsia(models.Model):
    desmembrado = models.ForeignKey(CircunstanciasExtraordinarias, on_delete=CASCADE)
    integridad_cadaverica = models.ForeignKey(IntegridadCadaverica, on_delete=CASCADE)
    municipio = models.ForeignKey(MunicipioZacatecas, on_delete=CASCADE)
    resguardo = models.ForeignKey(TipoResguardo, on_delete=CASCADE)
    fecha_ingreso_ml = models.DateField()
    inicio_necropsia = models.TimeField()
    cronotanatodx = models.ForeignKey(CronotanatoDiagnostico, on_delete=CASCADE)
    estado_preservacion = models.ForeignKey(EstadoPreservacion, on_delete=CASCADE)
    causa_muerte = models.ForeignKey(CausaMuerte, on_delete=CASCADE)
    
    def __str__(self):
        return f"DatosNecropsia({self.pk})"


class DatosMedicinaLegal(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    datos_necro = models.ForeignKey(DatosNecropsia, on_delete=CASCADE)
    
    capturas_por_mes = models.CharField(max_length=100)
    medico_designa = models.CharField(max_length=100)
    medico_deignado = models.CharField(max_length=100)
    via = models.CharField(max_length=100)
    desparicion_forzada = models.CharField(max_length=100)
    lugar_uei = models.CharField(max_length=100)
    muestras_recolectadas = models.CharField(max_length=100)
    numero_oficio_ml = models.CharField(max_length=100)
    secretario = models.CharField(max_length=100)
    fecha_entrega_bodega = models.DateField(max_length=100)
    receptor_bodega = models.CharField(max_length=100)
    folio_certificado_defuncion = models.CharField(max_length=100)
    oirgen_occiso = models.CharField(max_length=100)
    fecha_entrega_hoja_rosa_inegi = models.DateField(max_length=100)
    observaciones = models.CharField(max_length=100)
    adicciones = models.CharField(max_length=100)
    fecha_entrega = models.DateField(max_length=100)
    nombre_occiso = models.CharField(max_length=100)
    sexo = models.ForeignKey(Sexo, on_delete=CASCADE)
    edad = models.CharField(max_length=100)
    
    def __str__(self):
        return f"DatosML({self.pk}, caso={self.caso})"


class SolicitudMuestra(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    departamento = models.ForeignKey(Departamento, on_delete=CASCADE)
    estado = models.ForeignKey(EstadoMuestra, on_delete=CASCADE)
    tipo = models.ForeignKey(TipoMuestra, on_delete=CASCADE)
    comentarios = models.TextField()
    fecha_solicitud = models.DateField()
    fecha_finalizacion = models.DateField()
    
    def __str__(self):
        return f"SolicitudMuestra({self.pk}, caso={self.caso}, dpto={self.departamento})"

def upload_to(instance, filename):
    caso_value = instance.caso
    folder_name = f'data/{caso_value}'
    return os.path.join(folder_name, filename)


class DatosGeneralesACNID(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    estatus = models.ForeignKey(EstadoActual, on_delete=CASCADE, default=1)
    no_control_acnid = models.CharField(max_length=100)
    no_control_medleg = models.CharField(max_length=100)
    fecha_ingreso= models.DateField(max_length=100)
    edad = models.CharField(max_length=100, default=10)
    sexo = models.ForeignKey(Sexo, on_delete=CASCADE, default=1)
    # TODO: SETUP IMAGE SERVING ON VIEWS WITH THE PRIMARY KEY OF THE 'CASO'
    foto_rostro = models.ImageField(upload_to=upload_to, blank=True, null=True)
    foto_panoramica = models.ImageField(upload_to=upload_to, blank=True, null=True)
    
    def __str__(self):
        return f"DatosGeneralesACNID({self.pk}, caso={self.caso})"


class DatosCriminalisticaCampo(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    inhumacion_irregular = models.BooleanField()
    tipo_inhumacion_irregular = models.ForeignKey(TipoInhumacion, on_delete=CASCADE)
    numero_individuos = models.ForeignKey(IndividuosInhumacion, on_delete=CASCADE)
    relacion_anatomica = models.ForeignKey(RelacionAnatomicaInhumacion, on_delete=CASCADE)
    indicio = models.CharField(max_length=100)
    perito = models.ForeignKey(Perito, on_delete=CASCADE)
    no_oficio_dictamen = models.CharField(max_length=100)


class Evento(models.Model):
    
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    clasificacion_evento = models.ForeignKey(ClasificacionEvento, on_delete=CASCADE)
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=CASCADE)
    estado = models.ForeignKey(EstadoRepublica, on_delete=CASCADE)
    municipio = models.ForeignKey(Municipios, on_delete=CASCADE)
    localidad_comunidad_ranchera = models.CharField(max_length=100)
    lugar_hechos = models.CharField(max_length=100)
    coordenadas = models.CharField(max_length=100)
    
    # Datos del sitio
    tipo_sitio = models.CharField(max_length=1, choices=[("A", "Abierto"), ("C", "Cerrado")])
    propiedad = models.CharField(max_length=2, choices=[("pr", "privado"), ("pu", "publico")])
    clima = models.ForeignKey(ClimaSitio, on_delete=CASCADE)
    temporalidad = models.ForeignKey(TemporalidadDia, on_delete=CASCADE)
    ambiente = models.ForeignKey(EspacioEspecifico, on_delete=CASCADE)
    colocacion_cpm = models.ForeignKey(ColocacionCPM, on_delete=CASCADE)

    # Datos del CPM
    circunstancias_cpm = models.CharField(max_length=1, choices=[("C", "Cubierto"), ("E", "Expuesto")])
    vestimenta = models.ForeignKey(VestimentaCPM, on_delete=CASCADE)
    circustancias_extra = models.ForeignKey(CircunstanciasExtraordinarias, on_delete=CASCADE)
    ubicacion_cpm = models.ForeignKey(UbicacionCPM, on_delete=CASCADE)
    posicion_cadaverica = models.ForeignKey(PosicionCadavericaCPM, on_delete=CASCADE)
    flexion_cuerpo = models.ForeignKey(FlexionDelCuerpoCPM, on_delete=CASCADE)
    

class ElementosAsociados(models.Model):
    choices = [
        ("OV", "Objetos varios"),
        ("MQ", "Medicos quirurjucios"),
        ("MG", "Materiales de guerra"),
        ("MCO", "Mensajes del crimen organizado"),
        ("VM", "Vehiculos motorizados" )]

    tipo_elemento = models.CharField(max_length=3, choices=choices)
    descripcion_elemento = models.TextField()


class ElementosAsociadosEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=CASCADE)
    elementos = models.ForeignKey(ElementosAsociados, on_delete=CASCADE)
    

class DatosGeneralesGenetica(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    vinculo_biologico_con_resultado_adn = models.CharField(max_length=100)
    pocentaje_correspondencia = models.CharField(max_length=100)
    fecha_emision_resultado = models.CharField(max_length=100)


class DatosGeneticaRelativo(models.Model):
    datos_generales = models.ForeignKey(DatosGeneralesGenetica, on_delete=CASCADE)

    amp_solicita_cotejo_adn = models.ForeignKey(AgenteMP, on_delete=CASCADE)
    no_oficio_solicitud_muestra_cotejo = models.CharField(max_length=100)
    perito_toma_muestra_familiar = models.ForeignKey(Perito, on_delete=CASCADE, related_name="perito_toma_muestra_familiar")
    fecha_toma_muestra_familiar = models.DateField()
    nombre_familiar_muestra = models.CharField(max_length=200)
    muestra_biologica_referencia_familiar = models.ForeignKey(ElementosBiologicosReferenciales, on_delete=CASCADE)
    folio_ingreso_muestra_bd_lab = models.CharField(max_length=100)
    parentesco_con_cpm = models.ForeignKey(Parentesco, on_delete=CASCADE)
    perito_responsable_confronta = models.ForeignKey(Perito, related_name='perito_responsable_confronta', on_delete=models.CASCADE)


class DatosGeneticaCPM(models.Model):
    datos_generales = models.ForeignKey(DatosGeneralesGenetica, on_delete=CASCADE)

    responsable_muestra_adn = models.ForeignKey(Perito, on_delete=CASCADE)
    oficio_solicitud_muestra_adn = models.CharField(max_length=100)
    fecha_toma_muestra = models.DateField()
    elemento_biologico_referencia = models.ForeignKey(ElementoBiologico, on_delete=CASCADE)
    clave_interna_lab = models.CharField(max_length=100)
    folio_interno_ingreso_muestra_bd_lab = models.CharField(max_length=100)
    muestra_procesada = models.ForeignKey(TipoMuestra, on_delete=CASCADE)
    existe_perfil_genetico = models.BooleanField()


class DatosGeneralesAntropologia(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    perito = models.ForeignKey(Perito, on_delete=CASCADE)
    numero_oficio_solicitud_analisis = models.CharField(max_length=100)
    fecha_analisis = models.DateField(max_length=100)
    fecha_emision_resultado = models.DateField(max_length=100)
    no_oficio_dictamen = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    sexo = models.ForeignKey(Sexo, on_delete=CASCADE)


class DatosGeneralesArqueologia(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    perito = models.ForeignKey(Perito, on_delete=CASCADE)
    numero_oficio_solicitud_analisis = models.CharField(max_length=100)
    fecha_analisis = models.DateField(max_length=100)
    fecha_emision_resultado = models.DateField(max_length=100)
    no_oficio_dictamen = models.CharField(max_length=100)

class UnidadInvestigacion(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)
    amp_unidad_inv = models.ForeignKey(AgenteMP, on_delete=CASCADE, related_name="amp_unidad_inv")
    
    distrito_judicial = models.ForeignKey(DistritoJudicial, on_delete=CASCADE)
    nombre_fiscal_amp = models.ForeignKey(AgenteMP, on_delete=CASCADE, related_name="nombre_fiscal_amp")
    # solicitud de necropsia
    nombre_personal_solicitud = models.ForeignKey(Perito, related_name="nombre_personal_solicitud_necropsia", on_delete=CASCADE)
    cargo_personal_solicitud  = models.ForeignKey(Perito, related_name="cargo_personal_solicitud_necropsia", on_delete=CASCADE)


class DatosGeneralesOdontologia(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    perito = models.ForeignKey(Perito, on_delete=CASCADE)
    fecha_analisis = models.DateField()
    edad = models.CharField(max_length=100)


class DatosGeneralesDactiloscopia(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    perito = models.ForeignKey(Perito, on_delete=CASCADE)
    no_oficio_ficha_necrodactilar = models.CharField(max_length=100)
    fecha_oficio_ficha_necrodactilar = models.DateField()
    perito_toma_ficha_necrodactilar = models.ForeignKey(Perito, related_name="perito_toma_ficha_necrodactilar", on_delete=CASCADE)
    no_folio_resultado = models.CharField(max_length=100)
    fecha_emision_resultado = models.DateField(max_length=100)
    nombre_resultado_afis = models.CharField(max_length=100)
    domicilio_persona = models.TextField(max_length=100)
    tipo_registro = models.CharField(max_length=100)

class DatoIdentificador(models.Model):
    choices = [
            ("SPM", "senias particulares dientes"),
            ("SPV", "senias particulares varias"),
            ("TAT", "tatuajes"),
            ("PV", "pertenencias varias"),
            ("VES", "vestimenta"),
            ("CAL", "calzado ")
            ]

    tipo = models.CharField(max_length=3, choices=choices)
    descripcion = models.TextField()


class DatoIdentificadorCaso(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)
    dato_identificador = models.ForeignKey(DatoIdentificador, on_delete=CASCADE)


class HipotesisInvestigacion(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    correspondencia_plataforma_occsisos = models.BooleanField()
    cotejo_huellas_ine = models.BooleanField()
    cotejo_huellas_afis = models.BooleanField()
    vinculo_biologico_perfil_genetico = models.BooleanField()


class DatosReconocimiento(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    fecha_reconocimiento = models.DateField()
    sistema_identificacion = models.ForeignKey(MedioReconocimiento, on_delete=CASCADE)
    area_que_atiende = models.ForeignKey(AreaReconocimientoPositivo, on_delete=CASCADE)
    nombre_cadaver_identificado = models.CharField(max_length=150)
    foto_en_vida = models.DateField()
    fecha_nacimiento = models.DateField()
    municipio_nacimiento = models.ForeignKey(Municipios, on_delete=CASCADE)
    estado_nacimiento = models.ForeignKey(EstadoRepublica, on_delete=CASCADE)
    pais_nacimiento = models.ForeignKey(Paises, on_delete=CASCADE)
    persona_que_reconocio = models.CharField(max_length=150)
    parentesco_con_quien_reconoce = models.ForeignKey(Parentesco, on_delete=CASCADE)


class DatosOficioAutorizacionEntrega(models.Model):
    caso = models.ForeignKey(Caso, on_delete=CASCADE)

    no_autorizacion_entrega = models.CharField(max_length=150)
    fecha_entrega = models.DateField()
    amp_autoriza_entrega = models.ForeignKey(AgenteMP, on_delete=CASCADE)
    distrito_judicial = models.ForeignKey(DistritoJudicial, on_delete=CASCADE)
    nombre_licenciado = models.CharField(max_length=150)
    destino_actual_transitorio = models.CharField(max_length=150)
    destino_final = models.CharField(max_length=150)
