print("Tester: Irene Noer Ramadhany")
print("NIM   : 235150207111064")

print("\nTEST 1: EP & BVA TEST")

test_duration = [0,1,2,3,4,5]

for d in test_duration:
    if 1 <= d <= 4:
        print("Duration", d, "jam DITERIMA")
    else:
        print("Duration", d, "jam DITOLAK")

print("\nTEST 2: DECISION TABLE TEST")

def booking(mahasiswa, pelanggaran, ruang):
    if not mahasiswa:
        return "DITOLAK TIDAK TERDAFTAR"
    elif not pelanggaran:
        return "DITOLAK MEMILIKI PELANGGARAN"
    elif not ruang:
        return "DITOLAK RUANG TIDAK TERSEDIA"
    else:
        return "BOOKING BERHASIL"

test_cases = [
    (True, True, True),
    (False, True, True),
    (True, False, True),
    (True, True, False)
]

for tc in test_cases:
    print(tc, booking(*tc))

print("\nTEST 3: STATE TRANSITION TEST")

transitions = [
    ("AVAILABLE", "Booking", "BOOKED"),
    ("BOOKED", "Check-in", "IN_USE"),
    ("IN_USE", "Selesai", "FINISHED"),
    ("AVAILABLE", "Check-in", "INVALID"),
]

for t in transitions:
    print(t[0], t[1], t[2])