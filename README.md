# AoC
Solutions for Advent Of Code challenge + Tools

## Prerequisites

* Cookie for [adventofcode.com](adventofcode.com) domain
> Cookie / session secret is used to obtain and store puzzle input. Session secret can be obtained in the following way:
> * Goodle Chrome:
>   * Go to [adventofcode.com](adventofcode.com), make sure you're logged in 
>   * Open `Developers Tools` and go `Application` tab 
>   * In `Storage` section, under `Cookies` select site's cookie and copy value of session parameter
> 
> Session secret needs to be stored inside `AoC/res/aoc_session.txt` file.

## Usage
Generate solution template and download puzzle input for specific day and year:

```python
from aoc_tools.challenge import Challenge

Challenge.init_new_challenge(year=2020, day=7)
```

The above code generates python file with solution template (`solution_YEAR_DAY.py`), text file containing puzzle input
(`input_YEAR_DAY.txt`) and empty text file for sample/test input (`sample_input_YEAR_DAY.txt`).

Generated files will be organized in the following file structure:

```
AoC
└───YEAR
   └───day_DAY
   │   │   solution_YEAR_DAY.py
   │   │   input_YEAR_DAY.txt
   │   │   sample_input_YEAR_DAY.txt
   └───day_DAY
       │   solution_YEAR_DAY.py
       │   input_YEAR_DAY.txt
       └   sample_input_YEAR_DAY.txt
```
