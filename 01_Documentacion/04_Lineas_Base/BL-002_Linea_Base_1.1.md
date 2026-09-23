# BL-002 - Línea Base 1.1 de SoftEdu

## Información de la línea base

- Código: BL-002
- Proyecto: SoftEdu
- Nombre: Línea Base posterior a CR-001
- Versión del producto: 1.1
- Fecha de establecimiento: 23/09/2026
- Estado: Aprobada
- Responsable del establecimiento y aprobación: MIldredDelgado (owner)
- Responsable de la implementación y cierre documental: MInerva2026410
- Línea base anterior: BL-001 - Versión 1.0
- Solicitud de cambio asociada: CR-001 - Agregar teléfono al estudiante
- Etiqueta Git: v1.1

## 1. Objetivo

Establecer el conjunto de elementos de configuración aprobados que conforman la versión 1.1 de SoftEdu, después de incorporar CR-001 y completar su cierre documental.

Esta línea base sirve como referencia para recuperar la configuración aprobada y controlar los cambios posteriores.

## 2. Elementos incluidos en la línea base

| Código CI | Elemento de configuración | Versión | Estado |
|-----------|---------------------------|---------|--------|
| REQ-001 | Especificación de Requisitos | 1.1 | Aprobado |
| DIS-001 | Diseño del Sistema | 1.1 | Aprobado |
| SRC-001 | Gestión de Estudiantes | 1.1 | Aprobado |
| TST-001 | Plan y Casos de Prueba | 1.1 | Aprobado |
| TRA-001 | Matriz de Trazabilidad | 1.1 | Aprobado |

El presente documento BL-002 también se incorpora al repositorio antes de crear la etiqueta v1.1, para que forme parte del registro de esta configuración.

## 3. Cambio incorporado y trazabilidad

CR-001 incorpora el teléfono del estudiante y actualiza los elementos relacionados:

- REQ-001: actualización de RF-01, Registrar estudiante.
- DIS-001: incorporación del atributo teléfono en la entidad Estudiante.
- SRC-001: incorporación del teléfono en la gestión de estudiantes.
- TST-001: actualización de CP-01 para contemplar el teléfono.
- TRA-001: actualización de las relaciones entre requisitos, diseño, código y pruebas, y de las referencias de aprobación e integración.

Referencias del cambio:

| Registro | Propósito |
|----------|-----------|
| Issue #1 | Solicitud de cambio CR-001 |
| PR #2 | Revisión, aprobación e integración de la implementación de CR-001 |
| PR #3 | Revisión, aprobación e integración del cierre documental |

Enlaces:

- [Issue #1 - CR-001](https://github.com/MIldredDelgado/SoftEdu-SCM/issues/1)
- [PR #2 - Implementación de CR-001](https://github.com/MIldredDelgado/SoftEdu-SCM/pull/2)
- [PR #3 - Cierre documental de CR-001](https://github.com/MIldredDelgado/SoftEdu-SCM/pull/3)

## 4. Criterio de establecimiento y aprobación

MIldredDelgado, en su rol de owner, aprueba el establecimiento de BL-002 considerando que:

- La implementación de CR-001 fue revisada, aprobada e integrada en main mediante el PR #2.
- El cierre documental fue revisado, aprobado e integrado en main mediante el PR #3.
- Los cinco elementos de configuración incluidos registran la versión 1.1 y el estado Aprobado.
- La matriz de trazabilidad refleja la aprobación e integración de CR-001.
- Se conservan los registros históricos de la configuración anterior.

El cierre documental corrige los estados que permanecían en modificación o pendientes de revisión después de la integración de CR-001. No introduce cambios en el código funcional.

## 5. Alcance y limitaciones

BL-002 corresponde a la configuración académica de SoftEdu con el cambio de teléfono del estudiante incorporado.

RF-03, Registrar curso, y RF-04, Matricular estudiante, mantienen su código pendiente de implementación y su trazabilidad parcial, según TRA-001.

La aprobación de TST-001 corresponde al plan y los casos de prueba. Este documento de línea base no acredita por sí mismo la ejecución satisfactoria de las pruebas; sus resultados deben sustentarse en los registros de ejecución correspondientes.

El establecimiento de esta línea base no implica que todas las funcionalidades previstas para SoftEdu estén implementadas.

## 6. Identificación técnica

La configuración de BL-002 se identificará mediante la etiqueta Git:

`v1.1`

El owner creará esta etiqueta sobre el commit de main que incorpore este documento y que contenga las integraciones de los PR #2 y #3.

La etiqueta permitirá recuperar el estado exacto del repositorio correspondiente a BL-002. El commit asociado podrá consultarse desde la etiqueta en GitHub.

La etiqueta v1.0 se conservará para recuperar la línea base inicial BL-001.

## 7. Control posterior de cambios

Todo cambio posterior sobre los elementos incluidos deberá:

1. Registrarse en una solicitud de cambio.
2. Identificar los elementos de configuración afectados y analizar su impacto.
3. Implementarse en una rama de trabajo.
4. Registrarse mediante commits relacionados con la solicitud.
5. Revisarse y aprobarse antes de integrarse en main.
6. Actualizar los documentos y la trazabilidad afectados.
7. Generar una nueva línea base cuando corresponda.

Los cambios posteriores no deberán mover ni reemplazar la etiqueta v1.1. Se establecerá una nueva configuración y una nueva etiqueta cuando se apruebe otra línea base.
