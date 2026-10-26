# Contexto del proyecto
Laboratorio para aprender a crear juegos en Roblox. Aún NO es el juego final.

## Objetivo actual
[Ej: lograr un estilo low-poly consistente para props de entorno]

## Cómo trabajamos
- Los modelos 3D se generan como scripts de Blender en Python (bpy), no se describen.
- Todo modelo debe cumplir docs/specs-roblox.md y docs/estilo-visual.md.
- Antes de generar, revisa referencias/INDICE.md y las imágenes indicadas.
- Cada intento va en experimentos/NNN-nombre/.

## Stack
Roblox Studio, Luau, Rojo, Blender [versión].

## Estado
- Aprobado: [lista]
- En prueba: [lista]
- Descartado: [lista + motivo corto]

## Git workflow

Este repositorio sigue `GIT_WORKFLOW.md`. Reglas obligatorias para asistentes de IA:

- Ramas `tipo/descripcion-corta` (feature, fix, refactor, docs, chore, release, hotfix) desde `develop` (hotfix desde `main`). Nunca commit directo a `main` ni `develop`.
- Commits en Conventional Commits: `<tipo>(<scope>): <descripción>`, imperativo, minúscula, sin punto final, ≤ 72 caracteres.
- **No añadir coautorías** (`Co-Authored-By`) ni firmas de generación automática en commits, PRs, tags o releases.
- No modificar `user.name` ni `user.email`.
- No hacer `push`, `force-push`, reescritura de historial, merges a `main`/`develop` ni crear tags sin aprobación explícita.
- Proponer el mensaje del commit y el diff antes de ejecutar cuando el cambio no sea trivial.
- Antes de reescribir historial: `git branch backup/<descripcion>-<yyyymmdd>`.
