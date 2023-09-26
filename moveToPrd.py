import sys
import subprocess

# Проверяем, передан ли аргумент с тегом
if len(sys.argv) != 2:
    print("Пожалуйста, укажите имя тега.")
    sys.exit(1)

# Получаем имя тега из аргумента командной строки
tag_name = sys.argv[1]

# Переключаемся на ветку dev
subprocess.run(['git', 'checkout', 'dev'])

# Получаем последний коммит в ветке dev
result = subprocess.run(['git', 'log', '--format=%H', '-n', '1'], stdout=subprocess.PIPE)
latest_commit = result.stdout.decode().strip()

# Переносим изменения в ветку prd
subprocess.run(['git', 'checkout', 'prd'])
subprocess.run(['git', 'merge', latest_commit])

# Устанавливаем указанный тег
subprocess.run(['git', 'tag', tag_name])

# Переключаемся обратно на ветку dev
subprocess.run(['git', 'checkout', 'dev'])

print(f'Перенесено ветку dev в prd с тегом {tag_name}')
