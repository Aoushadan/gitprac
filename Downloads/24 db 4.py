

def safe_division(num, den):
    try:
        result = num / den
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        print("Division successful. Result:", result)
    finally:
        print("Execution of safe_division completed.")
    return result

safe_division(10, 2)
safe_division(10, 0)



def safe_division(num, den):
    try:

        num = float(num)
        den = float(den)


        result = num / den

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        result = None

    except TypeError:
        print("Error: Unsupported input type. Ensure both inputs are numbers.")
        result = None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        result = None

    else:
        print("Division successful. Result:", result)

    finally:
        print("Finished execution of safe_division.")

    return result
safe_division(10, 2)         
safe_division(10, 0)
safe_division("10", "5")
safe_division("ten", 5)
safe_division([10], 5)
