import unittest
from formas import forma

class TestFormas(unittest.TestCase):
    def testeAreaCirculo():
        self.assertEqual(706.85, forma.areaCirculo(15), .2)
        self.assertEqual(201.06, forma.areaCirculo(8), .2)

    def testeVolumeEsfera():
        self.assertEqual(10602.87, forma.volumeEsfera(15), .2)
        self.assertEqual(551713.93, forma.volumeEsfera(56), .2)

    def testeAreaQuadrado():
        self.assertEqual(100.0, forma.areaQuadrado(10), .1)
        self.assertEqual(441.0, forma.areaQuadrado(21), .1)

    def testeVolumeCubo():
        self.assertEqual(125.0, forma.volumeCubo(5), .1)
        self.assertEqual(32768.0, forma.volumeCubo(32), .1)

    def testeAreaTriangulo():
        self.assertEqual(100.0, forma.areaTriangulo(10,20), .1)
        self.assertEqual(4.0, forma.areaTriangulo(8,1), .1)

    def testeVolumePiramide():
        self.assertEqual(27.00, forma.volumePiramide(3,9), .2)
        self.assertEqual(84.00, forma.volumePiramide(6,7), .2)

    def testeAreaTetraedro():
        self.assertEqual(692.82, forma.areaTetraedro(20), .2)
        self.assertEqual(140.29, forma.areaTetraedro(9), .2)

    def testeVolumeTetraedro():
        self.assertEqual(3181.98, forma.volumeTetraedro(30), .2)
        self.assertEqual(0.94, forma.volumeTetraedro(2), .2)

    def testeVolumeCilindro():
        self.assertEqual(56548.66, forma.volumeCilindro(30,20), .2)
        self.assertEqual(1407.43, forma.volumeCilindro(8,7), .2)

    def testeAreaRetangulo():
        self.assertEqual(600.0, forma.areaRetangulo(20,30), .1)
        self.assertEqual(16.0, forma.areaRetangulo(8,2), .1)
