1. Transport vositalari tizimi
Shart: Transport vositalari uchun Vehicle nomli asosiy klass yarating. Undan voris oluvchi Car, Bicycle, va Truck klasslarini hosil qiling.

Vehicle klassi umumiy atributlarga ega bo‘lsin: name, speed.

Car, Bicycle, Truck klasslari har biri o‘ziga xos metodlarga ega bo‘lsin (honk(), load_cargo(), pedal()).

Ma’lumot: Masalan, Car obyektida honk() metodidan foydalansa, "Bip-bip!" degan natija chiqishi kerak.

2. Hayvonot bog‘i tizimi
Shart: Hayvonlarni ifodalovchi Animal nomli asosiy klass yarating. Undan voris oluvchi Lion, Eagle, va Shark klasslarini hosil qiling.

Animal klassida umumiy metodlar bo‘lsin (make_sound()).

Lion, Eagle, Shark klasslari make_sound() metodini o‘ziga xos tarzda o‘zgartirsin (roar(), screech(), splash()).

Ma’lumot: Masalan, Lion obyektida make_sound() metodini chaqirsak, natija "Roar!" bo‘lishi kerak.

3. Ishchilar boshqaruvi tizimi
Shart: Ishchilarni ifodalovchi Employee nomli asosiy klass yarating. Undan voris oluvchi Manager, Developer, va Designer klasslarini hosil qiling.

Employee klassida umumiy metod bo‘lsin: get_salary().

Manager, Developer, Designer klasslari har biri o‘zining alohida maosh hisoblash usuliga ega bo‘lsin.

Ma’lumot: Masalan, Developer klassining get_salary() metodi maoshni hourly_rate * hours_worked shaklida qaytarsin.

4. Onlayn do‘kon mahsulotlari
Shart: Product nomli asosiy klass yarating. Undan voris oluvchi Electronics, Clothing, va Food klasslarini hosil qiling.

Product klassi umumiy atributlarga ega bo‘lsin: name, price.

Electronics, Clothing, Food klasslari o‘ziga xos metodlarga ega bo‘lsin (apply_discount(), check_expiry()).

Ma’lumot: Masalan, Electronics klassida apply_discount() metodi mahsulot narxidan 10% chegirma hisoblasin.

5. Bank hisoblari tizimi
Shart: BankAccount nomli asosiy klass yarating. Undan voris oluvchi SavingsAccount va CheckingAccount klasslarini hosil qiling.

BankAccount klassi umumiy atributlarga ega bo‘lsin: balance.

SavingsAccount, CheckingAccount klasslari withdraw() metodini har xil ishlasin (cheklovlar bilan).

Ma’lumot: Masalan, SavingsAccount klassida withdraw() metodi faqat hisobda yetarlicha mablag‘ bo‘lsa ishlasin.
