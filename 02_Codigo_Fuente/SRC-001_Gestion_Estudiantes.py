# SRC-001 - Gestión de Estudiantes
# Proyecto: SoftEdu
# Versión: 1.0
# Estado: Aprobado para línea base inicial
# Fecha: 09/09/2026
# Responsable: Equipo SoftEdu


class Estudiante:
    def __init__(self, identificacion, nombre_completo, correo_electronico):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico

    def mostrar_informacion(self):
        return {
            "identificacion": self.identificacion,
            "nombre_completo": self.nombre_completo,
            "correo_electronico": self.correo_electronico
        }


def registrar_estudiante(identificacion, nombre_completo, correo_electronico):
    estudiante = Estudiante(
        identificacion,
        nombre_completo,
        correo_electronico
    )

    return estudiante