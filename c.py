import math, cmath

angles_a = [x * math.pi / 3. for x in range(0, 6)]
angles_b = [x * math.pi / 3. + math.pi / 6. for x in range(0, 6)]
angles_c = [x * math.pi / 3. + math.pi / 12. for x in range(0, 6)]

sum_a = 0j
sum_b = 0j
sum_c = 0j

for angle in angles_a:
    sum_a += cmath.exp(6.0j * angle)

for angle in angles_b:
    sum_b += cmath.exp(6.0j * angle)

for angle in angles_c:
    sum_c += cmath.exp(6.0j * angle)

print("psi_6(a)", sum_a / 6.)
print("psi_6(b)", sum_b / 6.)
print("psi_6(c)", sum_c / 6.)
print("psi_6(a) + psi_6(b)", (sum_a + sum_b) / 6.)