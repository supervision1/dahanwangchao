from __future__ import annotations

from dataclasses import dataclass


ALLOWED_EVENTS = {
    "session_completed",
    "paywall_exposed",
    "paywall_clicked",
    "checkout_started",
    "purchase_success",
    "purchase_refund",
    "hardware_bundle_viewed",
    "hardware_bundle_purchased",
}


@dataclass(frozen=True)
class Event:
    user_id: str
    name: str
    timestamp_ms: int


def validate_event(event: Event) -> None:
    if not event.user_id:
        raise ValueError("user_id is required")
    if event.name not in ALLOWED_EVENTS:
        raise ValueError(f"Unsupported event name: {event.name}")
    if event.timestamp_ms <= 0:
        raise ValueError("timestamp_ms must be positive")
