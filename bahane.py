#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otomatik Bahane Üreticisi
Hiçbir şey yapmamak için en bilimsel gerekçeleri üretir.
"""

import random
import time

bahaneler = [
    "Kuantum durumum şu anda süperpozisyon halinde, hem yapıyorum hem yapmıyorum. Gözlemleyene kadar karar veremiyorum.",
    "Termodinamik kanunlarına göre entropi artıyor, ben de bu artışa katkıda bulunuyorum. İş yaparsam evrenin ısı ölümünü geciktirmiş olurum, bu da etik değil.",
    "Beyin dalgalarım şu anda theta frekansında, bu durumda yapılan işler geçersiz sayılıyor (kendi kendime çıkardığım yasa).",
    "İnternet bağlantım var ama motivasyon bağlantım yok. DNS çözümlemesi başarısız.",
    "Bugün ayın 8'i, 8 sayısı sonsuzluğu temsil eder, yani iş bitmez. O yüzden başlamamak daha mantıklı.",
    "Kedi yatağımın üstünde uyuyor. Onu uyandırmak evrensel bir suçtur.",
    "Çay demlenmedi. Çaysız iş yapmak anayasaya aykırı olabilir (emin değilim ama kontrol etmedim).",
    "Rastgele sayı üreticim bugün çok yorgun, o yüzden ben de yoruldum."
]

def bahane_uret():
    print("Bahane üretiliyor... Lütfen bekleyin, bu işlem çok yoğun.")
    for i in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print()
    secilen = random.choice(bahaneler)
    print(f"\n🎯 Bugünkü resmi bahaneniz:\n{secilen}\n")
    print("Bu bahane %100 bilimsel olarak onaylanmıştır (onaylayan: ben).")

if __name__ == "__main__":
    print("=" * 50)
    print("OTOMATİK BAHANE ÜRETİCİSİ v1.0")
    print("Hiçbir şey yapmama konusunda lider")
    print("=" * 50)
    bahane_uret()
    print("\nİşiniz bitti mi? Hayır. Ama bahaneniz hazır. Kolay gelsin.")
