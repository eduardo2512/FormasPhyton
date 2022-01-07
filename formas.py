import math

class Formas:
  def areaCirculo(raio):
    return math.pow(raio, 2) * math.pi

  def volumeEsfera(raio):
    return (4/3) * math.pi * math.pow(raio, 3)

  def areaQuadrado(lado):
    return lado*lado

  def volumeCubo(lado):
    return lado*lado*lado

  def areaTriangulo(base, altura):
    return (base*altura)/2

  def volumePiramide(base, altura):
    return  (math.pow(base, 2) * altura)/3

  def areaTetraedro(aresta):
    return (math.pow(aresta,2) * math.sqrt(3))

  def volumeTetraedro(aresta):
    return (math.pow(aresta,3) * math.sqrt(2))/12

  def volumeCilindro(raio, altura):
    return math.pow(raio,2) * math.pi * altura

  def areaRetangulo(base, altura):
    return base*altura