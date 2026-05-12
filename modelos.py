import math
import re
from nucleo import EntidadBase, Servicio, ErrorValidacion

# **--- CLASE CLIENTE: ENCAPSULACIÓN Y VALIDACIÓN ---**

class Cliente(EntidadBase):
    """
    Gestiona la información de los clientes de Software FJ.
    Aplica encapsulamiento estricto mediante decoradores @property.
    """
    def __init__(self, id_cliente, nombre, email, telefono):
        super().__init__(id_cliente)
        # Atributos protegidos
        self.nombre = nombre  # Llama al setter automáticamente
        self.email = email    # Llama al setter automáticamente
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise ErrorValidacion(f"Nombre inválido: '{valor}'. Debe tener al menos 3 caracteres.")
        self._nombre = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        # Validación básica de email con Regex
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(patron, valor):
            raise ErrorValidacion(f"Formato de correo electrónico inválido: {valor}")
        self._email = valor

    def __str__(self):
        return f"ID: {self.id_entidad} | Cliente: {self.nombre} | Email: {self.email}"


# **--- SERVICIOS ESPECIALIZADOS (POLIMORFISMO) ---**

class ReservaSala(Servicio):
    def __init__(self, nombre, precio_por_hora, capacidad):
        super().__init__(nombre, precio_por_hora)
        self.capacidad = capacidad

    def calcular_costo(self, horas, descuento=0.0, es_festivo=False):
        """
        SOBRECARGA: El costo varía si es festivo (+15%) o si hay descuento.
        Fórmula: $$costo = (base \times horas) \times (1 + impuesto)$$
        """
        tasa_festivo = 1.15 if es_festivo else 1.0
        total = (self.precio_base * horas) * tasa_festivo
        total_con_impuesto = total * 1.19  # IVA del 19%
        return total_con_impuesto * (1 - descuento)

    def obtener_detalle(self):
        return f"SALA: {self.nombre} (Capacidad: {self.capacidad} personas)"


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, precio_por_dia, marca):
        super().__init__(nombre, precio_por_dia)
        self.marca = marca

    def calcular_costo(self, dias, descuento=0.0, seguro_opcional=True):
        """
        SOBRECARGA: Incluye un seguro obligatorio o extra.
        """
        costo_seguro = 15.0 if seguro_opcional else 5.0
        total = (self.precio_base * dias) + costo_seguro
        return total * (1 - descuento)

    def obtener_detalle(self):
        return f"EQUIPO: {self.nombre} | Marca: {self.marca}"


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, tarifa_sesion, especialista):
        super().__init__(nombre, tarifa_sesion)
        self.especialista = especialista

    def calcular_costo(self, sesiones, descuento=0.0):
        """
        Implementación simple del cálculo de asesoría.
        """
        total = self.precio_base * sesiones
        return total * (1 - descuento)

    def obtener_detalle(self):
        return f"ASESORÍA: {self.nombre} | Consultor: {self.especialista}"