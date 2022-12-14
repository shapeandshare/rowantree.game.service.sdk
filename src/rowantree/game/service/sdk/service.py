"""
The Rowan Tree Service Layer Interface
This should be used as the primary entry point for interactions.
"""
from typing import Optional

from rowantree.auth.sdk import AuthenticateUserCommand
from rowantree.auth.sdk import CommandOptions as AuthCommandOptions
from rowantree.contracts import ActionQueue, FeatureType, StoreType, User, UserFeatureState, UserState, UserStore

from .commands.action_queue_process import ActionQueueProcessCommand
from .commands.health_get import HealthGetCommand
from .commands.merchant_transforms_perform import MerchantTransformPerformCommand
from .commands.user.active_get import UserActiveGetCommand
from .commands.user.active_set import UserActiveSetCommand
from .commands.user.create import UserCreateCommand
from .commands.user.delete import UserDeleteCommand
from .commands.user.feature_active_get import UserFeatureActiveGetCommand
from .commands.user.features_get import UserFeaturesGetCommand
from .commands.user.income_get import UserIncomeGetCommand
from .commands.user.income_set import UserIncomeSetCommand
from .commands.user.merchant_transforms_get import UserMerchantTransformsGetCommand
from .commands.user.population_get import UserPopulationGetCommand
from .commands.user.state_get import UserStateGetCommand
from .commands.user.stores_get import UserStoresGetCommand
from .commands.user.transport import UserTransportCommand
from .commands.world_get import WorldStatusGetCommand
from .contracts.dto.command_options import CommandOptions
from .contracts.dto.world_status import WorldStatus
from .contracts.requests.merchant_transform import MerchantTransformRequest
from .contracts.requests.user.income_set import UserIncomeSetRequest
from .contracts.requests.user.transport import UserTransportRequest
from .contracts.user_active_status import UserActiveGetStatus


# pylint: disable=too-many-instance-attributes
class RowanTreeService:
    """
    Rowan Tree Service
    Provides an interface for access the service layer.
    """

    user_active_get_command: UserActiveGetCommand
    user_active_set_command: UserActiveSetCommand

    user_create_command: UserCreateCommand
    user_delete_command: UserDeleteCommand

    user_feature_active_get_command: UserFeatureActiveGetCommand
    user_features_get_command: UserFeaturesGetCommand

    user_income_get_command: UserIncomeGetCommand
    user_income_set_command: UserIncomeSetCommand

    user_merchant_transforms_get_command: UserMerchantTransformsGetCommand
    user_population_get_command: UserPopulationGetCommand
    user_state_get_command: UserStateGetCommand
    user_stores_get_command: UserStoresGetCommand
    user_transport_command: UserTransportCommand

    merchant_transform_perform_command: MerchantTransformPerformCommand
    action_queue_process_command: ActionQueueProcessCommand
    health_get_command: HealthGetCommand
    world_status_get_command: WorldStatusGetCommand

    def __init__(self, options: Optional[CommandOptions] = None):
        command_dict: dict = {}
        if options:
            auth_options: AuthCommandOptions = AuthCommandOptions.parse_obj(options.dict(by_alias=True))
            command_dict["options"] = options
            command_dict["authenticate_user_command"] = AuthenticateUserCommand(options=auth_options)

        self.user_active_get_command = UserActiveGetCommand.parse_obj(command_dict)
        self.user_active_set_command = UserActiveSetCommand.parse_obj(command_dict)

        self.user_create_command = UserCreateCommand.parse_obj(command_dict)
        self.user_delete_command = UserDeleteCommand.parse_obj(command_dict)

        self.user_feature_active_get_command = UserFeatureActiveGetCommand.parse_obj(command_dict)
        self.user_features_get_command = UserFeaturesGetCommand.parse_obj(command_dict)

        self.user_income_get_command = UserIncomeGetCommand.parse_obj(command_dict)
        self.user_income_set_command = UserIncomeSetCommand.parse_obj(command_dict)

        self.user_merchant_transforms_get_command = UserMerchantTransformsGetCommand.parse_obj(command_dict)
        self.user_population_get_command = UserPopulationGetCommand.parse_obj(command_dict)
        self.user_state_get_command = UserStateGetCommand.parse_obj(command_dict)
        self.user_stores_get_command = UserStoresGetCommand.parse_obj(command_dict)
        self.user_transport_command = UserTransportCommand.parse_obj(command_dict)

        self.merchant_transform_perform_command = MerchantTransformPerformCommand.parse_obj(command_dict)
        self.health_get_command = HealthGetCommand.parse_obj(command_dict)
        self.action_queue_process_command = ActionQueueProcessCommand.parse_obj(command_dict)
        self.world_status_get_command = WorldStatusGetCommand.parse_obj(command_dict)

    def user_active_get(self, user_guid: Optional[str] = None) -> UserActiveGetStatus:
        """
        Gets User Active State

        Parameters
        ----------
        user_guid: Optional[str]
            The user guid to look up.

        Returns
        -------
        user_active: UserActiveGetStatus
            The user active state object.
        """

        return self.user_active_get_command.execute(user_guid=user_guid)

    def user_active_set(self, active: bool, user_guid: Optional[str] = None) -> UserActiveGetStatus:
        """
        Sets the user active state.

        Parameters
        ----------
        user_guid: Optional[str]
            The user guid to target.
        active: bool
            The active state to set the user to.

        Returns
        -------
        user_active: UserActiveGetStatus
            The state of the user.
        """

        request: UserActiveGetStatus = UserActiveGetStatus(active=active)
        return self.user_active_set_command.execute(user_guid=user_guid, request=request)

    def user_create(self, user_guid: Optional[str] = None) -> User:
        """
        Creates a user.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.

        Returns
        -------
        user: User
            The newly created user.
        """

        return self.user_create_command.execute(user_guid=user_guid)

    def user_delete(self, user_guid: Optional[str] = None) -> None:
        """
        Deletes a user.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.
        """

        self.user_delete_command.execute(user_guid=user_guid)

    def user_feature_active_get(self, user_guid: Optional[str] = None) -> UserFeatureState:
        """
        Gets the active user feature.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.

        Returns
        -------
        user_feature: UserFeatureState
            The UserFeatureState.
        """

        return self.user_feature_active_get_command.execute(user_guid=user_guid)

    def user_features_get(self, user_guid: Optional[str] = None) -> set[FeatureType]:
        """
        Gets a (unique) list of user features.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.

        Returns
        -------
        user_features: set[FeatureType]
            A unique set of user features.
        """

        return self.user_features_get_command.execute(user_guid=user_guid)

    def user_income_get(self, user_guid: Optional[str] = None) -> dict[StoreType, UserStore]:
        """
        Gets (unique) list of user incomes.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.

        Returns
        -------
        user_income: dict[StoreType, UserStore]
        """

        return self.user_income_get_command.execute(user_guid=user_guid)

    def user_income_set(self, income_source_name: StoreType, amount: int, user_guid: Optional[str] = None) -> None:
        """
        Sets a user income. (Creates or dismisses a number of workers of the type).

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.
        income_source_name: StoreType
            The name of the income type.
        amount: int
            The amount to set the income type to (absolute).
        """

        request: UserIncomeSetRequest = UserIncomeSetRequest(income_source_name=income_source_name, amount=amount)
        self.user_income_set_command.execute(user_guid=user_guid, request=request)

    def user_merchant_transforms_get(self, user_guid: Optional[str] = None) -> set[StoreType]:
        """
        Gets a (unique) set of user merchant transforms.

        Parameters
        ----------
        user_guid: Optional[str]
            Target user guid.

        Returns
        -------
        user_merchants: set[StoreType]
            A (unique) set of user merchant transforms.
        """

        return self.user_merchant_transforms_get_command.execute(user_guid=user_guid)

    def user_population_get(self, user_guid: Optional[str] = None) -> int:
        """
        Gets the user population.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.

        Returns
        -------
        user_population: int
            User population size.
        """

        return self.user_population_get_command.execute(user_guid=user_guid)

    def user_state_get(self, user_guid: Optional[str] = None) -> UserState:
        """
        Gets the user game state.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.

        Returns
        -------
        user_state: UserState
            The user state object.
        """

        return self.user_state_get_command.execute(user_guid=user_guid)

    def user_stores_get(self, user_guid: Optional[str] = None) -> dict[StoreType, UserStore]:
        """
        Gets the (unique) set of user stores.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.

        Returns
        -------
        user_stores: dict[StoreType, UserStore]
            A (unique) set of user stores.
        """

        return self.user_stores_get_command.execute(user_guid=user_guid)

    def user_transport(self, location: FeatureType, user_guid: Optional[str] = None) -> UserFeatureState:
        """
        Performs a user transport. (feature to feature change)

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.
        location: FeatureType
            The feature/location to transport the user to.

        Returns
        -------
        feature_state: UserFeatureState
            The user's new active UserFeatureState.
        """

        request: UserTransportRequest = UserTransportRequest(location=location)
        return self.user_transport_command.execute(user_guid=user_guid, request=request)

    # Merchant Commands

    def merchant_transform_perform(self, store_name: StoreType, user_guid: Optional[str] = None) -> None:
        """
        Performs a merchant transform.

        Parameters
        ----------
        user_guid: Optional[str]
            The target user guid.
        store_name: StoreType
            The store name to perform the merchant transform on.
        """

        request: MerchantTransformRequest = MerchantTransformRequest(store_name=store_name)
        self.merchant_transform_perform_command.execute(user_guid=user_guid, request=request)

    # Admin Commands

    def health_get(self) -> bool:
        """
        Gets the server health.

        Returns
        -------
        health: bool
            The server health (true or false).
        """

        return self.health_get_command.execute()

    def action_queue_process(self, queue: ActionQueue) -> None:
        """
        Processes an action queue.

        Parameters
        ----------
        queue: ActionQueue
            The action queue to process.
        """

        self.action_queue_process_command.execute(request=queue)

    def world_status_get(self) -> WorldStatus:
        """
        Gets the world status.

        Returns
        -------
        world_status: WorldStatus
            The world status.
        """

        return self.world_status_get_command.execute()
