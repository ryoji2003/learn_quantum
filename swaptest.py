from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def create_circuit(prepare_psi, prepare_phi):
    qc = QuantumCircuit(3, 1) # 3量子ビット(q0:補助, q1:|ψ>, q2:|φ>), 1古典ビットの回路を作成

    prepare_psi(qc, 1)  # q1に|ψ>を準備
    prepare_phi(qc, 2)  # q2に|φ>を準備
    
    #回路の準備部分とスワップテスト部分を分けれるやつ
    qc.barrier()

    qc.h(0)            # 補助ビットにHゲート
    qc.cswap(0, 1, 2)  # 制御SWAPゲート
    qc.h(0)            # 補助ビットにHゲート
    
    qc.measure(0, 0)   # 補助ビット測定
    
    return qc

#|0>
def prepare_state_0(qc, target_qubit):
    pass

#|1>
def prepare_state_1(qc, target_qubit):
    qc.x(target_qubit) # Xゲートで|0>を|1>に反転
    
#|+>
def prepare_state_plus(qc, target_qubit):
    qc.h(target_qubit) # Hゲートで|0>を|+>に変換

simulator = AerSimulator()
shots = 4096 

#同一
print("|ψ>=|0>, |φ>=|0> の比較")

circuit_case1 = create_circuit(prepare_state_0, prepare_state_0)
job1 = simulator.run(circuit_case1, shots=shots)
counts1 = job1.result().get_counts(circuit_case1)

print(f"測定結果: {counts1}")
print(f"P(0) = {(counts1.get('0', 0)/shots)}")

figure1 = circuit_case1.draw(output='mpl')
figure1.savefig("circuit_case1.png")

print("-" * 50)

print(circuit_case1.draw(output='text'))


#直交するとき
print("|ψ>=|0>, |φ>=|1> の比較")

circuit_case2 = create_circuit(prepare_state_0, prepare_state_1)
job2 = simulator.run(circuit_case2, shots=shots)
counts2 = job2.result().get_counts(circuit_case2)

print(f"測定結果: {counts2}")
print(f"P(0) = {(counts2.get('0', 0)/shots)}")

figure2 = circuit_case2.draw(output='mpl')
figure2.savefig("circuit_case2.png")

print("-" * 50)

print(circuit_case2.draw(output='text'))


#内積が1/2の時
print("--- ケース3: |ψ>=|0>, |φ>=|+> の比較 ---")

circuit_case3 = create_circuit(prepare_state_0, prepare_state_plus)
job3 = simulator.run(circuit_case3, shots=shots)
counts3 = job3.result().get_counts(circuit_case3)

print(f"測定結果: {counts3}")
print(f"P(0) = {(counts3.get('0', 0)/shots)}")

figure3 = circuit_case3.draw(output='mpl')
figure3.savefig("circuit_case3.png")

print("-" * 50)

print(circuit_case3.draw(output='text'))