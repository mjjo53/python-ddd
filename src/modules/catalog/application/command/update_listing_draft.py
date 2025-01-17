from dataclasses import dataclass

from modules.catalog.application import catalog_module
from modules.catalog.domain.entities import Listing
from modules.catalog.domain.repositories import ListingRepository
from seedwork.application.command_handlers import CommandResult
from seedwork.application.commands import Command
from seedwork.domain.value_objects import GenericUUID, Money


@dataclass
class UpdateListingDraftCommand(Command):
    """A command for updating a listing"""

    listing_id: GenericUUID
    title: str
    description: str
    ask_price: Money
    modify_user_id: GenericUUID


@catalog_module.command_handler
def update_listing_draft(
    command: UpdateListingDraftCommand, repository: ListingRepository
) -> CommandResult:
    listing: Listing = repository.get_by_id(command.listing_id)
    listing.change_main_attributes(
        title=command.title,
        description=command.description,
        ask_price=command.ask_price,
    )
