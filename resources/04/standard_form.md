---
title: Standard Form
...

# Starter

::: {.Exercise t="Calculate:"}
#) `simplify('10^2')`
#) `simplify('10^3')`
#) `simplify('10^(-1)')`
#) `simplify('10^5')`
#) `simplify('10^(-2)')`
#) `simplify('10^0')`
:::

::: {.Exercise t="Match the equivalent operations:"}

-----------------------     ---------------------
$x \div 2^{-1}$             $x \times 10^{-3} =$  
$x \times 10^0$             $x \div 2^2 =$  
$x \div 10^3$               $x \div 10^4 =$  
$x \times 10^4$             $x \times 2 =$  
$x \div 2$                  $x \div 10^0 =$  
$x \times 2^{-2}$           $x \times 2^{-1} =$
-----------------------     ---------------------

:::

# Inconvenience of large numbers

::: {.Example t="Read out the number:"}
#) 70000000
#) 0.0000000025
#) 21000000000
:::

::: Example
#) Which number is bigger between 500000000 and 50000000?
#) Which number is smaller between 0.00000001 and 0.0000001?
:::

# Standard form

::: {.Definition t="Standard Form"}
A number that can be written as a decimal multiplied by a power of 10
:::

\begin{center}
\begin{tikzpicture}
\node (number) at (0, 0) {\LARGE \color{darkblue} $x$};
\node (numberconditions) at (0, -1.2) {\color{darkblue} $1 \leq x < 10$};
\draw[darkblue,thick,->] (numberconditions.north) -- (number.south);
\node[right=0cm of number.east] (power) {\Large $\times {\color{darkred} 10^a}$};
\node (powertext) at (3.5, 0) {\color{darkred} Power of 10};
\draw[darkred,thick,->] (powertext.west) -- (power.east);
\end{tikzpicture}
\end{center}

# Standard form

::: {.Example t="Are the following numbers in standard form?"}
#) $6 \times 10^3$ [1cm]{.gap}
#) $12 \times 10^{-6}$ [1cm]{.gap}
#) $3 \times 8^5$ [1cm]{.gap}
:::

# Mini-Whiteboard Activity

::: {.Example t="Are these numbers in Standard Form? Why?"}
#) $5 \times 10^2$ [1cm]{.gap}
#) $8 \times 10^9$ [1cm]{.gap}
#) $10 \times 10^6$ [1cm]{.gap}
#) $1.8 \times 10^2$ [1cm]{.gap}
#) $0.49 \times 10^{-20}$ [1cm]{.gap}
#) $4.75 \div 10^{-17}$ [1cm]{.gap}
:::

# Standard form

::: {.Example t="What does $5 \times 10^3$ represent?"}
$$5 \times {\color{darkred} 10^3} = 5 \times {\color{darkred} 1000} = 5000$$
:::

::: {.Solution t="Quicker method"}
$$5 \times 10^{\color{darkred} 3} = 5{{\color{darkred} 000}}$$
The power tells us how many NUMBERS come after the 5
:::

# Standard form

::: {.Example t="What does $4.3 \times 10^2$ represent?"}
$$4.3 \times {\color{darkred} 10^2} = 4.3 \times {\color{darkred} 100} = 430$$
:::

::: {.Solution t="Quicker way"}
$$4.3 \times 10^{\color{darkred} 2} = 4{{\color{darkred} 30}}$$
The power tells us how many NUMBERS come after the 4
:::

# Standard form

::: {.Exercise t="Convert the following into ordinary numbers"}
#) `stf2dec(400)`
#) `stf2dec(900)`
#) `stf2dec(20000)`
#) `stf2dec(1500)`
#) `stf2dec(28000)`
#) `stf2dec(3000000)`
#) `stf2dec(61000000)`
#) `stf2dec(975000000)`
:::

::: {.Extension t="Convert the following into ordinary numbers"}
#) `stf2dec(674000)`
#) `stf2dec(8045)`
#) `stf2dec(10000.1)`
:::

# Standard form

::: {.Example t="Convert 200 into standard form"}
$$200 = 2 \times {\color{darkred} 100} = 2 \times {\color{darkred} 10^2}$$
:::

::: {.Solution t="Quicker method"}
$$2{\color{darkred} 00} = 2 \times 10^{\color{darkred} 2}$$
The number of digits after the 2 tells us the power of 10
:::

# Standard form

::: {.Example t="Convert 5100 into standard form"}
$$5100 = 5.1 \times {\color{darkred} 1000} = 5.1 \times {\color{darkred} 10^3}$$
:::

::: {.Solution t="Quicker method"}
$$5{\color{darkred} 100} = 5.1 \times 10^{\color{darkred} 3}$$
The number of digits after the 5 tells us the power of 10
:::

# Standard form

::: {.Exercise t="Convert the following into standard form"}
#) `stf(300)`
#) `stf(6000)`
#) `stf(20)`
#) `stf(820)`
#) `stf(470000)`
#) `stf(10)`
#) `stf(552)`
#) `stf(13500000)`
:::

::: {.Extension t="Convert the following into standard form"}
#) `stf(505050)`
#) `stf(1)`
#) `stf(981040000000)`
:::

# Standard form

::: Remember
$x \times 10^{-3} = x \div 10^3$
:::

::: {.Example t="What does $5 \times 10^{-3}$ represent?"}
$$5 {\color{darkred} \times 10^{-3}} = 5 {\color{darkred} \div 10^3} = 5 {\color{darkred} \div 1000} = 0.005$$
:::

::: {.Solution t="Quicker method"}
$$5 \times 10^{\color{darkred} -3} = {{\color{darkred} 0.00}}5$$
The '-' power tells us how many ZEROS come BEFORE the 5 INCLUDING the one before the decimal point
:::

# Standard form

::: Remember
$x \times 10^{-4} = x \div 10^4$
:::

::: {.Example t="What does $4.3 \times 10^{-4}$ represent?"}
$$6.1 {\color{darkred} \times 10^{-4}} = 6.1 {\color{darkred} \div 10^4} = 6.1 {\color{darkred} \div 1000} = 0.00061$$
:::

::: {.Solution t="Quicker method"}
$$6.1 \times 10^{\color{darkred} -4} = {{\color{darkred} 0.000}}61$$
The '-' power tells us how many ZEROS come BEFORE the 6 INCLUDING the one before the decimal point
:::

# Standard form

::: {.Exercise t="Convert the following into ordinary numbers"}
#) `stf2dec(0.6)`
#) `stf2dec(0.03)`
#) `stf2dec(0.008)`
#) `stf2dec(0.55)`
#) `stf2dec(0.049)`
#) `stf2dec('0.0003')`
#) `stf2dec('0.000014')`
#) `stf2dec('0.00000245')`
:::

::: {.Extension t="Convert the following into ordinary numbers"}
#) `stf2dec('0.0000383')`
#) `stf2dec(0.0007106)`
#) `stf2dec('0.0000090099')`
:::

# Standard form

::: Remember
$x \div 10^2 = x \times 10^{-2}$
:::

::: {.Example t="Convert 0.02 into standard form"}
$$0.02 = 2 {\color{darkred} \div 100} = 2 {\color{darkred} \div 10^2} = 2 {\color{darkred}  \times 10^{-2}}$$
:::

::: {.Solution t="Quicker method"}
$${\color{darkred} 0.0}2 = 2 \times 10^{\color{darkred} {-2}}$$
The number of zeros before the 2 tells us the '-' power of 10
:::

# Standard form

::: Remember
$x \div 10^3 = x \times 10^{-3}$
:::

::: {.Example t="Convert 0.0045 into standard form"}
$$0.0045 = 4.5 {\color{darkred} \div 1000} = 4.5 {\color{darkred} \div 10^3} = 4.5 {\color{darkred} \times 10^{-3}}$$
:::

::: {.Solution t="Quicker method"}
$${\color{darkred} 0.00}45 = 4.5 \times 10^{\color{darkred} {-3}}$$
The number of zeros before the 4 tells us the '-' power of 10
:::

# Standard form

::: {.Exercise t="Convert the following into standard form"}
#) `stf(0.4)`
#) `stf(0.07)`
#) `stf(0.01)`
#) `stf(0.37)`
#) `stf(0.000506)`
#) `stf('0.00040')`
#) `stf('0.0000333')`
#) `stf('0.00000909')`
:::

::: {.Extension t="Convert the following into standard form"}
#) `stf(0.01023)`
#) `stf(1)`
#) `stf('0.101010')`
:::

# Multiplying numbers in standard form

::: {.Example t="Work out the following (leave answer in St.F)"}
$3 \times 10^2 \times 2 \times 10^3$
:::

::: Solution
$3 \times {\color{darkred} 10^2 \times 2} \times 10^3 = 3 \times {\color{darkred} 2 \times 10^2} \times 10^3 = 6 \times 10^5$
:::

::: {.Example t="Work out the following (leave answer in St.F)"}
$6 \times 10^{-4} \times 3 \times 10^2$
:::

::: Solution
$6 \times {\color{darkred} 10^{-4} \times 3} \times 10^2 = 6 \times {\color{darkred} 3 \times 10^{-4}} \times 10^2 = 18 \times 10^{-2}$

$= 1.8 \times 10 \times 10^{-2} = 1.8 \times 10^{-1}$
:::

# Multiplying numbers in standard form

::: {.Exercise t="Work out the following (leave answers in St.F)"}
#) `stfmult(100, 2000)`
#) `stfmult(300, 200)`
#) `stfmult(0.1, 9000)`
#) `stfmult(0.003, 0.00003)`
#) `stfmult(40000, 500)`
#) `stfmult(0.006, 0.0000009)`
#) `stfmult(5000, 0.0008)`
#) `stfmult(1200, 0.000004)`
:::

::: {.Extension t="Work out the following (leave answers in St.F)"}
#) `stfmult(5500, 0.000002)`
#) `stfmult(0.0042, 0.004)`
#) `stfmult(0.25, 0.0064)`
:::
