# FAIR EUN aLGO POUR LE SITE Ecomerce 
# Contrainte 
# 1.  On ne vend pas plus de 2
# 2. Vendre l'article Dispo seulment

products = [
    {
     "name": "StarlinkMini", 
     "price": 145000,
     "quantity": 15 
    },
      {
     "name": "Iphone17", 
     "price": 745000,
     "quantity": 12 
    }
]

# parcourir 
def traier_product(nom_produit, qty_demande):

    product_trouve = False

    for product in products:
        if product['name'] == nom_produit:
            product_trouve = True 
            print(f" Tentative d'achat: {qty_demande} * {product['name']} " )

            # Contrainte 1 
            if qty_demande > 5:
                print(f"ERREUR : Limite de 2 article par client atteinte.")
                return

            # Contrainte 2 : Vendre suelment si disponible 
            if product['quantity'] == 0:
                print("Erreur : Produit en RUPTURE de Stock")
            elif product['quantity'] < qty_demande:
                print(f"Erreur : Quantité demandée ({qty_demande}) supérieure au stock disponible ({product['quantity']}).")
            else:
                # Effectuer la vente 
                product['quantity'] = product["quantity"] - qty_demande
                total = product['price'] * qty_demande
                print(f"Achat réussi : {qty_demande} * {product['name']} pour un total de {total} FCFA.")
                print(f"Stock restant de {product['name']}: {product['quantity']} unités.")
            break

traier_product("StarlinkMini", 2)
traier_product("Iphone17", 3)