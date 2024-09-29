# quantum_gates.py

from qiskit import QuantumCircuit

class QuantumGates:
    def __init__(self, num_qubits):
        self.circuit = QuantumCircuit(num_qubits)
    
    def add_hadamard(self, qubit):
        self.circuit.h(qubit)
    
    def add_pauli_x(self, qubit):
        self.circuit.x(qubit)
    
    def add_pauli_y(self, qubit):
        self.circuit.y(qubit)
    
    def add_pauli_z(self, qubit):
        self.circuit.z(qubit)
    
    def add_cnot(self, control_qubit, target_qubit):
        self.circuit.cx(control_qubit, target_qubit)
    
    def add_swap(self, qubit1, qubit2):
        self.circuit.swap(qubit1, qubit2)
    
    def add_t_gate(self, qubit):
        self.circuit.t(qubit)
    
    def add_s_gate(self, qubit):
        self.circuit.s(qubit)
    
    def measure_all(self):
        self.circuit.measure_all()
    
    def get_circuit(self):
        return self.circuit
