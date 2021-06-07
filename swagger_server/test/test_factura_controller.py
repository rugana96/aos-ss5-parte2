# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.factura import Factura  # noqa: E501
from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFacturaController(BaseTestCase):
    """FacturaController integration test stubs"""

    def test_upm_aos_factura_delete(self):
        """Test case for upm_aos_factura_delete

        Elimina una factura.
        """
        response = self.client.open(
            '/factura/facturaId/{facturaId}'.format(factura_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_fget(self):
        """Test case for upm_aos_factura_fget

        Obtiene una factura por su ID
        """
        response = self.client.open(
            '/factura/facturaId/{facturaId}'.format(factura_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_foptions(self):
        """Test case for upm_aos_factura_foptions

        Proporciona la lista de los métodos HTTP soportados.
        """
        response = self.client.open(
            '/factura/facturaId/{facturaId}'.format(factura_id=56),
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_options(self):
        """Test case for upm_aos_factura_options

        Proporciona la lista de los métodos HTTP soportados.
        """
        response = self.client.open(
            '/factura',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_post(self):
        """Test case for upm_aos_factura_post

        Genera la factura de un usuario
        """
        body = None
        response = self.client.open(
            '/factura',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_put(self):
        """Test case for upm_aos_factura_put

        Modifica la factura.
        """
        body = None
        headers = [('if_match', 'if_match_example')]
        response = self.client.open(
            '/factura/facturaId/{facturaId}'.format(factura_id=56),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_uget(self):
        """Test case for upm_aos_factura_uget

        Obtiene todas las facturas de un usuario
        """
        response = self.client.open(
            '/factura/userId/{userId}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_uoptions(self):
        """Test case for upm_aos_factura_uoptions

        Proporciona la lista de los métodos HTTP soportados.
        """
        response = self.client.open(
            '/factura/userId/{userId}'.format(user_id=56),
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_vget(self):
        """Test case for upm_aos_factura_vget

        Obtiene todas las facturas de un vehiculo
        """
        response = self.client.open(
            '/factura/vehiculoId/{vehiculoId}'.format(vehiculo_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_factura_voptions(self):
        """Test case for upm_aos_factura_voptions

        Proporciona la lista de los métodos HTTP soportados.
        """
        response = self.client.open(
            '/factura/vehiculoId/{vehiculoId}'.format(vehiculo_id=56),
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_facturas_get(self):
        """Test case for upm_aos_facturas_get

        Obtiene todas las facturas
        """
        response = self.client.open(
            '/factura',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
