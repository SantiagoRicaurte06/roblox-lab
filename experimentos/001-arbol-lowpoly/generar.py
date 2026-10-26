"""001 - Árbol low-poly (punto de partida).

Uso: blender --background --python experimentos/001-arbol-lowpoly/generar.py
Crea un árbol simple (tronco + copa) con pivote en la base y lo exporta a FBX.
"""
import os

import bpy

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SALIDA = os.path.join(RAIZ, "modelos", "exportados", "arbol-lowpoly-001.fbx")


def material(nombre, color):
    mat = bpy.data.materials.new(nombre)
    mat.diffuse_color = (*color, 1.0)
    mat.use_nodes = True
    mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*color, 1.0)
    return mat


bpy.ops.wm.read_factory_settings(use_empty=True)

bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.25, depth=1.5, location=(0, 0, 0.75))
tronco = bpy.context.active_object
tronco.name = "Tronco"
tronco.data.materials.append(material("Madera", (0.36, 0.22, 0.12)))

bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=1.0, location=(0, 0, 2.1))
copa = bpy.context.active_object
copa.name = "Copa"
copa.data.materials.append(material("Hojas", (0.20, 0.55, 0.25)))

bpy.ops.object.select_all(action="SELECT")
bpy.context.view_layer.objects.active = tronco
bpy.ops.object.join()
arbol = bpy.context.active_object
arbol.name = "ArbolLowPoly"
bpy.ops.object.shade_flat()

# Pivote en la base (z = 0)
bpy.context.scene.cursor.location = (0, 0, 0)
bpy.ops.object.origin_set(type="ORIGIN_CURSOR")

tris = sum(len(p.vertices) - 2 for p in arbol.data.polygons)
print(f"Triángulos: {tris}")

os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
bpy.ops.export_scene.fbx(filepath=SALIDA, use_selection=True, apply_unit_scale=True)
print(f"Exportado: {SALIDA}")
