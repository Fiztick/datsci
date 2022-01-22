#  Import Class User di Folder basic
from basic.users import User

#  Import Functions di Folder basic
from basic.methodbase import biodata

def main():
    datas = [
        1, 2, 3, 4, 6, 7, 1, 3, 40, 100, 312, 3125, 64, 21
    ]

    users = User(keys = 3)
    result = users.pertambahan(datas)

    random_result = users.random_max(datas)

    return result, random_result

if __name__ == '__main__':
    result_pertambahan, result_random = main()
    
    # for i, hasil in enumerate(result_pertambahan):
    #     print(hasil["bagus"])

    # bio = biodata()    

    # for i, baris in enumerate(bio):
    #     print((i + 1), "|", baris["nama"], "|", baris["alamat"])

    #     # for key in baris:
    #     #     print(key, "=", baris[key])

    for baris in result_random:
        print(baris)
