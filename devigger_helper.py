import requests

KELLY_MULTIPLIER = 0.25
KELLY_BANKROLL = 18000

# helper function for devig cno api call and formatting the response for display
# TODO: make it also return the original single_book_odd and leg_odds_sharp_book
def devig_cno_api(single_book_odd, leg_odds_sharp_book):
    api_url = 'http://api.crazyninjaodds.com/api/devigger/v1/sportsbook_devigger.aspx?api=open'

    params = {
        'LegOdds': leg_odds_sharp_book,
        'FinalOdds': single_book_odd,
        'DevigMethod': 4,
        'Args': 'ev_p,fb_p,fo_o,kelly,dm'
    }

    try:
        api_response = requests.get(api_url, params=params)
        response = api_response.json()
        
        if api_response.status_code != 200 or 'Final' not in response:
            return {
                'success': False,
                'data': None,
                'error': f'Failed to fetch data. Status code: {api_response.status_code}. Response: {response}'
            }
        
        ev_percentage = response['Final']['EV_Percentage'] * 100
        ev_percentage_formatted = f'{ev_percentage:.1f}%'
        fair_value_odds = response['Final']['FairValue_Odds']
        fair_value_odds_formatted = f'{fair_value_odds:.0f}'
        
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
        kelly_wager = KELLY_BANKROLL / 100 * kelly_quarter_unit
        
        return {
            'success': True,
            'data': {
                'ev_percentage': ev_percentage,
                'ev_percentage_formatted': ev_percentage_formatted,
                'fair_value_odds': fair_value_odds,
                'fair_value_odds_formatted': fair_value_odds_formatted,
                'fair_value_percentage': fair_value_percentage,
                'fair_value_percentage_formatted': fair_value_percentage_formatted,
                'final_odds': final_odds,
                'market_juice_percentage': market_juice_percentage,
                'market_juice_percentage_formatted': market_juice_percentage_formatted,
                'fb_percentage': fb_percentage,
                'fb_percentage_formatted': fb_percentage_formatted,
                'leg1_odds': leg1_odds,
                'kelly_quarter_unit': kelly_quarter_unit,
                'kelly_wager': kelly_wager
            },
            'error': None
        }
    except Exception as e:
        return {
            'success': False,
            'data': None,
            'error': f'Exception occurred: {str(e)}'
        }
