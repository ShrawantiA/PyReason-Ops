def evaluate_rule(cpu_usage, mem_usage):
    """
    Basic operational decision rule.
    """
    if cpu_usage > 80 and mem_usage < 50:
        return "SCALE_UP"
    elif cpu_usage < 30:
        return "SCALE_DOWN"
    else:
        return "STABLE"
