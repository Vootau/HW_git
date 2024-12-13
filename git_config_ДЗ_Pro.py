import subprocess


def git_config_list():
    # Создаём список аргументов для команды 'git'
    command = ['git', 'config', '--global', '--list']

    # Выполняем команду с помощью subprocess.run и сохраняем результат
    result = subprocess.run(command, capture_output=True, text=True)

    # Проверка успешности выполнения команды
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f'Ошибка при выполнении команды: {result.stderr}')


if __name__ == '__main__':
    git_config_list()