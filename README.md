# Algorithmic-Toolbox
My solution for the "Algorithmic Toolbox" course on Coursera:
https://www.coursera.org/learn/algorithmic-toolbox/

Here are my notes from the course:

## Basics
### Fibonacci Numbers
$$F_n = F_{n-1} + F_{n-2}$$
with $F_0 = 0$ and $F_1 = 1$
1. Fibonacci numbers grow rapidly: $F_n \geq 2^{n/2}$ for $n \geq 6$.
2. Naive algorithm using recursion leads to a tree of recursive calls. $T_n = = T_{n-1} + T_{n-2} + c$ for $n>1$. Grows the same way as Fibonacci numbers themselves - exponentially.
3. Improved algorithm using iterative approach. O(n) complexity.

### Greatest Common Divisor
1. Naive Algorithm $T(a,b) = O(min(a, b))$
2. Lemma: Let $a'$ be the remainder when a is divided by b. Then, $GCD(a,b) = GCD(a',b) = GCD(b, a')$
3. Euclidean Algorithm is based on this lemma. Takes $log(ab)$ steps.

### Compute  Runtimes
1. Actual runtime of a program on a computer depends on things like speed of the computer, system architecture, compiler used and details of memory hierarchy of the machine.
2. Key Idea - All these issues can multiply runtimes by (possibly large) constant. So, measure runtimes in a way that ignores constant multiples.
3. It is thus helpful to see how the algorithm scales with the input size - ASYMPTOTIC RUNTIMES.
4. Big O notation: $f(n) = O(g(n))$ means $f$ is bounded above by $g$.
5. $f(n) = \Omega(g(n))$ means $f$ is bounded below by $g$.
6. $f(n) = \Theta(g(n))$ means $f$ grows at the same rate as $g$.
$$log(n) \prec \sqrt n \prec n \prec n*log(n) \prec n^a \prec b^n$$
where $a > 0$ and $b>1$

## Greedy Algorithms
1. **Greedy Strategy:**
    1. Make a safe move: A greedy choice is called a safe move if there is an optimal solution consistent with this first move
    2. Reduce to smaller sub-problem
    3. Iterate

2. Example problems:
* **Largest number** that can be constructed using the digits in an array.
    * Naive solution: $O(n!)$
    * Safe move: Choose the largest number to put at the most significant digit
    * Greedy solution: $O(nlog(n))$
* **Car fueling problem** Going from point A to B minimising the number of refills.
    * Naive solution: $O(2^n)$
    * Safe move: choose the farthest reachable gas station.
    * Greedy solution: $O(n)$
* **Celebration Party problem:** Many children come to a celebration. Organise them into a minimum possible number of groups such that any 2 children in the same group differ by a maximum of x years.
    * Naive solution: $\Omega(2^n)$
    * Safe move: If we represent each child as a point on the number line, the safe move is to cover the leftmost point with a segment of length x with left end at this point.
    * Greedy solution: $O(nlog(n))$
* **Fractional Knapsack problem:** We have n items with given weights and values. Given a bag which can carry a maximum weight W, if we can keep fractions of items, what items should we keep in what portion?
    * Safe move: Keep as much as possible of the item with the maximal value per unit weight.
    * Greedy solution: $O(nlog(n))$

## Divide and Conquer
1. **Strategy:**
    1. Divide: Break into non-overlapping problems of the same type.
    2. Conquer: Solve each sub-problem recursively.
    3. Combine: Combine the solutions of the sub-problems.

2. **Master Theorem:** If $T(n) = aT(\lceil n/b \rceil) + O(n^d)$ for constants $a>0$, $b>1$ and $d\geq0$, then, it can be proven using recurrence trees that:
![Master Theorem Equation](data:image/gif;base64,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)
<!-- $$
\begin{matrix}
T(n) &= \left\{
\begin{array}{ll}
O(n^d) & \text{for } d > \log_b a \\
O(n^d \log n) & \text{for } d = \log_b a \\
O(n^{\log_b a}) & \text{for } d < \log_b a \\
\end{array}
\right.
\end{matrix}
$$ -->

3. Example Problems:
* **Binary Search** to find the position of an element in a sorted array.
    * Time complexity: $T(n) = T(\lfloor n/2 \rfloor) + c$ where $c$ is a constant $=> T(n) = O(log(n))$.
* **Polynomial multiplication:** used for error-correcting codes, large integer multiplication, generating functions and convolutions in signal processing.
    * Naive Algorithm: $O(n^2)$ for polynomials of degree $n$.
    * Divide and conquer: Let $A(x) = D_1(x)x^{n/2} + D_0(x)$ and $B(x) = E_1(x)x^{n/2} + E_0(x)$. Then
    $$AB = (D_1E_1)x^n+(D_1E_0+D_0E_1)x^{n/2}+D_0E_0$$
    * This needs 4 multiplications, $D_1E_1$, $D_1E_0$, $D_0E_1$ and $D_0E_0$. Time complexity:
    $$T(n) = 4*T(n/2) + kn => T(n) = \sum_{i=0}^{log_2n} 4^ik(n/2^i) = \Theta(n^2)$$
    * Karatsuba approach: These 4 multiplications can be reduced to 3.
    $$AB = (D_1E_1)x^n+(D_1E_0+D_0E_1)x^{n/2}+D_0E_0 \\
         = (D_1E_1)x^n+((D_0+D_1)*(E_0+E_1)-)x^{n/2}+D_0E_0$$
    * Time reduces to: $T(n) = 3*T(n/2) + kn => T(n) = O(n^{1.58})$

4. Algorithms for sorting:
    * **Selection sort:** Select the minimum element among the remaining elements and put it at the beginning. The sorted part keeps on growing. Time: $O(n^2)$. Other quadratic time algorithms: Insertion Sort, Bubble Sort.
    * **Merge Sort:** Divide and conquer. Time: $\Theta(nlogn)$, which is also the lower bound for comparison based sorting.
    * **Non comparison based sorting:** Eg.: Counting sort algorithm. When there is a finite set of possible entities in the input array. Time: $O(n)$.
    * **Quick sort:** Random pivot implies $O(nlogn)$ time on average. Randomised version of divide and conquer. Balanced partitions save on the number of comparisons required to sort the array.
        * Quick sort is tail recursive. Tail recursive problems can be optimised in terms of space on stack by eliminating the last recursive call. Modern compilers do tail call elimination to optimize the tail-recursive code. Tail call elimination reduces the space complexity of recursion from O(N) to O(logN) in worst case.
        * Since there are 2 recursive calls, we can further be optimise time by choosing the shorter sub array for the recursive call so as to reduce the size of recursion stack.
        * Intro sort: used in many practical implementations of quick sort. Pivot selection is deterministic - on the basis of some heurstic like first/middle/last element. If the recursion depth exceeds a threshold $clogn$, algorithm switches to heap sort.

## Dynamic Programming
1. For problems that can be defined in a recursive fashion, when we memoize the results, it is called Dynamic programming.
2. Backtracking is used to reconstruct the optimal solution.
3. Example Problems:
    * **Coin change problem:**
    mincoins[amount] = 1 + min(mincoins[amount - coin_i] for coin_i in denominations).
    * **Edit distance problem:** 
    Types of possible edits between string1 and string2: matches, mismatches, insertions and deletions. We use 2D dynamic programmming where each matrix element $D[i,j]$ is the edit distance between string1[:i] and string2[:j]. We fill the matrix row by row using the rule:
![Edit Distance Equation](data:image/png;base64,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)
    <!-- \begin{aligned}
    D[i, j] &= 
    min \left\{
    \begin{array}{ll}
    D[i, j-1]+1 & \text{for insertion} \\
    D[i-1, j]+1 & \text{for deletion} \\
    D[i-1, j-1]+1 & \text{if } string1[i] \neq string2[j] \text{ for mismatch}\\
    D[i-1, j-1] & \text{if } string1[i] = string2[j] \text{ for match}\\
    \end{array}
    \right.
    \end{aligned} -->

    * **Discrete Knapsack Problem:** Choosing the object with maximum value per unit weight is not the optimal strategy anymore. Time complexity: $O(nW)$
        * With repetitions: 1D knapsack with:
        <br />$value(w) = \max_{\{i:w_i\leq w\}} \{value(w-w_i)+v_i\}$.
        * Without repetitions: Subproblem $value(w, i)$ is the maximum achievable value using a knapsack of weight $w$ using items $1,...,i$. Then the 2D knapsack problem becomes:
        <br /> $value(w, i) = max\{value(w-w_i, i-1) + v_i, value(w, i-1)\}$
    
    * **Placing parentheses** for an arithematic expression in order to maximise or minimise the value of the expression. $M(i, j)$ denotes the maximum possible value of sub expression from $i^{th}$  digit to $j^{th}$ digit and $m(i,j)$ denotes the minimum possible value.
        * 2D DP. We need to solve problems in order of increasing size, that is, increasing $j-i$.
        * Time complexity: $O(n^3)$.
        * We can determine the element $M(i,j)$ using the recurrence relation ($m(i, j)$ can be determined very similarly by choosing the minimum value instead of maximum):
 ![Placing Parentheses Equation](data:image/png;base64,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)
    <!-- \begin{aligned}
    M(i,j) &= 
    max_{i\leq k \leq j-1} \left\{
    \begin{array}{ll}
    M(i, k) op_k M(k+1, j) \\
    M(i, k) op_k m(k+1, j) \\
    m(i, k) op_k M(k+1, j) \\
    m(i, k) op_k m(k+1, j) \\
    \end{array}
    \right.
    \end{aligned} -->
4. Which one is faster? Recursive or iterative DP?
    * Iterative algorithm goes by solving the smaller problem and then larger ones. This can be slower in case we don't need to solve all kinds of sub problems.
    * Recursive algorithm: Top down. Can be slightly slower than iterative algorithms because of the recursion overhead. But can be faster, for example in the case of solving knapsack problem where all object weights are multiples of 100.
