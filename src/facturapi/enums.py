"""Enum constants"""

from enum import Enum
from typing import NamedTuple


class PaymentForm(Enum):
    """SAT's payment form codes"""

    EFECTIVO = "01"
    CHEQUE_NOMINATIVO = "02"
    TRANSFERENCIA_ELECTRONICA_DE_FONDOS = "03"
    TARJETA_DE_CREDITO = "04"
    MONEDERO_ELECTRONICO = "05"
    DINERO_ELECTRONICO = "06"
    VALES_DE_DESPENSA = "08"
    DACION_EN_PAGO = "12"
    PAGO_POR_SUBROGACION = "13"
    PAGO_POR_CONSIGNACION = "14"
    CONDONACION = "15"
    COMPENSACION = "17"
    NOVACION = "23"
    CONFUSION = "24"
    REMISION_DE_DEUDA = "25"
    PRESCRIPCION_O_CADUCIDAD = "26"
    A_SATISFACCION_DEL_ACREEDOR = "27"
    TARJETA_DE_DEBITO = "28"
    TARJETA_DE_SERVICIOS = "29"
    APLICACION_DE_ANTICIPOS = "30"
    INTERMEDIARIO_PAGOS = "31"
    POR_DEFINIR = "99"


class PaymentMethod(Enum):
    """SAT's payment method"""

    UNA_SOLA_EXHIBICION = "PUE"
    PARCIALIDADES_DIFERIDO = "PPD"


class InvoiceUse(Enum):
    """SAT's CFDI usage"""

    ADQUISICION_MERCANCIAS = "G01"
    DEVOLUCIONES_DESCUENTOS_BONIFICACIONES = "G02"
    GASTOS_EN_GENERAL = "G03"
    CONSTRUCCIONES = "I01"
    MOBILIARIO_Y_EQUIPO_DE_OFICINA = "I02"
    EQUIPO_DE_TRANSPORTE = "I03"
    EQUIPO_DE_COMPUTO = "I04"
    DADOS_TROQUELES_HERRAMENTAL = "I05"
    COMUNICACIONES_TELEFONICAS = "I06"
    COMUNICACIONES_SATELITALES = "I07"
    OTRA_MAQUINARIA = "I08"
    HONORARIOS_MEDICOS = "D01"
    GASTOS_MEDICOS_POR_INCAPACIDAD = "D02"
    GASTOS_FUNERALES = "D03"
    DONATIVOS = "D04"
    INTERESES_POR_CREDITOS_HIPOTECARIOS = "D05"
    APORTACIONES_VOLUNTARIAS_SAR = "D06"
    PRIMA_SEGUROS_GASTOS_MEDICOS = "D07"
    GASTOS_TRANSPORTACION_ESCOLAR = "D08"
    CUENTAS_AHORRO_PENSIONES = "D09"
    SERVICIOS_EDUCATIVOS = "D10"
    SIN_EFECTOS_FISCALES = "S01"
    PAGOS = "CP01"
    NOMINA = "CN01"


class InvoiceRelation(Enum):
    """SAT's Invoice Relation"""

    NOTA_DE_CREDITO = "01"
    NOTA_DE_DEBITO = "02"
    DELOVUCION_DE_MERCANCIA = "03"
    SUSTITUCION_DE_CFDI_PREVIOS = "04"
    TRASLADOS_DE_MERCANCIA_FACTURADOS_PREVIAMENTE = "05"
    FACTURA_POR_TRASLADOS_PREVIOS = "06"
    APLICACION_DE_ANTICIPO = "07"
    FACTURA_POR_PAGOS_PARCIALIDADES = "08"
    FACTURA_POR_PAGOS_DIFERIDOS = "09"


class TaxSystem(Enum):
    """SAT's Tax System (Fiscal Regime)"""

    GENERAL_LEY_DE_PERSONAS_MORALES = "601"
    PERSONAS_MORALES_CON_FINES_NO_LUCRATIVOS = "603"
    SUELDOS_Y_SALARIOS = "605"
    ARRENDAMIENTO = "606"
    ENAJENACION_ADQUISICION_DE_BIENES = "607"
    DEMAS_INGRESOS = "608"
    RESIDENTES_EN_EL_EXTRANJERO = "610"
    INGRESOS_POR_DIVIDENDOS = "611"
    PERSONAS_FISICAS_CON_ACTIVIDADES_EMPRESARIALES_Y_PROFESIONALES = "612"
    INGRESOS_POR_INTERESES = "614"
    SIN_OBLIGACIONES_FISCALES = "616"
    SOCIEDADES_COOPERATIVAS_DE_PRODUCCION = "620"
    INCORPORACION_FISCAL = "621"
    ACTIVIDADES_AGRICOLAS_GANADERAS_SILVICOLAS_Y_PESQUERAS = "622"
    OPCIONAL_PARA_GRUPOS_DE_SOCIEDADES = "623"
    COORDINADOS = "624"
    ACTIVIDADES_EMPRESARIALES_CON_INGRESOS_A_TRAVES_DE_PLATAFORMAS_TECNOLOGICAS = "625"
    REGIMEN_SIMPLIFICADO_DE_CONFIANZA = "626"
    HIDROCARBUROS = "628"
    REGIMENES_FISCALES_PREFERENTES_EMPRESAS_MULTINACIONALES = "629"
    ENAJENACION_ACCIONES_EN_BOLSA_DE_VALORES = "630"


class Month(Enum):
    """Months and bimonths"""

    ENERO = "01"
    FEBRERO = "02"
    MARZO = "03"
    ABRIL = "04"
    MAYO = "05"
    JUNIO = "06"
    JULIO = "07"
    AGOSTO = "08"
    SEPTIEMBRE = "09"
    OCTUBRE = "10"
    NOVIEMBRE = "11"
    DICIEMBRE = "12"
    ENERO_FEBRERO = "13"
    MARZO_ABRIL = "14"
    MAYO_JUNIO = "15"
    JULIO_AGOSTO = "16"
    SEPTIEMBRE_OCTUBRE = "17"
    NOVIEMBRE_DICIEMBRE = "18"


class ContractType(Enum):
    """SAT's Contract type"""

    TRABAJO_POR_TIEMPO_INDETERMINADO = "01"
    TRABAJO_PARA_OBRA_DETERMINADA = "02"
    TRABAJO_POR_TIEMPO_DETERMINADO = "03"
    TRABAJO_POR_TEMPORADA = "04"
    TRABAJO_SUJETO_A_PRUEBA = "05"
    TRABAJO_CON_CAPACITACION_INICIAL = "06"
    POR_PAGO_DE_HORA_LABORADA = "07"
    TRABAJO_POR_COMISION_LABORAL = "08"
    DONDE_NO_EXISTE_RELACION_DE_TRABAJO = "09"
    JUBILACION_PENSION_RETIRO = "10"
    OTRO_CONTRATO = "99"


class WorkingDayType(Enum):
    """SAT's Work day type"""

    DIURNA = "01"
    NOCTURNA = "02"
    MIXTA = "03"
    POR_HORA = "04"
    REDUCIDA = "05"
    CONTINUADA = "06"
    PARTIDA = "07"
    POR_TURNOS = "08"
    OTRA_JORNADA = "99"


class TaxSystemType(Enum):
    """SAT's Tax system type"""

    SUELDOS = "02"
    JUBILADOS = "03"
    PENSIONADOS = "04"
    ASIMILADOS_MIEMBROS_SOCIEDADES_COOPERATIVAS_PRODUCCION = "05"
    ASIMILADOS_INTEGRANTES_SOCIEDADES_ASOCIACIONES_CIVILES = "06"
    ASIMILADOS_MIEMBROS_CONSEJOS = "07"
    ASIMILADOS_COMISIONISTAS = "08"
    ASIMILADOS_HONORARIOS = "09"
    ASIMILADOS_ACCIONES = "10"
    ASIMILADOS_OTROS = "11"
    JUBILADOS_PENSIONADOS = "12"
    INDEMNIZACION_SEPARACION = "13"
    OTRO_REGIMEN = "99"


class JobRisk(Enum):
    """SAT's Job risk"""

    CLASE_I = "1"
    CLASE_II = "2"
    CLASE_III = "3"
    CLASE_IV = "4"
    CLASE_V = "5"
    NO_APLICA = "99"


class PeymentFrecuency(Enum):
    """SAT's payment frequency"""

    DIARIO = "01"
    SEMANAL = "02"
    CATORCENAL = "03"
    QUINCENAL = "04"
    MENSUAL = "05"
    BIMESTRAL = "06"
    UNIDAD_OBRA = "07"
    COMISION = "08"
    PRECIO_ALZADO = "09"
    DECENAL = "10"
    OTRA_PERIODICIDAD = "99"


class PerceptionType(Enum):
    """SAT's perception type"""

    SUELDOS_SALARIOS_RAYAS_JORNALES = "001"
    GRATIFICACION_ANUAL = "002"
    PARTICIPACION_DE_LOS_TRABAJADORES_EN_LAS_UTILIDADES_PTU = "003"
    REEMBOLSO_DE_GASTOS_MEDICOS_DENTALES_Y_HOSPITALARIOS = "004"
    FONDO_DE_AHORRO = "005"
    CAJA_DE_AHORRO = "006"
    CONTRIBUCIONES_A_CARGO_DEL_TRABAJADOR_PAGADAS_POR_EL_PATRON = "009"
    PREMIOS_POR_PUNTUALIDAD = "010"
    PRIMA_DE_SEGURO_DE_VIDA = "011"
    SEGURO_DE_GASTOS_MEDICOS_MAYORES = "012"
    CUOTAS_SINDICALES_PAGADAS_POR_EL_PATRON = "013"
    SUBSIDIOS_POR_INCAPACIDAD = "014"
    BECAS_PARA_TRABAJADORES_E_HIJOS = "015"
    HORAS_EXTRA = "019"
    PRIMA_DOMINICAL = "020"
    PRIMA_VACACIONAL = "021"
    PRIMA_POR_ANTIGUEDAD = "022"
    PAGOS_POR_SEPARACION = "023"
    SEGURO_DE_RETIRO = "024"
    INDEMNIZACIONES = "025"
    REEMBOLSO_POR_FUNERAL = "026"
    CUOTAS_DE_SEGURIDAD_SOCIAL_PAGADAS_POR_EL_PATRON = "027"
    COMISIONES = "028"
    VALES_DE_DESPENSA = "029"
    VALES_DE_RESTAURANTE = "030"
    VALES_DE_GASOLINA = "031"
    VALES_DE_ROPA = "032"
    AYUDA_PARA_RENTA = "033"
    AYUDA_PARA_ARTICULOS_ESCOLARES = "034"
    AYUDA_PARA_ANTEOJOS = "035"
    AYUDA_PARA_TRANSPORTE = "036"
    AYUDA_PARA_GASTOS_DE_FUNERAL = "037"
    OTROS_INGRESOS_POR_SALARIOS = "038"
    JUBILACIONES_PENSIONES_O_HABERES_DE_RETIRO = "039"
    JUBILACIONES_PENSIONES_O_HABERES_DE_RETIRO_EN_PARCIALIDADES = "044"
    INGRESOS_EN_ACCIONES_O_TITULOS_VALOR_QUE_REPRESENTAN_BIENES = "045"
    INGRESOS_ASIMILADOS_A_SALARIOS = "046"
    ALIMENTACION_DIFERENTES_A_LOS_ESTABLECIDOS_EN_LISR = "047"
    HABITACION = "048"
    PREMIOS_POR_ASISTENCIA = "049"
    VIATICOS = "050"
    GRATIFICACIONES_PRIMAS_COMPENSACIONES_RECOMPENSAS_OTROS_EN_PARCIALIDADES = "051"
    PAGOS_POR_JUBILACION_EN_PARCIALIDADES_DERIVADOS_DE_RESOLUCION_JUDICIAL = "052"
    PAGOS_POR_JUBILACION_EN_UNA_SOLA_EXHIBICION_DERIVADOS_DE_RESOLUCION_JUDICIAL = "053"


class HourType(Enum):
    """SAT's hour type"""

    DOBLES = "01"
    TRIPLES = "02"
    SIMPLES = "03"


class DeductionType(Enum):
    """SAT's deduction type"""

    SEGURIDAD_SOCIAL = "001"
    ISR = "002"
    APORTACIONES_A_RETIRO_CESANTIA_EN_EDAD_AVANZADA_Y_VEJEZ = "003"
    OTROS = "004"
    APORTACIONES_A_FONDO_DE_VIVIENDA = "005"
    DESCUENTO_POR_INCAPACIDAD = "006"
    PENSION_ALIMENTICIA = "007"
    RENTA = "008"
    PRESTAMOS_DEL_FONDO_NACIONAL_DE_LA_VIVIENDA_PARA_LOS_TRABAJADORES = "009"
    PAGO_POR_CREDITO_DE_VIVIENDA = "010"
    PAGO_DE_ABONOS_INFONACOT = "011"
    ANTICIPO_DE_SALARIOS = "012"
    PAGOS_HECHOS_CON_EXCESO_AL_TRABAJADOR = "013"
    ERRORES = "014"
    PERDIDAS = "015"
    AVERIAS = "016"
    ADQUISICION_DE_ARTICULOS_PRODUCIDOS_POR_LA_EMPRESA_O_ESTABLECIMIENTO = "017"
    CUOTAS_PARA_LA_CONSTITUCION_DE_SOCIEDADES_COOPERATIVAS_CAJAS_DE_AHORRO = "018"
    CUOTAS_SINDICALES = "019"
    AUSENCIA = "020"
    CUOTAS_OBRERO_PATRONALES = "021"
    IMPUESTOS_LOCALES = "022"
    APORTACIONES_VOLUNTARIAS = "023"
    AJUSTE_GRATIFICACION_ANUAL_EXENTO = "024"
    AJUSTE_GRATIFICACION_ANUAL_GRAVADO = "025"
    AJUSTE_PARTICIPACION_DE_LOS_TRABAJADORES_EN_LAS_UTILIDADES_PTU_EXENTO = "026"
    AJUSTE_PARTICIPACION_DE_LOS_TRABAJADORES_EN_LAS_UTILIDADES_PTU_GRAVADO = "027"
    AJUSTE_REEMBOLSO_DE_GASTOS_MEDICOS_DENTALES_Y_HOSPITALARIOS_EXENTO = "028"
    AJUSTE_FONDO_DE_AHORRO_EXENTO = "029"
    AJUSTE_CAJA_DE_AHORRO_EXENTO = "030"
    AJUSTE_CONTRIBUCIONES_A_CARGO_DEL_TRABAJADOR_PAGADAS_POR_EL_PATRON_EXENTO = "031"
    AJUSTE_PREMIOS_POR_PUNTUALIDAD_GRAVADO = "032"
    AJUSTE_PRIMA_DE_SEGURO_DE_VIDA_EXENTO = "033"
    AJUSTE_SEGURO_DE_GASTOS_MEDICOS_MAYORES_EXENTO = "034"
    AJUSTE_CUOTAS_SINDICALES_PAGADAS_POR_EL_PATRON_EXENTO = "035"
    AJUSTE_SUBSIDIOS_POR_INCAPACIDAD_EXENTO = "036"
    AJUSTE_BECAS_PARA_TRABAJADORES_E_HIJOS_EXENTO = "037"
    AJUSTE_HORAS_EXTRA_EXENTO = "038"
    AJUSTE_HORAS_EXTRA_GRAVADO = "039"
    AJUSTE_PRIMA_DOMINICAL_EXENTO = "040"
    AJUSTE_PRIMA_DOMINICAL_GRAVADO = "041"
    AJUSTE_PRIMA_VACACIONAL_EXENTO = "042"
    AJUSTE_PRIMA_VACACIONAL_GRAVADO = "043"
    AJUSTE_PRIMA_POR_ANTIGUEDAD_EXENTO = "044"
    AJUSTE_PRIMA_POR_ANTIGUEDAD_GRAVADO = "045"
    AJUSTE_PAGOS_POR_SEPARACION_EXENTO = "046"
    AJUSTE_PAGOS_POR_SEPARACION_GRAVADO = "047"
    AJUSTE_SEGURO_DE_RETIRO_EXENTO = "048"
    AJUSTE_INDEMNIZACIONES_EXENTO = "049"
    AJUSTE_INDEMNIZACIONES_GRAVADO = "050"
    AJUSTE_REEMBOLSO_POR_FUNERAL_EXENTO = "051"
    AJUSTE_CUOTAS_DE_SEGURIDAD_SOCIAL_PAGADAS_POR_EL_PATRON_EXENTO = "052"
    AJUSTE_COMISIONES_GRAVADO = "053"
    AJUSTE_VALES_DE_DESPENSA_EXENTO = "054"
    AJUSTE_VALES_DE_RESTAURANTE_EXENTO = "055"
    AJUSTE_VALES_DE_GASOLINA_EXENTO = "056"
    AJUSTE_VALES_DE_ROPA_EXENTO = "057"
    AJUSTE_AYUDA_PARA_RENTA_EXENTO = "058"
    AJUSTE_AYUDA_PARA_ARTICULOS_ESCOLARES_EXENTO = "059"
    AJUSTE_AYUDA_PARA_ANTEOJOS_EXENTO = "060"
    AJUSTE_AYUDA_PARA_TRANSPORTE_EXENTO = "061"
    AJUSTE_AYUDA_PARA_GASTOS_DE_FUNERAL_EXENTO = "062"
    AJUSTE_OTROS_INGRESOS_POR_SALARIOS_EXENTO = "063"
    AJUSTE_OTROS_INGRESOS_POR_SALARIOS_GRAVADO = "064"
    AJUSTE_JUBILACIONES_PENSIONES_RETIRO_UNA_SOLA_EXHIBICION_EXENTO = "065"
    AJUSTE_JUBILACIONES_PENSIONES_RETIRO_UNA_SOLA_EXHIBICION_GRAVADO = "066"
    AJUSTE_PAGOS_POR_SEPARACION_ACUMULABLE = "067"
    AJUSTE_PAGOS_POR_SEPARACION_NO_ACUMULABLE = "068"
    AJUSTE_JUBILACIONES_PENSIONES_RETIRO_EN_PARCIALIDADES_EXENTO = "069"
    AJUSTE_JUBILACIONES_PENSIONES_RETIRO_EN_PARCIALIDADES_GRAVADO = "070"
    AJUSTE_SUBSIDIO_PARA_EL_EMPLEO = "071"
    AJUSTE_INGRESOS_EN_ACCIONES_O_TITULOS_VALOR_QUE_REPRESENTAN_BIENES_EXENTO = "072"
    AJUSTE_INGRESOS_EN_ACCIONES_O_TITULOS_VALOR_QUE_REPRESENTAN_BIENES_GRAVADO = "073"
    AJUSTE_ALIMENTACION_EXENTO = "074"
    AJUSTE_ALIMENTACION_GRAVADO = "075"
    AJUSTE_HABITACION_EXENTO = "076"
    AJUSTE_HABITACION_GRAVADO = "077"
    AJUSTE_PREMIOS_POR_ASISTENCIA = "078"
    AJUSTE_PAGOS_DISTINTOS_A_LOS_LISTADOS = "079"
    AJUSTE_VIATICOS_GRAVADOS = "080"
    AJUSTE_VIATICOS = "081"
    AJUSTE_FONDO_DE_AHORRO_GRAVADO = "082"
    AJUSTE_CAJA_DE_AHORRO_GRAVADO = "083"
    AJUSTE_PRIMA_DE_SEGURO_DE_VIDA_GRAVADO = "084"
    AJUSTE_SEGURO_DE_GASTOS_MEDICOS_MAYORES_GRAVADO = "085"
    AJUSTE_SUBSIDIOS_POR_INCAPACIDAD_GRAVADO = "086"
    AJUSTE_BECAS_PARA_TRABAJADORES_E_HIJOS_GRAVADO = "087"
    AJUSTE_SEGURO_DE_RETIRO_GRAVADO = "088"
    AJUSTE_VALES_DE_DESPENSA_GRAVADO = "089"
    AJUSTE_VALES_DE_RESTAURANTE_GRAVADO = "090"
    AJUSTE_VALES_DE_GASOLINA_GRAVADO = "091"
    AJUSTE_VALES_DE_ROPA_GRAVADO = "092"
    AJUSTE_AYUDA_PARA_RENTA_GRAVADO = "093"
    AJUSTE_AYUDA_PARA_ARTICULOS_ESCOLARES_GRAVADO = "094"
    AJUSTE_AYUDA_PARA_ANTEOJOS_GRAVADO = "095"
    AJUSTE_AYUDA_PARA_TRANSPORTE_GRAVADO = "096"
    AJUSTE_AYUDA_PARA_GASTOS_DE_FUNERAL_GRAVADO = "097"
    AJUSTE_INGRESOS_ASIMILADOS_A_SALARIOS_GRAVADOS = "098"
    AJUSTE_INGRESOS_POR_SUELDOS_Y_SALARIOS_GRAVADOS = "099"
    AJUSTE_EN_VIATICOS_EXENTOS = "100"
    ISR_RETENIDO_DE_EJERCICIO_ANTERIOR = "101"
    AJUSTE_PAGOS_POR_GRATIFICACIONES_PRIMAS_COMPENSACIONES_RECOMPENSAS_U_OTROS = "102"
    AJUSTE_PAGOS_EN_PARCIALIDADES_DERIVADOS_DE_UNA_RESOLUCION_JUDICIAL_GRAVADOS = "103"
    AJUSTE_PAGOS_EN_PARCIALIDADES_DERIVADOS_DE_UNA_RESOLUCION_JUDICIAL_EXENTOS = "104"
    AJUSTE_PAGOS_EN_UNA_EXHIBICION_DERIVADOS_DE_RESOLUCION_JUDICIAL_GRAVADOS = "105"
    AJUSTE_PAGOS_EN_UNA_EXHIBICION_DERIVADOS_DE_RESOLUCION_JUDICIAL_EXENTOS = "106"
    AJUSTE_AL_SUBSIDIO_CAUSADO = "107"


class OtherPaymentType(Enum):
    """SAT's other payment type"""

    REINTEGRO_DE_ISR_PAGADO_EN_EXCESO = "001"
    SUBSIDIO_PARA_EL_EMPLEO = "002"
    VIATICOS = "003"
    APLICACION_DE_SALDO_A_FAVOR_POR_COMPENSACION_ANUAL = "004"
    REINTEGRO_DE_ISR_RETENIDO_EN_EXCESO_DE_EJERCICIO_ANTERIOR = "005"
    ALIMENTOS_EN_BIENES = "006"
    ISR_AJUSTADO_POR_SUBSIDIO = "007"
    SUBSIDIO_EFECTIVAMENTE_ENTREGADO_QUE_NO_CORRESPONDIA = "008"
    REEMBOLSO_DE_DESCUENTOS_EFECTUADOS_PARA_EL_CREDITO_DE_VIVIENDA = "009"
    PAGOS_DISTINTOS_A_LOS_LISTADOS = "999"


class CancellationReason(Enum):
    ERRORS_WITH_RELATION = "01"
    ERRORS_WITHOUT_RELATION = "02"
    OPERATION_NOT_CARRIED_OUT = "03"
    NOMINATIVE_TRANSACTION = "04"


class ReceiptPeriodicity(Enum):
    DAY = "day"
    WEEK = "week"
    FORTNIGHT = "fortnight"
    MONTH = "month"
    TWO_MONTHS = "two_months"


class Catalogs(NamedTuple):
    """Catalog codes"""

    payment_forms = PaymentForm
    payment_methods = PaymentMethod
    invoice_use = InvoiceUse
    invoice_relations = InvoiceRelation
    tax_systems = TaxSystem
    months = Month
    contract_types = ContractType
    working_day_types = WorkingDayType
    tax_system_types = TaxSystemType
    job_risks = JobRisk
    payment_frequencies = PeymentFrecuency
    perception_types = PerceptionType
    hour_types = HourType
    deduction_types = DeductionType
    other_payment_types = OtherPaymentType

    cancellation_reasons = CancellationReason

    receipt_periodicity = ReceiptPeriodicity
