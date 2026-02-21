from app.monetization import (
    UserProfile,
    UserTier,
    recommend_offer,
    segment_user,
    training_completion_trigger,
    winback_discount,
)


def test_segment_a_user():
    profile = UserProfile("u1", 20, 5, 0.9, 0.1)
    assert segment_user(profile) == UserTier.A


def test_segment_c_user():
    profile = UserProfile("u2", 2, 1, 0.1, 0.9)
    assert segment_user(profile) == UserTier.C


def test_offer_matches_tier():
    profile = UserProfile("u3", 15, 5, 0.8, 0.2)
    offer = recommend_offer(profile)
    assert offer.tier == UserTier.A
    assert "组合包" in offer.primary_offer


def test_training_trigger_rules():
    assert training_completion_trigger(1) == "3天挑战"
    assert training_completion_trigger(3) == "会员首购优惠"
    assert training_completion_trigger(5) == "硬件升级弹层"


def test_winback_discount_by_tier():
    assert winback_discount(4, UserTier.A) == 0.05
    assert winback_discount(4, UserTier.B) == 0.12
    assert winback_discount(4, UserTier.C) == 0.2
