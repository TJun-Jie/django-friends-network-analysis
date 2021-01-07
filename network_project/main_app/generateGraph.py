import matplotlib.pyplot as plt
import networkx as nx
import io

def create_graph():   
    G = nx.Graph()
    # rectanle width 1.5
    G.add_node('root')
    G.add_node('red')
    G.add_node('blue')
    # label: to_red
    G.add_edge('root', 'red')
    # label: to_blue
    G.add_edge('root', 'blue')
    nx.draw(G)
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    image_bytes = buf.getvalue().decode('utf-8')
    buf.close()
    plt.close()
    return image_bytes