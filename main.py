from app.experiments import assign_variant
from app.monetization import (
    UserProfile,
    recommend_offer,
    training_completion_trigger,
    winback_discount,
)


def run_demo() -> None:
    profile = UserProfile(
        user_id="u_1001",
        days_active_30d=18,
        sessions_7d=5,
        perceived_improvement_score=0.72,
        price_sensitivity_score=0.2,
    )
    offer = recommend_offer(profile)

    print(f"tier={offer.tier}")
    print(f"primary_offer={offer.primary_offer}")
    print(f"training_trigger={training_completion_trigger(5)}")
    print(f"winback_discount={winback_discount(4, offer.tier) * 100:.0f}%")

    for exp in ("paywall_headline", "first_purchase_incentive", "bundle_order"):
        print(f"{exp}={assign_variant(profile.user_id, exp)}")


if __name__ == "__main__":
    run_demo()
