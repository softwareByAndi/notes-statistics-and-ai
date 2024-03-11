---
tags:
  - "#statistics"
links:
  - "[[assessing the performance of linear regression]]"
---
$R^2$ represents the fraction of variation in $Y$ that has been explained
- [[Residual Sum of Squares - RSS|RSS]] describes the unexplained variation in Y
- [[Total Sum of Squares - TSS|TSS]] describes the "initial" variation in $Y$
# $R^2 = 1 - \frac{RSS}{TSS}$

note that $R^2$ always increases with the addition of new variables, so if more than one [[Datum Features|variable]] is used, then $R^2$ can be adjusted to consider multiple [[degrees of freedom - DOF]]
# $\text{adjusted } R^2: 1 - \frac{RSS / (n - m - 1)}{TSS / (n - 1)}$
- m = number of [[Datum Features|variables]]

an alternative equation

![[img_adjusted_r_squared_equation.png]]
