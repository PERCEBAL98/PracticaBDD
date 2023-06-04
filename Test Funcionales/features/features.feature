Feature: Test Funcionales

    Scenario Outline: visit "<browser_page>" and check "<browser_title>"
        When we visit "<browser_page>"
        Then it should have a title "<browser_title>"

        Examples:
            | browser_page       | browser_title                                              |
            | https://www.dia.es | Supermercado online \| ¡Recibe tu compra hoy mismo! \| Día |

    Scenario Outline: search "<article>" and count "<total> articles"
        When we search "<article>"
        Then it should be "<total>" articles

        Examples:
            | article | total |
            | ACUAREL | 5     |

    Scenario Outline: add "item" to shoppping cart and confirm added "<product add>"
        When we add "item" to shopping cart
        Then there should be "<product add>"
        Examples:
            | product add          |
            | Carrito (1 producto) |