




$(document).ready(function(){


	// Add to cart 
	$(document).on('click', ".add-to-cart", function(){

		var _vm=$(this);
		var _index=_vm.attr('data-index');
		var _qty=$(".product-qty-"+_index).val();
		var _productId=$(".product-id-"+_index).val();
		var _productImage=$(".product-image-"+_index).val();
		var _productTitle=$(".product-title-"+_index).val();
		var _productPrice=$(".product-price-"+_index).text();

		console.log(_qty,_productId,_productTitle);

		// Ajax Start 
		$.ajax({

			url: '/add-to-cart',
			data:{
				'id':_productId,
				'image':_productImage,
				'qty':_qty,
				'title':_productTitle,
				'price':_productPrice,
			},
			dataType: 'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$("cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
			}
		}); 
	});


	// Delete item cart 
	$(document).on('click', '.delete-item', function(){

		var _pId=$(this).attr('data-item');
		var _vm=$(this);
		
		// Ajax Start 
		$.ajax({

			url: '/delete-cart-item',
			data:{
				'id':_pId,		
			},
			dataType: 'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
				$("#cartList").html(res.data);
			}
		}); 
	});


	// Update item cart 
	$(document).on('click', '.update-item', function(){
		var _pId=$(this).attr('data-item');
		var _pQty=$(".product-qty-"+_pId).val();
		var _vm=$(this);
		// Ajax Start 
		$.ajax({
			url: '/update',
			data:{
				'id':_pId,	
				'qty':_pQty,	
			},
			dataType: 'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				//$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
				$("#cartList").html(res.data);
			}
		}); 
	});


}); 