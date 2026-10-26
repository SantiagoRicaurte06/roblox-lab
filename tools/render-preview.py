"""Render rápido de un modelo para comparar con la referencia.

Uso: blender --background --python tools/render-preview.py -- <modelo.fbx|.obj|.blend> <salida.png>
"""
import math
import os
import sys

import bpy
from mathutils import Vector

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
if len(args) != 2:
    sys.exit("Uso: blender --background --python tools/render-preview.py -- <modelo> <salida.png>")
modelo, salida = (os.path.abspath(a) for a in args)

ext = os.path.splitext(modelo)[1].lower()
if ext == ".blend":
    bpy.ops.wm.open_mainfile(filepath=modelo)
else:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    if ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=modelo)
    elif ext == ".obj":
        bpy.ops.wm.obj_import(filepath=modelo)
    else:
        sys.exit(f"Formato no soportado: {ext}")

escena = bpy.context.scene
mallas = [o for o in escena.objects if o.type == "MESH"]
puntos = [o.matrix_world @ Vector(c) for o in mallas for c in o.bound_box]
centro = sum(puntos, Vector()) / len(puntos)
tamano = max((p - centro).length for p in puntos)

cam_data = bpy.data.cameras.new("Preview")
cam = bpy.data.objects.new("Preview", cam_data)
escena.collection.objects.link(cam)
cam.location = centro + Vector((1, -1, 0.7)).normalized() * tamano * 3
cam.rotation_euler = (centro - cam.location).to_track_quat("-Z", "Y").to_euler()
escena.camera = cam

sol = bpy.data.objects.new("Sol", bpy.data.lights.new("Sol", "SUN"))
sol.rotation_euler = (math.radians(50), 0, math.radians(30))
escena.collection.objects.link(sol)

escena.render.engine = "BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in {
    e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items
} else "BLENDER_EEVEE"
escena.render.resolution_x = escena.render.resolution_y = 1024
escena.render.film_transparent = True
escena.render.filepath = salida
os.makedirs(os.path.dirname(salida), exist_ok=True)
bpy.ops.render.render(write_still=True)

tris = sum(len(p.vertices) - 2 for o in mallas for p in o.data.polygons)
print(f"Render: {salida} · Triángulos: {tris}")
