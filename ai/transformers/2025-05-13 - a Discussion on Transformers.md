T = token embedding - transforms raw text into token vectors which encode **learned** information
P = position embedding - encodes token position

I = Input vector : $I=(T+P)$ 

$W_Q$ = learned weight matrix for Q : $Q = I \cdot W_Q$ 
$W_K$ = learned weight matrix for K : $K = I \cdot W_K$  
$W_V$ = learned weight matrix for V : $V = I \cdot W_V$ 

Q = attention Query embedding
K = attention Key embedding
V = attention Value embedding

A = Attention Matrix : $A = Q \cdot K$


```
legend 
[
	H = hello
	W = world
	! = !
]

a (3x3) attention matrix (i,j) demonstrates how i attends to j:
--------       -------------
HH HW H!        1    0    0 
WH WW W!  -->  0.5   1    0
!H !W !!       0.5  0.1   1
--------       -------------
```