from devigger_helper import devig_cno_api
import re

def main():
    # target_book_odds = '120/340/200/500'
    # sharp_odds = '120/399/231/400, 123/305/420/112'
    target_book_odds = input('Enter the target book odds separated by slashes (ex. 120/340/200/500/...): ')
    sharp_odds = input('Enter the sharp odds separated by slashes. If multiple, separate by commas: ')
    # assuming the number of events being compared are the same
    # so each odd is 1 to 1. don't need identifiers on the odds.
    arr_target_book = target_book_odds.split('/')
    arr_sharp = re.split(r',\s*', sharp_odds) # separates all sets of odds and strips whitespace

    results = []
    for index, target_book_odd in enumerate(arr_target_book):
        holder = ''
        for element in arr_sharp:
            temp = element.split('/')
            temp = temp[index:] + temp[:index]
            holder = holder + ', ' + '/'.join(temp)
        final_string = 'avgb(' + holder[2:] + ')'
        results.append(devig_cno_api(target_book_odd, final_string))

    for res in results:
        if res['success']:
            data = res['data']
            if data['ev_percentage'] < 0:
                print(f'Target Leg {data['final_odds']} is Negative EV {data['ev_percentage_formatted']} {data['fair_value_odds_formatted']}\n')
            else:
                print(f'Sharp Leg ({data['leg1_odds']}); Market Juice = {data['market_juice_percentage_formatted']}; Fair Value = {data['fair_value_odds_formatted']} ({data['fair_value_percentage_formatted']})')
                print(f'Target (Final) Odds ({data['final_odds']})')
                print(f'Summary; EV% = {data['ev_percentage_formatted']}, Kelly Units = {data['kelly_quarter_unit']:.2f}u, Kelly Wager = ${data['kelly_wager']:.2f} (FB = {data['fb_percentage_formatted']})\n')
        else:
            print(f'Error: {res['error']}\n')
    
if __name__ == '__main__':
    main()
