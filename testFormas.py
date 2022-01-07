import unittest
from formas import Formas

class TestFormass(unittest.TestCase):
    def testeAreaCirculo(self):
        self.assertAlmostEqual(706.85, Formas.areaCirculo(15), 1)
        self.assertAlmostEqual(201.06, Formas.areaCirculo(8), 1)

    def testeVolumeEsfera(self):
        self.assertAlmostEqual(14137.16, Formas.volumeEsfera(15), 1)
        self.assertAlmostEqual(735618.58, Formas.volumeEsfera(56), 1)

    def testeAreaQuadrado(self):
        self.assertAlmostEqual(100.0, Formas.areaQuadrado(10), 1)
        self.assertAlmostEqual(441.0, Formas.areaQuadrado(21), 1)

    def testeVolumeCubo(self):
        self.assertAlmostEqual(125.0, Formas.volumeCubo(5), 1)
        self.assertAlmostEqual(32768.0, Formas.volumeCubo(32), 1)

    def testeAreaTriangulo(self):
        self.assertAlmostEqual(100.0, Formas.areaTriangulo(10,20), 1)
        self.assertAlmostEqual(4.0, Formas.areaTriangulo(8,1), 1)

    def testeVolumePiramide(self):
        self.assertAlmostEqual(27.00, Formas.volumePiramide(3,9), 1)
        self.assertAlmostEqual(84.00, Formas.volumePiramide(6,7), 1)

    def testeAreaTetraedro(self):
        self.assertAlmostEqual(692.82, Formas.areaTetraedro(20), 1)
        self.assertAlmostEqual(140.29, Formas.areaTetraedro(9), 1)

    def testeVolumeTetraedro(self):
        self.assertAlmostEqual(3181.98, Formas.volumeTetraedro(30), 1)
        self.assertAlmostEqual(0.94, Formas.volumeTetraedro(2), 1)

    def testeVolumeCilindro(self):
        self.assertAlmostEqual(56548.66, Formas.volumeCilindro(30,20), 1)
        self.assertAlmostEqual(1407.43, Formas.volumeCilindro(8,7), 1)

    def testeAreaRetangulo(self):
        self.assertAlmostEqual(600.0, Formas.areaRetangulo(20,30), 1)
        self.assertAlmostEqual(16.0, Formas.areaRetangulo(8,2), 1)
