def shopping_bag(request):
    shopping_bag = request.session.get('shopping_bag', {})
    context = {'items_in_shopping_bag': sum(shopping_bag.values())}
    return context
