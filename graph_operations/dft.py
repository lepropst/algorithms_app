from data_structures.nodes import GraphNode


def dft(node: GraphNode):
    st: list[GraphNode] = []
    visited = []
    visited.append(node)
    st.append(node)
    try:
        while (n := st.pop()) != None:
            if n in visited:
                print(f"N {n}")
            else:
                visited.append(n)
                print(f"N {n}")
            for vertice in n.vertices:
                if vertice in visited:
                    continue
                st.append(vertice)

                print([str(x) for x in visited])
        return [str(x) for x in visited]
    except IndexError:
        return [str(x) for x in visited]
