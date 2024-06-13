# forms.py
from django import forms
from api.models import *
from frontend.utils import snake_to_spaces

from .utils import camel_case_to_spaces
# ==================================================================================
# ======================== Formularios Medicina Legal ==============================
# ==================================================================================
class FormDatosNecropsia(forms.Form):
    # Fields from DatosNecropsia
    caso = forms.ModelChoiceField(queryset=Caso.objects.all())
    desmembrado = forms.ModelChoiceField(queryset=CircunstanciasExtraordinarias.objects.all())
    integridad_cadaverica = forms.ModelChoiceField(queryset=IntegridadCadaverica.objects.all())
    municipio = forms.ModelChoiceField(queryset=MunicipioZacatecas.objects.all())
    resguardo = forms.ModelChoiceField(queryset=TipoResguardo.objects.all())
    fecha_ingreso_ml = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "form-select w-auto d-inline-block" }))
    inicio_necropsia = forms.TimeField(help_text="Tiempo en formato 24 horas (Por ejemplo: 00:10, 22:54, 06:10)")
    estado_preservacion = forms.ModelChoiceField(queryset=EstadoPreservacion.objects.all())
    causa_muerte = forms.ModelChoiceField(queryset=CausaMuerte.objects.all())
    tipo_intervalo_pm = forms.ChoiceField(choices=CronotanatoDiagnostico.INTERVALOS)
    limite_inferior_pm = forms.IntegerField()
    limite_superior_pm = forms.IntegerField()
    valor_exacto_pm = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        super(FormDatosNecropsia, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'

class FormDatosMedicinaLegal(forms.Form):
    # Fields from DatosMedicinaLegal
    datos_necro = forms.ModelChoiceField(queryset=DatosNecropsia.objects.all())
    capturas_por_mes = forms.CharField(max_length=100)
    medico_designa = forms.CharField(max_length=100)
    medico_deignado = forms.CharField(max_length=100)
    via = forms.CharField(max_length=100)
    desparicion_forzada = forms.CharField(max_length=100)
    lugar_uei = forms.CharField(max_length=100)
    muestras_recolectadas = forms.CharField(max_length=100)
    numero_oficio_ml = forms.CharField(max_length=100)
    secretario = forms.CharField(max_length=100)
    fecha_entrega_bodega = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "form-select w-auto d-inline-block" }))
    receptor_bodega = forms.CharField(max_length=100)
    folio_certificado_defuncion = forms.CharField(max_length=100)
    oirgen_occiso = forms.CharField(max_length=100)
    fecha_entrega_hoja_rosa_inegi = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "form-select w-auto d-inline-block" }))
    observaciones = forms.CharField(max_length=100)
    adicciones = forms.CharField(max_length=100)
    fecha_entrega = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "form-select w-auto d-inline-block" }))
    nombre_occiso = forms.CharField(max_length=100)
    sexo = forms.ModelChoiceField(queryset=Sexo.objects.all())
    edad = forms.CharField(max_length=100)
    
    def __init__(self, *args, **kwargs):
        super(FormDatosMedicinaLegal, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'


class FormMedicinaLegal(forms.Form):
    # Example on how to use ForeignKeys
    # category = forms.ModelChoiceField(queryset=Category.objects.all())
    formDatosNecropsia = FormDatosNecropsia()
    formDatosMedicinaLegal = FormDatosMedicinaLegal()    

# ==================================================================================
# ============================ Formularios ACNID ===================================
# ==================================================================================

class FormMediaFiliacion(forms.ModelForm):
    
    class Meta: # type: ignore
        model = MediaFiliacion
        fields = "__all__"
        exclude = ['caso']  # Exclude specific fields

    
    def __init__(self, *args, **kwargs):
        super(FormMediaFiliacion, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'

        for field_name, field in self.fields.items():
            field.label = snake_to_spaces(field_name)


class FormDatosGeneralesACNID(forms.ModelForm):
    
    class Meta: # type: ignore
        model = DatosGeneralesACNID
        fields = "__all__"
        exclude = ['caso']  # Exclude specific fields
        widgets = {
            'fecha_ingreso': forms.SelectDateWidget(attrs={'class': 'form-select date-widget'}),
        }

    def __init__(self, *args, **kwargs):
        super(FormDatosGeneralesACNID, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'


class FormACNID(forms.Form):
    # Fields from DatosMedicinaLegal
    # datos_necro = forms.ModelChoiceField(queryset=DatosNecropsia.objects.all())
    formDatosGenerales = FormDatosGeneralesACNID()
    formMediaFiliacion = FormMediaFiliacion()

    def __init__(self, *args, **kwargs):
        super(FormACNID, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'


