# Установка и активация Windows10 и Microsoft Office.

## Установка

### Office
1. Для установки образа Microsoft Office [https://disk.yandex.ru/d/RXhFA60jXgRkfg](ru и eng версии).

2. После установки нужно нажать на файл .iso правой кнопкой мыши и подколючить образ.

3. Запустить файл setup.exe и разрешить ему вносить изменения на устройстве.

4. Активировать Office через `PowerShell` как показано ниже.

### Windows
1. Для установки образа Windows10 [https://disk.yandex.ru/d/RXhFA60jXgRkfg]

2. Здесь не будет полного гайда на установку Windows10, просьба обратиться к другим источникам.

3. Активировать Office через `PowerShell` как показано ниже.

---

## Активация Windows / Office?

1. Нажмите **Пуск**, введите `PowerShell` и откройте его.

2. Скопируйте и вставьте код ниже, затем нажмите **Enter**.

   **Для Windows 8.1, 10 и 11:**

   ```powershell
   irm https://get.activated.win | iex
   ```
   Если команда выше заблокирована (ISP/DNS), попробуйте эту(работает на Windows 10 или 11)
   
   ```powershell
   iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
   ```

3. В появившемся меню выберите нужный вам номер.

>Информация взята с репозитория Microsoft Activation Scripts (MAS) [https://github.com/GordeyGudim/activatewin/blob/main/README.md#способ-1---powershell-%EF%B8%8F] и поста на Дзен [https://dzen.ru/a/ZXKy7V_d5C72Ghn7]
