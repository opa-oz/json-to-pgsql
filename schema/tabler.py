import networkx as nx
import matplotlib.pyplot as plt
import opyls

from schema.sql import Table


def get_tables_graph(tables: list[Table]):
    output_dir = opyls.basedir('output', True)
    G = nx.DiGraph()

    for table in tables:
        G.add_node(table.name)

        for column in table.columns:
            if column.foreign_key:
                G.add_edge(table.name, column.foreign_key)

    nx.draw(G, with_labels=False, font_weight='bold')
    plt.show(block=False)
    plt.savefig(output_dir / "graph.png", format="PNG")
