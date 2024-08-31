import json

class Category:
    def __init__(self, name, subcategories):
        self.name = name
        self.subcategories = subcategories

    @classmethod
    def from_json(cls, data):
        categories = []
        for item in data:
            category = cls(item['name'], item['subcategories'])
            categories.append(category)
        return categories

    def __repr__(self):
        return f"Category(name={self.name}, subcategories={self.subcategories})"

json_data = [
    {
        "name": "Category1",
        "subcategories": [
            "subcategory11",
            "subcategory12",
            "subcategory13",
            "subcategory14",
        ]
    },
    {
        "name": "Category2",
        "subcategories": [
            "subcategory21",
            "subcategory22",
            "subcategory23",
            "subcategory24",
        ]
    },
    {
        "name": "Category3",
        "subcategories": [
            "subcategory31",
            "subcategory32",
            "subcategory33",
            "subcategory34",
        ]
    },
    {
        "name": "Category4",
        "subcategories": [
            "subcategory41",
            "subcategory42",
            "subcategory43",
            "subcategory44",
        ]
    },
]




    
def getCategories(data):
    print("Введите слово 'exit' для выхода")
    print("-----------------------------")
    categories = Category.from_json(data)
    
    for i in range(len(categories)):
        print(f"{i + 1}: {categories[i].name}")
    
    while True:
        temp_data = input("Выберите номер категории: ")
        
        if temp_data.lower() == "exit":
            print("Вы успешно вышли из функции")
            break

        if not temp_data.isdigit():
            print("Ошибка: Пожалуйста, введите корректный номер категории.")
            continue

        selected_category = int(temp_data)
        
        if 1 <= selected_category <= len(categories):
            print(f"Подкатегории для {categories[selected_category - 1].name}:")
            for j, subcategory in enumerate(categories[selected_category - 1].subcategories, start=1):
                print(f"{j}: {subcategory}")
        else:
            print("Ошибка: Пожалуйста, введите корректный номер категории.")
        
        print("-----------------------------")
        
getCategories(json_data) 