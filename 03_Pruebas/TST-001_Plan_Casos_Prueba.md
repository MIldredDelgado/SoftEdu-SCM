# TST-001 - Plan y Casos de Prueba de SoftEdu

## Información del elemento de configuración

- Código del CI: TST-001
- Nombre: Plan y Casos de Prueba
- Proyecto: SoftEdu
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 09/09/2026
- Responsable: Equipo SoftEdu

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 09/09/2026 | Creación inicial del plan y casos de prueba | Equipo SoftEdu |

## 1. Objetivo

Validar que las funcionalidades principales de SoftEdu cumplan con los requisitos definidos en REQ-001 versión 1.0.

## 2. Alcance de las pruebas

Las pruebas iniciales cubren:

- Registro de estudiantes.
- Consulta de estudiantes.
- Registro de cursos.
- Matrícula de estudiantes.

## 3. Casos de prueba

### CP-01 - Registrar estudiante correctamente

- Requisito asociado: RF-01
- Diseño asociado: DIS-001 - Entidad Estudiante
- Código asociado: SRC-001
- Precondición: El estudiante no debe existir previamente.

Datos de entrada:

- Identificación: 1001
- Nombre completo: Ana Pérez
- Correo electrónico: ana@email.com

Resultado esperado:

El sistema crea correctamente el estudiante y almacena identificación, nombre completo y correo electrónico.

Estado esperado: Aprobado.

### CP-02 - Consultar estudiante existente

- Requisito asociado: RF-02
- Diseño asociado: DIS-001 - Entidad Estudiante
- Código asociado: SRC-001
- Precondición: El estudiante debe estar registrado.

Resultado esperado:

El sistema muestra correctamente los datos del estudiante consultado.

Estado esperado: Aprobado.

### CP-03 - Registrar curso

- Requisito asociado: RF-03
- Diseño asociado: DIS-001 - Entidad Curso

Datos de entrada:

- Código: IS101
- Nombre: Introducción a Sistemas
- Créditos: 3

Resultado esperado:

El curso queda registrado correctamente.

Estado esperado: Aprobado.

### CP-04 - Matricular estudiante

- Requisito asociado: RF-04
- Diseño asociado: DIS-001 - Entidad Matricula

Precondiciones:

- El estudiante debe existir.
- El curso debe existir.

Resultado esperado:

El estudiante queda asociado correctamente al curso seleccionado.

Estado esperado: Aprobado.

## 4. Trazabilidad de pruebas

| Caso de prueba | Requisito | Diseño | Código |
|----------------|-----------|--------|--------|
| CP-01 | RF-01 | DIS-001 | SRC-001 |
| CP-02 | RF-02 | DIS-001 | SRC-001 |
| CP-03 | RF-03 | DIS-001 | No aplica en esta versión |
| CP-04 | RF-04 | DIS-001 | No aplica en esta versión |

## 5. Observaciones de configuración

Este documento constituye el Elemento de Configuración TST-001.

Los casos de prueba deberán actualizarse cuando una solicitud de cambio modifique los requisitos, el diseño o el código relacionado.
