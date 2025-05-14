T = token embedding - transforms raw text into token vectors which encode **learned** information
P = position embedding - encodes token position

I = Input vector : $I=(T+P)$ 

$W_Q$ = learned weight matrix for Q : $Q = I \cdot W_Q$ 
$W_K$ = learned weight matrix for K : $K = I \cdot W_K$  
$W_V$ = learned weight matrix for V : $V = I \cdot W_V$ 

Q = attention Query embedding
K = attention Key embedding
V = attention Value embedding

A = Attention Matrix : $A = Q \cdot K^T$


##### a (3x3) attention matrix (i,j) demonstrates how i attends to j:
`input = ['hello', 'world', '!']`
$I = (3x2) : W_i = (2x2)$  
$$
\begin{bmatrix}
	\text{HH} & \text{HW} & \text{H!} \\
	\text{WH} & \text{WW} & \text{W!} \\
	\text{!H} & \text{!W} & \text{!!}
\end{bmatrix}
$$
$$
\begin{align}
\underbrace{
	\begin{bmatrix}
		I \times W_q \\
		I \times W_k \\
		I \times W_v
	\end{bmatrix}
	\rightarrow
	\begin{bmatrix}
		Q \\
		K \\
		V
	\end{bmatrix}
}_{\text{do for all tokens}} 
\rightarrow
% QK multiplication result
&\underbrace{
  \begin{bmatrix}
    16 & 22 & 30 \\
    25 & 15 & 1 \\
    20 & 4 & 9
  \end{bmatrix}
}_{Q_{all \space tokens} \cdot K_{all \space tokens}^T}
% Scale arrow
\xrightarrow{\text{scale + mask + softmax + dropout}}
% Softmax result
\underbrace{
  \begin{bmatrix}
    1.0 & - & - \\
    0.7 & 0.5 & - \\
    0.5 & 0.2 & 0.1
  \end{bmatrix}
}_{\text{A}} 
\end{align}
$$
$$
A \times V \rightarrow \text{weighted output}
$$

