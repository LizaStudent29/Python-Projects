import subprocess

# Переключаемся на ветку dev
subprocess.run(['git', 'checkout', 'dev'])

# Получаем последний коммит в ветке dev
result = subprocess.run(['git', 'log', '--format=%H', '-n', '1'], stdout=subprocess.PIPE)
latest_commit = result.stdout.decode().strip()

# Переносим изменения в ветку prd
subprocess.run(['git', 'checkout', 'prd'])
subprocess.run(['git', 'merge', latest_commit])

# Устанавливаем тег для ревизии
tag_name = 'release-1.0'  
subprocess.run(['git', 'tag', tag_name])

# Переключаемся обратно на ветку dev
subprocess.run(['git', 'checkout', 'dev'])

print(f'Перенесено ветку dev в prd с тегом {tag_name}')

