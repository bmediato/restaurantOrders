from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    queijo = Ingredient('queijo provolone')

    assert queijo.name == 'queijo provolone'
    assert queijo == Ingredient('queijo provolone')

    assert hash(queijo) == hash('queijo provolone')

    assert Restriction.LACTOSE in queijo.restrictions
    assert Restriction.ANIMAL_DERIVED in queijo.restrictions

    assert repr(queijo) == "Ingredient('queijo provolone')"
