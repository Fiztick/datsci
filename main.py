#  Import Class User di Folder basic
from basic.users import User

from basic.methodbase import biodata

def main():
    datas = [
        1, 2, 3, 4, 6
    ]

    users = User(keys = 3)
    result = users.pertambahan(datas)

    return result

if __name__ == '__main__':
    result_pertambahan = main()
    
    for i, hasil in enumerate(result_pertambahan):
        print(hasil["bagus"])

    bio = biodata()    

    for i, baris in enumerate(bio):
        print((i + 1), "|", baris["nama"], "|", baris["alamat"])

        # for key in baris:
        #     print(key, "=", baris[key])
