var x1;
var x2;
var x3;
var x4;
var d;

maximize z: d;

s.t. con1: x2 - x1 >= d;
s.t. con2: x3 - x2 >= d;
s.t. con3: x4 - x3 >= d;
s.t. con4: 9.0 <= x1 <= 9.5;
s.t. con5: 10.0 <= x2 <= 11.0;
s.t. con6: 11.25 <= x3 <= 11.5;
s.t. con7: 12.0 <= x4 <= 12.25;


end;
