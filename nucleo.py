import logging
from abc import ABC, abstractmethod

# ==========================================
# 1. Configuración de Logs
# ==========================================
# Esto creará un archivo 'software_fj.log' donde se registrarán los eventos.
logging.basicConfig(
    filename='software_fj.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

# --- EXCEPCIONES PERSONALIZADAS ---
# Estas permiten que el sistema sea robusto y sepa qué falló exactamente.

class SoftwareFJError(Exception): 
    """Clase base para errores del sistema."""
    pass

class ErrorValidacion(SoftwareFJError): 
    """Errores en datos de entrada o parámetros."""
    pass

class ErrorFinanciero(SoftwareFJError): 
    """Errores en cálculos de costos o límites."""
    pass

class ServicioNoDisponible(SoftwareFJError): 
    """Errores cuando un servicio no puede procesarse."""
    pass

# --- CLASES ABSTRACTAS (EL CONTRATO) ---
# Aquí defines las reglas que las clases de tus compañeros deben seguir.

class EntidadBase(ABC):
    def __init__(self, id_entidad):  # Corregido: __init__
        self._id_entidad = id_entidad

    @property
    def id_entidad(self):
        """Permite leer el ID pero protege el atributo original."""
        return self._id_entidad

class Servicio(ABC):
    def __init__(self, nombre, precio_base):  # Corregido: __init__
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0.0):
        """
        Método obligatorio. 
        Tus compañeros DEBEN definir cómo se calcula el costo en sus clases.
        """
        pass

    @abstractmethod
    def obtener_detalle(self):
        """Método obligatorio para describir el servicio."""
        pass
    