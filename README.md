# Активация при помощи Microsoft Activation Scripts (MAS)

Открытый активатор Windows и Office, включающий методы HWID, Ohook, TSforge и Online KMS, а также расширенное устранение неполадок.

---

## Как активировать Windows / Office / Extended Security Updates (ESU)?

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

>Информация взята с репозитория Microsoft Activation Scripts (MAS) [https://github.com/GordeyGudim/activatewin/blob/main/README.md#способ-1---powershell-%EF%B8%8F]
