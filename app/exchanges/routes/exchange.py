# Python
from typing import Optional, List

# FastAPI
from fastapi import APIRouter, HTTPException
from fastapi import status
from fastapi import Query


# Project
from app.exchanges.models.exchange import ExchangeOut
from app.exchanges.mockdata.exchenges_mockdata import exchange_to


router: APIRouter = APIRouter()


@router.get(
    path="/api/exchange",
    status_code=status.HTTP_200_OK,
    summary="The dollar equivalent is returned in the selected currency.",
    tags=["Exchange"],
    response_model=ExchangeOut
)
def exchange_currency(
    currency_name: Optional[str] = Query(
        None,
        description="Currency code name",
        alias="Code Name",
        max_length=3
    ),
    values_to_exchange: Optional[List[float]] = Query(
        None,
        description="Value to exchange",
        alias="Value to exchange",
        gt=0
    )
):
    """
    # Exchange
    The dollar equivalent is returned in the selected currency.

    # Parameters
    - currency_name: Code of currency.
    - value_to_exchange: value or values to exchange.

    # Return
    - Returns the value or values in the selected currency.
    """
    currency_total = []
    if not currency_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad request")

    if not values_to_exchange:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad request")

    currency_for_change = exchange_to()

    for key, value in currency_for_change["rates"].items():
        if key in currency_name:
            for item in values_to_exchange:
                currency_total.append(round(item*value, 2))
            return ExchangeOut(converted_currency=list(currency_total))

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Currency {currency_name} not found.")
