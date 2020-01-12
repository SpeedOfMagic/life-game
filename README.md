# life-game
Modification to a game of 'Life', which features obstacles and 2 types of cells, where cells are 'shrimps' and 'fishes', and obstacles are 'mountains'.

The modified rules of a game:
- Fishes and shrimps obey to the normal Conway's Game of Life;
- Nothing can't be located on mountains;
- If fish and shrimp can appear in the same cell, then fish appears in that cell.

main.py features a console version, which takes the following arguments to the command line:
- rowsCount: amount of rows in a map;
- colsCount: amount of columns in a map;
- -pf, --pFish (optional): for each cell, probability that fish will appear in that cell (0.2 for default);
- -ps, --pShrimp (optional): for each cell, probability that shrimp will appear in that cell (0.3 for default);
- -pm, --pMountain (optional): for each cell, probability that mountain will appear in that cell (0.1 for default);
- -n, --none (optional): symbol that is used to display 'none' cell (space for default);
- -f, --fish (optional): symbol that is used to display 'fish' cell (F for default);
- -s, --shrimp (optional): symbol that is used to display 'shrimp' cell (S for default);
- -m, --mountain (optional): symbol that is used to display 'mountain' cell (# for default);

The program takes these arguments, creates random field from them, and then displays the initial field and its next states in console.
