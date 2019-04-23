from __future__ import annotations
from typing import Any, Union, Optional, Dict, List

# Python Abstract Syntax Tree (AST)
# =================================


class Expr:
    """An abstract class representing a Python expression.
    """
    def evaluate(self, env: Dict[str, Any]) -> Any:
        """Return the *value* of this expression.

        The returned value should be the result of how this expression would be
        evaluated by the Python interpreter.

        The given `env` is used to lookup variables.

        :return: Any
        """
        raise NotImplementedError


class Num(Expr):
    """A numeric constant literal.

    Attributes:
    ----------
    n: the value of the constant
    """
    n: Union[int, float]

    def __init__(self, number: Union[int, float]) -> None:
        """Initialize a new numerical constant."""
        self.n = number
        pass

    def evaluate(self, env: Dict[str, Any]) -> Any:
        """Return the *value of this expression.

        The returned value should be the result of how this expression would be
        evaluated by the Python interpreter.

        Return Value:
        -------------
        :return: Any

        Examples:
        ---------
        >>> number = Num(10.5)
        >>> number.evaluate()
        10.5
        """
        return self.n


class BinOp(Expr):
    """An arithmetic binary operation.

    Attributes:
    -----------
    left: the left operand
    op: the name of the operator
    right: the right operand

    Invariants:
    -----------
    - self.op == '+' or self.op == '*'
    """
    left: Expr
    op: str
    right: Expr

    def __init__(self, left: Expr, op: str, right: Expr) -> None:
        """Initialize a new binary operation express.

        Parameters:
        -----------
        :param left: the left operand
        :param op: the name of the operator
        :param right: the right operand

        Preconditions:
        --------------
        <op> is the string '+' or '*'.
        """
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, env: Dict[str, Any]) -> Any:
        """Return the *value* of this expression.
        :return:

        Examples:
        ---------
        >>> BinOp(BinOp(Num(5), '*', BinOp(Num(10), '+', Num(20))), '*', Num(10)).evaluate()
        1500

        """
        left_val = self.left.evaluate(env)
        right_val = self.right.evaluate(env)

        if self.op == '+':
            return left_val + right_val
        elif self.op == '*':
            return left_val * right_val
        else:
            raise ValueError(f'Invalid operator {self.op}')


class Name(Expr):
    """ A variable name.

    Attributes:
    -----------
    id: The variable name in this expression.
    """
    id: str

    def __init__(self, id: str) -> None:
        """Initialize a new name expression.

        :param id: the variable name in this expression
        """
        self.id = id

    def evaluate(self, env: Dict[str, Any]) -> Any:
        """Return the *value* of this expression.

        The name should be looked up in the `env` argument to this method.
        Raise a NameError if the name is not found.


        Parameters:
        -----------
        :param env:
        :return:

        Examples:
        ---------
        >>> expr = Name('x')
        >>> expr.evaluate({'x': 10})
        10
        """
        if self.id not in env.keys():
            raise NameError

        return env[self.id]


class Statement:
    """An abstract class representing a Python statement."""
    def evaluate(self, env: Dict[str, Any]) -> Optional[Any]:
        """Evaluate this statement."""
        raise NotImplementedError


class Assign(Statement):
    """An assignment statement with a single target, like `x = 10 + 3`.

    Attributes:
    -----------
    target: the variable name on the left-hand side of the equals sign.
    value: the expression on the right-hand side of the equals sign.
    """
    target: str
    value: Expr

    def __init__(self, target: str, value: Expr) -> None:
        """Initialize a new single assignment expression.

        :param target:
        :param value:
        """
        self.target = target
        self.value = value

    def evaluate(self, env: Dict[str, Any]) -> Optional[Any]:
        """Evaluate this statement.

        This does the following: evaluate the right-hand side expression,
        and then mutate <env> to store a binding between this statement's
        target and the corresponding value.

        :param env:
        :return:

        Examples:
        >>> stmt = Assign('x', BinOp(Num(10), '+', Num(3)))
        >>> env = {}
        >>> stmt.evaluate(env)
        13
        """
        env[self.target] = self.value.evaluate(env)
        return env[self.target]


class ParallelAssign(Statement):
    """A parallel assignment statement.

    Attribute:
    ----------
    targets: the variable names being assigned to --- the left-hand side of the =
    values: the expressions being assigned --- the right-hand side of the =
    """
    targets: List[str]
    values: List[Expr]

    def __init__(self, targets: List[str], values: List[Expr]) -> None:
        self.targets = targets
        self.values = values

    def evaluate(self, env: Dict[str, Any]) -> Optional[Any]:
        """Evaluate this statement.

        This does the following: evaluate each expression on the right-hand side
        and then bind each target to its corresponding value.

        Raise a ValueError if the lengths of self.targets and self.values
        are not equal.

        :param env:
        :return:

        Examples:
        ---------
        >>> stmt = ParallelAssign(['x', 'y'], [BinOp(Num(10), '+', Num(3)), \
        Num(-4.5)])
        >>> env = {}
        >>> stmt.evaluate(env)
        >>> env['x']
        13
        >>> env['y']
        -4.5
        """
        if len(self.targets) != len(self.values):
            raise ValueError

        evaluated = []
        for i in range(len(self.values)):
            evaluated.append(self.values[i].evaluate(env))

        for i in range(len(self.targets)):
            env[self.targets[i]] = evaluated[i]

        # Both implementations work. The values must first be evaluated before
        # changing the env.

        ## prevEnv = {}
        ## for key in env.keys():
        ##     prevEnv[key] = env[key]

        ## for i in range(len(self.targets)):
        ##     env[self.targets[i]] = self.values[i].evaluate(prevEnv)


class If(Statement):
    """An if statement.

    Attributes:
    test: The condition expression of this statement.
    body: A sequence of statements to evaluate if the condition is true.
    or_else: a sequence of statements to evaluate if the condition is false.
            (This would be empty in the case that there is no 'else' block.)
    """
    test: Expr
    body: List[Statement]
    or_else: List[Statement]

    def __init__(self, test: Expr, body: List[Statement], or_else: List[Statement]=[]) -> None:
        """Initialize a new if statement.

        Parameters:
        -----------

        :param test: the condition expression of this statement
        :param body: a sequence of statements to evaluate
        :param or_else: a sequence of statements to evaluate or empty
        """
        self.test = test
        self.body = body
        self.or_else = or_else

    def evaluate(self, env: Dict[str, Any]) -> Optional[Any]:
        if self.test.evaluate(env):
            for statement in self.body:
                statement.evaluate(env)

        else:
            for statement in self.or_else:
                statement.evaluate(env)


class ForRange(Statement):
    """A for loop that loops over a range of numbers.
        for <target> in range(<start>, <stop>):
            <body>

    Attributes:
    -----------
    target: The loop variable.
    start: The start for the range (inclusive)
    stop: The end of the range (this is *exclusive*, so <stop> is not included
          in the loop).
    body: The statements to execute in the loop body.
    """
    target: str
    start: Expr
    stop: Expr
    body: List[Statement]

    def __init__(self, target: str, start: Expr, stop: Expr, body: List[Statement]) -> None:
        self.target = target
        self.start = start
        self.stop = stop
        self.body = body

    def evaluate(self, env: Dict[str, Any]) -> Optional[Any]:
        """Raise a TypeError if either the start or the stop expressions
        do *not* evaluate to integers. (This is technically a bit stricter than
        real Python.)

        Parameters:
        -----------
        :param env: the variables in scope
        :return:

        Examples:
        ---------
        >>> statement = ForRange('x', Num(1), BinOp(Num(2), '+', Num(3)), \
         [Print(Name('x'))])
         >>> statement.evaluate({})
         1
         2
         3
         4
        """
        if not isinstance(self.start.evaluate(env), int) or not \
                isinstance(self.stop.evaluate(env), int):
            raise TypeError

        env[self.target] = self.start
        for i in range(self.start.evaluate(env), self.stop.evaluate(env)):
            for statement in self.body:
                statement.evaluate(env)

            env[self.target] += 1
