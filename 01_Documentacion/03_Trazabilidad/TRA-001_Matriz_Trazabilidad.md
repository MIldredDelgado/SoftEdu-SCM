# TRA-001 - Matriz de Trazabilidad de SoftEdu

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: SoftEdu
- Versión: 1.1
- Estado: Aprobado
- Fecha de actualización: 23/09/2026
- Responsable: Equipo SoftEdu
- Responsable del cambio: MInerva2026410
- Aprobación de CR-001: MIldredDelgado, mediante PR #2

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 09/09/2026 | Creación inicial de la matriz de trazabilidad | Equipo SoftEdu |
| 1.1 | 16/09/2026 | Actualización de la trazabilidad asociada a CR-001 - Agregar teléfono al estudiante | MInerva2026410 |

Nota de actualización documental — 23/09/2026: se conserva la versión 1.1 y se corrigen los estados y las referencias de CR-001 para reflejar la aprobación e integración realizadas mediante el PR #2. Responsable: MInerva2026410.

## 1. Objetivo

Relacionar los requisitos definidos para SoftEdu con los elementos de diseño, código fuente y pruebas que los implementan o verifican.

La matriz permite identificar qué elementos de configuración deben revisarse cuando un requisito sea modificado y registrar la trazabilidad de las solicitudes de cambio.

## 2. Matriz de trazabilidad

| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado de trazabilidad |
|-----------|-------------|--------------------|--------------------|--------------------|------------------------|
| RF-01 | Registrar estudiante | DIS-001 v1.1 - Entidad Estudiante | SRC-001 v1.1 - Gestión de Estudiantes | TST-001 v1.1 / CP-01 | Completa |
| RF-02 | Consultar estudiante | DIS-001 v1.1 - Entidad Estudiante | SRC-001 v1.1 - Gestión de Estudiantes | TST-001 v1.1 / CP-02 | Completa |
| RF-03 | Registrar curso | DIS-001 v1.1 - Entidad Curso | Pendiente de implementación | TST-001 v1.1 / CP-03 | Parcial |
| RF-04 | Matricular estudiante | DIS-001 v1.1 - Entidad Matrícula | Pendiente de implementación | TST-001 v1.1 / CP-04 | Parcial |

Las versiones indicadas corresponden a los documentos que contienen los elementos relacionados. Esto no implica que todos los requisitos hayan sido modificados por CR-001.

El estado de trazabilidad indica la existencia de relaciones entre los artefactos. No constituye evidencia de ejecución satisfactoria de las pruebas.

## 3. Relación entre elementos de configuración afectados por CR-001

La solicitud de cambio CR-001 incorpora el teléfono al registro de estudiantes y relaciona los siguientes elementos:

CR-001 - Agregar teléfono al estudiante

↓

REQ-001 v1.1 - RF-01 Registrar estudiante

↓

DIS-001 v1.1 - Entidad Estudiante

↓

SRC-001 v1.1 - Gestión de Estudiantes

↓

TST-001 v1.1 - CP-01 Registrar estudiante correctamente

↓

TRA-001 v1.1 - Actualización de la trazabilidad

Los elementos anteriores corresponden a los artefactos afectados por la solicitud de cambio CR-001.

## 4. Trazabilidad por requisito

### RF-01 - Registrar estudiante

- Requisito: REQ-001 v1.1
- Cambio asociado: CR-001 - Agregar teléfono al estudiante
- Diseño asociado: DIS-001 v1.1 - Entidad Estudiante
- Código asociado: SRC-001 v1.1 - Gestión de Estudiantes
- Caso de prueba asociado: TST-001 v1.1 / CP-01
- Estado de trazabilidad: Completa
- Estado del cambio: Aprobado e integrado en main mediante el PR #2
- Responsable de la aprobación e integración: MIldredDelgado
- Commit de integración: 7872add

### RF-02 - Consultar estudiante

- Requisito: REQ-001 v1.1
- Diseño asociado: DIS-001 v1.1 - Entidad Estudiante
- Código asociado: SRC-001 v1.1 - Gestión de Estudiantes
- Caso de prueba asociado: TST-001 v1.1 / CP-02
- Estado de trazabilidad: Completa

### RF-03 - Registrar curso

- Requisito: REQ-001 v1.1
- Diseño asociado: DIS-001 v1.1 - Entidad Curso
- Código asociado: Pendiente de implementación
- Caso de prueba asociado: TST-001 v1.1 / CP-03
- Estado de trazabilidad: Parcial

### RF-04 - Matricular estudiante

- Requisito: REQ-001 v1.1
- Diseño asociado: DIS-001 v1.1 - Entidad Matrícula
- Código asociado: Pendiente de implementación
- Caso de prueba asociado: TST-001 v1.1 / CP-04
- Estado de trazabilidad: Parcial

## 5. Trazabilidad de cambios

Toda solicitud de cambio aprobada para implementación debe permitir identificar los elementos afectados y seguir su evolución hasta la revisión e integración final.

Para CR-001, se registra la siguiente trazabilidad:

Solicitud de cambio CR-001 - Issue #1

↓

RF-01 de REQ-001 v1.1

↓

DIS-001 v1.1

↓

SRC-001 v1.1

↓

TST-001 v1.1 / CP-01

↓

TRA-001 v1.1

↓

Commits de implementación incluidos en el PR #2

↓

PR #2 - Revisado y aprobado por MIldredDelgado

↓

Integración en main - Commit 7872add

Referencias:

- Solicitud de cambio: [Issue #1 - CR-001](https://github.com/MIldredDelgado/SoftEdu-SCM/issues/1)
- Revisión e integración: [PR #2 - Agregar teléfono al estudiante](https://github.com/MIldredDelgado/SoftEdu-SCM/pull/2)
- Commit de integración: [7872add](https://github.com/MIldredDelgado/SoftEdu-SCM/commit/7872add)

## 6. Registro de cambios trazables

| Solicitud de cambio | Requisito afectado | Diseño afectado | Código afectado | Prueba afectada | Commit / PR | Estado |
|--------------------|--------------------|-----------------|-----------------|-----------------|-------------|--------|
| Sin cambios aprobados en la versión 1.0 | - | - | - | - | - | Línea base inicial |
| CR-001 - Agregar teléfono al estudiante | REQ-001 v1.1 / RF-01 | DIS-001 v1.1 | SRC-001 v1.1 | TST-001 v1.1 / CP-01 | PR #2 / Commit de integración 7872add | Aprobado e integrado en main |

La corrección documental del 23/09/2026 actualiza el registro de CR-001 para reflejar su aprobación e integración. Los commits de esta corrección deben hacer referencia a CR-001.

## 7. Observaciones

Este documento constituye el Elemento de Configuración TRA-001.

La versión 1.0 representa la trazabilidad correspondiente a la configuración inicial de SoftEdu establecida en BL-001.

La versión 1.1 registra el impacto y las relaciones generadas por la solicitud de cambio CR-001 - Agregar teléfono al estudiante.

CR-001 fue revisada y aprobada por MIldredDelgado e integrada en la rama main mediante el PR #2, con el commit de integración 7872add.

Esta actualización documental corrige las referencias que todavía indicaban revisión o integración pendientes. La aprobación y la integración de la implementación están registradas en el PR #2; la revisión de estas correcciones documentales quedará registrada en su propio Pull Request.

La creación de la línea base 1.1 será realizada por el owner después de revisar e integrar el cierre documental. Su composición, aprobación y etiqueta se registrarán en el documento correspondiente de líneas base.

RF-03 y RF-04 conservan trazabilidad parcial porque su código continúa pendiente de implementación. La aprobación de CR-001 no cambia esa condición.
