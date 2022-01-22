from basic.users import User


def main():
    datas = [
        1, 2, 3, 4, 6
    ]

    # test = [
    #     [1, 2, 3, 4],
    #     [1, 2, 3, 4],
    #     [1, 2, 3, 4],
    # ]
    

    users = User(keys = 3)
    result = users.pertambahan(datas)

    return result

if __name__ == '__main__':
    result_pertambahan = main()
    
    for i, hasil in enumerate(result_pertambahan):
        print(hasil)

    biodata = [
        {"nama": "bagus", "alamat": "depok"},
        {"nama": "mahesa", "alamat": "depok"},
        {"nama": "hafiz", "alamat": "depok"}
    ]

    for i, baris in enumerate(biodata):
        print(baris["nama"], "|", baris["alamat"])

        # for key in baris:
        #     print(key, "=" baris[key])
