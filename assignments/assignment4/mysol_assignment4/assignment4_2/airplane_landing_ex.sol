Problem:    airplane_landing_ex
Rows:       8
Columns:    5
Non-zeros:  14
Status:     OPTIMAL
Objective:  z = 1 (MAXimum)

   No.   Row name   St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 z            B              1                             
     2 con1         B              0            -0               
     3 con2         B           0.25            -0               
     4 con3         NL             0            -0                          -1 
     5 con4         NL             9             9           9.5         < eps
     6 con5         NL            10            10            11         < eps
     7 con6         NL         11.25         11.25          11.5            -1 
     8 con7         NU         12.25            12         12.25             1 

   No. Column name  St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 x1           B              9                             
     2 x2           B             10                             
     3 x3           B          11.25                             
     4 x4           B          12.25                             
     5 d            B              1                             

Karush-Kuhn-Tucker optimality conditions:

KKT.PE: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.DE: max.abs.err = 0.00e+00 on column 0
        max.rel.err = 0.00e+00 on column 0
        High quality

KKT.DB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
