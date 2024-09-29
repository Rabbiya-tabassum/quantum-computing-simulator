# basic_circuit.py

from gates.quantum_gates import QuantumGates

def build_simple_circuit():
    # Initialize the QuantumGates class with 2 qubits
    qg = QuantumGates(2)
    
    # Apply gates
    qg.add_hadamard(0)          # Apply Hadamard gate to qubit 0
    qg.add_cnot(0, 1)           # Apply CNOT gate with qubit 0 as control and qubit 1 as target
    qg.measure_all()            # Measure all qubits
    
    return qg.get_circuit()
