import random


exchange_usd = {
    "result": "success",
    "provider": "https://www.exchangerate-api.com",
    "documentation": "https://www.exchangerate-api.com/docs/free",
    "terms_of_use": "https://www.exchangerate-api.com/terms",
    "time_last_update_unix": 1642204951,
    "time_last_update_utc": "Sat, 15 Jan 2022 00:02:31 +0000",
    "time_next_update_unix": 1642291581,
    "time_next_update_utc": "Sun, 16 Jan 2022 00:06:21 +0000",
    "time_eol_unix": 0,
    "base_code": "USD",
    "rates": {
        "USD": 1,
        "AED": 3.67,
        "AFN": 105.07,
        "ALL": 106.87,
        "AMD": 481.02,
        "ANG": 1.79,
        "AOA": 538.97,
        "ARS": 103.82,
        "AUD": 1.38,
        "AWG": 1.79,
        "AZN": 1.7,
        "BAM": 1.71,
        "BBD": 2,
        "BDT": 86,
        "BGN": 1.71,
        "BHD": 0.376,
        "BIF": 1994.23,
        "BMD": 1,
        "BND": 1.35,
        "BOB": 6.87,
        "BRL": 5.53,
        "BSD": 1,
        "BTN": 74.15,
        "BWP": 11.59,
        "BYN": 2.57,
        "BZD": 2,
        "CAD": 1.25,
        "CDF": 2000.41,
        "CHF": 0.912,
        "CLP": 819.84,
        "CNY": 6.36,
        "COP": 3939.72,
        "CRC": 635.62,
        "CUP": 24,
        "CVE": 96.46,
        "CZK": 21.43,
        "DJF": 177.72,
        "DKK": 6.53,
        "DOP": 57.49,
        "DZD": 139.57,
        "EGP": 15.71,
        "ERN": 15,
        "ETB": 49.83,
        "EUR": 0.875,
        "FJD": 2.12,
        "FKP": 0.732,
        "FOK": 6.53,
        "GBP": 0.732,
        "GEL": 3.08,
        "GGP": 0.732,
        "GHS": 6.64,
        "GIP": 0.732,
        "GMD": 53.45,
        "GNF": 9127.6,
        "GTQ": 7.7,
        "GYD": 209.63,
        "HKD": 7.79,
        "HNL": 24.5,
        "HRK": 6.59,
        "HTG": 101.53,
        "HUF": 311.51,
        "IDR": 14240.71,
        "ILS": 3.11,
        "IMP": 0.732,
        "INR": 74.15,
        "IQD": 1463.36,
        "IRR": 42171.77,
        "ISK": 128.41,
        "JEP": 0.732,
        "JMD": 154.95,
        "JOD": 0.709,
        "JPY": 114.09,
        "KES": 113.59,
        "KGS": 84.84,
        "KHR": 4083.65,
        "KID": 1.38,
        "KMF": 430.37,
        "KRW": 1189.41,
        "KWD": 0.3,
        "KYD": 0.833,
        "KZT": 435.15,
        "LAK": 11229.58,
        "LBP": 1507.5,
        "LKR": 202.43,
        "LRD": 148.54,
        "LSL": 15.37,
        "LYD": 4.6,
        "MAD": 9.16,
        "MDL": 18.02,
        "MGA": 3132.94,
        "MKD": 53.9,
        "MMK": 1779.21,
        "MNT": 2869.99,
        "MOP": 8.02,
        "MRU": 36.41,
        "MUR": 43.84,
        "MVR": 15.36,
        "MWK": 820.19,
        "MXN": 20.33,
        "MYR": 4.18,
        "MZN": 64.34,
        "NAD": 15.37,
        "NGN": 417.3,
        "NIO": 35.37,
        "NOK": 8.74,
        "NPR": 118.64,
        "NZD": 1.47,
        "OMR": 0.384,
        "PAB": 1,
        "PEN": 3.89,
        "PGK": 3.51,
        "PHP": 51.39,
        "PKR": 176.46,
        "PLN": 3.97,
        "PYG": 6884.13,
        "QAR": 3.64,
        "RON": 4.32,
        "RSD": 103.01,
        "RUB": 76.34,
        "RWF": 1042.94,
        "SAR": 3.75,
        "SBD": 7.98,
        "SCR": 13.68,
        "SDG": 442.15,
        "SEK": 8.99,
        "SGD": 1.35,
        "SHP": 0.732,
        "SLL": 11390,
        "SOS": 579.91,
        "SRD": 21.3,
        "SSP": 432.89,
        "STN": 21.43,
        "SYP": 2524.97,
        "SZL": 15.37,
        "THB": 33.24,
        "TJS": 11.27,
        "TMT": 3.5,
        "TND": 2.78,
        "TOP": 2.26,
        "TRY": 13.52,
        "TTD": 6.77,
        "TVD": 1.38,
        "TWD": 27.58,
        "TZS": 2317.76,
        "UAH": 27.84,
        "UGX": 3527,
        "UYU": 44.47,
        "UZS": 10918.91,
        "VES": 4.63,
        "VND": 22822.27,
        "VUV": 112.62,
        "WST": 2.58,
        "XAF": 573.82,
        "XCD": 2.7,
        "XDR": 0.711,
        "XOF": 573.82,
        "XPF": 104.39,
        "YER": 250.64,
        "ZAR": 15.37,
        "ZMW": 17.14,
        "ZWL": 108.71
    }
}


supported_currencies = [{"currency": "AED", "name": "UAE Dirham", "country": "United Arab Emirates"},
                        {"currency": "AFN", "name": "Afghan Afghani",
                         "country": "Afghanistan"},
                        {"currency": "ALL", "name": "Albanian Lek",
                         "country": "Albania"},
                        {"currency": "AMD", "name": "Armenian Dram",
                         "country": "Armenia"},
                        {"currency": "ANG", "name": "Netherlands Antillian Guilder",
                         "country": "Netherlands Antilles"},
                        {"currency": "AOA", "name": "Angolan Kwanza",
                         "country": "Angola"},
                        {"currency": "ARS", "name": "Argentine Peso",
                         "country": "Argentina"},
                        {"currency": "AUD", "name": "Australian Dollar",
                         "country": "Australia"},
                        {"currency": "AWG", "name": "Aruban Florin",
                         "country": "Aruba"},
                        {"currency": "AZN", "name": "Azerbaijani Manat",
                         "country": "Azerbaijan"},
                        {"currency": "BAM", "name": "Bosnia and Herzegovina Mark",
                         "country": "Bosnia and Herzegovina"},
                        {"currency": "BBD", "name": "Barbados Dollar",
                         "country": "Barbados"},
                        {"currency": "BDT", "name": "Bangladeshi Taka",
                         "country": "Bangladesh"},
                        {"currency": "BGN", "name": "Bulgarian Lev",
                         "country": "Bulgaria"},
                        {"currency": "BHD", "name": "Bahraini Dinar",
                         "country": "Bahrain"},
                        {"currency": "BIF", "name": "Burundian Franc",
                         "country": "Burundi"},
                        {"currency": "BMD", "name": "Bermudian Dollar",
                         "country": "Bermuda"},
                        {"currency": "BND", "name": "Brunei Dollar",
                         "country": "Brunei"},
                        {"currency": "BOB", "name": "Bolivian Boliviano",
                         "country": "Bolivia"},
                        {"currency": "BRL", "name": "Brazilian Real",
                         "country": "Brazil"},
                        {"currency": "BSD", "name": "Bahamian Dollar",
                         "country": "Bahamas"},
                        {"currency": "BTN", "name": "Bhutanese Ngultrum",
                         "country": "Bhutan"},
                        {"currency": "BWP", "name": "Botswana Pula",
                         "country": "Botswana"},
                        {"currency": "BYN", "name": "Belarusian Ruble",
                         "country": "Belarus"},
                        {"currency": "BZD", "name": "Belize Dollar",
                         "country": "Belize"},
                        {"currency": "CAD", "name": "Canadian Dollar",
                         "country": "Canada"},
                        {"currency": "CDF", "name": "Congolese Franc",
                         "country": "Democratic Republic of the Congo"},
                        {"currency": "CHF", "name": "Swiss Franc",
                         "country": "Switzerland"},
                        {"currency": "CLP", "name": "Chilean Peso",
                         "country": "Chile"},
                        {"currency": "CNY", "name": "Chinese Renminbi",
                         "country": "China"},
                        {"currency": "COP", "name": "Colombian Peso",
                         "country": "Colombia"},
                        {"currency": "CRC", "name": "Costa Rican Colon",
                         "country": "Costa Rica"},
                        {"currency": "CUP", "name": "Cuban Peso", "country": "Cuba"},
                        {"currency": "CVE", "name": "Cape Verdean Escudo",
                         "country": "Cape Verde"},
                        {"currency": "CZK", "name": "Czech Koruna",
                         "country": "Czech Republic"},
                        {"currency": "DJF", "name": "Djiboutian Franc",
                         "country": "Djibouti"},
                        {"currency": "DKK", "name": "Danish Krone",
                         "country": "Denmark"},
                        {"currency": "DOP", "name": "Dominican Peso",
                         "country": "Dominican Republic"},
                        {"currency": "DZD", "name": "Algerian Dinar",
                         "country": "Algeria"},
                        {"currency": "EGP", "name": "Egyptian Pound",
                         "country": "Egypt"},
                        {"currency": "ERN", "name": "Eritrean Nakfa",
                         "country": "Eritrea"},
                        {"currency": "ETB", "name": "Ethiopian Birr",
                         "country": "Ethiopia"},
                        {"currency": "EUR", "name": "Euro",
                         "country": "European Union"},
                        {"currency": "FJD", "name": "Fiji Dollar", "country": "Fiji"},
                        {"currency": "FKP", "name": "Falkland Islands Pound",
                         "country": "Falkland Islands"},
                        {"currency": "FOK", "name": "Faroese Króna",
                         "country": "Faroe Islands"},
                        {"currency": "GBP", "name": "Pound Sterling",
                         "country": "United Kingdom"},
                        {"currency": "GEL", "name": "Georgian Lari",
                         "country": "Georgia"},
                        {"currency": "GGP", "name": "Guernsey Pound",
                         "country": "Guernsey"},
                        {"currency": "GHS", "name": "Ghanaian Cedi",
                         "country": "Ghana"},
                        {"currency": "GIP", "name": "Gibraltar Pound",
                         "country": "Gibraltar"},
                        {"currency": "GMD", "name": "Gambian Dalasi",
                         "country": "The Gambia"},
                        {"currency": "GNF", "name": "Guinean Franc",
                         "country": "Guinea"},
                        {"currency": "GTQ", "name": "Guatemalan Quetzal",
                         "country": "Guatemala"},
                        {"currency": "GYD", "name": "Guyanese Dollar",
                         "country": "Guyana"},
                        {"currency": "HKD", "name": "Hong Kong Dollar",
                         "country": "Hong Kong"},
                        {"currency": "HNL", "name": "Honduran Lempira",
                         "country": "Honduras"},
                        {"currency": "HRK", "name": "Croatian Kuna",
                         "country": "Croatia"},
                        {"currency": "HTG", "name": "Haitian Gourde",
                         "country": "Haiti"},
                        {"currency": "HUF", "name": "Hungarian Forint",
                         "country": "Hungary"},
                        {"currency": "IDR", "name": "Indonesian Rupiah",
                         "country": "Indonesia"},
                        {"currency": "ILS", "name": "Israeli New Shekel",
                         "country": "Israel"},
                        {"currency": "IMP", "name": "Manx Pound",
                         "country": "Isle of Man"},
                        {"currency": "INR", "name": "Indian Rupee",
                         "country": "India"},
                        {"currency": "IQD", "name": "Iraqi Dinar", "country": "Iraq"},
                        {"currency": "IRR", "name": "Iranian Rial", "country": "Iran"},
                        {"currency": "ISK", "name": "Icelandic Króna",
                         "country": "Iceland"},
                        {"currency": "JEP", "name": "Jersey Pound",
                         "country": "Jersey"},
                        {"currency": "JMD", "name": "Jamaican Dollar",
                         "country": "Jamaica"},
                        {"currency": "JOD", "name": "Jordanian Dinar",
                         "country": "Jordan"},
                        {"currency": "JPY", "name": "Japanese Yen",
                         "country": "Japan"},
                        {"currency": "KES", "name": "Kenyan Shilling",
                         "country": "Kenya"},
                        {"currency": "KGS", "name": "Kyrgyzstani Som",
                         "country": "Kyrgyzstan"},
                        {"currency": "KHR", "name": "Cambodian Riel",
                         "country": "Cambodia"},
                        {"currency": "KID", "name": "Kiribati Dollar",
                         "country": "Kiribati"},
                        {"currency": "KMF", "name": "Comorian Franc",
                         "country": "Comoros"},
                        {"currency": "KRW", "name": "South Korean Won",
                         "country": "South Korea"},
                        {"currency": "KWD", "name": "Kuwaiti Dinar",
                         "country": "Kuwait"},
                        {"currency": "KYD", "name": "Cayman Islands Dollar",
                         "country": "Cayman Islands"},
                        {"currency": "KZT", "name": "Kazakhstani Tenge",
                         "country": "Kazakhstan"},
                        {"currency": "LAK", "name": "Lao Kip", "country": "Laos"},
                        {"currency": "LBP", "name": "Lebanese Pound",
                         "country": "Lebanon"},
                        {"currency": "LKR", "name": "Sri Lanka Rupee",
                         "country": "Sri Lanka"},
                        {"currency": "LRD", "name": "Liberian Dollar",
                         "country": "Liberia"},
                        {"currency": "LSL", "name": "Lesotho Loti",
                         "country": "Lesotho"},
                        {"currency": "LYD", "name": "Libyan Dinar",
                         "country": "Libya"},
                        {"currency": "MAD", "name": "Moroccan Dirham",
                         "country": "Morocco"},
                        {"currency": "MDL", "name": "Moldovan Leu",
                         "country": "Moldova"},
                        {"currency": "MGA", "name": "Malagasy Ariary",
                         "country": "Madagascar"},
                        {"currency": "MKD", "name": "Macedonian Denar",
                         "country": "North Macedonia"},
                        {"currency": "MMK", "name": "Burmese Kyat",
                         "country": "Myanmar"},
                        {"currency": "MNT", "name": "Mongolian Tögrög",
                         "country": "Mongolia"},
                        {"currency": "MOP", "name": "Macanese Pataca",
                         "country": "Macau"},
                        {"currency": "MRU", "name": "Mauritanian Ouguiya",
                         "country": "Mauritania"},
                        {"currency": "MUR", "name": "Mauritian Rupee",
                         "country": "Mauritius"},
                        {"currency": "MVR", "name": "Maldivian Rufiyaa",
                         "country": "Maldives"},
                        {"currency": "MWK", "name": "Malawian Kwacha",
                         "country": "Malawi"},
                        {"currency": "MXN", "name": "Mexican Peso",
                         "country": "Mexico"},
                        {"currency": "MYR", "name": "Malaysian Ringgit",
                         "country": "Malaysia"},
                        {"currency": "MZN", "name": "Mozambican Metical",
                         "country": "Mozambique"},
                        {"currency": "NAD", "name": "Namibian Dollar",
                         "country": "Namibia"},
                        {"currency": "NGN", "name": "Nigerian Naira",
                         "country": "Nigeria"},
                        {"currency": "NIO", "name": "Nicaraguan Córdoba",
                         "country": "Nicaragua"},
                        {"currency": "NOK", "name": "Norwegian Krone",
                         "country": "Norway"},
                        {"currency": "NPR", "name": "Nepalese Rupee",
                         "country": "Nepal"},
                        {"currency": "NZD", "name": "New Zealand Dollar",
                         "country": "New Zealand"},
                        {"currency": "OMR", "name": "Omani Rial", "country": "Oman"},
                        {"currency": "PAB", "name": "Panamanian Balboa",
                         "country": "Panama"},
                        {"currency": "PEN", "name": "Peruvian Sol", "country": "Peru"},
                        {"currency": "PGK", "name": "Papua New Guinean Kina",
                         "country": "Papua New Guinea"},
                        {"currency": "PHP", "name": "Philippine Peso",
                         "country": "Philippines"},
                        {"currency": "PKR", "name": "Pakistani Rupee",
                         "country": "Pakistan"},
                        {"currency": "PLN", "name": "Polish Złoty",
                         "country": "Poland"},
                        {"currency": "PYG", "name": "Paraguayan Guaraní",
                         "country": "Paraguay"},
                        {"currency": "QAR", "name": "Qatari Riyal",
                         "country": "Qatar"},
                        {"currency": "RON", "name": "Romanian Leu",
                         "country": "Romania"},
                        {"currency": "RSD", "name": "Serbian Dinar",
                         "country": "Serbia"},
                        {"currency": "RUB", "name": "Russian Ruble",
                         "country": "Russia"},
                        {"currency": "RWF", "name": "Rwandan Franc",
                         "country": "Rwanda"},
                        {"currency": "SAR", "name": "Saudi Riyal",
                         "country": "Saudi Arabia"},
                        {"currency": "SBD", "name": "Solomon Islands Dollar",
                         "country": "Solomon Islands"},
                        {"currency": "SCR", "name": "Seychellois Rupee",
                         "country": "Seychelles"},
                        {"currency": "SDG", "name": "Sudanese Pound",
                         "country": "Sudan"},
                        {"currency": "SEK", "name": "Swedish Krona",
                         "country": "Sweden"},
                        {"currency": "SGD", "name": "Singapore Dollar",
                         "country": "Singapore"},
                        {"currency": "SHP", "name": "Saint Helena Pound",
                         "country": "Saint Helena"},
                        {"currency": "SLL", "name": "Sierra Leonean Leone",
                         "country": "Sierra Leone"},
                        {"currency": "SOS", "name": "Somali Shilling",
                         "country": "Somalia"},
                        {"currency": "SRD", "name": "Surinamese Dollar",
                         "country": "Suriname"},
                        {"currency": "SSP", "name": "South Sudanese Pound",
                         "country": "South Sudan"},
                        {"currency": "STN", "name": "São Tomé and Príncipe Dobra",
                         "country": "São Tomé and Príncipe"},
                        {"currency": "SYP", "name": "Syrian Pound",
                         "country": "Syria"},
                        {"currency": "SZL", "name": "Eswatini Lilangeni",
                         "country": "Eswatini"},
                        {"currency": "THB", "name": "Thai Baht",
                         "country": "Thailand"},
                        {"currency": "TJS", "name": "Tajikistani Somoni",
                         "country": "Tajikistan"},
                        {"currency": "TMT", "name": "Turkmenistan Manat",
                         "country": "Turkmenistan"},
                        {"currency": "TND", "name": "Tunisian Dinar",
                         "country": "Tunisia"},
                        {"currency": "TOP", "name": "Tongan Paʻanga",
                         "country": "Tonga"},
                        {"currency": "TRY", "name": "Turkish Lira",
                         "country": "Turkey"},
                        {"currency": "TTD", "name": "Trinidad and Tobago Dollar",
                         "country": "Trinidad and Tobago"},
                        {"currency": "TVD", "name": "Tuvaluan Dollar",
                         "country": "Tuvalu"},
                        {"currency": "TWD", "name": "New Taiwan Dollar",
                         "country": "Taiwan"},
                        {"currency": "TZS", "name": "Tanzanian Shilling",
                         "country": "Tanzania"},
                        {"currency": "UAH", "name": "Ukrainian Hryvnia",
                         "country": "Ukraine"},
                        {"currency": "UGX", "name": "Ugandan Shilling",
                         "country": "Uganda"},
                        {"currency": "USD", "name": "United States Dollar",
                         "country": "United States"},
                        {"currency": "UYU", "name": "Uruguayan Peso",
                         "country": "Uruguay"},
                        {"currency": "UZS", "name": "Uzbekistani So'm",
                         "country": "Uzbekistan"},
                        {"currency": "VES", "name": "Venezuelan Bolívar Soberano",
                         "country": "Venezuela"},
                        {"currency": "VND", "name": "Vietnamese Đồng",
                         "country": "Vietnam"},
                        {"currency": "VUV", "name": "Vanuatu Vatu",
                         "country": "Vanuatu"},
                        {"currency": "WST", "name": "Samoan Tālā",
                         "country": "Samoa"},
                        {"currency": "XAF", "name": "Central African CFA Franc",
                         "country": "CEMAC"},
                        {"currency": "XCD", "name": "East Caribbean Dollar",
                         "country": "Organisation of Eastern Caribbean States"},
                        {"currency": "XDR", "name": "Special Drawing Rights",
                         "country": "International Monetary Fund"},
                        {"currency": "XOF", "name": "West African CFA franc",
                         "country": "CFA"},
                        {"currency": "XPF", "name": "CFP Franc",
                         "country": "Collectivités d'Outre-Mer"},
                        {"currency": "YER", "name": "Yemeni Rial",
                         "country": "Yemen"},
                        {"currency": "ZAR", "name": "South African Rand",
                         "country": "South Africa"},
                        {"currency": "ZMW", "name": "Zambian Kwacha",
                         "country": "Zambia"},
                        {"currency": "ZWL", "name": "Zimbabwean Dollar",
                         "country": "Zimbabwe"},
                        ]


def all_supported_currencies():
    return supported_currencies


def exchange_to():
    return exchange_usd
