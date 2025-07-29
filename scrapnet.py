from module.console.banner import Banner
from module.core.google_search import Google_result

def main () :
    pass

if __name__ == "__main__":
    banner = Banner ()
    google_search = Google_result (['Mango', 'watermelon']) 
    google_search.googlesearch ()
    print (banner.getbanner ())

