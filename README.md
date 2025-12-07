# carcassonne-probabilities
Probabilites of tile draws in Carcassonne

## tl;dr
[online script to calculate probabilities of specific draws and distributions](https://yzemaze.de/bga/carcassonne-draw-probabilities.html)
[online script to calculate probabilities of more complex sets of conditions](https://yzemaze.de/bga/carcassonne-permutation-analyzer.html)

## What’s here?
[LibreOffice Calc sheet](draw-k-out-of-K.ods) featuring draw probabilities of exactly/at least k out of K desired tiles still present in N total tiles remaining. [cf. [ hypergeometric distribution](https://en.wikipedia.org/wiki/Hypergeometric_distribution)]
These are theoretical values. If you’d run the script below with enough iterations results should be similar.

[Python script](draw-a-before-b.py) simulating (2p Carcassonne) tile draws and printing corresponding stats. It calculates probabilities of drawing 1 out of A tiles before the other player does draw either 1 out of B different tiles or one of the players drawing 1 of C common tiles.
Additionally it prints a table of tile distribution probabilities according to the simulation. 

[html page](carcassonne-draw-probabilities.html) that does the same as the python script. It’s self-contained (includes JS and CSS), so it could be used locally or [online](https://yzemaze.de/bga/carcassonne-draw-probabilities.html).

[Permutation analyzer](carcassonne-permutation-analyzer.html) ([online](https://yzemaze.de/bga/carcassonne-permutation-analyzer.html)) calculates the probability of specific tile distribution conditions being met across all possible tile permutations. You can define complex conditions for specific tiles remaining with up to 3 sets of (multiple) quantitative rules (at least/most/exactly N of certain tiles/tile groups) combined with logical operators. Only one combination can feature the special operator ```before```, but many roads lead to Rome. Due to limitations in some specific cases you may also need to select the correct evaluation order.
For <= 10 tiles an exact permutation analysis is possible, but might still be slower than a simulation. For > 10 tiles only simulations are available.

## Please note
Player A will always be the one drawing first.
Don’t forget to add the tile already in your opponent’s hand to the remaining tiles count given by BGA’s interface.

## Draw Simulator Examples
Description: values of tiles remaining, A, B, C

Possible distributions of monasteries: 71, 0, 0, 6
![screenshot-ex1](/img/ex1-monasteries.png?raw=true)
1. correct inputs
2. 10^6 iterations should be enough and are computed reasonably fast.
3. A will likely draw the first monastery.
4. In roughly 2.5% of games one player will get all 6 monasteries. In about 80% of games both will get between 2 and 4 monasteries. Due to the starting player advantage of drawing 36 tiles the odds to draw more monasteries are in A’s favor.

15 tiles remaining, A is first to draw and needs one of 2 remaining starting tiles to complete a city, B needs one of 3 remaining straights to block, both could use the last curve (to either prevent or execute the block): 15, 2, 3, 1
![screenshot-ex2](/img/ex2-abc.png?raw=true)
1. B is ever so slightly favored to draw one of the needed tiles before A does.
2. A drew the curve in 53.2% of the simulations.

B is the 2nd player and according to BGA’s interface there are 6 tiles remaining. B would like to know how likely it is for them to either get the last dorito or win the flip for the last monastery: 7, 0, 1, 1
![screenshot-ex3](/img/ex3-bc.png?raw=true)
1. In about 57% of the simulations A won the flip for the monastery.
2. But in > 71% B drew at least 1 of the 2 specified tiles.

5 tiles remaining, to win A needs the last dagger before B draws the last vanilla cap: 5, 1, 1, 0
![screenshot-ex4](/img/ex4-ab.png?raw=true)
1. A will likely win about 45% of the time.
2. B should draw the vanilla cap before A gets the dagger in 25% of the cases.
3. In 30% of simulations neither one got one of the specified tiles.
4. In case of success A would have to wait 0.78 moves on average. (0 = their next move, 1 = their move after that etc. )

## Permutation Analyzer Example
![screenshot-ex5](/img/ex5-permutation-analyzer.png?raw=true)
1. 9 tiles remaining
2. straight, monastery, vanilla, cow, dagger (and 4 irrelvant ones)
3. A needs to draw either the straight to execute a block
4. before
5. B enters a field with monastery or vanilla
6. or
7. A needs to get the vanilla or dagger
8. and
9. a cow to complete a city.
10. A will succeed in roughly 64.34% of cases. (Switching the method to ```Calculation``` would result in 64.29%.)

## Feedback, problems, ideas etc.
Please start a [discussion](https://github.com/yzemaze/carcassonne-probabilities/discussions) or contact me on BGA or Discord.
