# carcassonne-probabilities
Probabilites of tile draws in Carcassonne

## What’s here?
[LibreOffice Calc sheet](draw-k-out-of-K.ods) featuring draw probabilities of exactly/at least k out of K desired tiles still present in N total tiles remaining. [cf. [ hypergeometric distribution](https://en.wikipedia.org/wiki/Hypergeometric_distribution)]

[python script](draw-a-before-b.py) simulating (2p Carcassonne) tile draws and printing corresponding stats. It calculates probabilities of drawing 1 out of a tiles before the other player does draw either 1 out of b different tiles or one of the players drawing 1 of c common tiles.
Additionally it prints a table of tile distribution probabilities according to the simulation. (A comparison with the theoretical values given in the [LibreOffice Calc sheet](draw-k-out-of-K.ods) might be interesting.)  
[version without tile distribution table](draw-a-before-b-no-distribution.py)

[html page](carcassonne-draw-probabilities.html) that does the same as the python script. It’s self-contained (includes JS and CSS), so it could be used locally or [online](https://yzemaze.de/bga/carcassonne-draw-probabilities.html).  
[version without tile distribution table](carcassonne-draw-probabilities-no-distribution.html) [online](https://yzemaze.de/bga/carcassonne-draw-probabilities-no-distribution.html).

## Feedback, problems, ideas etc.
Please start a [discussion](https://github.com/yzemaze/carcassonne-stats/discussions) or contact me on BGA.
