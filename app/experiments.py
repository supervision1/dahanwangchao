from __future__ import annotations

import hashlib


EXPERIMENTS = {
    "paywall_headline": ("A", "B"),
    "first_purchase_incentive": ("A", "B"),
    "bundle_order": ("A", "B"),
}


def assign_variant(user_id: str, experiment_name: str) -> str:
    if experiment_name not in EXPERIMENTS:
        raise ValueError(f"Unknown experiment: {experiment_name}")

    variants = EXPERIMENTS[experiment_name]
    digest = hashlib.sha256(f"{experiment_name}:{user_id}".encode("utf-8")).hexdigest()
    bucket = int(digest[:8], 16)
    return variants[bucket % len(variants)]
