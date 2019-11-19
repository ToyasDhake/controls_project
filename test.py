def test(Kp, Ki, Kd):
    result = Kp + Ki - Kd
    result = abs(0-result)
    return result

def testga(Kp, Ki, Kd):
    result = Kp + Ki - Kd
    result = 8-abs(result)
    return result

def testgwo(val):
    Kp, Ki, Kd = val[0], val[1], val[2]
    result = Kp + Ki - Kd
    result = abs(0-result)
    return result