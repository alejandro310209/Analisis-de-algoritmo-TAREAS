# Tarea 4 · Programación dinámica en LeetCode

**Curso:** Análisis de algoritmos
**Institución:** ITM
**Semestre:** 2026-2
**Modalidad:** Individual

## Objetivo

Resolver dos problemas de LeetCode utilizando programación dinámica, identificando el estado, la recurrencia, los casos base y la complejidad de cada solución.

Los problemas desarrollados son:

1. [322. Coin Change](https://leetcode.com/problems/coin-change/)
2. [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

---

# 1. 322. Coin Change

**Problema:** [LeetCode 322 - Coin Change](https://leetcode.com/problems/coin-change/)

## Descripción

Dado un conjunto de monedas y una cantidad `amount`, se debe encontrar el número mínimo de monedas necesarias para obtener exactamente esa cantidad. Cada denominación de moneda puede utilizarse una cantidad ilimitada de veces.

## Estado

`dp[x]` representa el número mínimo de monedas necesarias para formar exactamente la cantidad `x`.

## Casos base

El caso base es:

`dp[0] = 0`

Esto significa que para formar la cantidad 0 no se necesita ninguna moneda.

Inicialmente, las demás posiciones se establecen con un valor grande (`amount + 1`) para representar que todavía no se conoce una solución.

## Recurrencia

Para cada cantidad `x` y cada moneda `c` que pueda utilizarse:

`dp[x] = min(dp[x], 1 + dp[x - c])`

Se toma el mínimo entre la solución que ya se tenía y la solución obtenida utilizando una moneda adicional.

## Reutilización de las monedas

Las monedas se pueden utilizar **más de una vez**, por lo que corresponde a un problema de tipo **unbounded knapsack**.

Esto se refleja en que para calcular `dp[x]` se puede utilizar nuevamente cualquier moneda y consultar `dp[x - c]`.

El recorrido de las cantidades se realiza hacia adelante:

```python
for x in range(1, amount + 1):
    for coin in coins:
```

De esta manera se permite reutilizar las denominaciones de monedas.

## Complejidad

* `k` = número de tipos de monedas.
* `X` = cantidad `amount`.
* **Tiempo:** `O(k × X)`
* **Espacio:** `O(X)`

La complejidad es pseudo-polinomial porque depende del valor de `amount`.

## Implementación

El código utilizado se encuentra en:

[`coin-change/Coin Change.py`](./coin-change/Coin%20Change.py)

## Evidencia de aceptación

La siguiente imagen muestra la solución enviada y aceptada en LeetCode:

![Coin Change Accepted](./evidencias/coin-change-accepted.png)

---

# 2. 416. Partition Equal Subset Sum

**Problema:** [LeetCode 416 - Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

## Descripción

Dado un arreglo de números enteros positivos, se debe determinar si es posible dividirlo en dos subconjuntos cuya suma sea exactamente igual.

## Estado

`dp[w]` representa si es posible obtener exactamente la suma `w` utilizando los números considerados hasta ese momento.

El valor puede ser `True` o `False`.

## Casos base

El caso base es:

`dp[0] = True`

Esto significa que siempre es posible obtener una suma de 0 sin seleccionar ningún elemento.

Antes de aplicar la programación dinámica, se calcula la suma total. Si la suma es impar, no es posible dividirla en dos subconjuntos iguales y se retorna `False`.

Si la suma es par, el objetivo es obtener:

`target = total / 2`

## Recurrencia

Para cada número `num`:

`dp[w] = dp[w] OR dp[w - num]`

Esto significa que una suma `w` es posible si ya era posible anteriormente o si se puede obtener utilizando el número actual `num`.

## Uso de los elementos

Cada número puede utilizarse **como máximo una vez**, por lo que este problema corresponde a **0/1 knapsack**.

Para evitar utilizar el mismo número varias veces, el recorrido de `w` se realiza de forma descendente:

```python
for num in nums:
    for w in range(target, num - 1, -1):
        dp[w] = dp[w] or dp[w - num]
```

El recorrido hacia atrás es importante porque evita que el mismo elemento se reutilice dentro de la misma iteración.

## Complejidad

* `n` = cantidad de elementos de `nums`.
* `W` = mitad de la suma total de los elementos.
* **Tiempo:** `O(n × W)`
* **Espacio:** `O(W)`

## Implementación

El código utilizado se encuentra en:

[`partition-equal-subset-sum/Partition Equal Subset Sum.py`](./partition-equal-subset-sum/Partition%20Equal%20Subset%20Sum.py)

## Evidencia de aceptación

La siguiente imagen muestra la solución enviada y aceptada en LeetCode:

![Partition Equal Subset Sum Accepted](./evidencias/partition-equal-subset-sum-accepted.png)

---

# Conclusión

En esta actividad se implementaron dos soluciones utilizando programación dinámica. En **Coin Change** se permite reutilizar las monedas, mientras que en **Partition Equal Subset Sum** cada número puede utilizarse solamente una vez.

Las dos soluciones fueron probadas y enviadas en LeetCode hasta obtener el estado **Accepted**.
