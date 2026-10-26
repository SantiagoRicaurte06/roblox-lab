# Contexto del proyecto
Laboratorio para aprender a crear juegos en Roblox. Aún NO es el juego final.

## Fase actual: exploración de diseño con Higgsfield
Se generan imágenes y modelos 3D con Higgsfield hasta que el diseño convenza.
Todavía no se programa ni se modela a mano.

Flujo: referencia → prompt → generación en Higgsfield → comparar → ajustar prompt → repetir.
Un diseño solo pasa a `modelos/aprobados/` cuando tiene veredicto ✅.

## Objetivo actual
[Ej: lograr un estilo low-poly consistente para props de entorno]

## Cómo trabajamos
- Claude redacta y ajusta los prompts para Higgsfield (plantillas en `prompts/plantillas/higgsfield-*.md`); el usuario los ejecuta en Higgsfield y guarda los resultados.
- Cada intento va en `experimentos/NNN-nombre/`: el prompt exacto, ajustes (modelo, preset, seed, proporción) y el resultado en `generaciones/`.
- Para revisar, Claude compara las imágenes de `generaciones/` con las referencias indicadas y propone qué cambiar en el prompt, no todo de nuevo.
- Antes de generar, revisa `referencias/INDICE.md` y las imágenes indicadas.
- Todo diseño debe respetar `docs/estilo-visual.md`. Las reglas nuevas que salgan de un experimento se pasan ahí.
- Los modelos 3D generados deben cumplir `docs/specs-roblox.md` antes de aprobarse (triángulos, escala, pivote).
- Fase siguiente (cuando el estilo esté decidido): ajustar o recrear en Blender (bpy) y llevarlo a Roblox con Rojo.

## Stack
Higgsfield (imágenes y 3D), Roblox Studio, Luau, Rojo, Blender [versión].

## Estado
- Aprobado: [lista]
- En prueba: [lista]
- Descartado: [lista + motivo corto]
