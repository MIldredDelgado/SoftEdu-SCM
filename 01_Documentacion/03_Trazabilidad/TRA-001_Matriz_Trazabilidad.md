# TRA-001 - Matriz de Trazabilidad de SoftEdu

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: SoftEdu
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 09/09/2026
- Responsable: Equipo SoftEdu

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 09/09/2026 | Creación inicial de la matriz de trazabilidad | Equipo SoftEdu |

## 1. Objetivo

Relacionar los requisitos definidos para SoftEdu con los elementos de diseño, código fuente y pruebas que los implementan o verifican.

La matriz permite identificar qué elementos de configuración deben revisarse cuando un requisito sea modificado.

## 2. Matriz de trazabilidad inicial

| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
|-----------|-------------|--------------------|--------------------|--------------------|--------|
| RF-01 | Registrar estudiante | DIS-001 - Entidad Estudiante | SRC-001 - Gestión de Estudiantes | TST-001 / CP-01 | Completa |
| RF-02 | Consultar estudiante | DIS-001 - Entidad Estudiante | SRC-001 - Gestión de Estudiantes | TST-001 / CP-02 | Completa |
| RF-03 | Registrar curso | DIS-001 - Entidad Curso | Pendiente de implementación | TST-001 / CP-03 | Parcial |
| RF-04 | Matricular estudiante | DIS-001 - Entidad Matrícula | Pendiente de implementación | TST-001 / CP-04 | Parcial |

## 3. Relación entre elementos de configuración

La configuración inicial de SoftEdu presenta la siguiente relación:

REQ-001 v1.0
↓
DIS-001 v1.0
↓
SRC-001 v1.0
↓
TST-001 v1.0

El elemento TRA-001 registra y documenta estas relaciones.

## 4. Trazabilidad por requisito

### RF-01 - Registrar estudiante

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Entidad Estudiante
- Código asociado: SRC-001 - Gestión de Estudiantes
- Caso de prueba asociado: TST-001 / CP-01
- Estado de trazabilidad: Completa

### RF-02 - Consultar estudiante

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Entidad Estudiante
- Código asociado: SRC-001 - Gestión de Estudiantes
- Caso de prueba asociado: TST-001 / CP-02
- Estado de trazabilidad: Completa

### RF-03 - Registrar curso

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Entidad Curso
- Código asociado: Pendiente
- Caso de prueba asociado: TST-001 / CP-03
- Estado de trazabilidad: Parcial

### RF-04 - Matricular estudiante

- Requisito: REQ-001
- Diseño asociado: DIS-001 - Entidad Matrícula
- Código asociado: Pendiente
- Caso de prueba asociado: TST-001 / CP-04
- Estado de trazabilidad: Parcial

## 5. Trazabilidad de cambios

Cuando se apruebe una solicitud de cambio, esta matriz deberá registrar qué elementos fueron afectados.

La relación deberá seguir, cuando aplique, la siguiente estructura:

Solicitud de cambio
↓
Requisito afectado
↓
Diseño afectado
↓
Código afectado
↓
Prueba afectada
↓
Commit o Pull Request
↓
Nueva versión de los elementos afectados

## 6. Registro de cambios trazables

| Solicitud de cambio | Requisito afectado | Diseño afectado | Código afectado | Prueba afectada | Commit / PR | Estado |
|--------------------|--------------------|-----------------|-----------------|-----------------|-------------|--------|
| Sin cambios aprobados en la versión 1.0 | - | - | - | - | - | Línea base inicial |

## 7. Observaciones

Este documento constituye el Elemento de Configuración TRA-001.

La versión 1.0 representa la trazabilidad correspondiente a la configuración inicial de SoftEdu.

Toda modificación posterior deberá actualizar esta matriz y quedar relacionada con una solicitud de cambio aprobada.
