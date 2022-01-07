import math

class Formas:
  def areaCirculo(double raio):
    return math.pow(raio, 2) * math.pi()

  def volumeEsfera(double raio):
    return (4/3) * math.pi() * math.pow(raio, 3)

  def areaQuadrado(double lado):
    return lado*lado

  def volumeCubo(double lado):
    return lado*lado*lado

  def areaTriangulo(double base, double altura):
    return (base*altura)/2

  def volumePiramide(double base, double altura):
    return  (math.pow(base, 2) * altura)/3

  def areaTetraedro(double aresta):
    return (math.pow(aresta,2) * math.sqrt(3))

  def volumeTetraedro(double aresta):
    return (math.pow(aresta,3) * math.sqrt(2))/12

  def volumeCilindro(double raio, double altura):
    return math.pow(raio,2) * math.pi() * altura

  def areaRetangulo(double base, double altura):
    return base*altura