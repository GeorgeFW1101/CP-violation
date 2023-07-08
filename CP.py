def calculate_CP_violation(Asymmetry_direct, Asymmetry_indirect):
    return (Asymmetry_direct - Asymmetry_indirect) / (Asymmetry_direct + Asymmetry_indirect)
def invert_float(value):
    return 1 - value
while(True):
    # Example usage
    Asymmetry_direct = invert_float(float(input("Direct symmetry: ")))
    Asymmetry_indirect = invert_float(float(input("Indirect symmetry: ")))

    cp_violation_parameter = calculate_CP_violation(Asymmetry_direct, Asymmetry_indirect)
    print("CP Violation Parameter:", cp_violation_parameter)
    print()
