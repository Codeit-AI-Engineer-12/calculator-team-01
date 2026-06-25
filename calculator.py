from ops import root
from ops.add import add
from ops.multiply import multiply
from ops.subtract import subtract
from ops.divide import divide
from ops.power import power
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
    "min": minimum,
    "avg": average,
    "root": root,
}