# main.py

from circuits.basic_circuit import build_simple_circuit
from visualizations.plot_circuit import visualize_circuit, simulate_and_visualize

def main():
    # Build a simple circuit
    circuit = build_simple_circuit()
    
    # Visualize the circuit diagram
    print("Quantum Circuit:")
    visualize_circuit(circuit)
    
    # Simulate and visualize the results
    simulate_and_visualize(circuit)

if __name__ == "__main__":
    main()
