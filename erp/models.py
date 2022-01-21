from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=200)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']


class Product(models.Model):
    # Relations
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # Attributes
    name = models.CharField(verbose_name='Nombre', max_length=200)
    image = models.ImageField(
        verbose_name='Imagen', upload_to='avatar/%Y/%M/%D', null=True, blank=True,
    )
    pvp = models.CharField(verbose_name='PVP', max_length=50)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    last_names = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=11, verbose_name='CI', unique=True)
    born_date = models.DateField(verbose_name='Fecha de Nacimiento')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    sexo = models.CharField(verbose_name='Sexo', max_length=30)

    def __str__(self) -> str:
        return str(self.names)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Purchase(models.Model):
    # Relations
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # Attributes
    sold_at = models.DateTimeField(verbose_name='Fecha de Venta')
    subtotal = models.DecimalField(
        verbose_name='Subtotal', default=0.0, max_digits=16, decimal_places=2
    )
    total = models.DecimalField(
        verbose_name='Total', default=0.0, max_digits=16, decimal_places=2
    )

    def __str__(self) -> str:
        return f'client: {self.client} / {self.subtotal}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class PurchaseProducts(models.Model):
    # Relations
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    # Attributes
    amount = models.IntegerField(verbose_name='Cantidad',)
    subtotal = models.DecimalField(
        verbose_name='Subtotal', default=0.0, max_digits=16, decimal_places=2
    )
    price = models.DecimalField(
        verbose_name='Precio', default=0.0, max_digits=16, decimal_places=2
    )

    def __str__(self) -> str:
        return f'subtotal: {self.subtotal} / {self.amount}'

    class Meta:
        verbose_name = 'VentaProducto'
        verbose_name_plural = 'VentaProductos'
        ordering = ['id']

