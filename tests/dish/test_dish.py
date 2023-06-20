import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    risotoSalmao = Dish("risoto de salmão", 67.90)
    risotoCamarao = Dish("risoto de camarão", 70.00)

    assert risotoSalmao.name == "risoto de salmão"
    assert risotoSalmao.price == 67.90
    assert risotoSalmao.recipe == {}

    with pytest.raises(TypeError):
        Dish("risoto de salmão", "89.65")

    with pytest.raises(ValueError):
        Dish("risoto de salmão", -89.65)

    assert hash(risotoSalmao) == hash(risotoSalmao)
    assert hash(risotoSalmao) != hash(risotoCamarao)
    assert repr(risotoSalmao) == "Dish('risoto de salmão', R$67.90)"
    assert repr(risotoSalmao) != "Dish('risoto de camarão', R$70.00)"

    assert risotoSalmao.get_ingredients() == set()
    assert risotoSalmao == Dish("risoto de salmão", 67.90)
    assert risotoSalmao != Dish("risoto de camarão", 70.00)

    risotoSalmao.add_ingredient_dependency(Ingredient("salmão"), 1)
    assert risotoSalmao.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    assert risotoSalmao.get_ingredients() == {Ingredient("salmão")}
