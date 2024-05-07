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

<div class="math">
$$
\begin{aligned}
T(n) &= \left\{
\begin{array}{ll}
O(n^d) & \text{for } d > log_ba \\
O(n^dlogn) & \text{for } d = log_ba \\
O(n^{log_ba}) & \text{for } d < log_ba \\
\end{array}
\right.
\end{aligned}
$$
</div>

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
    <div class="math">
    $$
    \begin{aligned}
    D[i, j] &= 
    min \left\{
    \begin{array}{ll}
    D[i, j-1]+1 & \text{for insertion} \\
    D[i-1, j]+1 & \text{for deletion} \\
    D[i-1, j-1]+1 & \text{if } string1[i] \neq string2[j] \text{ for mismatch}\\
    D[i-1, j-1] & \text{if } string1[i] = string2[j] \text{ for match}\\
    \end{array}
    \right.
    \end{aligned}
    $$
    <\div>
    * **Discrete Knapsack Problem:** Choosing the object with maximum value per unit weight is not the optimal strategy anymore. Time complexity: $O(nW)$
        * With repetitions: 1D knapsack with:
        <br />$value(w) = \max_{\{i:w_i\leq w\}} \{value(w-w_i)+v_i\}$.
        * Without repetitions: Subproblem $value(w, i)$ is the maximum achievable value using a knapsack of weight $w$ using items $1,...,i$. Then the 2D knapsack problem becomes:
        <br /> $value(w, i) = max\{value(w-w_i, i-1) + v_i, value(w, i-1)\}$
    
    * **Placing parentheses** for an arithematic expression in order to maximise or minimise the value of the expression. $M(i, j)$ denotes the maximum possible value of sub expression from $i^{th}$  digit to $j^{th}$ digit and $m(i,j)$ denotes the minimum possible value.
        * 2D DP. We need to solve problems in order of increasing size, that is, increasing $j-i$.
        * Time complexity: $O(n^3)$.
        * We can determine the element $M(i,j)$ using the recurrence relation ($m(i, j)$ can be determined very similarly by choosing the minimum value instead of maximum):

    <div class="math">
    $$
    \begin{aligned}
    M(i,j) &= 
    max_{i\leq k \leq j-1} \left\{
    \begin{array}{ll}
    M(i, k) op_k M(k+1, j) \\
    M(i, k) op_k m(k+1, j) \\
    m(i, k) op_k M(k+1, j) \\
    m(i, k) op_k m(k+1, j) \\
    \end{array}
    \right.
    \end{aligned}
    $$
    <\div>

4. Which one is faster? Recursive or iterative DP?
    * Iterative algorithm goes by solving the smaller problem and then larger ones. This can be slower in case we don't need to solve all kinds of sub problems.
    * Recursive algorithm: Top down. Can be slightly slower than iterative algorithms because of the recursion overhead. But can be faster, for example in the case of solving knapsack problem where all object weights are multiples of 100.
