import requests

# helper function for devig cno api call and formatting the response for display
def devig_cno_api(single_book_odd, leg_odds_sharp_book):
    api_url = 'http://api.crazyninjaodds.com/api/devigger/v1/sportsbook_devigger.aspx?api=open'

    params = {
        'LegOdds': leg_odds_sharp_book,
        'FinalOdds': single_book_odd,
        'DevigMethod': 4,
        'Args': 'ev_p,fb_p,fo_o,kelly,dm'
    }

    api_response = requests.get(api_url, params=params)
    response = api_response.json()
    if (api_response.status_code == 200 and ('Final' in response)):
        ev_percentage = response['Final']['EV_Percentage'] * 100

        ev_percentage_formatted = f'{ev_percentage:.1f}%'
        fair_value_odds = response['Final']['FairValue_Odds']
        fair_value_odds_formatted = f'{fair_value_odds:.0f}'

        if (ev_percentage < 0):
            print('Negative EV ', ev_percentage_formatted, fair_value_odds_formatted, '\n')   
            return None

        # extract the response
        fair_value_percentage = response['Leg#1']['FairValue'] * 100
        fair_value_percentage_formatted = f'{fair_value_percentage:.1f}%'

        final_odds = response['Final']['Odds']

        market_juice_percentage = response['Leg#1']['MarketJuice'] * 100
        market_juice_percentage_formatted = f'{market_juice_percentage:.1f}%'

        fb_percentage = response['Final']['FB_Percentage'] * 100
        fb_percentage_formatted = f'{fb_percentage:.1f}%'

        leg1_odds = response['Leg#1']['Odds']

        kelly_quarter_unit = response['Final']['Kelly_Full'] * KELLY_MULTIPLIER
        kelly_wager = KELLY_BANKROLL/100 * kelly_quarter_unit

        print(f'Leg#1 ({leg1_odds}); Market Juice = {market_juice_percentage_formatted}; Fair Value = {fair_value_odds_formatted} ({fair_value_percentage_formatted})')
        print(f'Final Odds ({final_odds})')
        print(f'Summary; EV% = {ev_percentage_formatted}, Kelly Units = {kelly_quarter_unit:.2f}u, Kelly Wager = ${kelly_wager:.2f} (FB = {fb_percentage_formatted})\n')
        return None
    else:
        return {'error': f'Failed to fetch data. Status code: {api_response.status_code}. Response: {api_response.json()}'}
