from pathlib import Path

def total_salary(path):
    file_path = Path(path)

    if not file_path.exists():
        print(f"Файл не знайдено: {path}")
        return 0, 0
    
    try: 
        total = 0
        count = 0

        with file_path.open(encoding='utf-8') as file: 
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary_str = line.split(',')
                    salary = float(salary_str)
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Помилка обробки рядка: '{line}` - пропущено")
                    continue

        if count == 0:
            return 0, 0

        average = total / count
        return total, average
    
    except Exception as e:
        print(f"Виникла помилка при читанні фалйлу: {e}")
        return 0, 0


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")