## ТЗ “I-Bank” Часть-2 "История операций"

Дополнение к документу “ТЗ I-Bank Часть-1”


### Доработки

1. Необходимо добавить возможность просмотра всей **истории операций** над счетом клиента(поступление, снятие, переводы)

### Формат вывода истории:

**Пополнение** **600** руб. \
**Снятие** **400** руб. \
**Пополнение** **1000** руб. \
**Перевод** **750** руб. на счет клиента: **Петр** \
**Поступление** **300** руб. со счета клиента: **Александр** \
...

**Жирным** выделена информация, которая _обязательно_ должна присутствовать в строковом представлении истории операций.
Типы операций должны именоваться именно этими терминами: "Пополнение", "Снятие", "Перевод" и "Поступление".

**_Обратите внимание!_** Операция "перевод другому клиенту" создает две операции:
1. Операцию "**Перевод**", на счету отправителя
2. Операцию "**Поступление**", на счету получателя

### Правило реализации

Информацию о каждой операции (пополнение, снятие и т.д.) храним в виде отдельного объекта(см. `results/iBank_part2.py`)