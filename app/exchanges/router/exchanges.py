# Python
import random
from typing import List
from typing import Optional

# FastAPI
from fastapi import APIRouter, Body, HTTPException
from fastapi import status

# Project
from app.exchanges.models.exchanges import Currency, Exchange, ExchangeOut
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
            status_code=404, detail=f"Currency {currency} not found")

    if country != None:
        for item in all_supported_currencies():
            country_dict = dict(item)
            country_name = country_dict["country"]
            if country_name == country:
                return [country_dict]

        raise HTTPException(
            status_code=404, detail=f"Country {country} not found")

    return all_supported_currencies()


@router.post(
    path="/api/exchange/",
    status_code=status.HTTP_200_OK,
    summary="The dollar equivalent is returned in the selected currency.",
    tags=["Exchange"],
    response_model=ExchangeOut
)
def exchange_currency(currency: Exchange = Body(...)):
    """
    # Exchange
    The dollar equivalent is returned in the selected currency.

    # Parameters
    - currency: Code of currency. 

    # Return
    - Returns the value in the selected currency of the indicated dollars.
    """

    test_dict = dict(exchange_to())
    # print(test_dict["rates"])
    for coin in test_dict:
        if coin == currency.change_to:
            print(coin)

    value_out = {
        "value": currency.initial_value*round(random.uniform(0.78, 1.29), 2)
    }
    return value_out
