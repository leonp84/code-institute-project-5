# Shopping Bag context

def shopping_bag(request):
    '''
    This context view returns the number of items currently in the users
    shopping bag to enable accurate display in the shopping bag icon of the
    header of base.html. It does this by retrieving the users shopping bag
    from the django session variable 'shopping_bag'. See
    product.views.product_details and checkout.views.shopping_bag for details.
    '''
    shopping_bag = request.session.get('shopping_bag', {})
    context = {'items_in_shopping_bag': sum(shopping_bag.values())}
    return context
