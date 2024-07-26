from _typeshed import Incomplete

class InverseLaplaceTransform:
    ctx: Incomplete
    def __init__(self, ctx) -> None: ...
    def calc_laplace_parameter(self, t, **kwargs) -> None: ...
    def calc_time_domain_solution(self, fp) -> None: ...

class FixedTalbot(InverseLaplaceTransform):
    t: Incomplete
    tmax: Incomplete
    degree: Incomplete
    dps_goal: Incomplete
    dps_orig: Incomplete
    r: Incomplete
    theta: Incomplete
    cot_theta: Incomplete
    delta: Incomplete
    p: Incomplete
    def calc_laplace_parameter(self, t, **kwargs) -> None: ...
    def calc_time_domain_solution(self, fp, t, manual_prec: bool = False): ...

class Stehfest(InverseLaplaceTransform):
    t: Incomplete
    degree: Incomplete
    dps_goal: Incomplete
    dps_orig: Incomplete
    V: Incomplete
    p: Incomplete
    def calc_laplace_parameter(self, t, **kwargs) -> None: ...
    def calc_time_domain_solution(self, fp, t, manual_prec: bool = False): ...

class deHoog(InverseLaplaceTransform):
    t: Incomplete
    tmax: Incomplete
    degree: Incomplete
    dps_goal: Incomplete
    alpha: Incomplete
    tol: Incomplete
    np: Incomplete
    dps_orig: Incomplete
    scale: Incomplete
    T: Incomplete
    p: Incomplete
    gamma: Incomplete
    def calc_laplace_parameter(self, t, **kwargs) -> None: ...
    def calc_time_domain_solution(self, fp, t, manual_prec: bool = False): ...

class Cohen(InverseLaplaceTransform):
    t: Incomplete
    degree: Incomplete
    dps_goal: Incomplete
    dps_orig: Incomplete
    alpha: Incomplete
    p: Incomplete
    def calc_laplace_parameter(self, t, **kwargs) -> None: ...
    def calc_time_domain_solution(self, fp, t, manual_prec: bool = False): ...

class LaplaceTransformInversionMethods:
    def __init__(ctx, *args, **kwargs) -> None: ...
    def invertlaplace(ctx, f, t, **kwargs): ...
    def invlaptalbot(ctx, *args, **kwargs): ...
    def invlapstehfest(ctx, *args, **kwargs): ...
    def invlapdehoog(ctx, *args, **kwargs): ...
    def invlapcohen(ctx, *args, **kwargs): ...
