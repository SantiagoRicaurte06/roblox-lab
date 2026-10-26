# roblox-lab

Laboratorio para aprender a crear juegos en Roblox con ayuda de Claude: referencias visuales,
prompts, experimentos de modelos 3D generados con Blender (bpy) y código Luau sincronizado con Rojo.
Todavía **no** es el juego final.

## Estructura

| Carpeta | Para qué |
|---|---|
| `CLAUDE.md` | Contexto que Claude lee siempre (el archivo más importante) |
| `docs/` | Visión, estilo visual, specs de Roblox, log de decisiones y aprendizajes |
| `referencias/` | Imágenes, frames de video y moodboards, indexados en `referencias/INDICE.md` |
| `prompts/` | Plantillas de prompts y los que dieron buen resultado |
| `experimentos/` | Un intento por carpeta `NNN-nombre/` con prompt, script y renders |
| `modelos/` | `fuente/` (.blend), `exportados/` (.fbx/.obj), `aprobados/` (con ficha .md) |
| `juego/` | Proyecto Rojo (código sincronizado con Roblox Studio) |
| `tools/` | Scripts de apoyo (extraer frames, render rápido) |

## Primeros pasos tras clonar

```bash
git lfs install                         # los .blend, .fbx, .png, .jpg y .mp4 van por Git LFS
git config core.hooksPath .githooks     # activa los hooks del workflow (ver GIT_WORKFLOW.md)
npx skills@latest add santiagoricaurte06/discord --skill git-workflow   # skill para Claude Code
```

## Flujo de un experimento

1. Guarda referencias en `referencias/imagenes/...` y anótalas en `referencias/INDICE.md`.
2. Para videos: `./tools/extraer-frames.sh video.mp4 nombre 2` (1 frame cada 2 s).
3. Copia `experimentos/001-arbol-lowpoly/` como `NNN-nombre/` y rellena `prompt.md` usando `prompts/plantillas/modelo-3d.md`.
4. Ejecuta el script: `blender --background --python experimentos/NNN-nombre/generar.py`.
5. Render rápido: `blender --background --python tools/render-preview.py -- modelos/exportados/x.fbx experimentos/NNN-nombre/renders/x.png`.
6. Anota el veredicto en el `README.md` del experimento y pasa las reglas nuevas a `docs/estilo-visual.md`.
