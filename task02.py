from pathlib import Path

def get_cats_info(path):
    file_path = Path(path)

    if not file_path.exists():
        print(f"Файл не знайдено: {path}")
        return []

    try:
        cats_list = []         

        with file_path.open(encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue 
                try:
                    cat_id, name, age = line.split(',')
                    cats_list.append({
                        "id": cat_id.strip(), 
                        "name": name.strip(), 
                        "age": age.strip()
                    })                     
                except ValueError:
                    print(f"Помилка обробки рядка: `{line}` - пропущено")
                    continue

    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
        return []

    
    # return cats_list  -   якщо без форматування списку словників, що повертається
    formatted_cats_list = ["["]      
    for cat in cats_list:
        formatted_cats_list.append(
            f"""{{"id": "{cat["id"]}", "name": "{cat["name"]}", \n"age": "{cat["age"]}"}},"""
        )    
    formatted_cats_list.append("]") 
    return "\n".join(formatted_cats_list) 

cats_info = get_cats_info("cats_file.txt")
print(cats_info)