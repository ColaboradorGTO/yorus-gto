from django.db import models
from stdimage.models import StdImageField
from django.utils.text import slugify

# Create your models here.

class Offer(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	image = StdImageField('Imagem', upload_to='Offer', variations={'thumb': {'width': 423, 'height': 681, 'crop': True }}) 
	title = models.CharField('Título', max_length=255)
	description = models.TextField('Descrição', max_length=300)
	discount = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	def discount(self):
	    return self.discount

	class Meta:
	    verbose_name = 'Oferta'
	    verbose_name_plural = 'Ofertas'    	


class Category(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	image = StdImageField('Imagem', upload_to='Category', variations={'thumb': {'width': 250, 'height': 250, 'crop': True }}) 
	title = models.CharField('Título', max_length=255)
	 
	def __str__(self):
		return self.title 

	class Meta:
	    verbose_name = 'Categoria'
	    verbose_name_plural = 'Categorias'	


class Brand(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	image = StdImageField('Imagem', upload_to='Brand', variations={'thumb': {'width': 295, 'height': 295, 'crop': True }}) 
	title = models.CharField(max_length=255)
	# image 

	def __str__(self):
		return self.title 


class Color(models.Model):
	title = models.CharField(max_length=255)
	color_code = models.CharField(max_length=255)
	#price = models.IntegerField()

	def __str__(self):
		return self.title 


class Size(models.Model):
	title = models.CharField(max_length=255)
	#price = models.IntegerField()
	# image 

	def __str__(self):
		return self.title 		


class Product(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) 
	title = models.CharField(max_length=255)
	subtitle =  models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(max_length=255, unique=True, null=True, blank=True,)
	price = models.IntegerField()
	image1 = StdImageField('01. Imagem', upload_to='Product', variations={'thumb': {'width': 460, 'height': 597, 'crop': True }}) 
	image2 = StdImageField('02. Imagem', upload_to='Product', null=True, blank=True, variations={'thumb': {'width': 460, 'height': 597, 'crop': True }})
	image3 = StdImageField('03. Imagem', upload_to='Product', null=True, blank=True, variations={'thumb': {'width': 460, 'height': 557, 'crop': True }})
	image4 = StdImageField('04. Imagem', upload_to='Product', null=True, blank=True, variations={'thumb': {'width': 460, 'height': 597, 'crop': True }})
	image5 = StdImageField('05. Imagem', upload_to='Product', null=True, blank=True, variations={'thumb': {'width': 460, 'height': 597, 'crop': True }})
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True) 
	stock = models.IntegerField(default=1) 
	# Featuring  

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'

	def save(self, *args, **kwargs):
		value = f'{self.title}, {self.subtitle}, {self.id}' 
		self.slug = slugify(value, allow_unicode=False)
		super().save(*args, **kwargs)


		
		 


	# Usar esse módulo para calcular fretes e cupons 
	def get_product_price_by_size(self, size):
	    return self.price + SizeVariant.objects.get(size_name = size).price	


class ProductAttribute(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	color = models.ForeignKey(Color, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	price = models.IntegerField()

	def __str__(self):
		return self.product.title


	class Meta:
	    verbose_name = 'Atributo'
	    verbose_name_plural = 'Atributos'	 