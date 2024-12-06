def check_path(graph, starting_point, ending_point):
    visited = []
    
    if starting_point == ending_point:
        return True
    
    for next_point in graph.get(starting_point,[]):
        if next_point not in visited and check_path(graph, next_point, ending_point):
            return True
        
    return False

def main():
    graph_1 = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
    }

    print(check_path(graph_1, "A", "B")) # True
    print(check_path(graph_1, "B", "A")) # False
    print(check_path(graph_1, "A", "E")) # True
    print(check_path(graph_1, "E", "B")) # False
    
    print(f"{30 * "-"}")
    
    graph_2 = {
        "Tbilisi": ["Gori", "Telavi"],
        "Telavi": ["Akhmeta", "Tbilisi"],
        "Gori": ["Khashuri", "Tbilisi"],
        "Khashuri": ["Borjomi", "Kutaisi", "Tbilisi"],
        "Kutaisi": ["Zugdidi", "Mestia", "Khashuri"]
    }

    print(check_path(graph_2, "Tbilisi", "Borjomi")) # True
    print(check_path(graph_2, "Mestia", "Kutaisi")) # False
    print(check_path(graph_2, "Gori", "Zugdidi")) # True
    print(check_path(graph_2, "Telavi", "Borjomi")) # True

if __name__ == "__main__":
    main()