from .models import MenuItem

def main_menu(request):
    top = MenuItem.objects.filter(parent=None)
    menu = [{"item":i, "children":i.children.all()} for i in top]

    return {"main_menu":menu}
