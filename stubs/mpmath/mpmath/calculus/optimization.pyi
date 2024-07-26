from _typeshed import Incomplete

class OptimizationMethods:
    def __init__(ctx) -> None: ...

class Newton:
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    f: Incomplete
    df: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Secant:
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    x1: Incomplete
    f: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class MNewton:
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    f: Incomplete
    df: Incomplete
    d2f: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Halley:
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    f: Incomplete
    df: Incomplete
    d2f: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Muller:
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    x1: Incomplete
    x2: Incomplete
    f: Incomplete
    verbose: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Bisection:
    maxsteps: int
    ctx: Incomplete
    f: Incomplete
    a: Incomplete
    b: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Illinois:
    maxsteps: int
    ctx: Incomplete
    a: Incomplete
    b: Incomplete
    f: Incomplete
    tol: Incomplete
    verbose: Incomplete
    method: Incomplete
    getm: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

def Pegasus(*args, **kwargs): ...
def Anderson(*args, **kwargs): ...

class Ridder:
    maxsteps: int
    ctx: Incomplete
    f: Incomplete
    x1: Incomplete
    x2: Incomplete
    verbose: Incomplete
    tol: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class ANewton:
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    f: Incomplete
    df: Incomplete
    phi: Incomplete
    verbose: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

def jacobian(ctx, f, x): ...

class MDNewton:
    maxsteps: int
    ctx: Incomplete
    f: Incomplete
    x0: Incomplete
    J: Incomplete
    norm: Incomplete
    verbose: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

str2solver: Incomplete

def findroot(
    ctx, f, x0, solver: str = "secant", tol: Incomplete | None = None, verbose: bool = False, verify: bool = True, **kwargs
): ...
def multiplicity(ctx, f, root, tol: Incomplete | None = None, maxsteps: int = 10, **kwargs): ...
def steffensen(f): ...
