""" PopulationGetResponse Definition """

from rowantree.common.sdk import BaseModel


class PopulationGetResponse(BaseModel):
    """
    PopulationGetResponse DTO
    Defines a user population.

    Attributes
    ----------
    population: int
        The current size of the user population.
    """

    population: int
