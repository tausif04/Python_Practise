""" Operator Precedence Table (from highest to lowest)
             1. Exponentiation (``)**
                2. Unary plus, Unary minus, Bitwise NOT ( +x , -x , ~x )
                3. Multiplication, Division, Floor division, Modulus ( * , / , // , % )
                4. Addition, Subtraction ( + , - )
                5. Bitwise shift ( << , >> )
                6. Bitwise AND ( & )
                7. Bitwise XOR ( ^ )
                8. Bitwise OR ( | )
                9. Comparisons, Identity, Membership ( == , != , > , < , >= , <= , is , is not , in , not in )
                10. Logical NOT ( not )
                11. Logical AND ( and )
                12. Logical OR ( or )
                                                """

result = 2 ** 3 * 2
print("2 ** 3 * 2:", result) # Output: 16
# Explanation: 2 ** 3 is evaluated first (8), then 8 * 2 = 16

result = 10 + 3 * 2
print("10 + 3 * 2:", result) # Output: 16
# Explanation: 3 * 2 is evaluated first (6), then 10 + 6 = 16