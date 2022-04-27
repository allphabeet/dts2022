
# Menu

answer={"Ya","yes","YES","YEs","Yes","ya","yES","yeS","YA"}
result = {
}

def menu():
        print("===============================================")
        print("            Aplikasi Perhitungan BMI           ")
        print("===============================================")
        print("Main Menu :")
        print("1.Menghitung Berat Badan Ideal")
        print("2.Menampilkan Hasil Berat Badan")
        print()


def sub_menu_1():
        print("===============================================")
        print("            Aplikasi Perhitungan BMI           ")
        print("===============================================")
        print("Menampilkan Hasil Berat Badan :")
        print("1.Tampilkan Hasil Berat Badan Ideal Perorang")
        print("2.Tampilkan Semua Hasil Berat badan yg tersimpan")
        print("3.Kembali ke Menu Utama")
        print()


    


# Operation



def menu_loop():
    loop = True
    while loop:
        menu=int(input("Masukkan Pilihan Anda: "))
        if menu == 1:
            loop = True
            
            print()
            nama = str(input("Masukkan nama anda: "))
            berat=float(input("Masukkan berat badan anda (kg): "))
            tinggi=float(input("Masukkan tinggi badan anda (cm): "))
            tinggi = tinggi/100
            bmi = berat / (tinggi**2)
            print()
            if bmi >25 and bmi< 22.9:
                print ("Berat badan anda saat ini dalam kondisi OVERWEIGHT")
            elif bmi < 18.5:
                print("Berat badan anda saat ini dalam kondisi UNDERWEIGHT")
            elif bmi >18.5 and bmi <24.9:
                print("Berat badan anda NORMAL")
            elif bmi > 30:
                print("Anda mengalami OBESITAS")

            print()
            print("===============================================")
            print("Apakah anda akan menyimpan hasil? Yes or No") 
            simpan = str(input())
            if simpan not in answer:
                print()
                print("Data tidak tersimpan")
                break
            else:
                result.update({nama:bmi})
                print()
                print("Hasil anda sudah berhasil tersimpan")
            break
        
        elif menu == 2:
            loop = True
            sub_menu_1()
            pilihan2 = int(input("Masukkan pilihan anda: "))
            if pilihan2 == 1:
                nama_menu2 = str(input("Masukkan nama anda: "))
                print(f"Hasil anda sebelumnya {result[nama_menu2]}")
                if result[nama_menu2] >25 and result[nama_menu2]< 22.9:
                    print ("Status berat anda sebelumnya: OVERWEIGHT")
                elif result[nama_menu2] < 18.5:
                    print("Status berat anda sebelumnya: UNDERWEIGHT")
                elif result[nama_menu2] >18.5 and result[nama_menu2] <24.9:
                    print("Status berat anda sebelumnya: NORMAL")
                elif result[nama_menu2] > 30:
                    print("Status berat anda sebelumnya: OBESITAS")
                loops()
                break
            elif pilihan2 == 2:
                print(result)
                break
            else:
                menu()





            

def loops():

    loop = True
    gender={
        1:"Pria",
        2:"Wanita"
    }
    while loop:
        print()
        print("===============================================")
        jawaban = str(input("Perlu Mengulang? Yes or No? : "))
        if jawaban not in answer:
        
            loop = False
            break
        else:
        
            loop = True
            menu()
            print()
            menu_loop()

menu()
menu_loop()
loops()

