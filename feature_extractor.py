from __future__ import annotations

from urllib.parse import urlparse


SUSPICIOUS_WORDS = {
    "login",
    "verify",
    "update",
    "secure",
    "account",
    "bank",
    "signin",
    "confirm",
    "password",
    "free",
    "bonus",
    "wallet",
    "unlock",
}

SPECIAL_CHARACTERS = "@-_=%?&~"


def extract_features(url: str) -> list[int]:
    parsed = urlparse(url if "://" in url else f"http://{url}")
    hostname = parsed.netloc or parsed.path
    subdomains = [part for part in hostname.split(".")[:-2] if part]
    lowered = url.lower()

    suspicious_count = sum(1 for word in SUSPICIOUS_WORDS if word in lowered)
    special_char_count = sum(lowered.count(char) for char in SPECIAL_CHARACTERS)

    return [
        len(url),
        url.count("."),
        1 if parsed.scheme == "https" else 0,
        special_char_count,
        len(subdomains),
        suspicious_count,
    ]


FEATURE_NAMES = [
    "url_length",
    "num_dots",
    "uses_https",
    "special_characters",
    "subdomain_count",
    "suspicious_words",
]
