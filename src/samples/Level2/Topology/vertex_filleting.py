##Copyright 2008 Jelle Feringa (jelleferinga@gmail.com)####This file is part of pythonOCC.####pythonOCC is free software: you can redistribute it and/or modify##it under the terms of the GNU General Public License as published by##the Free Software Foundation, either version 3 of the License, or##(at your option) any later version.####pythonOCC is distributed in the hope that it will be useful,##but WITHOUT ANY WARRANTY; without even the implied warranty of##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the##GNU General Public License for more details.####You should have received a copy of the GNU General Public License##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.# A sample that shows how to generate the gear geometry according# to knowledgefrom OCC.BRepPrimAPI import *from OCC.BRepFilletAPI import *from OCC.TColgp import *from OCC.gp import *from OCC.TopExp import *from OCC.BRep import *from OCC.Utils.Topology import Topofrom OCC.Display.SimpleGui import *display, start_display, add_menu, add_function_to_menu = init_display()cube = BRepPrimAPI_MakeBox(100,100,100).Shape()topo = Topo(cube)vertex_iterator = topo.vertices()vertA  = vertex_iterator.next()vertB = vertex_iterator.next()def vertex_fillet(cube, vert):    afillet = BRepFilletAPI_MakeFillet(cube)    cnt = 0    for edg in topo.edges_from_vertex(vert):        first, last = TopExp().FirstVertex(edg), TopExp().LastVertex(edg)        vertex, first_vert, last_vert = BRep_Tool().Pnt(vert), BRep_Tool().Pnt(first), BRep_Tool().Pnt(last)        if edg.Orientation():            if not vertex.IsEqual(first_vert, 0.001):                afillet.Add(0, 20., edg)            else:                afillet.Add(20, 0, edg)            cnt+=1    afillet.Build()    if afillet.IsDone():        return afillet.Shape()    else:        raise AssertionError, 'you failed on me you fool!'filleted_vertA = vertex_fillet(cube,vertA)display.DisplayShape(filleted_vertA)start_display()    