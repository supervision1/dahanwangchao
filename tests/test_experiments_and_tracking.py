import pytest

from app.experiments import assign_variant
from app.tracking import Event, validate_event


def test_variant_is_stable():
    v1 = assign_variant("u100", "paywall_headline")
    v2 = assign_variant("u100", "paywall_headline")
    assert v1 == v2


def test_variant_values_are_ab():
    assert assign_variant("u100", "bundle_order") in {"A", "B"}


def test_event_validation_success():
    validate_event(Event(user_id="u1", name="session_completed", timestamp_ms=1))


def test_event_validation_raises_on_invalid_name():
    with pytest.raises(ValueError):
        validate_event(Event(user_id="u1", name="invalid_event", timestamp_ms=1))
