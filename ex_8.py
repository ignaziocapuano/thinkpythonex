#An online retailer sells two products: widgets and gizmos. Each widget weighs 75
#grams. Each gizmo weighs 112 grams. Write a program that reads the number of
#widgets and the number of gizmos in an order from the user. Then your program
#should compute and display the total weight of the order.

peso_gizmo=112
peso_widget=75

gizmo_qt=int(input('Quantità di gizmo='))
widget_qt=int(input('Quantità di widget='))

peso_tot=gizmo_qt*peso_gizmo+widget_qt*peso_widget

print('Il peso totale è',peso_tot,'grammi')
