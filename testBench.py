def main():
    sharp_odds = input('Enter the sharp odds separated by slashes (ex. 120/340/200/500/...): ')
    devig_book_odds = input('Enter the devig book odds separated by slashes (ex. 120/340/200/500/...): ')
    # assuming the amount is the same. so each odd is 1 to 1. don't need identifiers on the odds.
    arr_sharp = sharp_odds.split('/')
    arr_devig = devig_book_odds.split('/')


    for index, individualOdd in enumerate(arr_devig):
        out = []
        for j in range(len(arr_sharp)):
            if j == index:
                out.insert(0,arr_sharp[j])
            else:
                out.append(arr_sharp[j])
        print(individualOdd)
        print(out)








if __name__ == '__main__':
    main()