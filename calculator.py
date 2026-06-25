from ops.add import add
from ops.derivative import derivative
from ops.divide import divide
from ops.max import maximum
from ops.multiply import multiply
from ops.power import power
from ops.subtract import subtract
from ops.derivative import derivative
from ops.minimum import minimum
from ops.average import average

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "diff": derivative,
    "max": maximum,
}
    "min": minimum,
    "avg": average,
}
