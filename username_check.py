"""Modules"""
from colorama import Fore
import requests

"""Headers For Performance"""
_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'Access-Control-Allow-Credentials': 'true',
    'Content-Encoding': 'gzip'
}

"""Global Session For Performance"""
session = requests.session()

"""Checks Username from each website"""
def username_check():
    username = input(Fore.LIGHTMAGENTA_EX + '\n[+] Enter Target Username To Scan : ')
    
    """Websites list's"""
    Website_list = {
        # INSTAGRAM
        'instagram' : f'https://www.instagram.com/{username}',
        # FACEBOOK
        'facebook' : f'https://www.facebook.com/{username}',
        #TWITTER
        'twitter' : f'https://www.twitter.com/{username}',
        # YOUTUBE
        'youtube' : f'https://www.youtube.com/{username}',
        # BLOGGER
        'blogger' : f'https://{username}.blogspot.com',
        # GOOGLE+
        'google_plus' : f'https://plus.google.com/s/{username}/top',
        # REDDIT
        'reddit' : f'https://www.reddit.com/user/{username}',
        # WORDPRESS
        'wordpress' : f'https://{username}.wordpress.com',
        # PINTEREST
        'pinterest' : f'https://www.pinterest.com/{username}',
        # GITHUB
        'github' : f'https://www.github.com/{username}',
        # TUMBLR
        'tumblr' : f'https://{username}.tumblr.com',
        # FLICKR
        'flickr' : f'https://www.flickr.com/people/{username}',
        # STEAM
        'steam' : f'https://steamcommunity.com/id/{username}',
        # VIMEO
        'vimeo' : f'https://vimeo.com/{username}',
        # SOUNDCLOUD
        'soundcloud' : f'https://soundcloud.com/{username}',
        # DISQUS
        'disqus' : f'https://disqus.com/by/{username}',
        # MEDIUM
        'medium' : f'https://medium.com/@{username}',
        # DEVIANTART
        'deviantart' : f'https://{username}.deviantart.com',
        # VK
        'vk' : f'https://vk.com/{username}',
        # ABOUT.ME
        'aboutme' : f'https://about.me/{username}',
        # IMGUR
        'imgur' : f'https://imgur.com/user/{username}',
        # FLIPBOARD
        'flipboard' : f'https://flipboard.com/@{username}',
        # SLIDESHARE
        'slideshare' : f'https://slideshare.net/{username}',
        # FOTOLOG
        'fotolog' : f'https://fotolog.com/{username}',
        # SPOTIFY
        'spotify' : f'https://open.spotify.com/user/{username}',
        # MIXCLOUD
        'mixcloud' : f'https://www.mixcloud.com/{username}',
        # SCRIBD
        'scribd' : f'https://www.scribd.com/{username}',
        # BADOO
        'badoo' : f'https://www.badoo.com/en/{username}',
        # PATREON
        'patreon' : f'https://www.patreon.com/{username}',
        # BITBUCKET
        'bitbucket' : f'https://bitbucket.org/{username}',
        # DAILYMOTION
        'dailymotion' : f'https://www.dailymotion.com/{username}',
        # ETSY
        'etsy' : f'https://www.etsy.com/shop/{username}',
        # CASHME
        'cashme' : f'https://cash.me/{username}',
        # BEHANCE
        'behance' : f'https://www.behance.net/{username}',
        # GOODREADS
        'goodreads' : f'https://www.goodreads.com/{username}',
        # INSTRUCTABLES
        'instructables' : f'https://www.instructables.com/member/{username}',
        # KEYBASE
        'keybase' : f'https://keybase.io/{username}',
        # KONGREGATE
        'kongregate' : f'https://kongregate.com/accounts/{username}',
        # LIVEJOURNAL
        'livejournal' : f'https://{username}.livejournal.com',
        # ANGELLIST
        'angellist' : f'https://angel.co/{username}',
        # LAST.FM
        'last_fm' : f'https://last.fm/user/{username}',
        # DRIBBBLE
        'dribbble' : f'https://dribbble.com/{username}',
        # CODECADEMY
        'codecademy' : f'https://www.codecademy.com/{username}',
        # GRAVATAR
        'gravatar' : f'https://en.gravatar.com/{username}',
        # PASTEBIN
        'pastebin' : f'https://pastebin.com/u/{username}',
        # FOURSQUARE
        'foursquare' : f'https://foursquare.com/{username}',
        # ROBLOX
        'roblox' : f'https://www.roblox.com/user.aspx?username={username}',
        # GUMROAD
        'gumroad' : f'https://www.gumroad.com/{username}',
        # NEWSGROUND
        'newsground' : f'https://{username}.newgrounds.com',
        # WATTPAD
        'wattpad' : f'https://www.wattpad.com/user/{username}',
        # CANVA
        'canva' : f'https://www.canva.com/{username}',
        # CREATIVEMARKET
        'creative_market' : f'https://creativemarket.com/{username}',
        # TRAKT
        'trakt' : f'https://www.trakt.tv/users/{username}',
        # 500PX
        'five_hundred_px' : f'https://500px.com/{username}',
        # BUZZFEED
        'buzzfeed' : f'https://buzzfeed.com/{username}',
        # TRIPADVISOR
        'tripadvisor' : f'https://tripadvisor.com/members/{username}',
        # HUBPAGES
        'hubpages' : f'https://{username}.hubpages.com',
        # CONTENTLY
        'contently' : f'https://{username}.contently.com',
        # HOUZZ
        'houzz' : f'https://houzz.com/user/{username}',
        # WIKIPEDIA
        'wikipedia' : f'https://www.wikipedia.org/wiki/User:{username}',
        # HACKERNEWS
        'hackernews' : f'https://news.ycombinator.com/user?id={username}',
        # CODEMENTOR
        'codementor' : f'https://www.codementor.io/{username}',
        # REVERBNATION
        'reverb_nation' : f'https://www.reverbnation.com/{username}',
        # BANDCAMP
        'bandcamp' : f'https://www.bandcamp.com/{username}',
        # COLOURLOVERS
        'colourlovers' : f'https://www.colourlovers.com/love/{username}',
        # IFTTT
        'ifttt' : f'https://www.ifttt.com/p/{username}',
        # EBAY
        'ebay' : f'https://www.ebay.com/usr/{username}',
        # SLACK
        'slack' : f'https://{username}.slack.com',
        # OKCUPID
        'okcupid' : f'https://www.okcupid.com/profile/{username}',
        # TRIP
        'trip' : f'https://www.trip.skyscanner.com/user/{username}',
        # ELLO
        'ello' : f'https://ello.co/{username}',
        # TRACKY
        'tracky' : f'https://tracky.com/user/~{username}',
        # BASECAMP
        'basecamp' : f'https://{username}.basecamphq.com/login'
    }

    found_list = []
    print()
    for individual_website in Website_list:
        URL = Website_list[individual_website]
        try:
            print(Fore.LIGHTMAGENTA_EX + f'[+] Searching on {individual_website}')
            response = session.get(URL , timeout=10 , headers=_headers)

            if(response.status_code == 200):
                if(username in response.text):
                    print(Fore.LIGHTGREEN_EX + f'[-_0] {username} was Found on {individual_website}')
                    found_list.append(URL)   
                    print()
                else:
                    print(Fore.LIGHTYELLOW_EX + f'[!] {username} was Not Found on {individual_website} Might be a false positive!')
                    print()
            else:
                print(Fore.LIGHTRED_EX + f'[-] {username} was not Found on {individual_website}')
                print()

        except:
            print(Fore.RED + f'Error Occured while checking! {username} on {individual_website}! Skipping!!')

    if(len(found_list) != 0):
        print(Fore.YELLOW + f'\nUsername found on following Websites\n')
        for website_found in found_list:
            print(Fore.GREEN + website_found)
        print()
    else:
        print(Fore.RED + f'\nUsername not found on any Websites\n')

"""Main Function"""
if __name__ == '__main__':
    username_check()