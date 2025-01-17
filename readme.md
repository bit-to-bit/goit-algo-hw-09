Дослідження виконання алгоритмів, показує, що при малих заданих значеннях решти, алгоритм показують приблизно однаковий час виконання, проте при збільшенні заданого значення, жадібний алгоритм працює трохи швидше (+- на 10% швидше). Проте на занадто великих значеннях алгоритм динаміного програмування краше не застосовувати, адже він використовує рекурсивний підхід, і стек виконання може досягти свого обмеження. 
Детальні результати дослудження надано нижче: 

--------------------------------------------------------------------------------
For change = 0:

Results:
Greedy algorithm:       None
Dynamic programming:    None

Time:
Greedy algorithm:       1.0800082236528397e-05
Dynamic programming:    7.299706339836121e-06
Greedy / Dynamic:       1.48 / 1

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
For change = 1:

Results:
Greedy algorithm:       {1: 1}
Dynamic programming:    {1: 1}

Time:
Greedy algorithm:       5.4900068789720535e-05
Dynamic programming:    4.439987242221832e-05
Greedy / Dynamic:       1.24 / 1

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
For change = 3:

Results:
Greedy algorithm:       {2: 1, 1: 1}
Dynamic programming:    {1: 1, 2: 1}

Time:
Greedy algorithm:       9.320024400949478e-05
Dynamic programming:    9.019998833537102e-05
Greedy / Dynamic:       1.03 / 1

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
For change = 8:

Results:
Greedy algorithm:       {5: 1, 2: 1, 1: 1}
Dynamic programming:    {1: 1, 2: 1, 5: 1}

Time:
Greedy algorithm:       0.0001441999338567257
Dynamic programming:    0.00013739988207817078
Greedy / Dynamic:       1.05 / 1

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
For change = 12:

Results:
Greedy algorithm:       {10: 1, 2: 1}
Dynamic programming:    {2: 1, 10: 1}

Time:
Greedy algorithm:       0.00010399986058473587
Dynamic programming:    9.20998863875866e-05
Greedy / Dynamic:       1.13 / 1

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
For change = 23:

Results:
Greedy algorithm:       {10: 2, 2: 1, 1: 1}
Dynamic programming:    {1: 1, 2: 1, 10: 2}

Time:
Greedy algorithm:       0.00018510036170482635
Dynamic programming:    0.00018159998580813408
Greedy / Dynamic:       1.02 / 1

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
For change = 57:

Results:
Greedy algorithm:       {50: 1, 5: 1, 2: 1}
Dynamic programming:    {2: 1, 5: 1, 50: 1}

Time:
Greedy algorithm:       0.00014070002362132072
Dynamic programming:    0.00014329981058835983
Greedy / Dynamic:       0.98 / 1

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
For change = 8000:

Results:
Greedy algorithm:       {50: 160}
Dynamic programming:    {50: 160}

Time:
Greedy algorithm:       0.008115699980407953
Dynamic programming:    0.00922109978273511
Greedy / Dynamic:       0.88 / 1

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
For change = 40023:

Results:
Greedy algorithm:       {50: 800, 10: 2, 2: 1, 1: 1}
Dynamic programming:    {1: 1, 2: 1, 10: 2, 50: 800}

Time:
Greedy algorithm:       0.041359399911016226
Dynamic programming:    0.046244800090789795
Greedy / Dynamic:       0.89 / 1

--------------------------------------------------------------------------------