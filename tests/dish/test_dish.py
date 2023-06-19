import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    risotoSalmão = Dish('risoto de salmão', 67.90)

    with pytest.raises(TypeError):
        Dish('risoto de salmão', 'a')

    with pytest.raises(ValueError):
        Dish('risoto de salmão', -9)

    assert risotoSalmão.name == 'risoto de salmão'
    assert risotoSalmão.price == 67.90
    assert risotoSalmão == Dish('risoto de salmão', 67.90)
    assert hash(risotoSalmão) == hash('risoto de salmão')
    assert repr(risotoSalmão) == "Dish('risoto de salmão', R$67.90)"

    risotoSalmão.add_ingredient_dependency(Ingredient('salmão'), 1)
    assert risotoSalmão.get_ingredients() == {Ingredient('salmão')}
    assert risotoSalmão.get_restrictions() == {Restriction.ANIMAL_MEAT,
                                               Restriction.SEAFOOD,
                                               Restriction.ANIMAL_DERIVED}
