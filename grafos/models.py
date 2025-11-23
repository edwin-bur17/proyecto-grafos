from django.db import models

class Pasillo(models.Model):
    """Modelo que representa un pasillo de la tienda."""
    nombre = models.CharField(max_length=100, unique=True)
    nivel_congestion = models.FloatField(default=0.0)  # 0.0 a 1.0
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Pasillo"
        verbose_name_plural = "Pasillos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    """Modelo que representa una categoría de productos en la tienda."""
    nombre = models.CharField(max_length=100)
    padre = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        related_name='hijos', 
        on_delete=models.CASCADE
    )
    pasillo = models.ForeignKey(
        Pasillo,
        null=True,
        blank=True,
        related_name='categorias',
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Modelo que representa un producto disponible en la tienda."""
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, 
        related_name='productos', 
        on_delete=models.CASCADE
    )
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    stock = models.IntegerField(default=0)
    imagen_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.marca})"

