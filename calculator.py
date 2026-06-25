from ops.add import add
from ops.multiply import multiply
from ops.subtract import subtract
from ops.divide import divide
from ops.power import power
from ops.derivative import derivative

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "diff": derivative,
}