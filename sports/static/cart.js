$(document).ready(function() {

    var cart = {

        cartData: [],

        addProduct: function (id, name, price) {
            var addedToExistingItem = false;
            for (var i = 0; i < this.cartData.length; i++) {
                if (this.cartData[i].id == id) {
                    this.cartData[i].count++;
                    addedToExistingItem = true;
                    break;
                }
            }
            if (!addedToExistingItem) {
                this.cartData.push({
                    count: 1, id: id, price: price, name: name
                });
            }
            return addedToExistingItem;
        },

        removeProduct: function (id) {
            for (var i = 0; i < this.cartData.length; i++) {
                if (this.cartData[i].id == id) {
                    this.cartData.splice(i, 1);
                    break;
                }
            }
        },

        getItem: function(id) {
            var item;
            for (var i = 0; i < this.cartData.length; i++) {
                if (this.cartData[i].id == id) {
                    item = this.cartData[i];
                    break;
                }
            }
            return item;
        },

        getProducts: function () {
            return this.cartData;
        },

        total: function () {
            var total = 0;
            for (var i = 0; i < this.cartData.length; i++) {
                total += (this.cartData[i].price * this.cartData[i].count);
            }
            return total;
        },

        itemCount: function () { // returns number of order items
            var total = 0;
            for (var i = 0; i < this.cartData.length; i++) {
                total += this.cartData[i].count;
            }
            return total;
        },

        reset: function() {
            this.cartData = [];
        }
    };

    $(document).data('cart', cart);

    $('a.add-item').click(function() {
        var jqLink = $(this);
        var jqTd = jqLink.closest('td');
        var jqPrice = jqTd.prev();
        var price = jqPrice.text();
        var jqName = jqPrice.prev().prev().prev();
        var name = jqName.text();
        var jqId = jqName.prev();
        var id = jqId.text();

        var addedToExistingItem = cart.addProduct(id, name, price);

        var item = cart.getItem(id);
        var quantity = item.count;
        var subTotal = quantity * price;

        var tbody = $('#cart-summary-tbody');
        if (!addedToExistingItem) {

            var tr = $('<tr></tr>').attr('data-item-id', id);
            var td1 = $('<td class="text-center"></td>').text(quantity);
            var td2 = $('<td class="text-left"></td>').text(name);
            var td3 = $('<td class="text-right"></td>').text('$' + price);
            var td4 = $('<td class="text-right"></td>').text('$' + subTotal);
            var td5 = $('<td class="text-right"><button type="button" onclick="removeItem(this)" class="btn btn-sm btn-warning">Remove</button></td>');

            tr.append(td1, td2, td3, td4, td5);
            tbody.append(tr);

        } else {
            var jqTr = $('tr[data-item-id="' + id + '"]');
            var jqQuantity = jqTr.children().first().text(quantity);
            var jqSubtotal = jqQuantity.next().next().next().text('$' + subTotal);
        }

        setCartSummary(cart);
    });

    $('#cart-checkout').click(function() {
        var items = cart.getProducts();
        if(items.length == 0) {
            alert('No items in your cart so far!')
        } else {

            $('#header-row').hide();
            $('#product-list').hide();
            $('#place-order').hide();

            var total = cart.total();
            $('#cart-summary-total').text('$' + total);

            $('#cart-summary').show();
        }
    });

    $('#continue-shopping').click(function() {
        $('#cart-summary').hide();

        $('#header-row').show();
        $('#product-list').show();
    });

    $('#show-place-order').click(function() {
        $('#cart-summary').hide();

        $('#header-row').show();
        $('#order-form').trigger("reset"); // to reset the form
        $('#place-order').show();

        // 1st input element is not focused now, so focus it again
        $('input:text:first').focus();
    });

    $('#order-form').submit(function(event) {

        // prevent form submission because it's Ajax call
        event.preventDefault();

        var formData = $('#order-form').serializeArray();
        var items = cart.getProducts();

        var postData = {'items': items};
        $(formData).each(function(index, v) {
            postData[v.name] = v.value;
        });
        console.log(postData);

        $.post('/order', postData, function(data, textStatus, jqXHR) {
            var orderNo = data.orderNo;
            console.log('orderNo: ' + orderNo);

            $('#place-order').hide();

            cart.reset();
            setCartSummary(cart);
            $('tr', '#cart-summary-tbody').remove();

            $('#order-no').text(orderNo);
            $('#order-completed').show();
            $('#to-catalogue').show();
        });
    });

    $('#to-catalogue').click(function() {
        $('#order-completed').hide();
        $('#to-catalogue').hide();
        $('#product-list').show();
    });
});


function setCartSummary(cart) {
    var itemCount = cart.itemCount();
    $('#cart-item-count').text(itemCount);
    var total = cart.total();
    $('#cart-total').text(total);
}

// Do not put the function below within $(document).ready()
function removeItem(btnEl) {
    var td = $(btnEl).closest('td');
    var tr = td.closest('tr');
    var id = tr.attr('data-item-id');

    console.log('Removing order item for product ID: ' + id);
    var cart = $(document).data('cart');
    var item = cart.getItem(id);
    var name = item.name;

    cart.removeProduct(id);
    tr.remove();
    console.log('Removed: ' + name);

    var total = cart.total();
    $('#cart-summary-total').text('$' + total);

    setCartSummary(cart);
}