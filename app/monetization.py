from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class UserTier(str, Enum):
    A = "A"
    B = "B"
    C = "C"


@dataclass(frozen=True)
class UserProfile:
    user_id: str
    days_active_30d: int
    sessions_7d: int
    perceived_improvement_score: float  # 0.0 ~ 1.0
    price_sensitivity_score: float  # 0.0 ~ 1.0


@dataclass(frozen=True)
class OfferRecommendation:
    tier: UserTier
    primary_offer: str
    secondary_offer: str | None = None


def segment_user(profile: UserProfile) -> UserTier:
    """Segment user into A/B/C tier with simple rules from product doc."""
    if (
        profile.days_active_30d >= 14
        and profile.sessions_7d >= 4
        and profile.perceived_improvement_score >= 0.6
    ):
        return UserTier.A

    if profile.sessions_7d >= 2 and profile.perceived_improvement_score >= 0.3:
        return UserTier.B

    return UserTier.C


def recommend_offer(profile: UserProfile) -> OfferRecommendation:
    tier = segment_user(profile)

    if tier == UserTier.A:
        return OfferRecommendation(
            tier=tier,
            primary_offer="年费会员+Pro硬件组合包+延保",
            secondary_offer="专属程序包增值",
        )

    if tier == UserTier.B:
        return OfferRecommendation(
            tier=tier,
            primary_offer="月费会员",
            secondary_offer="限时硬件券",
        )

    return OfferRecommendation(
        tier=tier,
        primary_offer="7天体验包",
        secondary_offer="低价IAP程序",
    )


def training_completion_trigger(session_count: int) -> str:
    """Conversion trigger mapping for completion page."""
    if session_count <= 1:
        return "3天挑战"
    if session_count <= 3:
        return "会员首购优惠"
    if session_count >= 5:
        return "硬件升级弹层"
    return "弱提示：继续体验"


def winback_discount(days_inactive: int, tier: UserTier) -> float:
    """Return discount rate (0~1) based on inactivity and tier strategy."""
    if days_inactive < 3:
        return 0.0

    if tier == UserTier.A:
        return 0.05
    if tier == UserTier.B:
        return 0.12
    return 0.2
