import osmnx as ox
import matplotlib.pyplot as plt

# Configura el lugar que deseas analizar
place_name = "New York City, New York, USA"

# Obtiene la red de calles de la ciudad
G = ox.graph_from_place(place_name, network_type='drive')

# Dibuja la red de calles
fig, ax = ox.plot_graph(G, node_size=0, bgcolor='k', edge_color='w', edge_linewidth=0.5)
plt.title(f'Road Network of {place_name}')
plt.show()

# Coordenadas de los puntos de inicio y fin
start = (40.712776, -74.005974)  # Ejemplo: Times Square
end = (40.730610, -73.935242)    # Ejemplo: Central Park

# Encuentra los nodos más cercanos en la red de calles
orig_node = ox.distance.nearest_nodes(G, start[1], start[0])
dest_node = ox.distance.nearest_nodes(G, end[1], end[0])

# Calcula la ruta más corta
route = ox.shortest_path(G, orig_node, dest_node)

# Dibuja la ruta en la red
fig, ax = ox.plot_graph_route(G, route, node_size=0, bgcolor='k', edge_color='w', edge_linewidth=0.5)
plt.title('Optimal Route from Start to End')
plt.show()
