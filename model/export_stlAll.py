import os
import Mesh
import MeshPart
 
# 現在のディレクトリ
PWD = r'D:\openfoam\000_send\model'
print('現在のディレクトリ：',PWD)
print(os.getcwd())
 
labels = []
 
doc = App.ActiveDocument
print(doc)
 
for obj in doc.Objects:
  if obj.Visibility == True:
        mesh = doc.addObject("Mesh::Feature", "Mesh")
        print(mesh)
        # mefisto
        #mesh.Mesh = MeshPart.meshFromShape(Shape=obj.Shape, MaxLength=10)
        # standard
        mesh.Mesh = Mesh.Mesh(obj.Shape.tessellate(0.01))
        print(mesh.Mesh)

        label = obj.Label[:]
        labels.append(label)
        Mesh.export([mesh], fr'{PWD}/{label}.ast')
        print(label)
        doc.removeObject(mesh.Name)
          
print(doc.Label)
print(labels, type(labels))
 
with open(rf'{PWD}/{doc.Label}.stl', 'w') as f:
    print('test')
    for label in labels:
        with open(rf'{PWD}/{label}.ast', 'r') as fi:
            for line in fi:
                if line[:5] == 'solid':
                    line = 'solid ' + label + '\n'
                elif line[:8] == 'endsolid':
                    line = 'endsolid ' + label + '\n'
                f.write(line)
 
for label in labels:
    os.remove(rf'{PWD}/{label}.ast')