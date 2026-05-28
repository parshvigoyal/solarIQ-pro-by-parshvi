def calc_financials(
    annual_kwh,
    elec_cost_per_kwh,
    system_cost_per_watt,
    installed_kwp
):

    # Solar system practical performance ratio
    performance_ratio = 0.8

    # Effective annual energy after losses
    effective_annual_kwh = annual_kwh * performance_ratio

    # Calculate installation cost
    total_cost = (
        installed_kwp
        * 1000
        * system_cost_per_watt
    )

    # Calculate annual savings
    annual_savings = (
        effective_annual_kwh
        * elec_cost_per_kwh
    )

    # Calculate payback period safely
    if annual_savings == 0:
        payback_years = float('inf')
    else:
        payback_years = total_cost / annual_savings

    return (
        total_cost,
        annual_savings,
        payback_years
    )
