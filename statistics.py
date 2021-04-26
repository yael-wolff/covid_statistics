def mean(values):
    """
    This function finds the mean of given values.
    :parameters: values
    :type: float[]
    :returns: sum1
    :type: float
    """
    sum1 = 0
    count = 0
    for i in values:
        sum1 += i
        count = count + 1
    return (sum1 / count)


def median(values):
    n = len(values)
    sorted_values = sorted(values)
    return (sum(sorted_values[n // 2 - 1:n // 2 + 1]) / 2.0, sorted_values[n // 2])[n % 2] if n else None

