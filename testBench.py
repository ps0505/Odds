from devigger_helper import devig_cno_api

def main():
    sharp_odds = input('Enter the sharp odds separated by slashes (ex. 120/340/200/500/...): ')
    desired_book_odds = input('Enter the desired book odds separated by slashes (ex. 120/340/200/500/...): ')
    # assuming the amounts are the same. so each odd is 1 to 1. don't need identifiers on the odds.
    arr_sharp = sharp_odds.split('/')
    arr_desired_book = desired_book_odds.split('/')

    res = []
    for index, desired_book_odd in enumerate(arr_desired_book):
        out = arr_sharp[index:] + arr_sharp[:index] # each one is the specific ordering based on individual odd
        out = '/'.join(out)
        res.append(devig_cno_api(desired_book_odd, out))
    
    # need to format results with helper function
    print(res) # for now will print results and not handle errors
    
if __name__ == '__main__':
    main()