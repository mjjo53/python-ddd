import pytest

from modules.catalog.application.command import (
    CreateListingDraftCommand,
    PublishListingDraftCommand,
)
from seedwork.domain.value_objects import UUID, Money
from seedwork.infrastructure.logging import logger


def setup_app_for_bidding_tests(app, listing_id, seller_id, bidder_id):
    logger.info("Adding users")
    with app.transaction_context() as ctx:
        iam_service = ctx.dependency_provider["iam_service"]

        iam_service.create_user(
            user_id=seller_id,
            email="seller@example.com",
            password="password",
            access_token="token1",
        )
        iam_service.create_user(
            user_id=bidder_id,
            email="bidder@example.com",
            password="password",
            access_token="token2",
        )

    logger.info("Adding listing")
    app.execute_command(
        CreateListingDraftCommand(
            listing_id=listing_id,
            title="Foo",
            description="Bar",
            ask_price=Money(10),
            seller_id=seller_id,
        )
    )
    app.execute_command(PublishListingDraftCommand(listing_id=listing_id))
    logger.info("test setup complete")


@pytest.mark.integration
def test_place_bid(app, api_client):
    listing_id = UUID(int=1)
    seller_id = UUID(int=2)
    bidder_id = UUID(int=3)
    setup_app_for_bidding_tests(app, listing_id, seller_id, bidder_id)

    url = f"/bidding/{listing_id}/place_bid"

    response = api_client.post(url, json={"bidder_id": str(bidder_id), "amount": 11})
    assert response.status_code == 200