# plot_circuit.py

from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt

def visualize_circuit(circuit):
    # Draw the circuit
    circuit.draw(output='mpl')
    plt.show()

def simulate_and_visualize(circuit):
    from qiskit import Aer, execute
    
    # Simulate the quantum circuit
    simulator = Aer.get_backend('aer_simulator')
    result = execute(circuit, simulator).result()
    
    # Get the statevector
    statevector = result.get_statevector(circuit)
    
    # Visualize the Bloch sphere representation
    plot_bloch_multivector(statevector)
    plt.show()
    
    # Get measurement results
    counts = result.get_counts(circuit)
    
    # Plot the measurement results
    plot_histogram(counts)
    plt.show()
