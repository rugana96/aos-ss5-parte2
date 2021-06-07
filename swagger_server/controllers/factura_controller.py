from datetime import date
import connexion
import six
import datetime

from swagger_server.models.factura import Factura  # noqa: E501
from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from flask import make_response

example = [
    {
        'factura_id': 5623,
        'user_id': 21,
        'vehiculo_id': 67,
        'fecha_emision': datetime.date(2021, 3, 29),
        'importe': 234.00,
        'importe_iva': 283.14,
        'links': [
            {
                "href": "api/v1/trabajo/1111",
                "rel": "trabajo"
            },
            {
                "href": "api/v1/trabajo/1112",
                "rel": "trabajo"
            }
        ]
    },
    {
        'factura_id': 1234,
        'user_id': 54,
        'vehiculo_id': 12,
        'fecha_emision': datetime.date(1996, 9, 26),
        'importe': 234.00,
        'importe_iva': 283.14,
        'links': [
            {
                "href": "api/v1/trabajo/1113",
                "rel": "trabajo"
            }
        ]
    }
]

def upm_aos_factura_delete(factura_id):  # noqa: E501
    """Elimina una factura.

    Elimina la factura identificada por facturaId # noqa: E501

    :param factura_id: ID de la factura
    :type factura_id: int

    :rtype: None
    """
    return make_response(
         "{factura_id} successfully deleted".format(factura_id=factura_id), 204
    )


def upm_aos_factura_fget(factura_id):  # noqa: E501
    """Obtiene una factura por su ID

    Obtiene una factura identificada por su facturaID. # noqa: E501

    :param factura_id: ID de la factura
    :type factura_id: int

    :rtype: Factura
    """
    for factura in example:
        if (factura["factura_id"] == factura_id):
            return factura


def upm_aos_factura_foptions(factura_id):  # noqa: E501
    """Proporciona la lista de los métodos HTTP soportados.

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados (separados por comas). # noqa: E501

    :param factura_id: ID de la factura
    :type factura_id: int

    :rtype: None
    """
    for factura in example:
        if (factura["factura_id"] == factura_id):
            return make_response(
                "GET", "DELETE", "PUT", "POST", "OPTIONS", 204
            )


def upm_aos_factura_options():  # noqa: E501
    """Proporciona la lista de los métodos HTTP soportados.

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados (separados por comas). # noqa: E501


    :rtype: None
    """
    return make_response(
                "GET", "OPTIONS", 204
            )


def upm_aos_factura_post(body):  # noqa: E501
    """Genera la factura de un usuario

    Genera la factura con un conjunto de trabajos y un importe. # noqa: E501

    :param body: &#x60;Factura&#x60; data
    :type body: dict | bytes

    :rtype: Factura
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return make_response(
            "{body} successfully created".format(body=body), 201
        )


def upm_aos_factura_put(body, if_match, factura_id):  # noqa: E501
    """Modifica la factura.

    Actualiza la factura identificada por facturaId. # noqa: E501

    :param body: &#x60;Factura&#x60; data
    :type body: dict | bytes
    :param if_match: ETag del recurso que se desea modificar
    :type if_match: str
    :param factura_id: ID de la factura
    :type factura_id: int

    :rtype: Factura
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def upm_aos_factura_uget(user_id):  # noqa: E501
    """Obtiene todas las facturas de un usuario

    Obtiene todas las facturas de un usuario por su userId # noqa: E501

    :param user_id: ID del usuario
    :type user_id: int

    :rtype: Factura
    """
    for factura in example:
        if (factura["user_id"] == user_id):
            return factura


def upm_aos_factura_uoptions(user_id):  # noqa: E501
    """Proporciona la lista de los métodos HTTP soportados.

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados (separados por comas). # noqa: E501

    :param user_id: ID del usuario
    :type user_id: int

    :rtype: None
    """
    for factura in example:
        if (factura["user_id"] == user_id):
            return make_response(
                "GET", "OPTIONS", 204
            )


def upm_aos_factura_vget(vehiculo_id):  # noqa: E501
    """Obtiene todas las facturas de un vehiculo

    Obtiene todas las facturas de un vehiculo por su vehiculoId # noqa: E501

    :param vehiculo_id: ID del vehiculo
    :type vehiculo_id: int

    :rtype: Factura
    """
    for factura in example:
        if (factura["vehiculo_id"] == vehiculo_id):
            return factura


def upm_aos_factura_voptions(vehiculo_id):  # noqa: E501
    """Proporciona la lista de los métodos HTTP soportados.

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados (separados por comas). # noqa: E501

    :param vehiculo_id: ID del vehiculo
    :type vehiculo_id: int

    :rtype: None
    """
    for factura in example:
        if (factura["vehiculo_id"] == vehiculo_id):
            return make_response(
                "GET", "OPTIONS", 204
            )


def upm_aos_facturas_get():  # noqa: E501
    """Obtiene todas las facturas

     # noqa: E501


    :rtype: InlineResponse200
    """
    return example
