# Python
from typing import List
from typing import Optional

# FastAPI
from fastapi import APIRouter, HTTPException
from fastapi import status, Query

# Project
from app.exchanges.models.exchange import Currency
from app.exchanges.mockdata.exchenges_mockdata import all_supported_currencies


router: APIRouter = APIRouter()


@router.get(
    path="/api/currencies",
    status_code=status.HTTP_200_OK,
    summary="Get all currencies",
    tags=["Exchange"],
    response_model=List[Currency],
)
def get_currencies(
    currency: Optional[str] = Query(
        None,
        description="Code currency",
        alias="Code",
        max_length=3,
    ),
    country: Optional[str] = Query(
        None,
        description="Country Name",
        alias="Country Name",
        max_length=90,
    )
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
