from __future__ import annotations

import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any


_WHITESPACE_RE = re.compile(r"\s+")
_EMAIL_RE = re.compile(
    r"^(?=.{1,254}$)(?=.{1,64}@)"
    r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,63}$"
)


def clean_text(text: Any) -> str:
    """
    Normalize user-provided text.

    - Converts non-None values to string
    - Strips leading/trailing whitespace
    - Collapses internal whitespace to single spaces
    """
    if text is None:
        return ""
    s = str(text).strip()
    if not s:
        return ""
    return _WHITESPACE_RE.sub(" ", s)


def validate_email(email: Any) -> bool:
    """
    Basic, practical email validation (not fully RFC 5322).

    Accepts common emails like: `name.surname+tag@example.co.uk`
    Rejects whitespace, missing parts, invalid labels, overly long inputs.
    """
    if not isinstance(email, str):
        return False
    candidate = email.strip()
    if not candidate or " " in candidate:
        return False
    return _EMAIL_RE.fullmatch(candidate) is not None


def validate_phone(phone: Any) -> bool:
    """
    Validate a phone number using E.164-like rules.

    - Accepts digits with common separators: spaces, '-', '(', ')', '.'
    - Allows an optional leading '+'
    - Valid digit length: 10..15 (common min/max range for international numbers)
    """
    if phone is None:
        return False
    if not isinstance(phone, str):
        phone = str(phone)

    s = phone.strip()
    if not s:
        return False

    has_plus = s.startswith("+")
    digits = re.sub(r"\D", "", s)

    if has_plus:
        if not re.fullmatch(r"\+[\d\s().-]+", s):
            return False
    else:
        if not re.fullmatch(r"[\d\s().-]+", s):
            return False

    return 10 <= len(digits) <= 15


def format_currency(
    amount: Any,
    currency_symbol: str = "$",
    decimals: int = 2,
    thousands_sep: str = ",",
    decimal_sep: str = ".",
) -> str:
    """
    Format a number as a currency string (e.g. `$1,234.50`).

    - Rounds using bankers-unfriendly (typical finance) ROUND_HALF_UP
    - Accepts int/float/Decimal/str as `amount`
    """
    if decimals < 0:
        raise ValueError("decimals must be >= 0")
    if len(thousands_sep) != 1 or len(decimal_sep) != 1:
        raise ValueError("thousands_sep and decimal_sep must be single characters")

    try:
        d = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError("amount must be a number or numeric string") from e

    q = Decimal("1") if decimals == 0 else Decimal("1").scaleb(-decimals)
    d = d.quantize(q, rounding=ROUND_HALF_UP)

    sign = "-" if d.is_signed() else ""
    d_abs = abs(d)

    # Use a fixed-point string so we don't lose trailing zeros.
    fixed = format(d_abs, "f")
    whole_str, dot, frac_str = fixed.partition(".")
    if decimals == 0:
        frac_str = ""
        dot = ""
    else:
        frac_str = (frac_str + ("0" * decimals))[:decimals]
        dot = decimal_sep

    groups: list[str] = []
    while whole_str:
        groups.append(whole_str[-3:])
        whole_str = whole_str[:-3]
    whole_grouped = thousands_sep.join(reversed(groups)) if groups else "0"

    return f"{sign}{currency_symbol}{whole_grouped}{dot}{frac_str}"


def calculate_percentage(part: Any, whole: Any, decimals: int = 2) -> float:
    """
    Calculate percentage: (part / whole) * 100.

    Raises ValueError if `whole` is 0 or non-numeric.
    """
    if decimals < 0:
        raise ValueError("decimals must be >= 0")

    try:
        p = Decimal(str(part))
        w = Decimal(str(whole))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError("part and whole must be numbers or numeric strings") from e

    if w == 0:
        raise ValueError("whole must not be 0")

    pct = (p / w) * Decimal("100")
    q = Decimal("1") if decimals == 0 else Decimal("1").scaleb(-decimals)
    return float(pct.quantize(q, rounding=ROUND_HALF_UP))

