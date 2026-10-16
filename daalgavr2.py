
catalog = {
    "P001": {
        "name": "Нөүтбүүк",
        "category": "электроник",
        "specs": (3500000, 4.7),
        "tags": {"gaming", "wireless", "rgb", "өндөр хүчин чадалтай"}
    },
    "P002": {
        "name": "Утасгүй хулгана",
        "category": "электроник",
        "specs": (80000, 4.5),
        "tags": {"gaming", "wireless", "bluetooth", "оффис"}
    },
    "P003": {
        "name": "Механик гар",
        "category": "электроник",
        "specs": (250000, 4.9),
        "tags": {"gaming", "rgb", "оффис"}
    },
    "P004": {
        "name": "Сандал",
        "category": "тавилга",
        "specs": (600000, 4.3),
        "tags": {"оффис", "тухтай"}
    }
}


def filter_by_tags(catalog, preferred_tags, min_match_count):
    result = []

    for product_id, product in catalog.items():
        common = preferred_tags.intersection(product["tags"])

        if len(common) >= min_match_count:
            result.append(product_id)

    result.sort(key=lambda product_id: catalog[product_id]["specs"][1], reverse=True)

    return result


def find_price_range_items(catalog, price_range_tuple):
    min_p, max_p = price_range_tuple
    result = []

    for product_id, product in catalog.items():
        price = product["specs"][0]

        if min_p <= price <= max_p:
            result.append(product_id)

    return result


def get_common_tags_in_category(catalog, category_name):
    common_tags = set()
    first = True

    for product in catalog.values():
        if product["category"] == category_name:
            if first:
                common_tags = product["tags"].copy()
                first = False
            else:
                common_tags = common_tags.intersection(product["tags"])

    return common_tags


if __name__ == "__main__":
    print("--- Таг шүүх ---")
    print(filter_by_tags(catalog, {"gaming", "rgb"}, 2))

    print("\n--- Үнийн хязгаар шүүх ---")
    print(find_price_range_items(catalog, (50000, 500000)))

    print("\n--- Нийтлэг таг шүүх ---")
    print(get_common_tags_in_category(catalog, "электроник"))
