# スワップテストの導出

### 1. 初期状態
初期状態 $|\Psi_0\rangle$ は、補助ビット $|0\rangle$ と2つの入力状態 $|\psi\rangle, |\phi\rangle$ のテンソル積で与えられる。
$$
|\Psi_0\rangle = |0\rangle |\psi\rangle |\phi\rangle
$$

### 2. Hゲート
補助ビットにアダマール(H)ゲートを作用させる。
$$
|\Psi_1\rangle = \frac{1}{\sqrt{2}} (|0\rangle|\psi\rangle|\phi\rangle + |1\rangle|\psi\rangle|\phi\rangle)
$$

### 3. CSWAPゲート
補助ビットを制御ビットとして、制御SWAP(CSWAP)ゲートを作用させる。
$$
|\Psi_2\rangle = \frac{1}{\sqrt{2}} (|0\rangle|\psi\rangle|\phi\rangle + |1\rangle|\phi\rangle|\psi\rangle)
$$

### 4. 2回目のHゲート
再び補助ビットにHゲートを作用させ、補助ビットの状態で式を整理する。
$$
|\Psi_3\rangle = \frac{1}{2} [ (|0\rangle + |1\rangle)|\psi\rangle|\phi\rangle + (|0\rangle - |1\rangle)|\phi\rangle|\psi\rangle ]
$$
$$
= \frac{1}{2} |0\rangle (|\psi\rangle|\phi\rangle + |\phi\rangle|\psi\rangle) + \frac{1}{2} |1\rangle (|\psi\rangle|\phi\rangle - |\phi\rangle|\psi\rangle)
$$

### 5. 測定確率 P(0) の計算
補助ビットが $|0\rangle$ として測定される確率は、対応する状態ベクトルのノルムの2乗である。
$$
P(0) = \left\| \frac{1}{2} (|\psi\rangle|\phi\rangle + |\phi\rangle|\psi\rangle) \right\|^2 = \frac{1}{4} \langle \psi\phi + \phi\psi | \psi\phi + \phi\psi \rangle
$$
内積を展開すると、
$$
P(0) = \frac{1}{4} ( \langle\psi\phi|\psi\phi\rangle + \langle\psi\phi|\phi\psi\rangle + \langle\phi\psi|\psi\phi\rangle + \langle\phi\psi|\phi\psi\rangle )
$$
各項ha、
* $\langle\psi\phi|\psi\phi\rangle = 1$
* $\langle\psi\phi|\phi\psi\rangle = |\langle\psi|\phi\rangle|^2$
* $\langle\phi\psi|\psi\phi\rangle = |\langle\psi|\phi\rangle|^2$
* $\langle\phi\psi|\phi\psi\rangle = 1$

したがって、
$$
P(0) = \frac{1}{4} (2 + 2|\langle\psi|\phi\rangle|^2)
$$

### 6. 最終結果
$$
P(0) = \frac{1}{2} + \frac{1}{2} |\langle\psi|\phi\rangle|^2
$$