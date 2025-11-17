def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def input_angka():
    global numbers
    n = int(input("Masukkan jumlah nilai tugas: "))
    numbers = []
    for i in range(n):
        number = int(input(f"Angka {i+1}: "))
        numbers.append(number)
    print("Input selesai. Kembali ke menu pilihan.")

def sorting():
    global numbers
    if not numbers:
        print("Tidak ada angka yang diinput.")
        return
    sorted_numbers = bubble_sort(numbers.copy())
    print("Hasil sorting : ", sorted_numbers)

def searching():
    global numbers
    if not numbers:
        print("Tidak ada angka yang diinput.")
        return
    search_value = int(input("Masukkan angka yang dicari : "))
    if search_value in numbers:
        print("Angka ditemukan")
    else:
        print("Angka tidak ditemukan")

def menu():
    while True:
        print("\nMENU PILIHAN")
        print("1. Input angka")
        print("2. Sorting")
        print("3. Searching")
        print("4. Selesai")
        choice = int(input("Masukkan pilihan [1/2/3/4] : "))

        if choice == 1:
            input_angka()
        elif choice == 2:
            sorting()
        elif choice == 3:
            searching()
        elif choice == 4:
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Global variable to store numbers
numbers = []

# Start the program
menu()