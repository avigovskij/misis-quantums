from qiskit import QuantumRegister, QuantumCircuit


class BellStateUpdater:
    """Class that updates quantum circuit with chosen bell state by named methods"""

    def __init__(self, qbits: QuantumRegister, circuit: QuantumCircuit) -> None:
        """
        Initial method for bell state updater
        :param qbits:   Register with qbits
        :param circuit: Circuit to update
        """
        self._qbits = qbits
        self._circuit = circuit

    def bell_phi_plus(self, qbit_indexes=None):
        """Method updates circuit to 1/sqrt(2)(|00> + |11>) state"""
        qbit_indexes = qbit_indexes if qbit_indexes else [0, 1]
        qbit_0, qbit_1, *_ = self._qbits[qbit_indexes[0]], self._qbits[qbit_indexes[1]]

        self._circuit.h(qubit=qbit_0)
        self._circuit.cx(control_qubit=qbit_0, target_qubit=qbit_1)

    def bell_phi_minus(self, qbit_indexes):
        """Method updates circuit to 1/sqrt(2)(|00> - |11>) state"""
        qbit_indexes = qbit_indexes if qbit_indexes else [0, 1]
        qbit_0, qbit_1, *_ = self._qbits[qbit_indexes[0]], self._qbits[qbit_indexes[1]]

        self._circuit.x(qubit=qbit_0)
        self._circuit.h(qubit=qbit_0)
        self._circuit.cx(control_qubit=qbit_0, target_qubit=qbit_1)

    def bell_psi_plus(self, qbit_indexes):
        """Method updates circuit to 1/sqrt(2)(|01> + |10>) state"""
        qbit_indexes = qbit_indexes if qbit_indexes else [0, 1]
        qbit_0, qbit_1, *_ = self._qbits[qbit_indexes[0]], self._qbits[qbit_indexes[1]]

        self._circuit.h(qubit=qbit_0)
        self._circuit.cx(control_qubit=qbit_0, target_qubit=qbit_1)
        self._circuit.x(qubit=qbit_1)

    def bell_psi_minus(self, qbit_indexes):
        """Method updates circuit to 1/sqrt(2)(|01> - |10>) state"""
        qbit_indexes = qbit_indexes if qbit_indexes else [0, 1]
        qbit_0, qbit_1, *_ = self._qbits[qbit_indexes[0]], self._qbits[qbit_indexes[1]]

        self._circuit.x(qubit=qbit_0)
        self._circuit.h(qubit=qbit_0)
        self._circuit.cx(control_qubit=qbit_0, target_qubit=qbit_1)
        self._circuit.x(qubit=qbit_1)
