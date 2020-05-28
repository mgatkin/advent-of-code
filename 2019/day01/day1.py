'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

data = [
74364,
146203,
128470,
91616,
115655,
134147,
53470,
126471,
70040,
88750,
142353,
143329,
86356,
118399,
97959,
148345,
117705,
87624,
63862,
71962,
106974,
66255,
119735,
78726,
93698,
148680,
144638,
83341,
149571,
147196,
54526,
91775,
63153,
143441,
71134,
114131,
120931,
109833,
106073,
64547,
126938,
52877,
89945,
59466,
79660,
147815,
55381,
100052,
78824,
121844,
104155,
117313,
69305,
144645,
81350,
123512,
81467,
120836,
118612,
143999,
90792,
71054,
138942,
56481,
71850,
85266,
77437,
86530,
147311,
133699,
126684,
58708,
149482,
104101,
67985,
81648,
95290,
77155,
76578,
116025,
83980,
59517,
62078,
89003,
126205,
122542,
116388,
144040,
102560,
77098,
127534,
56415,
85703,
85580,
86787,
72029,
82533,
132187,
70849,
98839
]

def fuel(mass):
    return int(mass / 3) - 2

def total_fuel(mass):
    total_fuel = 0
    remaining_mass = mass
    while fuel(remaining_mass) > 0:
        this_fuel = fuel(remaining_mass)
        remaining_mass = this_fuel
        total_fuel += this_fuel
    return total_fuel

print(sum([fuel(i) for i in data]))
print(sum([total_fuel(i) for i in data]))

    