"""Fixed Income Corporate Router."""
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

router = Router(prefix="/corporate")

# pylint: disable=unused-argument


@router.command(model="ICEBofA")
def ice_bofa(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """ICE BofA US Corporate Bond Indices.

    The ICE BofA US Corporate Index tracks the performance of US dollar denominated investment grade corporate debt
    publicly issued in the US domestic market. Qualifying securities must have an investment grade rating (based on an
    average of Moody’s, S&P and Fitch), at least 18 months to final maturity at the time of issuance, at least one year
    remaining term to final maturity as of the rebalance date, a fixed coupon schedule and a minimum amount
    outstanding of $250 million. The ICE BofA US Corporate Index is a component of the US Corporate Master Index.
    """
    return OBBject(results=Query(**locals()).execute())


@router.command(model="MoodyCorporateBondIndex")
def moody(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Moody Corporate Bond Index.

    Moody's Aaa and Baa are investment bonds that acts as an index of
    the performance of all bonds given an Aaa or Baa rating by Moody's Investors Service respectively.
    These corporate bonds often are used in macroeconomics as an alternative to the federal ten-year
    Treasury Bill as an indicator of the interest rate.
    """
    return OBBject(results=Query(**locals()).execute())


@router.command(model="HighQualityMarketCorporateBond")
def hqm(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """High Quality Market Corporate Bond.

    The HQM yield curve represents the high quality corporate bond market, i.e.,
    corporate bonds rated AAA, AA, or A.  The HQM curve contains two regression terms.
    These terms are adjustment factors that blend AAA, AA, and A bonds into a single HQM yield curve
    that is the market-weighted average (MWA) quality of high quality bonds.
    """
    return OBBject(results=Query(**locals()).execute())


@router.command(model="SpotRate")
def spot_rates(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Spot Rates.

    The spot rates for any maturity is the yield on a bond that provides a single payment at that maturity.
    This is a zero coupon bond.
    Because each spot rate pertains to a single cashflow, it is the relevant interest rate
    concept for discounting a pension liability at the same maturity.
    """
    return OBBject(results=Query(**locals()).execute())


@router.command(model="CommercialPaper")
def commercial_paper(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Commercial Paper.

    Commercial paper (CP) consists of short-term, promissory notes issued primarily by corporations.
    Maturities range up to 270 days but average about 30 days.
    Many companies use CP to raise cash needed for current transactions,
    and many find it to be a lower-cost alternative to bank loans.
    """
    return OBBject(results=Query(**locals()).execute())
