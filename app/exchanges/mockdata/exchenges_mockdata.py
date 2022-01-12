import random

test = [{"number": 1}, {"number": 2}, {"number": 3}]

exchange_usd = {
    "base_code": "USD",
    "rates": {
        "USD": 1,
        "AED": 3.67,
        "AFN": 104.88,
        "ALL": 107.84,
        "AMD": 482.33,
        "ANG": 1.79,
        "AOA": 537.21,
        "ARS": 103.48,
        "AUD": 1.39,
        "AWG": 1.79,
        "AZN": 1.7,
        "BAM": 1.72,
        "BBD": 2,
        "BDT": 85.84,
        "BGN": 1.72,
        "BHD": 0.376,
        "BIF": 1993.24,
        "BMD": 1,
        "BND": 1.35,
        "BOB": 6.87,
        "BRL": 5.65,
        "BSD": 1,
        "BTN": 73.85,
        "BWP": 11.67,
        "BYN": 2.58,
        "BZD": 2,
        "CAD": 1.26,
        "CDF": 1999.89,
        "CHF": 0.925,
        "CLP": 834.38,
        "CNY": 6.38,
        "COP": 4015.48,
        "CRC": 640.48,
        "CUP": 24,
        "CVE": 97.23,
        "CZK": 21.55,
        "DJF": 177.72,
        "DKK": 6.58,
        "DOP": 57.44,
        "DZD": 139.6,
        "EGP": 15.7,
        "ERN": 15,
        "ETB": 49.06,
        "EUR": 0.882,
        "FJD": 2.12,
        "FKP": 0.736,
        "FOK": 6.58,
        "GBP": 0.736,
        "GEL": 3.09,
        "GGP": 0.736,
        "GHS": 6.52,
        "GIP": 0.736,
        "GMD": 53.03,
        "GNF": 9237.28,
        "GTQ": 7.7,
        "GYD": 209.48,
        "HKD": 7.8,
        "HNL": 24.53,
        "HRK": 6.64,
        "HTG": 100.61,
        "HUF": 315.64,
        "IDR": 14270.02,
        "ILS": 3.13,
        "IMP": 0.736,
        "INR": 73.85,
        "IQD": 1461.15,
        "IRR": 41942.17,
        "ISK": 129.56,
        "JEP": 0.736,
        "JMD": 154.29,
        "JOD": 0.709,
        "JPY": 115.38,
        "KES": 113.43,
        "KGS": 84.77,
        "KHR": 4078.56,
        "KID": 1.39,
        "KMF": 433.81,
        "KRW": 1193.99,
        "KWD": 0.3,
        "KYD": 0.833,
        "KZT": 435.23,
        "LAK": 11225.94,
        "LBP": 1507.5,
        "LKR": 202.24,
        "LRD": 147.77,
        "LSL": 15.57,
        "LYD": 4.61,
        "MAD": 9.2,
        "MDL": 17.94,
        "MGA": 3037.82,
        "MKD": 54.51,
        "MMK": 1774.97,
        "MNT": 2863.36,
        "MOP": 8.03,
        "MRU": 36.35,
        "MUR": 43.76,
        "MVR": 15.41,
        "MWK": 820.4,
        "MXN": 20.39,
        "MYR": 4.19,
        "MZN": 63.04,
        "NAD": 15.57,
        "NGN": 413.43,
        "NIO": 35.5,
        "NOK": 8.81,
        "NPR": 118.16,
        "NZD": 1.48,
        "OMR": 0.384,
        "PAB": 1,
        "PEN": 3.93,
        "PGK": 3.51,
        "PHP": 51.15,
        "PKR": 176.56,
        "PLN": 4,
        "PYG": 6932.4,
        "QAR": 3.64,
        "RON": 4.36,
        "RSD": 103.6,
        "RUB": 74.85,
        "RWF": 1042.99,
        "SAR": 3.75,
        "SBD": 7.99,
        "SCR": 13.86,
        "SDG": 425.57,
        "SEK": 9.06,
        "SGD": 1.35,
        "SHP": 0.736,
        "SLL": 11269.99,
        "SOS": 579.23,
        "SRD": 21.31,
        "SSP": 432.86,
        "STN": 21.6,
        "SYP": 2524.2,
        "SZL": 15.57,
        "THB": 33.44,
        "TJS": 11.26,
        "TMT": 3.5,
        "TND": 2.81,
        "TOP": 2.28,
        "TRY": 13.81,
        "TTD": 6.78,
        "TVD": 1.39,
        "TWD": 27.66,
        "TZS": 2306.25,
        "UAH": 27.48,
        "UGX": 3529.28,
        "UYU": 44.61,
        "UZS": 10719.04,
        "VES": 4.63,
        "VND": 22635.56,
        "VUV": 113.09,
        "WST": 2.61,
        "XAF": 578.42,
        "XCD": 2.7,
        "XDR": 0.714,
        "XOF": 578.42,
        "XPF": 105.23,
        "YER": 250.5,
        "ZAR": 15.57,
        "ZMW": 16.98,
        "ZWL": 108.67
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