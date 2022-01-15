# Python
from typing import List
from typing import Optional

# FastAPI
from fastapi import APIRouter, HTTPException
from fastapi import status

# Project
from app.exchanges.models.exchanges import Currency, ExchangeOut
from app.exchanges.mockdata.exchenges_mockdata import all_supported_currencies, exchange_to


router: APIRouter = APIRouter()


@router.get(
    path="/api/currencies",
    status_code=status.HTTP_200_OK,
    summary="Get all currencies",
    tags=["Exchange"],
    response_model=List[Currency],
)
def get_currencies(
    currency: Optional[str] = None,
    country: Optional[str] = None
):
    """
    # Currencies
    Get all availables currencies.

    # Parameters
    - currency: Code of currency.
    - country: Name of country.

    # Return
    - You can query by currency or country name, if not return all available currencies.
    """

    if currency != None:
        for item in all_supported_currencies():
            currency_dict = dict(item)
            code = currency_dict["currency"]
            if code == currency:
                return [currency_dict]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Currency {currency} not found")

    if country != None:
        for item in all_supported_currencies():
            country_dict = dict(item)
            country_name = country_dict["country"]
            if country_name == country:
                return [country_dict]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Country {country} not found")

    return all_supported_currencies()


@router.get(
    path="/api/exchange",
    status_code=status.HTTP_200_OK,
    summary="The dollar equivalent is returned in the selected currency.",
    tags=["Exchange"],
    response_model=ExchangeOut
)
def exchange_currency(currency_name: Optional[str] = None, value_to_exchange: Optional[int] = None):
    """
    # Exchange
    The dollar equivalent is returned in the selected currency.

    # Parameters
    - currency_name: Code of currency.
    - value_to_exchange: value to exchange.

    # Return
    - Returns the value in the selected currency of the indicated dollars.
    """

    if currency_name == None or value_to_exchange == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad request")

    currency_for_change = exchange_to()

    for key, value in currency_for_change["rates"].items():
        if currency_name == key:
            total = value*value_to_exchange
            return {"converted_currency": total}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Currency {currency_name} not found.")
